import os, time
print("Script by Abhay Vachhani")
print("Run script with sudo")
print("When ask to root password press enter don't type any password")
time.sleep(5)
# ----- Install -----
os.system("sudo apt install -y apache2 php mysql-server libapache2-mod-php php-mysql php-mbstring php-gettext php-xml")
if not os.path.exists("phpMyAdmin-5.1.0-all-languages.zip"):
    os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.1.0/phpMyAdmin-5.1.0-all-languages.zip")

if not os.path.exists("phpMyAdmin-5.1.0-all-languages"):
    os.system("sudo unzip phpMyAdmin-5.1.0-all-languages.zip")

if not os.path.exists("phpmyadmin"):
    os.system("mv phpMyAdmin-5.1.0-all-languages phpmyadmin")

if not os.path.exists("/var/www/html/phpmyadmin"):
    os.system("sudo cp -r phpmyadmin /var/www/html/")

os.system("sudo chmod +777 /var/www/html/phpmyadmin")
os.system("sudo cp /var/www/html/phpmyadmin/config.sample.inc.php /var/www/html/phpmyadmin/config.inc.php")

# ----- Install -----

# ----- Change PassAuth -----
with open('/var/www/html/phpmyadmin/config.inc.php', 'r') as fp:
    old = fp.readlines()
new = ''
for i in old:
    # print(i.encode())
    if i == "$cfg['Servers'][$i]['AllowNoPassword'] = false;\n":
        new += "$cfg['Servers'][$i]['AllowNoPassword'] = true;\n"
        continue
    if i == "$cfg['blowfish_secret'] = ''; /* YOU MUST FILL IN THIS FOR COOKIE AUTH! */\n":
        new += "$cfg['blowfish_secret'] = 'ASDFGHJKLQWERTYUIOPZXCVBNM123456'; /* YOU MUST FILL IN THIS FOR COOKIE AUTH! */\n"
        continue
    new += i
with open('/var/www/html/phpmyadmin/config.inc.php', 'w') as fp:
    fp.write(new)
# ----- Change PassAuth -----

# ----- Change Port -----
with open('/etc/apache2/ports.conf', 'r') as fp:
    old = fp.readlines()
new = ''
for i in old:
    # print(i.encode())
    if i == 'Listen 80\n':
        new += 'Listen 8080\n'
        continue
    new += i
with open('/etc/apache2/ports.conf', 'w') as fp:
    fp.write(new)
# ----- Change Port -----
if not os.path.exists("/usr/bin/start_server"):
    with open('/usr/bin/start_server', 'w') as fp:
        fp.write("sudo service apache2 start\nsudo service mysql start")
    os.system("sudo chmod +x /usr/bin/start_server")

if not os.path.exists("/usr/bin/stop_server"):
    with open('/usr/bin/stop_server', 'w') as fp:
        fp.write("sudo service apache2 stop\nsudo service mysql stop")
    os.system("sudo chmod +x /usr/bin/stop_server")

if not os.path.exists("/usr/bin/status_server"):
    with open('/usr/bin/status_server', 'w') as fp:
        fp.write("sudo service apache2 status\nsudo service mysql status")
    os.system("sudo chmod +x /usr/bin/status_server")

# os.system('sudo service mysql start')
# os.system('sudo service apache2 start')

print(':~ Type sudo mysql')
print(':~ when mysql open type "ALTER USER \'root\'@\'localhost\' IDENTIFIED WITH mysql_native_password BY \'\';"')
print(':~ after type "FLUSH PRIVILEGES;"')
print(':~ after type "exit" to exit from mysql')
print('\t\t Thank you')
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
# FLUSH PRIVILEGES;