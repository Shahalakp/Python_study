import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",db="assignment1")
cur=conn.cursor()
# cur.execute("create database assignment1")
# cur.execute("create table phonebook(id int primary key auto_increment,cname varchar(50),phone bigint)" )
# conn.commit()

def addcontact(cname,phone):
    query=f"insert into phonebook values(null,'{cname}',{phone})"
    cur.execute(query)
    conn.commit()
    return 1

def viewcontact():
    query="select * from phonebook"
    cur.execute(query)
    res=cur.fetchall()
    return res

conn.close()