import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))  # config.py路径

LOG_PATH = BASE_PATH + "/logs/app.log"  # 程序日志文件路径
ERR_PATH = BASE_PATH + "/logs/"  # 标准输出文件重定向路径
PID_PATH = BASE_PATH + "/pid/"
BINANCE_API_KEY = "CXIoBPigpTjF3WGktkHjjF86QYBZUrNZh0517KAMucTXE0t2ExV7NJRmnfs8v9sS"
BINANCE_API_SECRET = "hfZPOMyE1IUgd2r5VxCAy7XL3hSWWLoPNcyV0dcDmrfVbrodaQlNTnyWpQ3mX8m4"
# BINANCE_API_KEY = "BsPqdk6eO4TmHMlFzIg61f0M44UeyBoO65dXyvjmD9duNyHhTSxE9d9MieZmuOoJ"
# BINANCE_API_SECRET = "sLOD5GSHSFytaoWXperTQaSNXgP8jf42yG4l2wrxW7aCSwxIFT3fJXU7MyQSDQta"
DINGDING_BOT = "https://oapi.dingtalk.com/robot/send?access_token=6f9e7e9b9e46f9b23b6055c414893d3bf77d5079f4eaebe7049d8de320c1b582"
DINGDING_KEYWORD = "now:"
