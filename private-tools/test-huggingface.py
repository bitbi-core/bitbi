import requests
import requests
import requests
import requests
import base64
import base64
import base64
import base64
import json
import json
import json
import json




# Open the image file in binary mode, convert to base64
# Open the image file in binary mode, convert to base64
# Open the image file in binary mode, convert to base64
# Open the image file in binary mode, convert to base64
with open('image.jpg', 'rb') as image_file:
with open('image.jpg', 'rb') as image_file:
with open('image.jpg', 'rb') as image_file:
with open('image.jpg', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')








API_URL = "https://api-inference.huggingface.co/models/InstantX/InstantID"
API_URL = "https://api-inference.huggingface.co/models/InstantX/InstantID"
API_URL = "https://api-inference.huggingface.co/models/InstantX/InstantID"
API_URL = "https://api-inference.huggingface.co/models/InstantX/InstantID"
headers = {"Authorization": "Bearer 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"}
headers = {"Authorization": "Bearer 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"}
headers = {"Authorization": "Bearer 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"}
headers = {"Authorization": "Bearer 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"}




# Prepare the data
# Prepare the data
# Prepare the data
# Prepare the data
data = {
data = {
data = {
data = {
    'inputs': {
    'inputs': {
    'inputs': {
    'inputs': {
        'image': {
        'image': {
        'image': {
        'image': {
            'b64': encoded_string
            'b64': encoded_string
            'b64': encoded_string
            'b64': encoded_string
        }
        }
        }
        }
    }
    }
    }
    }
}
}
}
}




def query(payload):
def query(payload):
def query(payload):
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	response = requests.post(API_URL, headers=headers, json=payload)
	response = requests.post(API_URL, headers=headers, json=payload)
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
	return response.content
	return response.content
	return response.content
image_bytes = query(data)
image_bytes = query(data)
image_bytes = query(data)
image_bytes = query(data)
# You can access the image with PIL.Image for example
# You can access the image with PIL.Image for example
# You can access the image with PIL.Image for example
# You can access the image with PIL.Image for example
import io
import io
import io
import io
from PIL import Image
from PIL import Image
from PIL import Image
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image = Image.open(io.BytesIO(image_bytes))
image = Image.open(io.BytesIO(image_bytes))
image = Image.open(io.BytesIO(image_bytes))
image.save("result.jpg")image.save("result.jpg")image.save("result.jpg")image.save("result.jpg")