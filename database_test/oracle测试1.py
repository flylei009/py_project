import cx_Oracle

conn = cx_Oracle.connect('yxgl/yinhai123@192.168.0.111/itpuxdb') #用自己的实际数据库用户名、密码、主机ip地址 替换即可
print('测试成功')
curs=conn.cursor()
sql='SELECT * FROM B_CODECLASS' #sql语句
rr=curs.execute (sql)
row=curs.fetchone()
print(row)
curs.close()
conn.close()
