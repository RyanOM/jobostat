import os
import io
import json
from collections import Counter, defaultdict

import datetime

from skills import SKILLS, ALIASES

# Set of all skills/subskills
ALL_SKILLS = set(sum([
    [skill]+subskills
    for skill, subskills in SKILLS.items()
], []))

NOW = datetime.datetime.now()


def invert_skills(skills):
    skill_index = {}
    for skill, subskills in skills.items():
        for subskill in subskills:
            skill_index[subskill] = skill
    return skill_index

# So we can easily map a subskill to its parent skill
SUBSKILLS_TO_SKILLS = invert_skills(SKILLS)

##
# Word / normalization functions
##


def normalize_word(word):
    # Nornalize to lowercase
    word = word.lower()
    # Remove trailing comas or dots
    word = word.rstrip('-.,;*()/\\')
    word = word.lstrip('-,;*()/\\')
    return word


def flatten(list_of_lists):
    return sum(list_of_lists, [])


def text_to_words(paragraph):
    return [normalize_word(word) for word in paragraph.split()]


def word_to_skills(word):
    # Not a skill
    if word not in ALL_SKILLS:
        return []
    # Is a subskill
    if word in SUBSKILLS_TO_SKILLS:
        parent_skill = SUBSKILLS_TO_SKILLS[word]
        return [word, parent_skill]
    # Is a parent skill / category
    return [word]


def unalias(word):
    return ALIASES.get(word, word)


# trigrams returns a list
def trigrams(words):
    n = len(words)
    for idx, word in enumerate(words):
        bigram = ""
        if idx+1 < n:
            bigram = words[idx+1]
        trigram = ""
        if idx+2 < n:
            trigram = words[idx+2]
        yield word, bigram, trigram


# skills returns a list of skills and subskills that appear in a given paragraph
def skills(paragraph):
    words = text_to_words(paragraph)
    skills = []
    for word, bigram, trigram in trigrams(words):
        w = word_to_skills(unalias(word))
        b = word_to_skills(unalias(bigram))
        t = word_to_skills(unalias(trigram))
        skills.extend([w, b, t])
    return flatten(skills)

##
# JSON stuff
##

JSON_FOLDERS = [
    "../normalized_data/netcarreiras",
    "../normalized_data/apinfo",
    "../normalized_data/trampos",
]


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
    save_path = '../analzed_data/%s' % file_name
    with io.open(save_path, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data_json, sort_keys=True, indent=4, ensure_ascii=False)))
        print'Created file: %s' % file_name


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


##
# Main
##
def print_counter(counter):
    for word, freq in counter.most_common():
        print("%d %s" % (freq, word))


def print_histogram(skill, histogram):
    # Sort histogram items
    sorted_items = sorted(histogram.items(), key=lambda e: e[0])
    print("# %s" % skill)
    json_data = {}
    json_data['skill_name'] = skill,
    json_data['data'] = {}

    for month, count in sorted_items:
        print("%s %s" % (month, count))
        json_data['data'][month] = count

    json_data['data'] = complete_data_dates(json_data['data'])
    save_data(skill, json_data)


def skills_histograms():
    histogram = {
        skill: defaultdict(int)
        for skill in ALL_SKILLS
    }
    for job in jobs():
        month = job_month(job['date'])
        job_skills = skills(job['job_description'])
        for skill in set(job_skills):
            histogram[skill][month] = histogram[skill][month] + 1
    return histogram


def main_all_histograms():
    histograms = skills_histograms()
    for skill, histogram in histograms.items():
        print_histogram(skill, histogram)
        print("")


def main_all_skills():
    title_skills = flatten([
        skills(job['job_description'])
        for job in jobs()
    ])
    counter = Counter(title_skills)
    print_counter(counter)


def main():
    main_all_histograms()

if __name__ == '__main__':
    main()
