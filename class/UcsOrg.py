import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\ncookie=\"1572041350/a19f08f5-59cf-45a0-9a59-e4457a96317e\"\ninHierarchical=\"false\">\n    <inConfigs>\n<pair key=\"org-root/org-PythonMaster\">\n    <orgOrg\n    name=\"PythonMaster\"\n    dn=\"org-root/org-PythonMaster\"\n    \n    status=\"created\"\n    \n    sacl=\"addchild,del,mod\">\n    </orgOrg>\n</pair>\n    </inConfigs>\n</configConfMos>"
headers = {'Authorization': 'Basic Y2lzY286Y2lzY28='}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
