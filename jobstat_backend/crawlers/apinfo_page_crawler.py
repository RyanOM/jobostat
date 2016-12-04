# -*- coding: utf-8 -*-
import os
import re


from selenium import webdriver
from bs4 import BeautifulSoup

from common import check_or_create_save_folder

PHANTOMJS_PATH = './phantomjs/bin/phantomjs'

JOB_PLATFORM = "apinfo"
JOB_OFFERS_URL = 'http://www.apinfo.com/apinfo/inc/list4.cfm'
SAVE_PATH = '../crawled_data/%s' % JOB_PLATFORM

# Quits after encountering X offers that aren't available or already saved
ACCESS_LIMIT = 200


def save_html_file(file_name, html_contents, access_limit):
    html = html_contents.prettify("utf-8")
    file_path = '%s/%s' % (SAVE_PATH, file_name)
    if not os.path.isfile(file_path):
        with open(file_path, "wb") as htmlfile:
            htmlfile.write('%s\n%s' % ('<meta charset="UTF-8">', html))
            print'Created file: %s' % file_name
    else:
        print'File already exists: %s' % file_name
        access_limit -= 1

    return access_limit


def get_number_of_page_results(html_contents):
    return int(re.findall("\d de (\d+)", html_contents.text)[0])


def main():
    check_or_create_save_folder(SAVE_PATH)
    browser = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)
    browser.get(JOB_OFFERS_URL)
    print("[+] The bot is starting!")

    page_html = BeautifulSoup(browser.page_source)
    nb_pages = get_number_of_page_results(page_html)

    access_limit = ACCESS_LIMIT

    for i in range(1, nb_pages):
        page_html = BeautifulSoup(browser.page_source)
        job_descriptions = page_html.find_all('div', class_="box-vagas")

        for jd in job_descriptions:
            info = jd.find('div', class_="texto").contents[3]
            job_id = re.findall(r'\d{4,9}', info.text)[0]
            file_name = "%s-%s.html" % (JOB_PLATFORM, job_id)
            access_limit = save_html_file(file_name, jd, access_limit)

        if access_limit <= 0:
            print "\nNo new jobs found. Exiting..."
            break

        # Simulate click on next page button
        browser.find_element_by_xpath("//input[contains(@value,'OK')]").click()


if __name__ == '__main__':
    main()
