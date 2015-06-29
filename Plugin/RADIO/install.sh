#! /bin/bash


sudo chmod +x radio.sh
sudo cp radio.sh /bin/radio.sh

sudo chmod +x stop_radio.sh
sudo cp stop_radio.sh /bin/stop_radio.sh
	
sudo apt-get install mpc

echo ""
echo "for add new streaming radio use one terminal and save to list1"
echo "mpc add"
echo "for example for add Flaix FM"
echo "mpc add http://176.31.246.109:8000/flaixfm"
echo "mpc save list1"


echo ""
echo "Add radio.sh to Lily manage of CHANEL_RADIO"
