#! /bin/bash

sudo pip install feedparser

sudo aptitude install festival festlex-cmu festlex-poslex festvox-kallpc16k libestools1.2 festvox-ellpc11k

sudo chmod +x  news.sh
sudo cp news.sh /bin/news.sh

sudo chmod +x stop_news.sh
sudo cp stop_news.sh /bin/stop_news.sh


echo "Add voice, cpy the folder JuntaDeAndalucia_es_sf_diphon /usr/share/festival/voices/spanish "

echo "Add chanels on the file chanels.conf (max 9)"

echo "Add the script news.sh to Lily manage"
