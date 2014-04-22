'''
Created on 17 avr. 2014

@author: admin
'''
from os import listdir
from os.path import isfile, isdir, join

def detailDb(c):
    """
    View num of row and content
    """
    c.execute("SELECT Name from files")
    files = c.fetchall()
    if files . __len__() > 0:
        print ">> Sum of row (" + str(files . __len__()) + ") in table 'files' ('Name')"
        print ">> -- example: " + str(files[0])

def getNameFiles(mypath):
    files = []
    for d in listdir(mypath):
        if isdir(join(mypath,d)):
            for f in listdir( mypath + d ):
                if isfile( join( mypath + d,f ) ) :
                    files.append(d + "/" + f)
    return files

def cleanDb(c):
    """
    Drop table
    """
    c.execute("DROP TABLE IF EXISTS files")

def getList(c):
    """
    Return list
    """
    c.execute("SELECT Name from files")
    return c.fetchall()

def getFiles(c,con, mypath):
    tableexist = 0;
    try:
        c.execute("SELECT * FROM sqlite_master WHERE name ='files' and type='table'; ")
        tableexist = c.fetchone()
    except ValueError:
        error = 0
    if tableexist == None:
        c.execute("DROP TABLE IF EXISTS files")
        c.execute("CREATE TABLE files(Name TEXT)")
        files = getNameFiles(mypath)
        for item in files:
            c.execute('insert into files values (?)', (item,))
            con.commit()
    else:
        c.execute("SELECT Name from files")
        files = c.fetchall()
    return files