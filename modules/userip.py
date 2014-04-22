'''
Created on 17 avr. 2014

@author: admin
'''
import json

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

def getList(c):
    """
    Return list
    """
    c.execute("SELECT User, Ip, Intip from user_ip")
    return c.fetchall()

def detailDb(c):
    """
    View num of row and content
    """
    #c.execute("DROP TABLE IF EXISTS user_ip")
    c.execute("SELECT User, Ip, Intip from user_ip")
    user_ip = c.fetchall()
    if user_ip . __len__() > 0:
        print ">> Sum of row (" + str(user_ip . __len__()) + ") in table 'user_ip' ('User , Ip , Intip ')"
        print ">> -- example: " + str(user_ip[0])

def cleanDb(c):
    """
    Drop table
    """
    c.execute("DROP TABLE IF EXISTS user_ip")

def getUserIp(c,con, files, events, mypath):
    tableexist = 0;
    try:
        c.execute("SELECT * FROM sqlite_master WHERE name ='user_ip' and type='table'; ")
        tableexist = c.fetchone()
    except ValueError:
        error = 0
    user_ip = []
    extractformfile = False
    if tableexist != None:
        c.execute("SELECT User, Ip, Intip from user_ip")
        user_ip = c.fetchall()
        #print user_ip . __len__()
        if user_ip . __len__() == 0:
            extractformfile = True
    else:
        extractformfile = True
    num = 0
    if extractformfile == True:
        c.execute("DROP TABLE IF EXISTS user_ip") 
        c.execute("CREATE TABLE user_ip(User TEXT, Ip TEXT, Intip INT)")
        for x in range( 0, files . __len__() ):
            with open( mypath + files[x][0] ) as f:
                lines = f.readlines()
                f.close()
                for line in lines :
                    try:
                        if any(event[0] in line for event in events):
                            data = json.loads( line )
                            if [data['username'],data['ip'],getIntFromIP( data['ip'] )] not in user_ip:
                                user_ip.append( [data['username'],data['ip'],getIntFromIP( data['ip'] )])
                                c.execute('insert into user_ip values (?, ?, ?)', ( [data['username'],data['ip'],getIntFromIP( data['ip'] )]))
                                con.commit()
                                num = num + 1
                                print str(num) + " user + ip "
                    except:
                        print "error"
    else:
        try:
            c.execute("SELECT User, Ip, Intip from user_ip")
            user_ip = c.fetchall()
            if user_ip . __len__() == 0:
                for x in range( 0, files . __len__() ):
                    with open( mypath + files[x][0] ) as f:
                        lines = f.readlines()
                        f.close()
                        for line in lines :
                            user_ip.append(getUserIp(line)) 
                            c.execute('insert into user_ip values (?, ?, ?)', getUserIp(line))
                        con.commit()
        except ValueError:
            error = 0
    return user_ip