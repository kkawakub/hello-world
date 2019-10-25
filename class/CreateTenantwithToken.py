import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\":{\r\n\t\t\"attributes\":{\r\n\t\t\t\"name\":\"admin\",\r\n\t\t\t\"pwd\":\"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
headers = {'Authorization': 'Basic ZW5hYmxlXzE6Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)

json_response = json.loads(response.text)
#print(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

tokenfromlogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])

url = "http://192.168.10.1/api/node/mo/uni/tn-TEST_TENANT.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-TEST_TENANT\",\r\n\t\t\t\"name\": \"TEST_TENANT\",\r\n\t\t\t\"rn\": \"tn-TEST_TENANT\",\r\n\t\t\t\"status\": \"created\"\r\n\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}\r\n"
cookie = {"APIC-cookie":tokenfromlogin}
#headers = {'Authorization': 'Basic ZW5hYmxlXzE6Y2lzY28='}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
