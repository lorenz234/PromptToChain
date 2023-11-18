import requests
import shutil
import os

openai_key = os.environ.get('openai_key')

def generate_image(prompt, save_path):
    # API endpoint for the OpenAI DALL·E image generator
    url = "https://api.openai.com/v1/images"

    # Set up the request headers
    headers = {
        "Authorization": openai_key,
        "Content-Type": "application/json"
    }

    # Set up the request payload with the prompt
    payload = {
        "prompt": prompt,
        "max_images": 1
    }

    # Send the POST request to the API
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    # Get the image URL from the response
    image_url = response.json()["images"][0]["url"]

    # Download the image and save it to the specified path
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    with open(save_path, "wb") as file:
        shutil.copyfileobj(response.raw, file)

    print("Image saved successfully!")

