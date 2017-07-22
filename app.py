#I will be connecting to api.github.com
# I shall list all public repositories via the termial
import requests
## first get the api url from the terminal #Url to the public repo
url=input('Enter api url please include https or http:')

#https://api.github.com/gists/public 
response = requests.get(url)
#we receive the reponse
assert response.status_code == 200
#response status must be 200 for success

#we loop all the repo and print repo langage and name
for repo in response.json():
  
     print ('[{}] {}'.format(repo['files'], repo['name']))