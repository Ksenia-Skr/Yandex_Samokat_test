import requests
import configuration
import data
# функция для создания заказа
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
# функция для вызова заказа через трек
def get_order (track_id):
    params = {'t': track_id}
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH, params=params)
