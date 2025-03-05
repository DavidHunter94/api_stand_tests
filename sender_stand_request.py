import requests
import configuration
import data


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # URL completa
                         json=body,  # Cuerpo de la solicitud
                         headers=data.headers)  # Encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())