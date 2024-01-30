from selenium import webdriver
from selenium.webdriver.edge.service import Service
from lxml import etree
dct = {'GBP':'英镑','HKD':'港元','USD':'美元','CHF':'瑞士法郎','SGD':'新加坡元','SEK':'瑞典克朗','DKK':'丹麦克朗','NOK':'挪威克朗','JPY':'日元','CAD':'加拿大元','AUD':'澳大利亚元','EUR':'欧元','MOP':'澳门元','PHP':'菲律宾比索','THP':'泰国铢','NZD':'新西兰元','KRW':'韩元','SUR':'卢布','MYR':'林吉特',"TWD":'新台币','ESP':'西班牙比塞塔','ITL':'意大利里拉',"NLG":'荷兰盾',"BEF":'比利时法郎',"FIM":'芬兰马克','IDR':'印尼卢比','BRL':'巴西里亚尔','AED':'阿联酋迪拉姆','INR':'印度卢比','ZAR':'南非兰特','SAR':'沙特里亚尔','TRL':'土耳其里拉'}
# 该网站上只有这些可查询的外汇币种
def get_exchange_rate(date,exchange):
    date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    exchange = dct[exchange]
    # 将货币从标准符号改为查询条件中的中文名称
    url = f"https://srh.bankofchina.com/search/whpj/search_cn.jsp?erectDate={date}&nothing={date}&pjname={exchange}" # post请求该网站信息，与原网站不同，可以通过一个post请求完成
    path = r'C:\Users\VernonGe\Desktop\msedgedriver.exe'
    service = Service(executable_path=path)
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    driver.get(url=url)
    res = driver.page_source
    html = etree.HTML(res)
    for record_index in range(2,22):# 一夜有二十条信息，获得任意一条即可，然而现汇卖出价可能未记录，搜寻整个网页的现汇卖出价，同时不存在记录的可能性较小
        exchange_rate_xpath = f'/html/body/div/div[4]/table/tbody/tr[{record_index}]/td[4]/text()' #现汇卖出价的xpath路径
        res = html.xpath(exchange_rate_xpath)
        if len(res) == 0: #判断是否有记录
            continue
        else:
            break
    res = res[0].split('\n')[0]
    return res
if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    date = s[0]
    exchange = s[1]
    output_path = r'C:\Users\VernonGe\Desktop\result.txt'
    res = get_exchange_rate(date,exchange)
    fp = open(output_path,'w')
    fp.write(f'{date}-{exchange}-{res}')
    fp.close()