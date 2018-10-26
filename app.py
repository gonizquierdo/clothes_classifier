from InstagramAPI import InstagramAPI
import requests
import json
from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client_id = 'f0dbadf3c8c040089f5ff3ada44333db'
client_secret = '5021b99e9964479092836736e20c2d6f'

# Token (23/10 - 19.00hs aprox): 610637464.f0dbadf.40429666ce554609812c7ac91208c8b2


#res = requests.get('https://api.instagram.com/v1/users/self/', {'access_token':token})
#print(res.url)

@app.route("/user/<token>", methods=['GET', 'POST'])
def get_name(token):
    instagram_api = InstagramAPI(client_id, client_secret, token);
    user = instagram_api.get_user()

    response = {}
    print("Incoming request")
    return Response(json.dumps({"user":user}))
@app.route("/recent_media/<token>", methods=['GET', 'POST'])

def save_recent_media(token):
    instagram_api = InstagramAPI(client_id, client_secret, token);
    recent_media = instagram_api.get_recent_media()
    for pic in recent_media:
        img_data = requests.get(pic['images']['standard_resolution']['url']).content
        with open('images/img_'+pic['created_time']+'.jpg', 'wb') as handler:
            handler.write(img_data)

    return Response(json.dumps({"user": 'Gonzi'}))

if __name__ == "__main__":
    app.run()