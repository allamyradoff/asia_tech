import requests
s_city = "Mary,TM"
city_id = 0
appid = "django-insecure-$d2rh6tuw(zew_g)f9&7yqvg)p=oyon%tw_t815kzp=$d%^b18"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass