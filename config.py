#!/usr/bin/env python
# coding=utf-8

# 使用的SMTP服务器
SMTP_SERVER = "smtp.qq.com"

# 使用的SMTP服务器的端口 Int
SMTP_PORT = 465

# 你使用的发信邮箱的帐号
SENDER_ACCOUNT = ""

# 接收者帐号，可以设置多个
RECIVER_ACCOUNTS = []

# 发信人的用户名
SENDER_UNAME = ""

# 身份认证密码
SENDER_TOKEN = ""

# 查询招商银行服务器间隔 秒
QUERY_INTERVAL = 60

# 是否向目标邮箱发送错误日志
SEND_ERROR_LOG = True

# 运行产生的日志文件
LOG_FILE = "./log"

# 是否发送邮件通知用户服务器已启动
SEND_EMAIL_ON_STARTUP = True

# 是否发送服务器运转正常邮件
SEND_SERVER_RUNNING_EMAIL = True

# 发送服务器运转正常邮件的周期，即相隔几个QUERY_INTERVAL向用户发送邮件，示例中是60个，即一小时
SEND_SERVER_RUNNING_EMAIL_INTERVAL = 60
