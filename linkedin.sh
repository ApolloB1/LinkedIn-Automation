#!/bin/bash

python -m pip install selenium
python -m pip install pyvirtualdisplay

geckodriver_x86_64='https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz'
geckodriver_x86_32='https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz'

MACHINE_TYPE=`uname -m`

if [ $MACHINE_TYPE == 'x86_64' ]
then
    wget $geckodriver_x86_64
    tar -xvf geckodriver-v0.26.0-linux64.tar.gz
    rm geckodriver-v0.26.0-linux64.tar.gz
    mv geckodriver /usr/sbin
    if [ -e /usr/bin/geckodriver ]
    then
        rm /usr/bin/geckodriver
    fi
    ln -s /usr/sbin/geckodriver /usr/bin/geckodriver
else
    wget $geckodriver_x86_32
    tar -xvf geckodriver-v0.26.0-linux32.tar.gz
    rm geckodriver-v0.26.0-linux32.tar.gz
    mv geckodriver /usr/sbin
    if [ -e /usr/bin/geckodriver ]
    then
        rm /usr/bin/geckodriver
    fi
    ln -s /usr/sbin/geckodriver /usr/bin/geckodriver
fi
