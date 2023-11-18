import requests
import os
client_id = os.environ.get('client_id')


def upload_image_to_imgur(image_path, client_id):
    headers = {'Authorization': f'Client-ID {client_id}'}
    with open(image_path, 'rb') as image:
        response = requests.post(
            '/Users/lorenz/Desktop/ETH-Istanbul/web3modal/public/ai-image.jpg',
            headers=headers,
            files={'image': image}
        )
    return response.json()

