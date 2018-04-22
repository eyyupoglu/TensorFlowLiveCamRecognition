subscription_key = "7de5a340f2c6416082bc20b5578255d7"
assert subscription_key


vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "analyze"

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
image2 = "https://image.ibb.co/fhnLtc/fight.jpg"
image3 = "https://raw.githubusercontent.com/eyyupoglu/TensorFlowLiveCamRecognition/master/mike2.jpg"
import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Categories,Description,Color'}
data     = {'url': image3}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(image_caption)


