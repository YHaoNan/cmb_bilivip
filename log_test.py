#!/usr/bin/env python
# coding=utf-8

import config as cfg
import log_utils as log
log.init(cfg)
log.log("Asdf")
log.error("asdf")

print(log.getLastTenLog())
