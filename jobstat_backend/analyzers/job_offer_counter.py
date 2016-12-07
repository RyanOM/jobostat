import os
import io
import json
import datetime


RESULTS_FOLDER = "../analyzed_data"
NOW = datetime.datetime.now()

JSON_FOLDERS = [
    "../normalized_data/netcarreiras",
    "../normalized_data/apinfo",
    "../normalized_data/trampos",
    "../normalized_data/ceviu"
]

##
# JSON operations
##


def json_files():
    for json_folder in JSON_FOLDERS:
        for filepath in os.listdir(json_folder):
            if not filepath.endswith(".json"):
                continue
            yield "%s/%s" % (json_folder, filepath)


def jobs():
    for file in json_files():
        yield json.loads(open(file).read())


def save_data(skill_name, data_json):
    file_name = "%s.json" % skill_name
    save_path = '%s/%s' % (RESULTS_FOLDER, file_name)
    with io.open(save_path, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data_json, sort_keys=True, indent=4, ensure_ascii=False)))
        print'Created file: %s' % file_name


def check_or_create_save_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print "Created folder for parsed results: %s" % folder_path


##
# Date functions
##


# "09/06/2016" -> "06/2016"
def job_month(job_date):
    day, month, year = job_date.split('/', 3)
    if len(year) < 4:
        year = "20%s" % year
    return "%s/%s" % (year, month)


def month_year_iter(start_month, start_year, end_month, end_year):
    ym_start = 12 * start_year + start_month - 1
    ym_end = 12 * end_year + end_month - 1
    for ym in range(ym_start, ym_end):
        y, m = divmod(ym, 12)
        yield y, m + 1


def complete_data_dates(dic):
    for ym in month_year_iter(5, 2012, NOW.month + 1, NOW.year):
        y = ym[0]
        m = "%02d" % ym[1]
        ym_key = "%s/%s" % (y, m)

        if ym_key not in dic:
            dic[ym_key] = 0

    return dic


def job_month_counter():
    data = {}
    for job in jobs():
        month = job_month(job['date'])

        if month not in data:
            data[month] = 1
        else:
            data[month] += 1

    sorted_items = sorted(data.items(), key=lambda e: e[0])
    print("Total job offers per month")
    json_data = {}
    json_data['skill_name'] = 'all',
    json_data['data'] = {}

    for month, count in sorted_items:
        print("%s %s" % (month, count))
        json_data['data'][month] = count

    json_data['data'] = complete_data_dates(json_data['data'])
    save_data('all', json_data)


def main():
    check_or_create_save_folder(RESULTS_FOLDER)
    job_month_counter()

if __name__ == '__main__':
    main()
