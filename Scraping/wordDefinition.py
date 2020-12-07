# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:02:32 2020

@author: 323917
"""
import requests
from bs4 import BeautifulSoup


word_list=[]
meaning_list=[]

numWords = int(input("How many words to list????"))


for word in range(numWords):
    w = input("Enter a word: ")
    word_list.append(w)
    URL = "https://www.merriam-webster.com/dictionary/"
    r = requests.get("https://www.merriam-webster.com/dictionary/{}".format(w))
    soup = BeautifulSoup(r.content, "html.parser")
    meaning = soup.find("span", attrs={"class":"dtText"}).text
    meaning_list.append(meaning)
    
for index in range(numWords):
    print(str(index) + " The definition of " + word_list[index] + " is " + meaning_list[index])
    
