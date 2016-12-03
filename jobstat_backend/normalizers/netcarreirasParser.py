from bs4 import BeautifulSoup
import os
import re

from common import clean_text, save_json_file, check_or_create_save_folder

job_platform = 'netcarreiras'
JOB_FOLDER = "../crawled_data/%s" % job_platform
SAVE_FILE_PATH = "../normalized_data/%s" % job_platform

ERROR_LOG_FILE = "../normalized_data/%s_error_log.txt" % job_platform


def main():
    # List all scraped files related to NetCarreiras
    for html_file_path in os.listdir(JOB_FOLDER):

        check_or_create_save_folder(SAVE_FILE_PATH)

        # Parse only HTML files
        if html_file_path.endswith(".html"):
            job_id = re.findall(r'\d+', html_file_path)[0]
            json_file_name = "%s-%s.json" % (job_platform, job_id)
            save_path = "%s/%s" % (SAVE_FILE_PATH, json_file_name)
            if not os.path.isfile(save_path):
                try:

                    htmlfile = open(JOB_FOLDER+"/"+html_file_path)
                    soup = BeautifulSoup(htmlfile.read())

                    date = soup.find('div', class_="profile").contents[3].text
                    date = clean_text(date)

                    location = soup.find('div', {'id': "location"}).text
                    location = clean_text(location)
                    city = re.search('(.*) -', location, re.IGNORECASE).group(1)
                    state = re.search('- (.*) \(', location, re.IGNORECASE).group(1)

                    job_title = soup.find("h1").text
                    job_title = clean_text(job_title)

                    company = None
                    if soup.find_all('a', href=re.compile('^vagas-na-(.*)')):
                        company = soup.find_all('a', href=re.compile('^vagas-na-(.*)'))[0].text
                        company = clean_text(company)

                    job_description = soup.find('article').contents[11].text
                    job_description = clean_text(job_description)

                    data = {
                        'date': date,
                        'job_title': job_title,
                        'location_city': city,
                        'location_state': state,
                        'job_description': job_description,
                        'job_platform': job_platform,
                        'job_platform_id': job_id
                    }

                    if company:
                        data['company'] = company

                    save_json_file(save_path, data)

                # Log errors to a text file
                except Exception as e:
                    target = open(ERROR_LOG_FILE, "a")
                    error_details = ""
                    if job_id:
                        error_details += "%s: " % job_id
                        print(job_id)
                    print(e)
                    error_details += str(e)
                    target.write("%s\n" % error_details)

if __name__ == '__main__':
    main()
