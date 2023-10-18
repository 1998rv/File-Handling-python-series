# Developer Name :- Ravi Kumawat
# Date :- 18-10-2023
# Code :- To save any image in our path

import requests
from io import BytesIO
from PIL import Image

#  == image url which we want to save

def save_image(url):
    for i in range(0,10):
        response = requests.get(url) #  == to get response for this image we are using request
        captcha_image = Image.open(BytesIO(response.content))

        #======== put your path where you want to save image
        path = "C:\\Users\\pc\\PycharmProjects\\pythonProject\\rv_saveimg"

        captcha_image.save(f"{path}\\{i}.png")
        print(i)


url = "https://ceouttarpradesh.nic.in/rollpdf/CImage.aspx"
save_image(url)
