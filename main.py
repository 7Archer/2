import json
from time import strftime, sleep

import requests as requests


def say():
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    url='https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/714c63f8-075d-4d20-b69c-246ac48d9da1'
    res = requests.get(url, headers=head)
    dict1 = json.loads(res.text)
    print('----------'+'商品:'+dict1['data']['name']+'----------')
    print('规格:' + dict1['data']['spec'])
    print('价格:' + str(int(dict1['data']['price'])/100))
    print('原价/折扣价:' + str(int(dict1['data']['market_price'])/100)+'/'+str(int(dict1['data']['price'])/100))
    print('详细内容:' + dict1['data']['share_content'])
    print('')
    print('----------'+'"'+ dict1['data']['name'] +'"'+'的价格波动'+ '----------')
    try:
        while (True):
            nowtime = strftime('%Y' + '-' + '%m' + '-' + '%d' + ' %H:%M:%S,价格为' + str(int(dict1['data']['price'])/100))
            print(nowtime)
            sleep(3)
    except:
        print("运行完成")
if __name__ == '__main__':
    say()