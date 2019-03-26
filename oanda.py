# 必要なライブラリの読み込み
import pandas as pd
import oandapy
import datetime
from datetime import datetime, timedelta
import pytz
# API接続設定のファイルを読み込む
import configparser
 
# 設定
config = configparser.ConfigParser()
config.read('./config/config_v1.txt') # パスの指定が必要です
account_id = config['oanda']['account_id']
api_key = config['oanda']['api_key']
instruments = config['oanda']['instruments']
environment = config['oanda']['environment']
 
# APIへ接続
oanda = oandapy.API(environment=environment, access_token=api_key)
 
# ドル円の現在のレートを取得
res = oanda.get_prices(instruments=instruments)
 
# 中身を確認
print(res)

# 文字列 -> datetime
def iso_to_jp(iso):
    date = None
    try:
        date = datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S.%fZ')
        date = pytz.utc.localize(date).astimezone(pytz.timezone("Asia/Tokyo"))
    except ValueError:
        try:
            date = datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S.%f%z')
            date = date.astimezone(pytz.timezone("Asia/Tokyo"))
        except ValueError:
            pass
    return date

# datetime -> 表示用文字列
def date_to_str(date):
    if date is None:
        return ''
    return date.strftime('%Y/%m/%d %H:%M:%S')

# ドル円の現在のレートを取得
res = oanda.get_prices(instruments=instruments)

print(date_to_str(iso_to_jp(res['prices'][0]['time'])))

# 口座の基本情報
res_acct = oanda.get_accounts()
print(res_acct)


# 口座の詳細情報
res_acct_detail = oanda.get_account(account_id)
print(res_acct_detail)


# 成行注文
order_1 = oanda.create_order(accountId=account_id,
                              instrument = instruments,
                              units=10000,
                              side="sell",
                              type="market")
order_1 = orders.OrderCreate(
        account_id,
        data=MarketOrderRequest(instrument=instruments, units=1).data)


# 確認
print(order_1)


 
