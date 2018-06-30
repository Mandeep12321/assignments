:1 Create a database. Create the following tables:
#            1. Book
#            2. Titles
#            3. Publishers
#            4. Zipcodes
#            5. AuthorsTitles
#            6. Authors       
#Refer to the diagram below
#SOLUTION:
import pymysql 
db=pymysql.connect('localhost','Mandeep dhiman','Mysql039','student')
cursor=db.cursor()
Books="""create table book (Book_Id int, Title_Id int ,Location char(30) , Genre char(30))"""
Titles = """create table titles(Title_Id int,Title char(30),ISBN int,publisher_ID int,Publication_year int)"""
Author_titles="""create table author_titles(Author_Title_ID int,Author_ID int,Title_Id int)"""
Publisher="""create table publisher(Publisher_ID int,Name char(20),Street_Address char(500),Suite_Number int,Zip_Code_ID int)"""
Authors="""create table authors(Author_ID int,First_Name char(30),Middle_Name char(30),Last_name char(30))"""
Zip_code="""create table Zip_Code(Zip_Code_ID int,City char(30),State char(30),Zip_Code int)"""
cursor.execute(Books)
cursor.execute(Titles)
cursor.execute(Author_titles)
cursor.execute(Publisher)
cursor.execute(Authors)
cursor.execute(Zip_code)
db.close()


#QUESTION:2 Insert values in the tables.
#SOLUTION:
import pymysql as py

db=py.connect("localhost","root","Mysql039","library")
cursor=db.cursor()

cursor.execute("insert into book values(001,'looking for alaska','india','fiction')")
cursor.execute("insert into titles values(001,'looking for alaska','1001',101,2005)")
cursor.execute("insert into publishers values(001,'abc','london',10002,11001)")
cursor.execute("insert into zip_code values(001,'ambala','haryana',133203)")
cursor.execute("insert into auther_titles values(001,10010,1012012)")
cursor.execute("insert into authors values(001,'john','null','pink')")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()

#QUESTION:3 Update any values in any of the tables. Print the original and updated values.
#SOLUTION:
import pymysql as py

db=py.connect("localhost","root","Mysql039","library")
cursor=db.cursor()
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
cursor.execute("update book set genre='romance' where book_id=001")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close() 
