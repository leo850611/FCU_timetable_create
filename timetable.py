# coding=utf-8
import requests
import json
## Copyright (C) 2017 Leo Sheu. <loli>

nid = 'D0380000'

info = {'nid' : nid}
header = {
    'Connection' : 'Keep-Alive',
    'Content-Type' : 'application/x-www-form-urlencoded',
    'referer' : 'https://140.134.4.38/1.0/fculdap',
    'User-Agent' : 'Dalvik/2.1.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.224)',
    'Host' : '140.134.4.38',
    'Accept-Encoding' : 'gzip'
}
row = ['                <tr class="row2">\n', '                <tr class="row1">\n']
num = [
    '                    <td>第1節<br>08:10~09:00</td>\n',
    '                    <td>第2節<br>09:10~10:00</td>\n',
    '                    <td>第3節<br>10:10~11:00</td>\n',
    '                    <td>第4節<br>11:10~12:00</td>\n',
    '                    <td>第5節<br>12:10~13:00</td>\n',
    '                    <td>第6節<br>13:10~:00</td>\n',
    '                    <td>第7節<br>14:10~15:00</td>\n',
    '                    <td>第8節<br>15:10~16:00</td>\n',
    '                    <td>第9節<br>16:10~17:00</td>\n',
    '                    <td>第10節<br>17:10~18:00</td>\n',
    '                    <td>第11節<br>18:10~19:00</td>\n',
    '                    <td>第12節<br>19:10~20:00</td>\n',
    '                    <td>第13節<br>20:10~21:00</td>\n'
]
url = 'https://140.134.4.38/3.0/getCoursesSchedule?api_key=83f1e4a91019fdf6ba17b9d8555aedd081fc6a26'

getclass = requests.post(url , data = info, headers = header, verify = False)
list = getclass.json()['data']

if(len(list)== 0):
    print(nid + ' 學號不存在OAO')
else:
    list.append({'period': 0, 'weekday': 0})
    f = open(nid+'.html', 'w', encoding = 'utf-8')
    f.write('''<!DOCTYPE>
    <html>
    <head>
        <meta charset="UTF8">
        <title>Course</title>
        <style>
            body { text-align: center; margin: auto; padding-top: 20px;}
            table { text-align: center; margin: auto; border: 2px #FFE9AC solid; width: 90%;}
            tr.row0 { background-color: #760000; color: #EEEEEE}
            tr.row1 { background-color: #FFE9AC; color: #760000}
            tr.row2 { background-color: #FDF0CD; color: #760000}
        </style><style type=text/css> 
        body { font-family: 微軟正黑體; }
        </style>
    </head>
    <body>
        <h1>105學年度第2學期課程資訊(課表)</h1>
        <table>
            <thead>
                <tr class="row0">
                    <th>節次</th>
                    <th>週一</th>
                    <th>週二</th>
                    <th>週三</th>
                    <th>週四</th>
                    <th>週五</th>
                </tr>
            </thead>
            <tbody>
    ''')

    i = 0
    for session in range(13):
        f.write(row[session%2])
        f.write(num[session])
        for day in range(1,6):
            if (list[i]['period'] == session + 1):
                if (list[i]['weekday'] == day):
                    f.write('                    <td>' + list[i]['course'] + '<br>' + list[i]['classroom'] + '<br>' + list[i]['tname'] + '</td>\n')
                    i = i+1
                else:
                    f.write('                    <td></td>\n')
            else:
                f.write('                    <td></td>\n')
    
    f.write('                </tr>\n')
    f.write('''                <tr class="row1">
                    <td><br></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>''')
    f.close()
    print(nid +'.html 課表產生成功!')