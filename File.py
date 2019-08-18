import sqlite3
import csv
import pandas as pd
conn=sqlite3.connect("e.db")
cursor=conn.cursor()
print("done")
csv_data=csv.reader(open("Employee.csv"))
for row in csv_data:
    cursor.execute('insert into eff(id,name,city,age,salary)values("%s","%s","%s","%s","%s")')
    print(row)
data=pd.read_csv("Employee.csv")
data.sort_values("age",axis=0,ascending=True,inplace=True,na_position='first')
data.sort_values("salary",axis=0,ascending=True,inplace=True,na_position='first')
print(data)
conn.commit()
cursor.close()
print("done")
'''conn=sqlite3.connect("e.db")
conn.execute('create table eff(id int,name text,city text,age int,salary int)')
conn.commit()
conn.close()'''
 
