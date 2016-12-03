from bs4 import BeautifulSoup
import os
import re

from common import clean_text, save_json_file, check_or_create_save_folder

job_platform = 'ceviu'
JOB_FOLDER = "../crawled_data/%s" % job_platform
SAVE_FILE_PATH = "../normalized_data/%s" % job_platform

ERROR_LOG_FILE = "../normalized_data/%s_error_log.txt" % job_platform


def main():

    check_or_create_save_folder(SAVE_FILE_PATH)

    # List all scraped files related to Ceviu
    for html_file_path in os.listdir(JOB_FOLDER):

        # Parse only HTML files
        if html_file_path.endswith(".html"):

            job_id = re.findall(r'\d+', html_file_path)[0]
            json_file_name = "%s-%s.json" % (job_platform, job_id)
            save_path = "%s/%s" % (SAVE_FILE_PATH, json_file_name)
            if not os.path.isfile(save_path):
                try:

                    htmlfile = open(JOB_FOLDER+"/"+html_file_path)
                    soup = BeautifulSoup(htmlfile.read())

                    job_info = soup.find("p", class_="codigo-data-vaga").text.strip()
                    date = job_info.rsplit('Data: ', 1)[1].strip()

                    location = soup.find('div', class_="localizacao-vaga").text
                    location = clean_text(location)
                    city = re.search('Localizacao (.*)/', location, re.IGNORECASE).group(1)
                    state = re.search('/(.*)', location, re.IGNORECASE).group(1)

                    job_title = soup.find("h2", class_="titulo-vaga").text
                    job_title = clean_text(job_title)

                    company = None
                    if soup.find('a', class_="nome-empresa"):
                        company = soup.find('a', class_="nome-empresa").text
                        company = clean_text(company)

                    job_description = soup.find('div', class_='descricao-vaga').text
                    job_description = clean_text(job_description)
                    job_description = re.sub("Descricao da vaga ", "", job_description)
                    job_description = re.sub("Vaga Patrocinada ", "", job_description)


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
