import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados")
        return []