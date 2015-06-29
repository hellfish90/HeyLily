#! /bin/bash

rm ~/Plugin/NEWS/festival_news.festival
touch ~/Plugin/NEWS/festival_news.festival
python ~/Plugin/NEWS/parseUrl.py $1 
festival ~/Plugin/NEWS/festival_news.festival & 
echo $! > /tmp/pid_news
exit 1
