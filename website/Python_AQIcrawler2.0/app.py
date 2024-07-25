from flask import Flask, render_template, jsonify,request, redirect

import requests

app = Flask(__name__)

# 全域變數，用於存儲編號
global_number = None

@app.route('/')
def index():
    url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
    data = requests.get(url)
    data_json = data.json()
    

    aqi_records = []
    for index, record in enumerate(data_json['records']):
        aqi_records.append({
            'index':index+1,
            'county': record['county'],
            'sitename': record['sitename'],
            'aqi': record['aqi'],
            'status': record['status']
        })
    aqi_records_num = enumerate(aqi_records)
    
    return render_template('index.html',aqi_records=aqi_records,aqi_records_num=aqi_records_num)

@app.route('/send_number', methods=['POST'])
def send_number():
    global global_number
    global_number = request.form['number']
    print(global_number)
    return redirect('/')


@app.route('/num')
def num():
    return render_template('num.html', number=global_number)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)