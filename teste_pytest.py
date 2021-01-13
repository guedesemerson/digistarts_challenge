import requests
import json


class TestNumber:

    headers = {'Accept': '*/*',
               'User-agent': 'request'}
    url_base = {'GET': 'http://localhost:8000/number/list_register/',
                'RETRIEVE': 'http://127.0.0.1:8000/number/retrieve-register/',
                'POST': 'http://localhost:8000/number/execute_algorithm/',
                'DELETE': 'http://127.0.0.1:8000/number/delete_register/',
                'UPDATE': 'http://localhost:8000/number/update_register/'}

    def find_id(self):
        list_object = requests.get(url=self.url_base['GET'], headers=self.headers)
        return list_object.json()[0]['id']

    def test_post_number(self):
        object_number = {"number_array":[1, 5, 3]}
        list_object = requests.post(url=self.url_base['POST'],headers={"Content-Type": "application/json"},
                                    data=json.dumps(object_number))

        assert list_object.status_code == 201

    def test_get_numbers(self):
        list_object = requests.get(url=self.url_base['GET'], headers=self.headers)
        assert list_object.status_code == 200

    def test_get_number(self):
        id_number = str(self.find_id())
        list_object = requests.get(url=self.url_base['RETRIEVE']+id_number,
                                   headers=self.headers)
        assert list_object.status_code == 200

    def test_put_number(self):
        id_number = str(self.find_id())
        updated = {"number_array": [1, 1, 2]}
        list_object = requests.put(url=self.url_base['UPDATE']+id_number,
                                   headers={"Content-Type": "application/json"},
                                   data=json.dumps(updated))
        assert list_object.status_code == 201




    def test_delete_number(self):
        id_number = str(self.find_id())
        list_object = requests.delete(url=self.url_base['DELETE']+id_number,
                                      headers=self.headers)
        assert list_object.status_code == 204









