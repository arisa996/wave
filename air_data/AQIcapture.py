import requests
import csv
import os
import datetime


# now_time = datetime.datetime.now()
# date_time = now_time.strftime("%Y%m%d_%H")
# print("格式化後的日期和時間是：", date_time)

file_path ='TaiwanAir.csv'


csvfile = open(file_path, 'w',encoding='utf-8-sig')    # 建立空白並可寫入的 CSV 檔案
csv_write = csv.writer(csvfile)       # 設定 csv_write 為寫入

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
data = requests.get(url)
data_json = data.json()

output = [["county","sitename","aqi","空氣品質"]]    # 設定 output 變數為二維串列，第一筆資料為開頭
for i in data_json['records']:
    # 依序將取得的資料加入 output 中
    output.append([i['county'],i['sitename'],i['aqi'],i['status']])
# print(output)
csv_write.writerows(output)   # 多行寫入 CSV

# for i in data_json['records']:       # 依序取出 records 內容的每個項目
#     print(i['county'] + ' ' + i['sitename'], end='，')    # 印出城市與地點名稱
#     print('AQI:' + i['aqi'], end='，')                    # 印出 AQI 數值
#     print('空氣品質' + i['status'])                        # 印出空氣品質狀態