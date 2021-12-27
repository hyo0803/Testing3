import get
import requests
import json

key = (get.get_key) # получение ключа 

get_header_query = {"auth_key ": key, "filter": "my_pets"}

request_url = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

def get_list_of_pets( url, header ):

    r = requests.get( url, headers=header )

    print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
    print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx

    templates = r.text # получаем ключ с помощью метода .text

    dict_id = json.loads(templates)

    di = list(dict_id.values())

    # id питомцев
    print(f' ID и имя всех питомццев:')
    for i in range( len(di[0]) ):
        print( { di[0][i]['name'] }, { di[0][i]['id'] } )
    return di

get_list = get_list_of_pets(request_url, get_header_query)