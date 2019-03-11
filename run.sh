#!/bin/bash

clear
echo "Checking/Installing dependencies"
apt install python3.6 -y
clear
echo "Installed python3.6"

pip3 install discord.py
clear
echo "Installed discord.py"
pip3 install requests
clear
echo "Installed requests"

if [ ! -f /home/lulaz/Desktop/Ll/files/token.txt ]; then
    echo "Token.txt not found, create one inside files/ with the respective token for the bot"
fi

chmod +x bot.py

clear

./bot.py
