#!/bin/bash

# A script file for Google Colaboratory

# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log

# logs
rm -rf *.log

# ArViz & PyMC3
pip install yellowbrick &> yellow.log
pip install pymc3==3.11.2 &> pymc3.log

# https://linux.die.net/man/1/wget
wget -q https://github.com/plausibilities/sars/raw/develop/sars.zip

# https://linux.die.net/man/1/unzip
rm -rf credit
unzip -u -q credit.zip
rm -rf credit.zip