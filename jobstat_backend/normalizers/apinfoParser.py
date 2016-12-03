from bs4 import BeautifulSoup
import os
import re

from common import save_json_file, clean_text, check_or_create_save_folder

job_platform = 'apinfo'
JOB_FOLDER = "../crawled_data/%s" % job_platform
SAVE_FILE_PATH = "../normalized_data/%s" % job_platform

ERROR_LOG_FILE = "../normalized_data/%s_error_log.txt" % job_platform


def clean_apinfo_jobtitle(job_title):
    return job_title.replace("\n ", "").replace("\n\n", " ").replace("  \n  ", "").replace("  ", "").replace(" \n", "")


def main():

    check_or_create_save_folder(SAVE_FILE_PATH)

    # List all scraped files related to ApInfo
    for html_file_path in os.listdir(JOB_FOLDER):

        # Parse only HTML files
        if html_file_path.endswith(".html"):

            job_id = re.findall(r'\d+', html_file_path)[0]
            json_file_name = "%s-%s.json" % (job_platform, job_id)
            save_path = "%s/%s" % (SAVE_FILE_PATH, json_file_name)

            # Check if file hasn't already been parsed
            if not os.path.isfile(save_path):
                try:
                    htmlfile = open(JOB_FOLDER+"/"+html_file_path)
                    soup = BeautifulSoup(htmlfile.read())

                    job_info = soup.find("div", class_="info-data").text.strip()
                    date = job_info.rsplit('-', 1)[1].strip()
                    location = clean_text(job_info.rsplit('-', 1)[0])
                    city = location.rsplit('-', 1)[0].strip()
                    state = location.rsplit('-', 1)[1].strip()

                    job_title = soup.find("div", class_="cargo m-tb").text
                    job_title = clean_apinfo_jobtitle(job_title)
                    company = clean_text(soup.find('div', class_="texto").contents[3].contents[2])
                    job_description = clean_text(soup.find('div', class_="texto").contents[1].text)

                    data = {
                        'date': date,
                        'job_title': job_title,
                        'company': company,
                        'location_city': city,
                        'location_state': state,
                        'job_description': job_description,
                        'job_platform': job_platform,
                        'job_platform_id': job_id
                    }

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
