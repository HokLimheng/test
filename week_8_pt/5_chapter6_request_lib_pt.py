import requests

title = input("put here: ")
api_key = '7cc82b34'
endpoint = 'http://www.omdbapi.com/'

r = requests.get('http://www.omdbapi.com/?apikey=7cc82b34&t=ABC')
# # print(r)
# input = input("put here: ")
# if input == "Title":
#     print(r.json()["Year"])
# print(r.text)

### using params parameter ####
params = {
    "apikey": api_key,
    "t": title
}

r = requests.get(endpoint, params=params).json()
Rating = r["imdbRating"]
created = r["Year"]
print(f'Result for {title}')
print(f'created in {created}')
print(f'Rating: {Rating}/10')