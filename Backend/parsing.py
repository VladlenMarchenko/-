#Тут мы парсим данные с 2Гис, Яндекс карт и Google maps
import requests

twogis = requests.get('https://2gis.ru/moscow/search/%D0%A8%D0%B0%D1%83%D1%80%D0%BC%D0%B0%20(%D1%88%D0%B0%D0%B2%D0%B5%D1%80%D0%BC%D1%8B)/attributeId/70000201006754290?m=37.601417%2C55.749941%2F12.25')
twogis.status_code
#yandex_map =  requests.get('')