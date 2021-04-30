#!/bin/bash

# A script file for Google Colaboratory


# Setting-up
rm -rf warehouse
mkdir warehouse


# https://linux.die.net/man/1/wget
wget -q https://github.com/briefings/credit/raw/develop/warehouse/trace.zip
wget -q -P warehouse https://github.com/briefings/credit/raw/develop/warehouse/baseline.pkl
wget -q -P warehouse https://github.com/briefings/credit/raw/develop/warehouse/model.pkl
wget -q -P warehouse https://raw.githubusercontent.com/briefings/credit/develop/data/testing.csv


# https://linux.die.net/man/1/unzip
rm -rf trace
unzip -u -q trace.zip
rm -r trace.zip