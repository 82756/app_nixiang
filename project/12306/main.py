import requests
import json

url = "https://mobile.12306.cn/otsmobile/app/mgs/mgw.htm"

hea = {
    "nbappid": "60000001",
    "nbversion": "5.6.2.109",
    "dfpstr": "",
    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 10; 16T Build/QKQ1.191222.002)",
    "Platform": "ANDROID",
    "AppId": "9101430221728",
    "WorkspaceId": "product",
    "signType": "0",
    "Cookie": "BIGipServernginxformobile=2313683210.50215.0000; AlteonMobile=EijOKD/UAQpapec59FJpAA$$; JSESSIONID=66776C5BD58969E41134C8073BDAF1F5; otsBusiness=FIEVaxzlAgod8+JVhFrjQQ$$",
    "Accept-Language": "zh-Hans",
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Retryable2": "0",
    "Host": "mobile.12306.cn",
}

data = {
    "operationType":"com.cars.otsmobile.queryLeftTicket",
    "requestData":'[{"train_date":"20230701","purpose_codes":"00","from_station":"SJP","to_station":"BJP","station_train_code":"","start_time_begin":"0000","start_time_end":"2400","train_headers":"QB#","train_flag":"","seat_type":"0","seatBack_Type":"","ticket_num":"","dfpStr":"","baseDTO":{"check_code":"b2b5a8c15986c088981c60e372128b10","device_no":"TEMP-ZJbYroxRDFkDAFEyy0m2+pw+","h5_app_id":"60000001","h5_app_version":"5.6.2.109","mobile_no":"","os_type":"a","time_str":"20230624195420","version_no":"5.6.0.8"}}]',
    "ts":"1687607660763",
    "sign":"",
}

fw = requests.get(url,headers=hea, params=data)

data = fw.json()['result']['ticketResult']
for zdata in data:
    print(zdata)