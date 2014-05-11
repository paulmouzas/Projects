import ftplib

def getFile(ftp, filename):
    f = open(filename, 'wb')
    ftp.retrlines('RETR ' + filename, f.write)
    f.close

def upload(ftp, filename):
    ftp.storlines("STOR " + filename, open(filename, 'r'))
    listDir(ftp)
    
def listDir(ftp):
    files = ftp.nlst()
    for f in files:
        print f
    return
    
def cd(ftp, pathname):
    ftp.cwd(pathname)
    listDir(ftp)

def help():
    print "\n\n"
    print "*" * 10 + " COMMANDS " + "*" * 10
    print "get\t\tDownloads a file."
    print "ls\t\tLists contents of directory."
    print "cd\t\tChanges directories. Type out the full path."
    print "help\t\tPrints this list of commands." 
    print "quit\t\tQuits program."
    print "\n\n"
    
def main():
    url = raw_input("Please enter a url.")
    user = raw_input("Enter your username: ")
    pswd = raw_input("Enter your password: ")
    ftp = ftplib.FTP(url, user, pswd)
    help()
    
    while True:
        query = raw_input("What would you like to do? >").split()
        if len(query) == 1:
            command = query[0]
            if command == 'ls':
                listDir(ftp)
            elif command == 'quit':
                print "Bye!"
                break
            elif command == 'help':
                help()
            else:
                print "Sorry. I didn't get that."
        elif len(query) == 2:
            command, arg = query
            if command == 'get':
                getFile(ftp, arg)
            elif command == 'cd':
                cd(ftp, arg)
            elif command == 'upload':
                upload(ftp, arg)
            else:
                print "Sorry. Invalid command."
if __name__ == '__main__':
    main()