import urllib3
import requests


url1 = "https://samples.clarifai.com/metro-north.jpg"
url2 = "https://s3.amazonaws.com/amazon-reviews-pds/tsv/sample_us.tsv"

response = requests.get(url2)
if response.status_code == 200:
    print("yes available")
elif response.status_code == 404:
    print("nothing is available")

print(response)

manager = urllib3.PoolManager()
response1 = manager.request('GET',url2,preload_content=False)

print(response1)

if response1 is not None:
    #with open('output.jpg','wb') as out:
    with open('sample.tsv', 'wb') as out:
        while True:
            data = response1.read()
            if not data:
                break
            out.write(data)