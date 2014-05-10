import ftplib

#url = raw_input("Please enter a url.")
url = "paulmouzas.com"
ftp = ftplib.FTP(url)

#user = raw_input("Enter your username: ")
#pswd = raw_input("Enter your password: ")
user = "paulm7224"
pswd = "luap,mo86"

ftp.login(user, pswd)

def getText(ftp, file):
    pass
    
def listDir(ftp):
    files = ftp.nlst()
    for f in files:
        print f
    return
    
def help():
    print "\n\n"
    print "*"*10 + "COMMANDS" + "*"*10
    print "download\t\tDownloads a file"
    print "ls\t\tLists contents of directory"
    print "cd\t\tChanges directories"
    print "up\t\tBrings you up one directory"
    print "\n\n"

commands = {
    'ls':listDir
    }
    
commands['ls'](ftp)
