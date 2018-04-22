import http, urllib

headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Categories,Description,Color'}
data     = {'url': image3}

conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

print("Obtaining response...")
conn.request("POST","/vision/v1.0/%s" % headers, params)
response = conn.getresponse()

data = response.read()
#    print(data)
conn.close()