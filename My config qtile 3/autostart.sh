#!/bin/sh


autorandr --load bettersetup
nitrogen --restore & 
#picom

picom -b --config ~/.config/qtile/picomqtile/picom.conf

blueman-applet
volctl &
greenclip daemon 


