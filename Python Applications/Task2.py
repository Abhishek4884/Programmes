import schedule
import time
import datetime
import sys

def Task_terminator():
    sys.exit()

def Task_Minute():
    print("Task based on minutes gets scheduled at :"  , datetime.datetime.now())

def Task_Hour():
    print("Task based on Hour gets scheduled at :"  , datetime.datetime.now())

def Task_Day():
    print("Task based on day gets scheduled at :"  , datetime.datetime.now())



def main():
    print("Inside task Scheduler")
    print("Current time" , datetime.datetime.now())

    schedule.every(5).seconds.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every(1).saturday.at("20:36").do(Task_Day)
    schedule.every(30).seconds.do(Task_terminator)


    while(True):
        schedule.run_pending()
        time.sleep(1)




if __name__=="__main__":
    main()