#! /bin/bash

sudo apt-get install lirc

echo " "
echo "Add this to your /etc/modules file:"
echo "If you like to change the IR receiver or transmitter GPIO, change the gpio_in_pin or gpio_out_pin value "
echo ""
echo "lirc_dev"
echo "lirc_rpi gpio_in_pin=2 gpio_out_pin=3"
echo " "
read -p "Press any key for continue..."

sudo rm /etc/lirc/hardware.conf
sudo cp hardware.conf /etc/lirc/hardware.conf


sudo /etc/init.d/lirc stop
sudo /etc/init.d/lirc start

sudo chmod +x television.sh
sudo cp television.sh /bin/

echo "Edit your /boot/config.txt file and add:"
echo "If you like to change the IR receiver or transmitter GPIO, change the gpio_in_pin or gpio_out_pin value "
echo ""
echo "dtoverlay=lirc-rpi,gpio_in_pin=2,gpio_out_pin=3"
read -p "Press any key for continue..."

echo "Now you need to configure the remote for your tv, you can found the file config here:"
echo "http://lirc.sourceforge.net/remotes/"
echo "if you found the file, download and change it to /etc/lirc/lircd.conf"
echo "open the file and take the name of the remotefor example: PHILIPS_15PF4121 , and put the name to the file remote.conf in ~/Plugins/TV/remote.conf"
echo ""
echo "if you can't found your file, I hope you be to luky with the next setup steps:"
echo " Stop lirc to free up /dev/lirc0 "
echo "sudo /etc/init.d/lirc stop"

echo "Create a new remote control configuration file (using /dev/lirc0) and save the output to ~/lircd.conf"
echo "irrecord -d /dev/lirc0 ~/lircd.conf"

echo "Make a backup of the original lircd.conf file"
echo "sudo mv /etc/lirc/lircd.conf /etc/lirc/lircd_original.conf"

echo "Copy over your new configuration file"
echo "sudo cp ~/lircd.conf /etc/lirc/lircd.conf"

echo "Start up lirc again"
echo "sudo /etc/init.d/lirc start"

echo "you can found more information on http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/"

echo "Finish, now add the script television.sh on the lilymanage with name CHANEL_TV"

