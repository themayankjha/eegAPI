import mysql.connector

def databaseentry(username,attention,meditation):
    db = mysql.connector.connect(
        host="remotemysql.com",
        user="hwW4R6cA0s",
        passwd="9bVe4xsxvX",
        db="hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "INSERT INTO eeg VALUES (%s,%s,%s)"
    val = (attention,meditation,username)
    cursor.execute(sql, val)
    db.commit()
    params = dict()
    (params['code'])=("successful")
    return params


def databaseinfogather(username):
    db = mysql.connector.connect(
        host="remotemysql.com",
        user="hwW4R6cA0s",
        passwd="9bVe4xsxvX",
        db="hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "SELECT * FROM eeg WHERE username = %s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    params = dict()
    (params['attention'],params['meditation'],params['username'])=result[0]
    return params
