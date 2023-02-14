import schedule

import time


def task1():
    print('Running task 1')


def task2():
    print('Running task 2')


def task3():
    print('Running task 3')


# schedule task to run every hour
# schedule.every(1).hours.do(task1)

schedule.every(5).seconds.do(task2) # schedule task to run every hour
schedule.every().day.at("09:00").do(task3)# schedule task to every day at 9am

while True:
    schedule.run_pending()
