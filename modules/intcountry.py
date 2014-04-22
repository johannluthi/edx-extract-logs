'''
Created on 17 avr. 2014

@author: admin
'''
import csv
import sqlite3 as lite

# Connection to db
con = lite.connect('edx-logs.db')
c = con.cursor()

def detailDb(c):
    """
    View num of row and content
    """
    # test if data already save
    c.execute("SELECT Fromip, Toip, country from intcountry")
    intcountry = c.fetchall()
    if intcountry . __len__() > 0:
        print ">> Sum of row (" + str(intcountry . __len__()) + ") in table 'intcountry' ('Fromip, Toip, country')"
        print ">> -- example: " + str(intcountry[0])

def getIntFromIP(c, ip):
    """
    Return int of the IP
    """
    try:
        o = map(int,ip.split('.'))
        res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
        return res
    except ValueError:
        error = 0

def getList():
    """
    Return list
    """
    c.execute("SELECT Fromip, Toip, country from intcountry")
    return c.fetchall()

def cleanDb(c):
    """
    Drop table
    """
    c.execute("DROP TABLE IF EXISTS intcountry") 

def extractIntcountry(c, con):  
    # get files
    tableexist = 0;
    try:
        c.execute("SELECT * FROM sqlite_master WHERE name ='intcountry' and type='table'; ")
        tableexist = c.fetchone()
    except ValueError:
        error = 0
    extractformfile = False
    if tableexist != None:
        c.execute("SELECT Fromip, Toip, country from intcountry")
        intcountry = c.fetchall()
        if intcountry . __len__() == 0:
            extractformfile = True
    else:
        extractformfile = True        
    if extractformfile == True:
        c.execute("DROP TABLE IF EXISTS intcountry") 
        c.execute("CREATE TABLE intcountry(Fromip INT, Toip INT, country TEXT)")
        with open('data/iplocation/country.csv', 'Ur') as f:
            country = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
        intcountry = []
        for i in country:
            int1    =   getIntFromIP (c, i [ 0 ] )
            int2    =   getIntFromIP (c, i [ 1 ] )
            intcountry.append( [ int1 , int2 , i[ 2 ]  ] )
            c.execute('insert into intcountry values (?, ?, ?)', (int1 , int2, str(i[ 2 ])))
        con.commit()
    else:
        c.execute("SELECT Fromip, Toip, country from intcountry")
        intcountry = c.fetchall()
    return intcountry