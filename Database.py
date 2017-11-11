import pymysql
import time
#name of the Image recognizer will go here
import pallindrome
def databaseStore(input1, pal):
    database = pymysql.connect("127.0.0.1", "root", "welcome", "new")

    cursor = database.cursor()
    inp = "'{}'".format(str(input1))
    #time = 123456788
    pall = "'{}'".format(pal)
    insert = """INSERT INTO NAME(time, input, pallindrome)
                VALUES ({}, {}, {})""".format(time.time(), inp, pall )
    print(insert)

    try:
        cursor.execute(insert)
        database.commit()
    except:
        database.rollback()
        print("Error: Could not be completed")

        database.close()
