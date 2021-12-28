import pytest
import requests

# #get
import get
import get_pets

#post
import post_create_pet
import post_add_pet_w_info
import post_add_photo

#delete
import delete_pet

#put
import put

# ФИКСТУРЫ

# get:
@pytest.fixture()
def get_fixture():
    get
    return True
def test_getf(get_fixture):
    assert get_fixture == 1, "GetKey Error"

# get_list
@pytest.fixture()
def get_pets_fixture():
    get_pets
    return True
def test_get_pets(get_pets_fixture):
    assert get_pets_fixture == 1, "GetPets Error"



# post:

# create pet
@pytest.fixture()
def post_create_pet_fixture():
    post_create_pet
    return True
def test_post_create_pet(post_create_pet_fixture):
    assert post_create_pet_fixture == 1, "PostCreatePet Error"


# post add_new_with_info
@pytest.fixture()
def post_add_pet_w_info_fixture():
    post_add_pet_w_info
    return True
def test_post_add_pet_w_info(post_add_pet_w_info_fixture):
    assert post_add_pet_w_info_fixture == 1, "PostAddPetWInfo Error"


# post add_photo
@pytest.fixture()
def post_add_photo_fixture():
    post_add_photo
    return True
def test_post_add_photo(post_add_photo_fixture):
    assert post_add_photo_fixture == 1, "AddPhoto Error"


#delete
@pytest.fixture()
def delete_pet_fixture():
    delete_pet
    return True
def test_delete_pet(delete_pet_fixture):
    assert delete_pet_fixture == 1, "DeletePet Error"



#put
@pytest.fixture()
def put_pet_new_info_fixture():
    put
    return True
def test_put_new_pet(put_pet_new_info_fixture):
    assert put_pet_new_info_fixture == 1, "PutNewInfo Error"


# ПАРАМЕТРИЗАЦИЯ
# POST
key = '802cc048b84f7ca443618ce18ce9990bd8f3c2707e3331b69e848228'
wrong_key = '12345'

request_url_pet_simple = "https://petfriends1.herokuapp.com/api/create_pet_simple"
request_url_new_pet = "https://petfriends1.herokuapp.com/api/pets"

post_header_formData_pet_simple = { "auth_key": key, "name": "Sarah", "animal_type":"Doberman", "age": "2"}
post_header_formData_new_pet = {"auth_key":wrong_key, "name":"Sarah", "animal_type":"Doberman","age": '1',"pet_photo": ""}


@pytest.mark.parametrize('url, param, header, result',
                         [  # post_simple_pet
                             (request_url_pet_simple, post_header_formData_pet_simple, post_header_formData_pet_simple, True), # позитивный сценарий 
                             # post_add_info
                             (request_url_new_pet, post_header_formData_new_pet, post_header_formData_new_pet, False), # негативный сценарий 
                         ]
                         )
def test_post( url, param, header, result ):

    r = requests.post( url, params=param, headers=header )

    if requests.codes["ok"] == result:
        print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx
    else:
        print(" PostError")

# GET
key = '802cc048b84f7ca443618ce18ce9990bd8f3c2707e3331b69e848228'
wrong_key = '12345'

request_url = 'https://petfriends1.herokuapp.com/api/key' # ссылка на API с ключем
request_url_list_of_pets = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

get_email_pass_header = { 'email':'petlover@ya.com', 'password':'123456' } # информация о пользователе, который значится в БД
get_header_query_wrong = {"auth_key ": key, "filter": "pets"}

@pytest.mark.parametrize('url, param, header, result',
                         [  # get_api_key
                             (request_url, get_email_pass_header, get_email_pass_header, True), # позитивный сценарий
                             # get_my_pets_list
                             (request_url_list_of_pets, get_header_query_wrong, get_header_query_wrong, False) # негативный сценарий 
                         ]
                         )
def test_get( url, param, header, result ):

    r = requests.get( url, params=param, headers=header )

    if requests.codes["ok"] == result:
        print( f' Status: {r.status_code == requests.codes["ok"]}' ) # возвращает True, если код статуса не 4xx и не 5xx
    else:
        print(" PostError")