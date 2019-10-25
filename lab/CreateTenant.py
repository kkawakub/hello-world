import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-TEST_TENANT.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-TEST_TENANT\",\r\n\t\t\t\"name\": \"TEST_TENANT\",\r\n\t\t\t\"rn\": \"tn-TEST_TENANT\",\r\n\t\t\t\"status\": \"created\"\r\n\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}\r\n"
cookie = {"APIC-cookie":"bA0iyg5WBFY6h680VTR9rw5WNDeJpHjPCO/eY0PlUw/2MFbOQZpFowh8kkRBCTGRdXJjeTsgGFpwkH9WcNbuRoXu5g6Qjbvp0r3uAMPSyQdvbBhcz05xE6n0+15BM4r5zlcdrhStEFGS94uPOvmE52l4VM0bH2s3+eOFE8jrks0="}
headers = {'Authorization': 'Basic ZW5hYmxlXzE6Y2lzY28='}

response = requests.request("POST", url, data=payload, cookies=cookie, headers=headers)

print(response.text)