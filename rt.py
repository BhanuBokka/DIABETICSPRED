import sqlite3

conn=sqlite3.connect("Patient1.db")

cur=conn.cursor()

#cur.execute("CREATE TABLE PATIENTSINFO(Name varchar(30),Result varchar(20) )")
cur.execute("INSERT INTO PATIENTSINFO VALUES('SHAL',' NO DIABETIC')")
conn.commit()