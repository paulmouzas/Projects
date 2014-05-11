import ftplib

def getFile(ftp, filename):
    f = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, f.write)
    f.close
    
def listDir(ftp):
    files = ftp.nlst()
    for f in files:
        print f
    return
    
def help():
    print "\n\n"
    print "*"*10 + " COMMANDS " + "*"*10
    print "get\tDownloads a file"
    print "ls\t\tLists contents of directory"
    print "cd\t\tChanges directories"
    print "up\t\tBrings you up one directory"
    print "help\t\tHelp" 
    print "quit\t\tQuits program"
    print "\n\n"

commands = {
    'ls':listDir,
    'help':help
    }
    
if __name__ == '__main__':
    #url = raw_input("Please enter a url.")
    #user = raw_input("Enter your username: ")
    #pswd = raw_input("Enter your password: ")
    
    url = "paulmouzas.com"
    user = "paulm7224"
    pswd = "luap,mo86"
    ftp = ftplib.FTP(url, user, pswd)
    help()
    
    while True:
        
        query = raw_input("What would you like to do? >").split()
        if len(query) == 1:
            command = query[0]
            if command == 'ls':
                listDir(ftp)
            elif command == 'quit':
                break
        else:
            command, arg = query
            if command == 'get':
                getFile(ftp, arg)
