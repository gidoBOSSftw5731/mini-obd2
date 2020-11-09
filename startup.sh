#!/bin/sh
#use sh for some security
# you know, it is plugged into your 2 ton death machine
#  just sayin'

#please do this as root or something reasonable
#please?

rfcomm bind rfcomm0 11:22:33:dd:ee:ff

#you'll be changing this
#if you care enough to solder this and put it in your car, I think
# you can edit one god damn file or make a PR with a config
while true; do sudo -u gido5731 python3 /home/gido5731/mini-obd2/main.py; done
