'''
Created on 18 avr. 2014

@author: admin
'''
def detailDb(c):
    """
    View num of row and content
    """
    c.execute("SELECT username, ip, intip, fromip, toip, country from results")
    results = c.fetchall()
    if results . __len__() > 0:
        print ">> Sum of row (" + str(results . __len__()) + ") in table 'results' ('username, ip, intip, fromip, toip, country')"
        print ">> -- example: " + str(results[0])

def cleanDb(c):
    """
    Drop table
    """
    c.execute("DROP TABLE IF EXISTS results")

def getList(c):
    """
    Return list
    """
    c.execute("SELECT username, ip, intip, fromip, toip, country from results")
    results = c.fetchall()

def getResults(c, con, user_ip, intcountry):
    numUserIp = user_ip . __len__()
    # get intcountry
    tableexist = 0;
    try:
        c.execute("SELECT * FROM sqlite_master WHERE name ='results' and type='table'; ")
        tableexist = c.fetchone()
    except ValueError:
        error = 0
    extractformfile = False
    if tableexist != None:
        c.execute("SELECT username, ip, intip, fromip, toip, country from results")
        results = c.fetchall()
        #print intcountry . __len__()
        if results . __len__() == 0:
            extractformfile = True
    else:
        extractformfile = True
    if tableexist == None:
        c.execute("CREATE TABLE results(username TEXT, ip TEXT, intip INT, fromip INT, toip INT, country TEXT)")
        results = []
        num = 0
        for i in user_ip:
            for j in intcountry:
                if i[2] > j[0]:
                    if i[2] < j[1]:
                        results.append([ str( i [ 0 ] ) , str( i [ 1 ] ), i [ 2 ], j [ 0 ], j [ 1 ], str( j [ 2 ] ) ] )
                        c.execute('insert into results values (?, ?, ?, ?, ?, ?)', ([ str( i [ 0 ] ) , str( i [ 1 ] ), i [ 2 ], j [ 0 ], j [ 1 ], str( j [ 2 ] ) ] ))
                        num = num + 1
                        print str(num) + " / " + str(numUserIp)
                        con.commit()
    else:
        c.execute("SELECT username, ip, intip, fromip, toip, country from results")
        results = c.fetchall()
    return results