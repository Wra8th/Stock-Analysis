import requests
from dotenv import dotenv_values

# extracting the .env file
config = dotenv_values(".env")

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(config['REDDIT_APP_SCRIPT_KEY'], config['REDDIT_APP_SECRET_KEY'])

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': config['REDDIT_USERNAME'],
        'password': config['REDDIT_PASSWORD']}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'stockTrader/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)


res = requests.get("https://oauth.reddit.com/r/DalalStreetTalks/hot",
                   headers=headers)

# print(res.json())  # let's see what we get

for post in res.json()['data']['children']:
    print(post['data']['title'])