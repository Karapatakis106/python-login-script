import os

with open('pwd.txt', 'r') as file:
    userpwd = file.read().replace('\n', '')
pwd=input("enter password"))

if pwd==userpwd:
   print ("Correct!")
else:
   print ("Wrong.")
