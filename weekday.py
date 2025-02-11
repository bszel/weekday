import datetime
import random

def random_date(start_date: datetime, end_date: datetime):
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    date = start_date + datetime.timedelta(days = random_days)
    return date

def read_answer():
    answer = ''
    while answer not in ['1', '2', '3', '4', '5', '6', '7']:
        answer = input()
    return answer

while True:
    print('start...')
    input()
    start_time = datetime.datetime.now()
    date = random_date(datetime.date(1900, 1, 1), datetime.date(2099, 12, 31))
    print(date)
    answer = read_answer()
    if answer == str(date.isoweekday()):
        print('correct')
        end_time = datetime.datetime.now()
        print((end_time - start_time).total_seconds())
    else:
        print('wrong: ', date.isoweekday())