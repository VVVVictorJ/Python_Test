import requests


# get请求
payload = {'t':'1', 'q':'2'}
r1 = requests.get('http://127.0.0.1:5000/httptest', params=payload)
print(r1.text)


# post请求
user_info = {'Q':['5','6']}
r2 = requests.post("http://127.0.0.1:5000/httptest", data=user_info)
print(r2.text)
