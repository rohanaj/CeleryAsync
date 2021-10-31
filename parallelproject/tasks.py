from celery import shared_task
import time
def rotate_str(string):
    newstr = ""
    for i in string:
        newstr += chr(ord(i)+15) # shift the charachter by 15 places in ascii
    return newstr

@shared_task
def process(q):
    new_str = rotate_str(q) 
    for i in range(60):
        time.sleep(1)
        print(i)
    return new_str

