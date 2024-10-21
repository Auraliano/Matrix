from time import sleep
from datetime import datetime, time
from dateutil import parser
import requests

def get_history_data_from_local():
    dt = []
    open = []
    high = []
    close = []
    low =[]
    volume = []

    return dt, open, high, close, low,volume


def bar_generator(ticket,dt,open,high,close,low,volume):

    #open 开盘价
    #high 最高价
    #close 收盘价
    #low 最低价

    has_created_bar=False
    if(ticket[0].minute % 5 ==0 and has_created_bar is False):
        has_created_bar =True
        dt.insert(0,ticket[0])
        open.insert(0,ticket[1])
        high.insert(0,ticket[1])
        close.insert(0,ticket[1])
        low.insert(0,ticket[1])
    else:
        #更新当前价
        close[0] =ticket[1]
        dt[0]=ticket[0]
        # 更新最低价
        if(ticket[1] < low[0]):
            low[0] =ticket[1]
        # 更新最高价格
        if(ticket[1] > high[0]):
            high[0]=ticket[1]



def buy():
    pass

def sell():
    pass

def strategy(dt,open,high,close,volume):
    # 策略函数，根据tick信息执行交易策略
    # 请注意，这里的策略函数不完整，需要您根据实际策略来实现
    ma20=0
    total_price=0
    for i in close[0:20]:
        total_price +=close[i]
    ma20 =total_price /20 

    if(close[0]<= ma20 *0.8):
        buy()
    elif(close[0]>= ma20 * 1.05):
        sell()
    else:
        pass


def getTick():
    # 访问新浪财经接口获取最新的股票行情信息
    page = requests.get("http://hq.sinajs.cn/?format=text&list=sh600000")
    stock_info = page.text

    # 解析股票信息
    mt_info = stock_info.split(",")

    # 获取最新的价格和交易时间
    last = float(mt_info[1])
    trade_datetime = mt_info[30] + '' + mt_info[31]

    # 构造tick对象，包含最新价格和交易时间
    tick = (last, trade_datetime)
    return tick

# 设置交易时间，从早上9:30到下午3:00
trade_time = time(9, 30)
while time(9, 0) <= trade_time <= time(15, 0):
    last_tick = getTick()

    dt, open, high, close,low,volume =get_history_data_from_local()
    # 调用策略函数
    bar_generator(last_tick,dt=dt,open=open,high=high,close=close,low=low,volume=0)
    strategy(dt=dt,open=open,high=high,close=close,low=low,volume=0)

    # 解析tick中的时间
    trade_time = parser.parse(last_tick[1]).time()

    # 等待一段时间，这里是3秒
    sleep(3)

print("job done")





