import requests, json

image_url = 'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2023-01/robert-downey-jr-2-te-230112-5af7b1.jpg'

response = requests.get(image_url)

with open("images/test.jpg", "wb") as file:
    file.write(response.content)