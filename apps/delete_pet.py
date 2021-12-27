import get
import get_pets
import requests

key = (get.get_key) # получение ключа 

dct = get_pets.get_list

for i in range( len(dct[0]) ): # необходимо указывать имя питомца в ручную в коде
    if dct[0][i]['name'] == 'Arolf':
        pet_id = dct[0][i]['id'] 

delete_header_path = {"auth_key": key, "pet_id": pet_id}

request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id

def delete( url, param, header ):
    r = requests.delete(url, params=param, headers=header )

    if r.status_code == requests.codes["ok"]:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(' Питомец был удален')
    else:
        print(" PostError") 

delete( request_url, delete_header_path, delete_header_path)