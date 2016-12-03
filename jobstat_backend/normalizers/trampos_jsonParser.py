import os
import re
import json

from common import clean_text, save_json_file, check_or_create_save_folder

job_platform = 'trampos'
JOB_FOLDER = "../crawled_data/%s" % (job_platform + "_json")
SAVE_FILE_PATH = "../normalized_data/%s" % job_platform

ERROR_LOG_FILE = "../normalized_data/%s_error_log.txt" % job_platform


def get_date(json_date):
    year = json_date.split("-")[0]
    month = json_date.split("-")[1]
    day = re.findall(r'\d+', json_date.split("-")[2])[0]
    return "%s/%s/%s" % (day, month, year)


def main():

    check_or_create_save_folder(SAVE_FILE_PATH)

    # List all scraped files related to Trampos
    for json_file_path in os.listdir(JOB_FOLDER):

        # Parse only JSON files
        if json_file_path.endswith(".json"):

            job_id = re.findall(r'\d+', json_file_path)[0]
            json_file_name = "%s-%s.json" % (job_platform, job_id)
            save_path = "%s/%s" % (SAVE_FILE_PATH, json_file_name)

            # Check if file hasn't already been parsed
            if not os.path.isfile(save_path):
                try:
                    with open("%s/%s" % (JOB_FOLDER, json_file_path)) as json_data:
                        job_data = json.load(json_data)['opportunity']
                        data = {}

                        data['date'] = get_date(job_data['published_at'])

                        if 'city' in job_data and 'state' in job_data:
                            data['city'] = clean_text(job_data['city'])
                            data['state'] = clean_text(job_data['state'])
                        elif 'home_office' in job_data:
                            data['home_office'] = True

                        data['job_title'] = clean_text(job_data['name'])

                        if 'company' in job_data and job_data['company']:
                            data['company'] = clean_text(job_data['company']['name'])

                        data['job_description'] = "%s %s %s" % (clean_text(job_data['description']), clean_text(job_data['prerequisite']), clean_text(job_data['desirable']))

                        data['job_platform'] = job_platform
                        data['job_platform_id'] = job_id

                        save_json_file(save_path, data)

                # Log errors to a text file
                except Exception as e:
                    target = open(ERROR_LOG_FILE,  "a")
                    error_details = ""
                    if job_id:
                        error_details += "%s: " % job_id
                        print(job_id)
                    print(e)
                    error_details += str(e)
                    target.write("%s\n" % error_details)

if __name__ == '__main__':
    main()
