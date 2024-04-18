import requests

r = requests.get("https://httpbin.org/get")
print(r)

r = requests.get("https://httpbin.org/get")
print(dir(r))

r = requests.get("https://httpbin.org/get")
print(help(r))

r = requests.get("https://httpbin.org/get")
print(r.status_code)
