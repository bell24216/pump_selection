import mysql.connector

mydb_user = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)

cursor = mydb_user.cursor()
name = "aukit"  # แทนที่ด้วยชื่อผู้ใช้ที่ต้องการตรวจสอบ
sql = "SELECT * FROM user_table WHERE user_name = %s"
data = (name,)
print(sql)
print(data)
# execute คำสั่ง SQL
cursor.execute(sql, data)

# ตรวจสอบว่ามีการพบข้อมูลหรือไม่
if cursor.fetchone():
    print("ชื่อผู้ใช้มีอยู่ในฐานข้อมูล")
else:
    print("ชื่อผู้ใช้ไม่มีอยู่ในฐานข้อมูล")