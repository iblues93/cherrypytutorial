import requests, base64, os

path = input("What is your file path?")

print("Attempting GET request for filename to localhost at port 8080...")
response = requests.get("http://127.0.0.1:8080/echo_file_name?filepath={}".format(path))
if response.status_code == 200:
    print("Request succeeded!")
    print(response.text)
else:
    print("Failed request!")

# For transfering of large files, this requires the use of POST. GET do not work because of large Base64 strings for large images
print("Testing uploading photo through webservice...")

input("Continue?")

image_path = "test.jpg"

with open(image_path, "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read())

# Convert into string, and removing of b' and ' at both end of the string
encoded_img_to_send = str(encoded_img)[2:-1]

print("Attempting POST request to upload image to localhost at port 8080...")
response = requests.post("http://127.0.0.1:8080/get_img",data={"filename":image_path,"data":encoded_img_to_send})
if response.status_code == 200:
    print("Request succeeded!")
    print(response.text)
else:
    print(response)