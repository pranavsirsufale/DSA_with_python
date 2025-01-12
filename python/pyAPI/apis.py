import requests

def fetch_random_user_freeapi():
    url ='https://api.freeapi.app/api/v1/public/randomusers/user/random'

    response = requests.get(url)
    data = response.json()

    if(data['success'] and 'data' in data ):
        user_data = data['data'] 
        print(user_data)

fetch_random_user_freeapi()
        






