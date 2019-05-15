# coding=utf-8
import csv

with open("python.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(["魏叔叔","Pbase"])
    writer.writerow(["赵叔叔", "Flask"])
    writer.writerow(["超哥哥", "Spider"])