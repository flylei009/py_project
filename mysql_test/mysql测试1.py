import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="mysql@pwd123"  # 数据库密码
)

print(mydb)

# #1、创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库：
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE runoob_db")


# #2、 创建数据库前我们也可以使用 "SHOW DATABASES" 语句来查看数据库是否存在：
# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)


#3、 创建数据表使用 "CREATE TABLE" 语句，创建数据表前，需要确保数据库已存在，以下创建一个名为 sites 的数据表：
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="mysql@pwd123",  # 数据库密码
    database="runoob_db"  # 之前已经创建了
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


#4、 我们也可以使用 "SHOW TABLES" 语句来查看数据表是否已存在：
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

#5、 给表创建主键。
# mycursor = mydb.cursor()
# mycursor.execute("drop table  sites")
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")




#6、 向 sites 表插入一条记录。
# mycursor = mydb.cursor()
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("RUNOOB", "https://www.runoob.com")
# mycursor.execute(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")


#7、 批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
# mycursor = mydb.cursor()
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = [
#     ('Google', 'https://www.google.com'),
#     ('Github', 'https://www.github.com'),
#     ('Taobao', 'https://www.taobao.com'),
#     ('stackoverflow', 'https://www.stackoverflow.com/')
# ]
# print(type(val))
# mycursor.executemany(sql, val)
# mydb.commit()  # 数据表内容有更新，必须使用到该语句
# print(mycursor.rowcount, "记录插入成功。")


#8、 如果我们想在数据记录插入后，获取该记录的 ID ，可以使用以下代码：
# mycursor = mydb.cursor()
# sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 条记录已插入, ID:", mycursor.lastrowid)

# 9、查询数据使用 SELECT 语句：
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM sites")
# myresult = mycursor.fetchall()  # fetchall() 获取所有记录
# for x in myresult:
#     print(x)


# 10、为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
# mycursor = mydb.cursor()
# sql = "SELECT * FROM sites WHERE name = %s"
# na = ("RUNOOB",)
# mycursor.execute(sql, na)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# 11、删除 name 为 stackoverflow 的记录：
mycursor = mydb.cursor()
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")