#! /bin/bash

chanel=$(cat "/tmp/chanel") 

if [[ $chanel == *"1"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 1 
fi

if [[ $chanel == *"2"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 2 
fi

if [[ $chanel == *"3"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 3 
fi

if [[ $chanel == *"4"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 4 
fi

if [[ $chanel == *"5"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 5 
fi

if [[ $chanel == *"6"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 6 
fi

if [[ $chanel == *"7"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 7 
fi

if [[ $chanel == *"8"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 8 
fi

if [[ $chanel == *"9"* ]]
then
  sh ~/Plugin/NEWS/startReadNews.sh 9 
fi
