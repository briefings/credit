#!/bin/bash

# A script file for Google Colaboratory

# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log

# Setting-up
rm -rf log
rm -rf config.py
mkdir logs

# Packages
pip install yellowbrick==1.3.post1 &> logs/yellow.log
pip install pymc3==3.11.2 &> logs/pymc3.log
pip install cloudpickle==1.6.0 &> logs/cloudpickle.log
pip install dask[complete]==2.30.0 &> logs/dask.log

# https://linux.die.net/man/1/wget
wget -q https://github.com/briefings/risk/raw/develop/risk.zip
wget -q https://raw.githubusercontent.com/briefings/risk/develop/config.py

# https://linux.die.net/man/1/unzip
rm -rf risk
unzip -u -q risk.zip
rm -rf risk.zip
