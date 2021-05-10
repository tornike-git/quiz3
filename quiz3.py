# import requests
# import json
# import sqlite3
#
# key = '026288e9b73e8747a756f697d52ab8dd'
#
#
# latitude = 41.7
# longitude = 45.8
# units = 'metric'
# cnt = 50
#
#
#
# url = f'https://api.openweathermap.org/data/2.5/find?lat={latitude}&lon={longitude}&appid={key}&units={units}&cnt={cnt}'
# r = requests.get(url)
# # print(r.status_code)
# # print(r.headers)
# # print(r.text)
# # print(r.content)
# t = r.text
# result = json.loads(t)
# structured = json.dumps(result, indent=4)
#
#
# with open('circle_weather.json', 'w')as w:
#     json.dump(result, w, indent=4)
#
# connect = sqlite3.connect('southeast_caucasian_weather.sqlite')
# cursor = connect.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS current_weather
#               (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                country VARCHAR(20),
#                city VARCHAR(30),
#                temperature INTEGER,
#                feels FLOAT,
#                humidity FLOAT)
#               ''')
#
# for each in result['list']:
#     city = each['name']
#     temperature = each['main']['temp']
#     country = each['sys']['country']
#     feels = each['main']['feels_like']
#     humidity = each['main']['humidity']
#     print(f"ქალაქი: {city}, ქვეყანა: {country}, ტემპერატურა: {temperature}, იგრძნიბა როგორც: {feels}, ტენიანობა: {humidity}")
#     cursor.execute("INSERT INTO current_weather (country, city, temperature, feels, humidity) VALUES (?,?,?,?,?)",
#                    (country, city, temperature, feels, humidity))
# ცხრილში შენახულია openweathermap-იდან აღებული მონაცემები. კონკრეტულად აღებულია კოორდინატები და მის გარშემო წრიულად
# მდებარე ქალაქებისა თუ სოფლების
# სხვადასხვა მონაცემები: თუ რომელი ქალაქია, რომელ ქვეყანას ეკუთვნის(ეს მონაცემები იმიტომ, რომ ძირითადად სამხრეთ კავკასიის
# აღმოსავლეთ ნაწილია აღებული და შედის ოთხი სხვადასხვა ქვეყანა), რა ტემპერატურაა, როგორ იგრძნობა და ტენიანობა.
#
#
#

# connect.commit()
# connect.close()