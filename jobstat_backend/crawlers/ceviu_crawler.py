# -*- coding: utf-8 -*-
import os
import random
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from common import check_or_create_save_folder

PHANTOMJS_PATH = './phantomjs/bin/phantomjs'

LATEST_JOB_ID = '488298'
JOB_PLATFORM = "ceviu"
SAVE_PATH = "../crawled_data/%s" % JOB_PLATFORM

JOB_OFFER_URL = 'http://www.ceviu.com.br/vaga/%s'
LATEST_JOBS_URL = 'https://www.ceviu.com.br/buscar/empregos?ini=0&ordenar=1'


# Oldest job offer avaliable
OLDEST_JOB_ID = 340000


def get_latest_job_id(homepagesoup):
    job_links = homepagesoup.find_all('a', class_="tituloVaga")
    recent_job_link = job_links[0]
    recent_job_url = recent_job_link.attrs['href']
    job_id = re.findall('[0-9]+', recent_job_url)[0]
    return int(job_id)


def check_job_page(job_id, page_html):

    if 'encontrada' in page_html.text:
        print '404: %s' % job_id
    elif 'pode ser visualizado por candidatos premium' in page_html.text:
        print 'premium: %s' % job_id
        return '404'
    elif 'VEJA OUTROS NA MESMA' in page_html.text:
        print 'Job no longer avaliable: %s' % job_id
        return '410'
    elif 'ERRO 429' in page_html.text:
        print 'Reached ip limit: %s' %job_id
        time.sleep(50)
        return 'limit'
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
        return 'created'


def get_job_opportunity(browser, job_id):
    job_url = JOB_OFFER_URL % job_id
    browser.get(job_url)
    time.sleep(random.uniform(0.4, 0.7))
    page_html = BeautifulSoup(browser.page_source)
    status = check_job_page(job_id, page_html)
    if status == 'limit':
        return status


def main():
    check_or_create_save_folder(SAVE_PATH)

    browser = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
    browser.get(LATEST_JOBS_URL)

    print("[+] The bot is starting!")

    home_page = BeautifulSoup(browser.page_source)
    latest_job_id = get_latest_job_id(home_page)

    for job_id in reversed(range(OLDEST_JOB_ID, latest_job_id+1)):
        limit = get_job_opportunity(browser, job_id)

        # If API access limit reached, pause scraping
        if limit == "404":
            time.sleep(12)
        if limit == "limit":
            time.sleep(60)
            get_job_opportunity(browser, job_id)
            job_id -= 1


if __name__ == '__main__':
    main()
