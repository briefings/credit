#!/bin/bash

# A script file for Google Colaboratory

# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log


# Setting-up
rm -rf log
rm -rf config.py
rm -rf warehouse

mkdir logs
mkdir warehouse


# Packages
pip install yellowbrick==1.3.post1 &> logs/yellow.log
pip install pymc3==3.11.2 &> logs/pymc3.log
pip install cloudpickle==1.6.0 &> logs/cloudpickle.log
pip install dask[complete]==2.30.0 &> logs/dask.log


# https://linux.die.net/man/1/wget
wget -q https://github.com/briefings/credit/raw/develop/credit.zip
wget -q https://github.com/briefings/credit/raw/develop/warehouse/trace.zip
wget -q https://raw.githubusercontent.com/briefings/credit/develop/config.py

wget -q -P warehouse https://github.com/briefings/credit/raw/develop/warehouse/baseline.pkl
wget -q -P warehouse https://github.com/briefings/credit/raw/develop/warehouse/model.pkl
wget -q -P warehouse https://raw.githubusercontent.com/briefings/credit/develop/data/testing.csv


# https://linux.die.net/man/1/unzip
rm -rf credit
unzip -u -q credit.zip
rm -rf credit.zip

rm -rf trace
unzip -u -q trace.zip
rm -r trace.zip