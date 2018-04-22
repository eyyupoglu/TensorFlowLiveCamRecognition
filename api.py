import subprocess

def pushPictureToGithub(fileName):
    try:
        subprocess.call("(git pull)", shell=True)
        subprocess.call("(git add )" + fileName, shell=True)
        subprocess.call("(git commit -m \"asdasd\")", shell=True) 
        subprocess.call("(git push)", shell=True)
    except:
        print("could not push picture")



def getApi(fileName):
    subscription_key = "7de5a340f2c6416082bc20b5578255d7"
    assert subscription_key
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    vision_analyze_url = vision_base_url + "analyze"

    link = "https://raw.githubusercontent.com/eyyupoglu/TensorFlowLiveCamRecognition/master/"+fileName
    image3 = "https://raw.githubusercontent.com/eyyupoglu/TensorFlowLiveCamRecognition/master/mike2.jpg"
    import requests
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
    params   = {'visualFeatures': 'Categories,Description,Color'}
    data     = {'url': link}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()

    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    print(image_caption)

    import pyttsx3
    engine = pyttsx3.init()
    engine.say(image_caption)
    engine.runAndWait()


    return image_caption


