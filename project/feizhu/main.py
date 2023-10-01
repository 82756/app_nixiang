import requests
import json
import time

import urllib3

import hk_rpc

http = urllib3.PoolManager()




url = "https://acs.m.taobao.com/gw/mtop.trip.search.dinamicx.pattern.render/1.0/"
# data = '{"args":"{"appName":"LX","callSource":"active_search","exposureSize":0,"firstEnter":0,"hotelNearby":false,"hotelNewPage":false,"isNewPage":1,"keyword":"汉庭","nav":"AUCTION","pagenum":"1","queryCorrect":true,"referFrom":"home","searchVersion":"34","selectedCityIsAbroad":false,"selectedHotelCityCode":0,"source":"globalSearch","userJustChangeHotelCity":false}","bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}'
data = '{"args":"{\"appName\":\"LX\",\"callSource\":\"home\",\"exposureSize\":0,\"firstEnter\":0,\"hotelNearby\":false,\"hotelNewPage\":false,\"isNewPage\":1,\"keyword\":\"汉庭\",\"nav\":\"AUCTION\",\"pagenum\":\"1\",\"queryCorrect\":true,\"referFrom\":\"home\",\"searchVersion\":\"34\",\"selectedCityIsAbroad\":false,\"selectedHotelCityCode\":0,\"source\":\"globalSearch\",\"userJustChangeHotelCity\":false}","bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}'
# data = '{"args":"{\"appName\":\"LX\",\"callSource\":\"active_search\",\"exposureSize\":0,\"firstEnter\":0,\"hotelNearby\":false,\"hotelNewPage\":false,\"isNewPage\":1,\"keyword\":\"汉庭\",\"nav\":\"AUCTION\",\"pagenum\":\"1\",\"queryCorrect\":true,\"referFrom\":\"home\",\"searchVersion\":\"34\",\"selectedCityIsAbroad\":false,\"selectedHotelCityCode\":0,\"source\":\"globalSearch\",\"userJustChangeHotelCity\":false}","bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}'

