import mysql.connector as con

coon = con.connect(host="localhost", user="root", passwd="<2916>")

print('Connection is :    ', coon)

cur = coon.cursor()
try:
    dbs = cur.execute("use TempDemo;")
    dbs = cur.execute("select * from DemoT1;")
except:
    coon.rollback()

for x in cur:
    temp = list(x)
    for j in range(len(temp)):
        print(temp[j], end="\t")
    print()


coon.close()
