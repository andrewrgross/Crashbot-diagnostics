#!/bin/bash

# Send the hostname and wifi network to slack on startup

. /etc/profile
#. ~/.bash_profile
. ~/.bashrc
#printenv >/home/crashbot/Crashbot-diagnostics/out

#/opt/ros/melodic/bin/roslaunch create_bringup create_2.launch >> /home/crashbot/Crashbot-diagnostics/temp
python /home/crashbot/Desktop/crashbot-startup.py >/home/crashbot/Crashbot-diagnostics/startupScriptOut 2>/home/crashbot/Crashbot-diagnostics/startupScripterr
