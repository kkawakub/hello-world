import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\":{\r\n\t\t\"attributes\":{\r\n\t\t\t\"name\":\"admin\",\r\n\t\t\t\"pwd\":\"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
headers = {'Authorization': 'Basic ZW5hYmxlXzE6Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)