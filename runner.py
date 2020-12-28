from follow_follower import *
from fav_retweet import *

import schedule
import time

def runner1():
        main()

def runner2():
        main_(["#100daysofcode"])

schedule.every(10).minutes.do(runner2)
schedule.every(1).minutes.do(runner1)

while True:
    schedule.run_pending()
    time.sleep(5)
