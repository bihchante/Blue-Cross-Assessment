# Blue-Cross-Assessment: file_transfer_app
I run a cronjob to move files from nfs location (source) to server location using python3 where ansible will be running
create dockerfile specifying base image, python program to help in moving files, location to cpoy files, execute the python program
monunt nfs location
create ansible playbook 
- specifying FTP instalation, 
- start firewall service (since it isalready pressent on my ubuntu server)
- start FTP server
- expose ports 21 (FTP Control)  and 20 (FTP data transfer)
- user and user password
- path: /srv/ftp (by default)
- modify FTPd configuration file as per requirement
create persistent voulume
create persistent volume claim to specify how much volume to claim
create .gitlab-ci.yml
