# coding=utf-8
import requests
import json
import os
## Copyright (C) 2017 Leo Sheu. <loli>

nid = 'D0380000'
password = 'NIDpassword'

fcu = {
    'Account' : nid,
    'Password' : password
}
header = {
    'Connection' : 'keep-alive',
    'Content-Type' : 'text/json',
    'Host' : 'service206-sds.fcu.edu.tw',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.1.1; D6653 Build/23.4.A.1.232; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36'
}
row = ['                <tr class="row1">\n', '                <tr class="row2">\n']
number = [
    '                    <td>第1節<br>08:10~09:00</td>\n',
    '                    <td>第2節<br>09:10~10:00</td>\n',
    '                    <td>第3節<br>10:10~11:00</td>\n',
    '                    <td>第4節<br>11:10~12:00</td>\n',
    '                    <td>第5節<br>12:10~13:00</td>\n',
    '                    <td>第6節<br>13:10~14:00</td>\n',
    '                    <td>第7節<br>14:10~15:00</td>\n',
    '                    <td>第8節<br>15:10~16:00</td>\n',
    '                    <td>第9節<br>16:10~17:00</td>\n',
    '                    <td>第10節<br>17:10~18:00</td>\n',
    '                    <td>第11節<br>18:10~19:00</td>\n',
    '                    <td>第12節<br>19:10~20:00</td>\n',
    '                    <td>第13節<br>20:10~21:00</td>\n',
    '                    <td>第14節<br>21:10~22:00</td>\n'
]

classtable = requests.post("https://service206-sds.fcu.edu.tw/mobileservice/CourseService.svc/Timetable", json = fcu, headers = header, verify = False)

timetable = classtable.json()['TimetableTw']
#print(timetable)

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

for num in range(1,15):
    f.write(row[num%2])
    f.write(number[num-1])
    for day in range(1,6):
        flag = 0
        for t in timetable:
            if (t['SctWeek'] == day) and (t['SctPeriod'] == num):
                f.write('                    <td>' + t['SubName'] + '<br>')
                try:
                    f.write(t['RomName'])
                except:
                    pass
                f.write('</td>\n')
                flag = 1
        if (flag != 1):
            f.write('                    <td></td>\n')
f.write('                </tr>\n')
f.write('''
        </tbody>
    </table>
</body>
</html>''')
f.close()
print(nid +'.html 課表產生成功!')