import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="mysql@pwd123",  # 数据库密码
    database="yan_test"  # 之前已经创建了
)

# 9、查询数据使用 SELECT 语句：
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM 每日统计")
# myresult = mycursor.fetchall()  # fetchall() 获取所有记录
# for x in myresult:
#     print(type(x))
#     print(x)

myresult1 = mycursor.fetchone()  # fetchall() 获取所有记录
print(myresult1)

desc = mycursor.description
object_dict = [
    dict(zip([col[0] for col in desc], row))
    for row in mycursor.fetchall()
]
for row in object_dict:
    print(row)  # 格式如下：{'姓名': '陈海峰-霏微科技', '考勤组': '未加入考勤组', '部门': '‘xxx’}



