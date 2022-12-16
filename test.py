#!/usr/bin/env python
import os
import ftplib
file_to_upload = "/opt/src/*"
server = '192.168.43.1'
username = 'ftpuser'
password = 'ftpuserpwd'
ftp_connection = ftplib.FTP(server, username, password)
remote_path = "/temp/"
ftp_connection.cwd(remote_path)
fh = open(file_to_upload, 'rb')
ftp_connection.storbinary('STOR %s' % os.path.basename(file_to_upload), fh)
fh.close()

