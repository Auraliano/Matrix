class Data:

    dt = []
    open = []
    high = []
    close = []
    low =[]
    volume = []
    

    @classmethod
    def bar_generator(ticket):

        #open 开盘价
        #high 最高价
        #close 收盘价
        #low 最低价

        has_created_bar=False
        if(ticket[0].minute % 5 ==0 and has_created_bar is False):
            has_created_bar =True
            Data.dt.insert(0,ticket[0])
            Data.open.insert(0,ticket[1])
            Data.high.insert(0,ticket[1])
            Data.close.insert(0,ticket[1])
            Data.low.insert(0,ticket[1])
        else:
            #更新当前价
            Data.close[0] =ticket[1]
            Data.dt[0]=ticket[0]
            # 更新最低价
            if(ticket[1] < Data.low[0]):
                Data.low[0] =ticket[1]
            # 更新最高价格
            if(ticket[1] > Data.high[0]):
                Data.high[0]=ticket[1]