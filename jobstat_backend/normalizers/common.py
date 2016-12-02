import re
import os
import io
import json
from unidecode import unidecode


def clean_text(text):
    cleaned_text = re.sub('\s+', ' ', text).strip()
    cleaned_text = unidecode(cleaned_text).encode('ascii')
    return cleaned_text


def normalize_date(date):
    date = clean_text(date)
    return date


def save_json_file(save_path, data):
    if not os.path.isfile(save_path):
        with io.open(save_path, 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)))

