# working on API's
#start with Yelp API
# https://www.yelp.com/developers

"""
API KEYS ARE PRIVATE

"""

"""
REST API

COLLECTION OF INFORMATION OR A PLACE YOU CAN GO TO REQUEST INFORMATION

[DATA BASE] <> [API] <> [PYTHON APPLICATION]

THE OWNER OF THE DATABASE AND API CAN CONTROL WHAT IS PERMISSABLE USAGE OF THEIR DATA
CAN THEY READ OR WRITE
CAN THEY ONLY ACCESS IT A CERTAIN NUMBER OF TIMES



"""

import requests  #library for connecting API that we are working with
import json #java script object notation convert incoming data to object or dictionary


#registered account the yelp
api_key = 'UlHOGohef62Nsi0mFd_-IBE11BSpubGgiEUR0W0k1iC87oItjHSXsPQMY2zAFSNjO6wXbbxVQrJulKhqjiRHfNqf4snyfhyeBSdz8FGw1XZ6sy6FYr5fGxbXVmC7XHYx'


#pass headers

headers = {'Authorization': 'Bearer %s' %api_key } #need to pass headers
"""
url = "https://api.yelp.com/v3/businesses/search" #from yelp developer documentation, end point url



params = {'term':'seafood', 'location': 'New York City'} #parameters for the end point

#makeing a GEt request to the YELP API
req = requests.get(url, params=params, headers=headers)
#get is a method inside the request library
#we set the url above

print(req)
#<Response[200]> server found or page found
#,Response[404]> means the server or page not found

print(json.loads(req.text)) #using json library to print out what was actually in the request

"""
"""
#business reviews

url = "https://api.yelp.com/v3/businesses/I3_QvspB0SsqiUTN18-TlQ/reviews"

req = requests.get(url,headers=headers)
print('the status code is {}', format(req.status_code))
print(json.loads(req.text))

"""

#print reviews

id = 'I3_QvspB0SsqiUTN18-TlQ'
url = "https://api.yelp.com/v3/businesses/" + id + "/reviews"
req = requests.get(url,headers=headers)
parsed = json.loads(req.text)
reviews = parsed["reviews"]

for review in reviews:
    print(review['user']['name'], review['text'], review['rating'])


