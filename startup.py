'''
Created on 11 avr. 2014

@author: Johann luethi
'''
import modules.events
import modules.intcountry
import modules.files
import modules.userip
import modules.db
import modules.result

import sqlite3 as lite

# Connection to db
con = lite.connect('edx-logs.db')
c = con.cursor()

mypath = "data/logs/"

#modules.intcountry.cleanDb(c)
#modules.events.cleanDB(c)
#modules.files.cleanDb(c)
#modules.userip.cleanDb(c)
#modules.result.cleanDb(c)

files       =   modules.files.getFiles(c,con, mypath)
modules.files.detailDb(c)
events      =   modules.events.getEvents(c, con)
modules.events.detailDb(c)
intcountry  =   modules.intcountry.extractIntcountry(c, con)
modules.intcountry.detailDb(c)
userip      =   modules.userip.getUserIp(c, con, files, events, mypath)
modules.userip.detailDb(c)
results     =   modules.result.getResults(c, con, userip, intcountry)
modules.result.detailDb(c)

c.close()
con.close()

modules.db.consoleDB()