#! /bin/bash

chanel=$(cat "/tmp/chanel") 
tv=$(cat ~/Plugin/TV/tvname.conf)  


if [[ $chanel == *"1"* ]]
then
  irsend SEND_ONCE $tv KEY_1
fi

if [[ $chanel == *"2"* ]]
then
  irsend SEND_ONCE $tv KEY_1
fi

if [[ $chanel == *"3"* ]]
then
  irsend SEND_ONCE $tv KEY_3
fi

if [[ $chanel == *"4"* ]]
then
  irsend SEND_ONCE $tv KEY_4
fi

if [[ $chanel == *"5"* ]]
then
  irsend SEND_ONCE $tv KEY_5
  mpc play 5
fi

if [[ $chanel == *"6"* ]]
then
  irsend SEND_ONCE $tv KEY_6
fi

if [[ $chanel == *"7"* ]]
then
  irsend SEND_ONCE $tv KEY_7
fi

if [[ $chanel == *"8"* ]]
then
  irsend SEND_ONCE $tv KEY_8
fi

if [[ $chanel == *"9"* ]]
then
  irsend SEND_ONCE $tv KEY_9
fi

