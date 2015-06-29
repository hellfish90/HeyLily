#! /bin/bash

chanel=$(cat "/tmp/chanel") 
mpc load list1


if [[ $chanel == *"1"* ]]
then
  echo "play 1";
  mpc play 1
fi

if [[ $chanel == *"2"* ]]
then
  echo "play 2";
  mpc play 2
fi

if [[ $chanel == *"3"* ]]
then
  echo "play 3";
  mpc play 3
fi

if [[ $chanel == *"4"* ]]
then
  echo "play 4";
  mpc play 4
fi

if [[ $chanel == *"5"* ]]
then
  echo "play 5";
  mpc play 5
fi

if [[ $chanel == *"6"* ]]
then
  echo "play 6";
  mpc play 6
fi

if [[ $chanel == *"7"* ]]
then
  echo "play 7";
  mpc play 7
fi

if [[ $chanel == *"8"* ]]
then
  echo "play 8";
  mpc play 8
fi

if [[ $chanel == *"9"* ]]
then
  echo "play 9";
  mpc play 9
fi

if [[ $chanel == *"10"* ]]
then
  echo "play 10";
  mpc play 10
fi
