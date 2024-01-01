import mysql.connector

# conn=mysql.connector.connect(host="localhost",user="root",password="root")
# cur=conn.cursor()
# print(conn)

# cur.execute("create database mydb")

conn=mysql.connector.connect(host="localhost",user="root",password="root",db="mydb")
cur=conn.cursor()
cur.execute("create table contacts (id int primary key auto_increment, 'cname' varchar(50), phone bigint)")

print("table created")

cur.execute("insert into contacts values(null,'ajith',9877564538)")
conn.commit()
print("value entered")
cur.execute("select * from contacts")
