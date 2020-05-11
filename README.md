# RaspberryVoiceControl
Its possible to control gpio pins of raspberry with voice

First you need to install some modules to the raspberry system, one of them is libttspico-utils, its possible that this module will not being compatible with your raspberry, it depends on the version of the last one.
Then its important to change the user that will execute apache2 in raspberry.
## Use the command
	sudo nano /etc/apache2/envvars, an document will be open then you put this code: 
        export APACHE_RUN_USER=pi
	      export APACHE_RUN_GROUP=pi

Save and exit, the its necessary to create a directory to save the certifications, use sudo mkdir /etc/apache2/ssl command and then sudo openssl req -x509 -nodes -days 1095 -newkey rsa:2048 -out /etc/apache2/ssl/server.crt -keyout /etc/apache2/ssl/server.key
#
Something like certificate image you maybe see, and you can complete with your personal information.
Then you need to enable Apache modules, use sudo a2enmod ssl command.
Then create connection with the apache2 configuration, use 
# sudo ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/000-default-ssl.conf      command
Then we have to edit the certificate path, use sudo nano /etc/apache2/sites-enabled/000-default-ssl.conf command, then find and change as this:
                   SSLCertificateFile     /etc/apache2/ssl/server.crt
                   SSLCertificateKeyFile    /etc/apache2/ssl/server.key
Finally re-start apache2, use sudo /etc/init.d/apache2 restart command.
All the archive have to be copy in this path: /var/www/html
And then you can introduce the raspberry ip in your favorite browser and give the necessary permission.

NOTE: you can control your raspberry with differents programs like putty or MobaXterm.
      Open the php code, to see the voice commands you can use, to enable differents GPIO pins of the raspberry
