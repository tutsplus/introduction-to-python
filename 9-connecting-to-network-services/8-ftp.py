import ftplib

def list_files():
    ftp_client = ftplib.FTP('ftp.kernel.org', 'anonymous', 'jensendp@gmail.com')
    ftp_client.cwd('/pub/linux/kernel/v4.x')
    files = ftp_client.dir()
    print files

    changelogFile = open('ChangeLog-4.0.1.txt', 'wb')

    ftp_client.retrbinary('RETR ChangeLog-4.0.1', changelogFile.write)
    changelogFile.close()
    ftp_client.quit()

if __name__ == '__main__':
    list_files()
