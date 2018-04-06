import os
import csv

fp1 = os.path.join("D:"
                  ,"Desktop"
                  ,"STP_Practice"
                  ,"Challenges"
                  ,"Chapter 09"
                  ,"movies.csv")

fp = os.path.join("D:",os.sep,fp1)

movie_lists = [["Top Gun","Risky Business","Minority Report"]
               ,["Titanic","The Revenant","Inception"]
               ,["Training Day","Man on Fire","Flight"]]

with open(fp,'w+',newline='') as f:
    w = csv.writer(f,delimiter=",")
    for movie_list in movie_lists:
        w.writerow(movie_list)

