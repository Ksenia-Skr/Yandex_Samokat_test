#Скрысанова Ксения, 47 когорта - финальный проект, инженере по тестированию плюс
# импортируем нужные нам данные
import sender_stand_request
import data

def test_get_order_by_track():
    # создаем новый заказа
    new_order_response = sender_stand_request.post_new_order(data.order_body)
    # убеждаемся, что заказ создан и на этом этапе ошибки нет
    assert new_order_response.status_code == 201
    # получаем трек заказа, который должен быть в ответе и в формате json
    json_data = new_order_response.json()
    track_id = json_data["track"]
    # получаем заказ через трек
    get_new_order = sender_stand_request.get_order(track_id)
    # убеждаемся, что функция сработала верно, ожидаемы ответ системы 200
    assert get_new_order.status_code == 200