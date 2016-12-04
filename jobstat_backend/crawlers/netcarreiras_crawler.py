# -*- coding: utf-8 -*-
import os
import random
import time
import re

from bs4 import BeautifulSoup
from selenium import webdriver

from common import check_or_create_save_folder

PHANTOMJS_PATH = './phantomjs/bin/phantomjs'

JOB_PLATFORM = "netcarreiras"
JOB_OFFER_URL = 'http://www.netcarreiras.com.br/vaga-x-%s.html'
SAVE_PATH = '../crawled_data/%s' % JOB_PLATFORM
LATEST_JOBS_URL = 'http://www.netcarreiras.com.br/vagas.html'

# Quits after encountering X offers that aren't available or already saved
ACCESS_LIMIT = 200


def check_job_page(job_id, page_html, access_limit):
    if 'Erro 410' in page_html.text:
        print '410: %s' % job_id
        access_limit -= 1
    else:
        html = page_html.prettify("utf-8")
        file_name = "%s-%s.html" % (JOB_PLATFORM, job_id)
        file_path = '%s/%s' % (SAVE_PATH, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, "wb") as htmlfile:
                htmlfile.write(html)
                print'Created file: %s' % file_name
        else:
            print'File already exists: %s' % file_name
            access_limit -= 1

    return access_limit


def get_job_opportunity(browser, job_id, access_limit):
    job_url = JOB_OFFER_URL % job_id
    browser.get(job_url)
    time.sleep(random.uniform(0.1, 0.3))
    page_html = BeautifulSoup(browser.page_source)
    access_limit = check_job_page(job_id, page_html, access_limit)
    return access_limit


def get_latest_job_id(browser):
    browser.get(LATEST_JOBS_URL)
    page_html = BeautifulSoup(browser.page_source)
    job_offers = page_html.find("section", id="items")
    for offer in job_offers.contents:
        try:
            first_job_link = offer.attrs['href']
            first_job_id = re.findall(r'\d+', first_job_link)[0]
            return int(first_job_id)
        except:
            continue

    print "\nWasn't able to retrieve most recent job id"
    return 0


def main():
    check_or_create_save_folder(SAVE_PATH)
    browser = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
    job_id = get_latest_job_id(browser)
    print("[+] The bot is starting!")
    access_limit = ACCESS_LIMIT

    while job_id > 0 and access_limit > 0:
        access_limit = get_job_opportunity(browser, job_id, access_limit)
        job_id -= 1

        if access_limit <= 0:
            print "\nNo new jobs found. Exiting..."


if __name__ == '__main__':
    main()
