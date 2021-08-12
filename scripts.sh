#!/bin/bash

# A script file for Google Colaboratory


# TeX
# apt-get install texlive-latex-extra  &> tex.log
# apt-get install ghostscript &>> tex.log
# apt-get install dvipng &>> tex.log


# Directories
rm -rf warehouse
mkdir warehouse && mkdir warehouse/model

rm -rf logs
mkdir logs


# Packages
pip install yellowbrick==1.3.post1 &> logs/yellow.log
pip install pymc3==3.11.2 &> logs/pymc3.log
pip install cloudpickle==1.6.0 &> logs/cloudpickle.log
pip install dask[complete]==2.30.0 &> logs/dask.log
pip install scikit-learn==0.24.2 &> logs/learn.log
pip install imbalanced-learn==0.8.0 >> logs/learn.log


# https://linux.die.net/man/1/wget
wgqt -q https://github.com/exhypotheses/risk/raw/develop/risk.zip

wget -q -P warehouse/model https://raw.githubusercontent.com/exhypotheses/risk/master/warehouse/model/model.gv
wget -q -P warehouse/model https://github.com/exhypotheses/risk/raw/master/warehouse/model/pocket.pkl
wget -q -P warehouse/model https://github.com/exhypotheses/risk/raw/master/warehouse/model/trace.zip


# https://linux.die.net/man/1/unzip
rm -rf trace
unzip -u -q -d . warehouse/model/trace.zip
rm -rf trace.zip

rm -rf risk
unzip -u -q risk.zip
rm -rf risk.zip
