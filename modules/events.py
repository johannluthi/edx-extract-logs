'''
Created on 17 avr. 2014

@author: admin
'''
import csv

def detailDb(c):
    """
    View num of row and content
    """
    c.execute("SELECT event from events")
    events = c.fetchall()
    if events . __len__() > 0:
        print ">> Sum of row (" + str(events . __len__()) + ") in table 'events' ('event')"
        print ">> -- example: " + str(events[0])

def getIntFromIP(ip):
    """
    Return int of the IP
    """
    try:
        o = map(int,ip.split('.'))
        res = (16777216 * o[0]) + (65536 * o[1]) + (256 * o[2]) + o[3]
        return res
    except ValueError:
        print "error"

def cleanDB(c):  
    """
    Drop table
    """
    c.execute("DROP TABLE IF EXISTS events") 

def getList(c):
    """
    Return list
    """
    c.execute("SELECT event from events")
    return c.fetchall()

def getEvents(c, con):
    """
    Function to get events listed on events.csv or on db
    return list of event
    """  
    tableexist = 0;
    try:
        c.execute("SELECT * FROM sqlite_master WHERE name ='events' and type='table'; ")
        tableexist = c.fetchone()
    except ValueError:
        error = 0
    extractformfile = False
    if tableexist != None:
        c.execute("SELECT event from events")
        intcountry = c.fetchall()
        if intcountry . __len__() == 0:
            extractformfile = True
    else:
        extractformfile = True
    if extractformfile == True:
        c.execute("DROP TABLE IF EXISTS events") 
        c.execute("CREATE TABLE events(event TEXT)")
        with open('data/events/events.csv', 'Ur') as f:
            events = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
        for i in events:
            c.execute('insert into events values (?)', (i))
        con.commit()
    else:
        c.execute("SELECT event from events")
        events = c.fetchall()
    return events