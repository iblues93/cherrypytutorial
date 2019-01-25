import requests

path = input("What is your file path?")

print("Attempting GET request to localhost at port 8080...")
response = requests.get("http://127.0.0.1:8080/echo_file_name?filepath={}".format(path))
if response.status_code == 200:
    print("Request succeeded!")
    print(response.text)
else:
    print("Failed request!")