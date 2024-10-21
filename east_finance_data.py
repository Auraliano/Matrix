
from typing import List
import requests
def getData(fltt:int,invt:int,fields:List[str],secid:str):

    #fltt=2 表示股票类型为A股。
    #invt=2 表示交易市场为沪市。
    #fields=f120,f121,f122 表示需要获取的字段，f120 代表股票代码，f121 代表股票名称，f122 代表最新价。
    #secid=1.600000 是股票的市场和代码，这里以浦发银行为例。
    #http://push2.eastmoney.com/api/qt/stock/get?fltt=2&invt=2&fields=f120,f121,f122&secid=1.600000

    result:dict[str:str]={}
    fields_str =result_string = ",".join(fields)
    url =f"http://push2.eastmoney.com/api/qt/stock/get?fltt={fltt}&invt={invt}&fields={fields_str}&secid={secid}"
    print(f"request url {url}")
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("请求失败")
    
    data = response.json()
    if 'data' not in data:
        raise Exception("响应中没有 'data' 字段")
    
    print(f"response data: {data['data']}")
    return data['data']



fields =["f120","f121","f122"]
data=getData(fltt=2,invt=2,fields=fields,secid="1.600000")