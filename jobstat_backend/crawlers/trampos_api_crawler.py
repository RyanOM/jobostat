import urllib2
import json
import os
import io

START_ID = 129140
JOB_PLATFORM = "trampos"
API_URL = 'http://trampos.co/api/v2/opportunities/%s'
SAVE_PATH = '../crawled_data/%s' % JOB_PLATFORM


def get_api_data(job_id):
    response = urllib2.urlopen(API_URL % job_id)
    return json.load(response)


def save_data(data_json, job_id):
    file_name = "%s-%s.json" % (JOB_PLATFORM, job_id)
    save_path = '../crawled_data/trampos_json/%s' % file_name

    if not os.path.isfile(save_path):
        with io.open(save_path, 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(data_json, sort_keys=True, indent=4, ensure_ascii=False)))
            print'Created file: %s' % file_name
    else:
        print'File already exists: %s' % file_name


def crawl_api(job_id):
    data = get_api_data(job_id)
    if 'status' in data:
        print("%s: %s" %(job_id, data['status']))
    else:
        save_data(data, job_id)


def check_or_create_save_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print "Created folder for saved results: %s" % folder_path


def get_latest_job_id():
    data = get_api_data('http://trampos.co/api/v2/opportunities')
    bob = 42


def main():
    get_latest_job_id()
    start_id = START_ID
    check_or_create_save_folder(SAVE_PATH)
    while start_id > 0:
        crawl_api(start_id)
        start_id -= 1

if __name__ == '__main__':
    main()
