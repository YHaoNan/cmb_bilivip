#!/usr/bin/env python
# coding=utf-8
import config as cfg
import email_utils as mail
import time
import requests
import json
import sys

REQ_URL = "https://act.cmbchina.com/ActShipMobile/api/actshipprd/ACT20191009111228Y6pWLw23"

if not mail.init():
    print("[-] Mail system init faild, please check the config.py")
    sys.exit(0)
print("[+] OK!")

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
            mail.send_email("Stock Updated! Rest: %s !!!!!"%stock)
            print("[+] Stock updated! %s"%stock)
        else:
            print("[-] No stock")
    except Exception as err:
        error_msg = err

    if error_msg != None:
        print("[-] An error raised: %s"%error_msg)
        if cfg.SEND_ERROR_LOG:
            mail.send_email("An error raised: %s"%error_msg)

    time.sleep(cfg.QUERY_INTERVAL)
