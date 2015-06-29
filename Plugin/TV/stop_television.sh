#! /bin/bash

tv=$(cat ~/Plugin/TV/tvname.conf)  

irsend SEND_ONCE $tv KEY_POWER
