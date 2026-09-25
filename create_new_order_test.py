#Скрысанова Ксения, 47 когорта - финальный проект, инженере по тестированию плюс
import sender_stand_request
import data

def test_get_order_by_track():
    new_order_response = sender_stand_request.post_new_order(data.order_body)
    assert new_order_response.status_code == 201
    json_data = new_order_response.json()
    track_id = json_data["track"]
    print ("Трек закза", track_id)
    get_new_order = sender_stand_request.get_order(track_id)
    assert get_new_order.status_code == 200
    print (get_new_order.status_code)