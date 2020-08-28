import mysql.connector as mysql
import datetime
from random import random
import numpy as np
conn = mysql.connect(host="localhost", user="root", password="", db="ecommerce")

def getNew():
    cur = conn.cursor(dictionary=True)
    qry = "SELECT item_id,name FROM `item` "
    cur.execute(qry)
    item = cur.fetchall()
    return item

def checkID(userid):
    
    cur=conn.cursor(dictionary=True)
    qry="SELECT * FROM `user` WHERE `user_id`= '{}'".format(userid)
    cur.execute(qry)
    user = cur.fetchone()
    return user

def savemsg(msg):
    cur = conn.cursor(dictionary=True)
    qry = "INSERT INTO `inquiry` (msg) VALUES('{}')".format(msg)
    cur.execute(qry)
    conn.commit()
    return 0
    
def reg_user(userid,userpass):
    cur=conn.cursor(dictionary=True)
    qry = "INSERT INTO `user` (user_id,pass) VALUES('{},{}')".format(userid,userpass)
    cur.execute(qry)
    conn.commit()



def add_order(itm):
    ordr=np.random.randint(100)
    cur=conn.cursor(dictionary=True)
    qry = "INSERT INTO `orders` (order_id,item_id) VALUES('{}','{}')".format(ordr,int(itm))
    cur.execute(qry)
    conn.commit()
    qry="SELECT * FROM `orders` WHERE `order_id`= '{}'".format(ordr)
    cur.execute(qry)
    getordr = cur.fetchone()
    return getordr




def get_order(ordr):
    cur=conn.cursor(dictionary=True)
    qry="SELECT * FROM `orders` WHERE `order_id`= '{}'".format(ordr)
    cur.execute(qry)
    getordr = cur.fetchone()
    
    return getordr  

def delete_order(ordr):
    cur=conn.cursor(dictionary=True)
    qry = "DELETE FROM `orders` WHERE `orders`.`order_id` = {}".format(ordr)
    cur.execute(qry)
    conn.commit()   