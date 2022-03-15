import json
from time import strftime, sleep

import requests as requests


def say():
    # 用户代理，使得服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    # 抓取包的网址
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/714c63f8-075d-4d20-b69c-246ac48d9da1'
    res = requests.get(url, headers=head)
    # 获取所需信息
    dict1 = json.loads(res.text)
    print('----------'+'商品:'+dict1['data']['name']+'----------') #商品名
    print('规格:' + dict1['data']['spec']) #规格
    print('价格:' + str(int(dict1['data']['price'])/100)) #价格
    print('原价/折扣价:' + str(int(dict1['data']['market_price'])/100)+'/'+str(int(dict1['data']['price'])/100)) #原价与折扣价
    print('详细内容:' + dict1['data']['share_content']) #详细内容
    print('')
    print('----------'+'"'+ dict1['data']['name'] +'"'+'的价格波动'+ '----------')
    # 通过精确实时记录价格
    try:
        # 每4秒记录一次抓取商品的信息
        while (True):
            nowtime = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + str(int(dict1['data']['price'])/100))
            print(nowtime)
            sleep(4)

    except:
        print("运行完成")
    if __name__ == '__main__':
        say()