import requests
from pytz import timezone
from datetime import datetime, time


URL_DEVMAN_API = 'http://devman.org/api/challenges/solution_attempts/'
START_TIME_OF_NIGHT = time(0, 0, 0)
END_TIME_OF_NIGHT = time(5, 59, 59)


def load_attempts(url):
    pages = 1
    page = 1
    while page <= pages:
        response = requests.get(url, params={'page': page})
        if response.status_code == requests.codes.ok:
            if page == 1:
                pages = int(response.json()['number_of_pages'])
            page += 1
            records = response.json()['records']
            for record in records:
                yield {
                       'username': record['username'],
                       'timestamp': record['timestamp'],
                       'timezone': record['timezone'],
                      }


def get_midnighters(records):
    midnighters = set()
    for record in records:
        if record['timestamp'] and record['timezone']:
            time_record = datetime.fromtimestamp(
                                                 record['timestamp'],
                                                 timezone(record['timezone'])
                                                 ).time()
            if START_TIME_OF_NIGHT <= time_record <= END_TIME_OF_NIGHT:
                midnighters.add(record['username'])
    return midnighters


def output_midnighters(midnighters):
    if midnighters:
        print('"Совы" на devman.org:')
        for midnighter in midnighters:
            print(midnighter)


if __name__ == '__main__':
    records = load_attempts(URL_DEVMAN_API)
    midnighters = get_midnighters(records)
    output_midnighters(midnighters)
