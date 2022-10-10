# Импориитируем библиотеку для общения с сервером
import requests
s_city = "Moscow,RU"
# Вводим Api ключ
appid = "7225e8e1fcede5d7c782369baa90e2e9"
# Получаем данные с сайта
res = requests.get("http://api.openweathermap.org/data/2.5/weather",# по протаколу http(протакол передачи гипер текста)
             params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid}) # Пишем параметры
# Распаковываем json файл (получаем в формате json(словарь), а словарь это тип ключ значения (сити это ключ, а значение москва(ключ и значение)))
data = res.json()
# Пишем значения
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
# Тоже самое
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
             params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
# Прохожу по дате цикла для упоряд инф
for i in data['list']:
    print(i)
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")
