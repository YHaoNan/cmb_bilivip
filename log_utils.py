#!/usr/bin/env python
# coding=utf-8

import logging

logger = None
cfg = None

def init(config):
    global logger , cfg
    cfg = config
    logger = logging.getLogger("cmb_bilivip")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(cfg.LOG_FILE)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s  - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)

def log(msg):
    logger.info(msg)

def error(msg):
    logger.error(msg)

def getLastTenLog():
    string = ""
    with open(cfg.LOG_FILE,"r") as f:
        content = f.read()
        lineArr = content.split('\n')
        for i in range(max(0,len(lineArr) - 11) ,len(lineArr)):
            print(i)
            string = string + lineArr[i] + "\n"
    return string
