from selenium import webdriver
import time



myBrowser = webdriver.Firefox()
site = input("enter url of the target site: ")
myBrowser.get(site)
time.sleep(7)
acik = []
title = myBrowser.title

def control(x):
    if "404" not in title and"404" not in title and"403" not in title and"402" not in title and "401" not in title:
        print("acik bulundu")
        acik.append(x)
        print(acik) #trailing /n not included********************************
        myBrowser.close()




def forGetMethod():
    xssFinder = open("payload.txt","r")
    a = 1
    while a <= 6125:
        x = xssFinder.readline().replace('"', '')
        newLink = site + x
        myBrowser.get(newLink)
        a += 1
        time.sleep(1.5)
        control(x)

forGetMethod()