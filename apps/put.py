import get
import get_pets
import requests

key = (get.get_key) # получение ключа 

dct = get_pets.get_list

for i in range( len(dct[0]) ): # необходимо указывать имя питомца в ручную в коде
    if dct[0][i]['name'] == 'Six':
        pet_id = dct[0][i]['id'] 

put_header_path_formData = { "auth_key": key, "pet_id": pet_id, "name": "Eight", "animal_type":"Burmese Cat", "age": "3" }

request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id

def rename( url, param, header ):
    r = requests.put(url, params=param, headers=header )

    if r.status_code == requests.codes["ok"]:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(' Питомец был переименован')
    else:
        print(" PostError") 


rename( request_url, put_header_path_formData, put_header_path_formData)