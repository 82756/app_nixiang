# -- coding:utf-8 --
import requests
import datetime

citylists = ['大庆', '哈尔滨', '鹤岗', '黑河', '鸡西', '佳木斯', '牡丹江', '七台河', '齐齐哈尔', '双鸭山', '绥化', '白城', '白山', '吉林', '四平', '松原', '通化', '延边朝鲜族自治州', '长春', '鞍山', '本溪', '朝阳', '大连', '丹东', '抚顺', '阜新', '葫芦岛', '锦州', '辽阳', '盘锦', '沈阳', '铁岭', '营口', '滨州', '德州', '东营', '菏泽', '济南', '济宁', '聊城', '临沂', '青岛', '日照', '泰安', '威海', '潍坊', '烟台', '枣庄', '淄博', '北京', '保定', '沧州', '承德', '邯郸', '衡水', '廊坊', '秦皇岛', '石家庄', '唐山', '邢台', '张家口', '固原', '吴忠', '银川', '中卫', '大同', '晋城', '晋中', '临汾', '吕梁', '朔州', '太原', '忻州', '运城', '长治', '安康', '宝鸡', '汉中', '商洛', '铜川', '渭南', '西安', '咸阳', '延安', '榆林', '天津', '福州', '龙岩', '南平', '宁德', '莆田', '泉州', '三明', '厦门', '漳州', '潮州', '东莞', '佛山', '广州', '河源', '惠州', '揭阳', '茂名', '梅州', '清远', '汕头', '汕尾', '韶关', '深圳', '阳江', '湛江', '肇庆', '中山', '珠海', '百色', '北海', '防城港', '桂林', '柳州', '南宁', '钦州', '澄迈县', '儋州', '定安县', '海口', '陵水黎族自治县', '琼海', '三亚', '万宁']
header = {
        'token':'8cef02d50c074a6d94eb2104d7541cc0254490211',
        'user-token':'8cef02d50c074a6d94eb2104d7541cc0254490211',
        'client-platform':'APP-ANDROID',
        'skipsign':'1',
        'content-type':'application/json',
        'access_token':'Fav4+s6QR/23gw+y2PCdi147tXsQcLe83Im8+t8xxItddwVNWec+85WOERc1/CJQh8vkp7qQVToO4VOX72JoytztvL6O4uM=',
        'screenheight':'2232',
        'screenwidth':'1080',
        'devicefingerprinting':'13712377361311021023627151210',
        'pageid':'-1',
        'traceid':'90caab9a-2c56-4429-93cb-1234548c1beb',
        'pretraceid':'null',
        'os':'10',
        'echotoken':'cefb6e6e-4c06-40b4-ba46-27dc6cb25256',
        'platform':'android',
        'ver':'9.3.1',
        'jpush_push_token':'f62f04afcce90c707f294c207f1166d7',
        'language':'zh-CN',
        'jpush_channel_id':'getui',
        'push_token':'f62f04afcce90c707f294c207f1166d7',
        'brand':'meizu',
        'mac':'null',
        'channel_id':'getui',
        'model':'16T',
        'channel':'Huawei',
        'manufacturer':'meizu',
        'devno':'792a1b3f79505e61',
        'usertoken':'8cef02d50c074a6d94eb2104d7541cc0254490211',
        'Host':'hweb-hotel.huazhu.com',
        'Accept-Encoding':'gzip',
        'Cookie':'CSRF-NWACT=d8955250-c767-4c8b-8987-8c662e7fef55',
        'User-Agent':'okhttp/3.12.1',
        'Connection':'keep-alive',
    }

def huazhuhui_get_cityid(cityname):
    url = f"https://hweb-hotel.huazhu.com/hotels/city/queryHotelListCity?searchWord={cityname}"
    fw = requests.get(url,headers=header)
    print(fw.json())

def huazhuhui_get_hotels(cityname, keywords, checkInDate=datetime.date.today(), checkOutDate=datetime.date.today()+datetime.timedelta(days=1)):
    """
    :param cityname: 城市地点 （北京）
    :param keywords: 搜索的酒店名称 (汉庭)
    :param checkInDate: 住宿开始时间 （2023-09-18）
    :param checkOutDate: 离开时间 （2023-09-19）
    :return:
    """
    url = f"https://hweb-hotel.huazhu.com/hotels/search/search?cityName={cityname}&keyword={keywords}&source=1&checkInDate={checkInDate}&checkOutDate={checkOutDate}&sortChannelType=T"
    data = requests.get(
        url=url,
        headers=header,
    ).json()
    for hotel in data['content']:
        print(hotel)

def huazhuhui_search_getHotelList(cityName, name, checkInDate=datetime.date.today(), checkOutDate=datetime.date.today()+datetime.timedelta(days=1)):
    """
    :param cityName: 地区 （石家庄）
    :param name: 搜索的关键字 （汉庭酒店）
    :param checkInDate: 预计住宿日期 （2023-09-18）
    :param checkOutDate: 预计离开酒店日期 （2023-09-19）
    :return:
    """
    url = "https://hweb-hotel.huazhu.com/hotels/hotel/getHotelList"
    params = {
        "searchDicts": [{
            "key": "orderBy",
            "value": "0",
            "name": "推荐排序"
        }, {
            "key": "HotelStyle",
            "value": "allHT",
            "name": name.strip(),
        }],
        "cityName": cityName.strip(),
        "checkInDate": str(checkInDate),
        "checkOutDate": str(checkOutDate),
        "pageIndex": 1,
        "pageSize": "10",
        "source": 1,
        "uuid": "FDyPxcnET6MNAMzk",
        "hasUsePositioning": False,
        "useOldSort": "10"
    }
    data = requests.post(
        url=url,
        json=params,
        headers=header
    ).json()
    # print(data)
    for hotel in data['content']['hotels']:
        print(hotel)

def login_ceshi():
    url = "https://hweb-personalcenter.huazhu.com/login/login"
    data = {
        "loginType": 1,
        "account": "17603342428",
        "mobilePlace": "86",
        "passCode": "g17603342428",
        "challenge": "f494f158a00dbff040e1086e55f4b351",
        "seccode": "57d4674d8ec47a2db3671c1667666192|jordan",
        "validate": "57d4674d8ec47a2db3671c1667666192"
    }

    fw = requests.post(url,json=data)
    print(fw.text)

if __name__ == '__main__':
    # login_ceshi()
    # huazhuhui_get_hotels("石家庄", "汉庭")
    # huazhuhui_cityid("石家庄")
    huazhuhui_search_getHotelList("石家庄","汉庭")

