#!/usr/bin/env python
# coding=utf-8
import config as cfg
import email_utils as mail
import time
import requests
import json
import sys
import log_utils as log


REQ_URL = "https://act.cmbchina.com/ActShipMobile/api/actshipprd/ACT20191009111228Y6pWLw23"

log.init(cfg)

if not mail.init(cfg):
    log.error("[-] Mail system init faild, please check the config.py")
    sys.exit(0)

log.log("[+] OK!")

if cfg.SEND_EMAIL_ON_STARTUP:
    mail.send_email("Congratulations! Your server started successfully!")

query_times = 0

while True:
    error_msg = None
    try:
        resp = requests.get(REQ_URL)
        if resp.status_code != 200:
            raise Exception("Got a wrong code: %d"%resp.status_code)
        result_obj = json.loads(resp.text)
        stock = result_obj[0]["prdstock"]
        if stock != "0":
            # Send email to notify user
            mail.send_email("Congratulations! Stock Updated! Rest: %s !!!!!"%stock)
            log.log("[+] Stock updated! %s"%stock)
        else:
            log.log("[-] No stock")
    except Exception as err:
        error_msg = err

    if error_msg != None:
        log.error("[-] An error raised: %s"%error_msg)
        if cfg.SEND_ERROR_LOG:
            mail.send_email("An error raised: %s"%error_msg)
            
    if cfg.SEND_SERVER_RUNNING_EMAIL:
        query_times = query_times + 1
        if query_times == cfg.SEND_SERVER_RUNNING_EMAIL_INTERVAL:
            mail.send_email("Server running!\nLast ten log\n"+log.getLastTenLog())
            query_times = 0

    time.sleep(cfg.QUERY_INTERVAL)
