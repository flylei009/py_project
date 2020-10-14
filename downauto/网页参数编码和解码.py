from urllib.parse import *
url1 = '{"cityId":2501,"carId":"143938"}'
url2 = 'http://car.bitauto.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A2501%2C%22carId%22%3A%22143938%22%7D'
url3 = '%7B%7D'

print('http://car.bitauto.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param='+quote(url1))
print(unquote(url2))

# http://car.bitauto.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A2501%2C%22carId%22%3A%22143938%22%7D
# http://car.bitauto.com/web_api/car_model_api/api/v1/car/config_new_param?cid=508&param=%7B%22cityId%22%3A2501%2C%22carId%22%3A%22143938%22%7D


# 易车网获取区域
# http://car.bitauto.com/web_api/web_app/api/v1/city/get_area_list?cid=508&param=%7B%7D
print('http://car.bitauto.com/web_api/web_app/api/v1/city/get_area_list?cid=508&param=' + unquote(url3))