data1 = 'data=%7B%22args%22%3A%22%7B%5C%22appName%5C%22%3A%5C%22LX%5C%22%2C%5C%22callSource%5C%22%3A%5C%22active_search%5C%22%2C%5C%22exposureSize%5C%22%3A0%2C%5C%22firstEnter%5C%22%3A0%2C%5C%22hotelNearby%5C%22%3Afalse%2C%5C%22hotelNewPage%5C%22%3Afalse%2C%5C%22isNewPage%5C%22%3A1%2C%5C%22keyword%5C%22%3A%5C%22%E6%B1%89%E5%BA%AD%5C%22%2C%5C%22nav%5C%22%3A%5C%22AUCTION%5C%22%2C%5C%22pagenum%5C%22%3A%5C%221%5C%22%2C%5C%22queryCorrect%5C%22%3Atrue%2C%5C%22referFrom%5C%22%3A%5C%22sug%5C%22%2C%5C%22searchVersion%5C%22%3A%5C%2234%5C%22%2C%5C%22selectedCityIsAbroad%5C%22%3Afalse%2C%5C%22selectedHotelCityCode%5C%22%3A0%2C%5C%22source%5C%22%3A%5C%22globalSearch%5C%22%2C%5C%22userJustChangeHotelCity%5C%22%3Afalse%7D%22%2C%22bizType%22%3A%22tripsearch%22%2C%22name%22%3A%22SrpAuctionDynamic%22%2C%22version%22%3A%229.9.32.104%22%2C%22platform%22%3A%22android%22%7D'
c_data = '{"appName":"LX","callSource":"home","exposureSize":0,"firstEnter":0,"hotelNearby":false,"hotelNewPage":false,"isNewPage":1,"keyword":"汉庭","nav":"AUCTION","pagenum":"1","queryCorrect":true,"referFrom":"home","searchVersion":"34","selectedCityIsAbroad":false,"selectedHotelCityCode":0,"source":"globalSearch","userJustChangeHotelCity":false}'
# data = {"args":{"appName":"LX","callSource":"active_search","exposureSize":0,"firstEnter":0,"hotelNearby":False,"hotelNewPage":False,"isNewPage":1,"keyword":"汉庭","nav":"AUCTION","pagenum":"1","queryCorrect":True,"referFrom":"home","searchVersion":"34","selectedCityIsAbroad":False,"selectedHotelCityCode":0,"source":"globalSearch","userJustChangeHotelCity":False},"bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}
d_data = '{"args":' + json.dumps(c_data) + ',"bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}'
data2 = {"args":{"appName":"LX","callSource":"home","exposureSize":0,"firstEnter":0,"hotelNearby":False,"hotelNewPage":False,"isNewPage":1,"keyword":"汉庭","nav":"AUCTION","pagenum":"1","queryCorrect":True,"referFrom":"home","searchVersion":"34","selectedCityIsAbroad":False,"selectedHotelCityCode":0,"source":"globalSearch","userJustChangeHotelCity":False},"bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}
# data = {"args":"{\"appName\":\"LX\",\"callSource\":\"home\",\"exposureSize\":0,\"firstEnter\":0,\"hotelNearby\":false,\"hotelNewPage\":false,\"isNewPage\":1,\"keyword\":\"汉庭\",\"nav\":\"AUCTION\",\"pagenum\":\"1\",\"queryCorrect\":true,\"referFrom\":\"home\",\"searchVersion\":\"34\",\"selectedCityIsAbroad\":false,\"selectedHotelCityCode\":0,\"source\":\"globalSearch\",\"userJustChangeHotelCity\":false}","bizType":"tripsearch","name":"SrpAuctionDynamic","version":"9.9.32.104","platform":"android"}
data = 'data=%7B%22args%22%3A%22%7B%5C%22appName%5C%22%3A%5C%22LX%5C%22%2C%5C%22callSource%5C%22%3A%5C%22home%5C%22%2C%5C%22exposureSize%5C%22%3A0%2C%5C%22firstEnter%5C%22%3A0%2C%5C%22hotelNearby%5C%22%3Afalse%2C%5C%22hotelNewPage%5C%22%3Afalse%2C%5C%22isNewPage%5C%22%3A1%2C%5C%22keyword%5C%22%3A%5C%22%E6%B1%89%E5%BA%AD%5C%22%2C%5C%22nav%5C%22%3A%5C%22AUCTION%5C%22%2C%5C%22pagenum%5C%22%3A%5C%221%5C%22%2C%5C%22queryCorrect%5C%22%3Atrue%2C%5C%22referFrom%5C%22%3A%5C%22home%5C%22%2C%5C%22searchVersion%5C%22%3A%5C%2234%5C%22%2C%5C%22selectedCityIsAbroad%5C%22%3Afalse%2C%5C%22selectedHotelCityCode%5C%22%3A0%2C%5C%22source%5C%22%3A%5C%22globalSearch%5C%22%2C%5C%22userJustChangeHotelCity%5C%22%3Afalse%7D%22%2C%22bizType%22%3A%22tripsearch%22%2C%22name%22%3A%22SrpAuctionDynamic%22%2C%22version%22%3A%229.9.32.104%22%2C%22platform%22%3A%22android%22%7D'

t = str(int(time.time()))

header1 = {
    'x-sgext':'JAfrlH4BiLkw5QMuJUsOXpTapNuh2LfZodKjyKfYosinx6HHpMelx6XHpcelx6XHpcelx6fTuNq42KzHp9O427jbuNu427jbuNu427jbuNu427jauN%2Bhx6DeuNqkx6THpMem07faotKh26bbptKlyKTZoI2k26Tap4ryj%2Fberd632KTdt9qgyPKIt9uk26PIp8ilyKfIpcimyKbIpsilyKbdt9%2B32q3Ipd6327eOt9u327fbt8jxyPKOt9u32%2FLS8tnwyKTbpNuk',
    'b-fpt':'fsk(home)',
    'x-sign':'azCJEK002xAALEOIpXAk2W8jFatGjFOMQYCTuhu76HbBzjueMCjwQptvM6Tq8RTPQYTUCko8KBnQhoeAGDZ32PQ4sh6AvEOMQLxDjE',
    'x-sid':'182b219b523ce715a3b61f8fdbf09754',
    'x-uid':'2207560347204',
    'x-nettype':'WIFI',
    'x-pv':'6.3',
    'x-disastergrd':'',
    'x-nq':'WIFI',
    'x-features':'27',
    'x-mini-wua':'HHnB_gzREjOtEi9Ybb%2FP7ctWaZX9SwN5xDAtsro%2FpQ6Uz1tft6u2X%2F4wtXapiRF4BH4iuOQvIhBi2zJLN25s6N01oiFqOibwEonFv57c2Pb5ssNgZ76G0OdXM2OxAu8%2BN12JyJIazwkVRfq%2BAsB8%2BIr5zHx40ekmwtgdP4kkF%2FeXFxVw%3D',
    'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Content-Length':'847',
    'x-t':f'{t}',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie':'cna=PLuKHfTq53ICAWoJWx82p4Z7; _fli_barHeight=24; _fli_titleHeight=68; unb=2207560347204; sn=; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UUphzWIcjgnnlFOBbg%3D%3D&vt3=F8dCsGSJR7tGlRqgulw%3D&nk2=F5RARJlKJV8TYeQ%3D; uc1=existShop=false&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=Uoe9aOa4v9%2FU%2Bg%3D%3D&cookie21=VFC%2FuZ9ainBZ; csg=323428c6; lgc=tb566366162; cancelledSubSites=empty; t=0f20329703cfb5fd441f4b59559fd23c; cookie17=UUphzWIcjgnnlFOBbg%3D%3D; dnk=tb566366162; skt=5f384371e5624fcb; munb=2207560347204; cookie2=182b219b523ce715a3b61f8fdbf09754; uc4=id4=0%40U2grFn0vUolLCNTgV%2Fymkc0CN3Soaeol&nk4=0%40FY4L6MeBW7IFTCYFgs5IF7NWhNBF8A%3D%3D; tracknick=tb566366162; _cc_=W5iHLLyFfA%3D%3D; ti=; sg=246; _l_g_=Ug%3D%3D; _nk_=tb566366162; cookie1=WqHwVl49g7vBBfl%2FGK%2BvhWAijlINCr67J6FKqZS6mc4%3D; _tb_token_=ed39e7f3be3e4; sgcookie=W100yJsMxnojR9OYWbQVnoUjcQjYdFmXjgbDLmwIs5GPEuch04ICYWk4CzJS9MhQbgoee4CP7lVfsBcs0Nj9ftYxqQwLL5HIuBOg4bTWX%2BJ%2FKnadlHepc2sItJMqNXnTNJaA; imewweoriw=36DFHrod%2B5l0ZKkh8DOSzRLn4JoU3IziWMvKPZlfS7w%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8b4v9z%2F0F0Uix1HA%3D%3D; _w_tb_nick=tb566366162; ockeqeudmj=uD9jCZo%3D; _samesite_flag_=true; tfstk=dGvwrAYeSqa6QBAhh1624eb021cOeT3SoK_fmnxcfNbi6VQDTe_QhcBsMt8V8EQ11OXgurbH8-_1hnjciFtciRit6sb2Ww9XfnG93x8Djsbj6Zs03n8Cii92D-SDmEnOlchBvhBAn4gSPYt9X58ZP4Ns54PRHt0SPWwc6YWvzFlCoTJkCAGrp_4WXwv_8hz8S-ff8-2z0G5GcYQ3n-vFbH7lQm4AxweJHKHYg1jdYaiEYz2Ul4f..; l=fBSv8HW4PODwwzgyBOfwnurza77tQCOfguPzaNbMi9fP_DC659cVW1hk7NTBCnGRFsC2R3rFwv_pBeYBYnAtkPERayPCSMMqnmOk-Wf..; isg=BNXVBBfAHBM-AjhrChYBe30L79iP0onkQGyXo1d6h8ybrvSgHyJvtRpsfLQYrqGc; x5sec=7b226d746f703b32223a226134646130363734363265653964313132623834653130636331373330663631434b62366e366747454a58357a4a3445476738794d6a41334e5459774d7a51334d6a41304f7a4969413235736344444237613769426b4143222c22733b32223a2238623637313161663631326632303836227d',
    'x-bx-version':'6.5.56',
    'f-refer':'mtop',
    'x-extdata':'openappkey%3DDEFAULT_AUTH',
    'x-ttid':'10002659%40travel_android_9.9.32.104',
    'x-app-ver':'9.9.32',
    'x-c-traceid':'ZQPNHxmNzyADACL2ehl%2FY%2FXw1695023046323030412597',
    'fliggy-nick':'tb566366162',
    'x-umt':'vXuBUB9LPEx32AKKp0oxkU9OFT%2BeMV1o',
    'a-orange-q':'appKey=12663307&appVersion=9.9.32&clientAppIndexVersion=1120230918153603176&clientVersionIndexVersion=0',
    'x-utdid':'ZQPNHxmNzyADACL2ehl%2FY%2FXw',
    'fliggy-uid':'2207560347204',
    'x-appkey':'12663307',
    'x-devid':'ArLGY7s64LdnHc70_ueTkoXl2-ZUDNz0ltdgD0s5txQq',
    'user-agent':'MTOPSDK%2F3.1.1.7+%28Android%3B9%3Bvivo%3BV2217A%29',
    'Host':'acs.m.taobao.com',
    'Accept-Encoding':'gzip',
    'Connection':'Keep-Alive',

}

header = {
    'x-sgext':'',
    'x-sign':'',
    'x-nettype':'WIFI',
    'x-nq':'WIFI',
    'x-sid':'182b219b523ce715a3b61f8fdbf09754',
    'x-uid':'2207560347204',
    'x-pv':'6.3',
    'x-features':'27',
    'x-mini-wua':'',
    'x-t':f'{t}',
    'Cookie':'cna=PLuKHfTq53ICAWoJWx82p4Z7; _fli_barHeight=24; _fli_titleHeight=68; unb=2207560347204; sn=; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&id2=UUphzWIcjgnnlFOBbg%3D%3D&vt3=F8dCsGSJR7tGlRqgulw%3D&nk2=F5RARJlKJV8TYeQ%3D; uc1=existShop=false&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=Uoe9aOa4v9%2FU%2Bg%3D%3D&cookie21=VFC%2FuZ9ainBZ; csg=323428c6; lgc=tb566366162; cancelledSubSites=empty; t=0f20329703cfb5fd441f4b59559fd23c; cookie17=UUphzWIcjgnnlFOBbg%3D%3D; dnk=tb566366162; skt=5f384371e5624fcb; munb=2207560347204; cookie2=182b219b523ce715a3b61f8fdbf09754; uc4=id4=0%40U2grFn0vUolLCNTgV%2Fymkc0CN3Soaeol&nk4=0%40FY4L6MeBW7IFTCYFgs5IF7NWhNBF8A%3D%3D; tracknick=tb566366162; _cc_=W5iHLLyFfA%3D%3D; ti=; sg=246; _l_g_=Ug%3D%3D; _nk_=tb566366162; cookie1=WqHwVl49g7vBBfl%2FGK%2BvhWAijlINCr67J6FKqZS6mc4%3D; _tb_token_=ed39e7f3be3e4; sgcookie=W100yJsMxnojR9OYWbQVnoUjcQjYdFmXjgbDLmwIs5GPEuch04ICYWk4CzJS9MhQbgoee4CP7lVfsBcs0Nj9ftYxqQwLL5HIuBOg4bTWX%2BJ%2FKnadlHepc2sItJMqNXnTNJaA; imewweoriw=36DFHrod%2B5l0ZKkh8DOSzRLn4JoU3IziWMvKPZlfS7w%3D; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8b4v9z%2F0F0Uix1HA%3D%3D; _w_tb_nick=tb566366162; ockeqeudmj=uD9jCZo%3D; _samesite_flag_=true; tfstk=dGvwrAYeSqa6QBAhh1624eb021cOeT3SoK_fmnxcfNbi6VQDTe_QhcBsMt8V8EQ11OXgurbH8-_1hnjciFtciRit6sb2Ww9XfnG93x8Djsbj6Zs03n8Cii92D-SDmEnOlchBvhBAn4gSPYt9X58ZP4Ns54PRHt0SPWwc6YWvzFlCoTJkCAGrp_4WXwv_8hz8S-ff8-2z0G5GcYQ3n-vFbH7lQm4AxweJHKHYg1jdYaiEYz2Ul4f..; l=fBSv8HW4PODwwzgyBOfwnurza77tQCOfguPzaNbMi9fP_DC659cVW1hk7NTBCnGRFsC2R3rFwv_pBeYBYnAtkPERayPCSMMqnmOk-Wf..; isg=BNXVBBfAHBM-AjhrChYBe30L79iP0onkQGyXo1d6h8ybrvSgHyJvtRpsfLQYrqGc; x5sec=7b226d746f703b32223a226134646130363734363265653964313132623834653130636331373330663631434b62366e366747454a58357a4a3445476738794d6a41334e5459774d7a51334d6a41304f7a4969413235736344444237613769426b4143222c22733b32223a2238623637313161663631326632303836227d',
    'x-bx-version':'6.5.56',
    'f-refer':'mtop',
    'x-extdata':'openappkey%3DDEFAULT_AUTH',
    'x-ttid':'10002659%40travel_android_9.9.32.104',
    'x-app-ver':'9.9.32',
    'x-umt':'',
    'x-utdid':'ZQPNHxmNzyADACL2ehl/Y/Xw',
    'x-appkey':'12663307',

    'user-agent':'MTOPSDK%2F3.1.1.7+%28Android%3B10%3Bmeizu%3B16T%29',
    'Host':'acs.m.taobao.com',
    'Accept-Encoding':'gzip',

}

signjm = hk_rpc.d_rpc(t,d_data)
print(signjm)
signjm = str(signjm[1:-1]).split(",")
for zsign in signjm:
    hsign = zsign.split("=",1)
    print(hsign)
    header1[hsign[0].strip()] = hsign[1].strip()


print(header1)
print(header1['x-umt'])

fw = requests.post(url,data=data,headers=header1)
print(fw.text)
