import get
import requests

key = (get.get_key) # получение ключа 


post_header_formData = {"auth_key":key, "name":"Sarah", "animal_type":"Doberman","age": '2',"pet_photo": ""}

request_url = "https://petfriends1.herokuapp.com/api/pets"

def add_info_new_pet(url, post_params, post_headers):

    r = requests.post(url, params=post_params, headers=post_headers, files={"pet_photo": open('apps/sarah.jpg', 'rb')})

    if r.status_code == requests.codes["ok"]:
        print( f'\n Status-Code: {r.status_code}' ) # принтит статус 
        print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx
        print(f' Sucsess!\n Name: {post_header_formData["name"]}\n Animal Type: {post_header_formData["animal_type"]}\n Age: {post_header_formData["age"]}')
    else:
        print(" PostError")


add_info_new_pet( request_url, post_header_formData, post_header_formData ) 