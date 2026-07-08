import requests

def test_random_dog():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
    assert response.json()['status'] == 'success'