import requests
import json

url = 'https://XX.XX.XX.XX/zabbix/api_jsonrpc.php' #IP do Zabbix
auth = "YYYYYY" #Token de autenticação gerado pelo Zabbix
header = {'Content-Type':'application/json'}


def host_get():
    data = {
        "method": "host.get",
        "params": {
            "output": ["name"]
        },
        "jsonrpc": "2.0",
        "auth": "3fa4ee58ecca428ee97488067960f648",
        "id": "1"
    }

    data= json.dumps(data).encode()

    list_host = requests.post(url=url, data=data, headers=header, verify=False)
    return list_host.json()

def list_get():
    data = {
        "method": "item.get",
        "params": {
            "output": [
                "name", "hostid", "key_"
                ]
        },
        "jsonrpc": "2.0",
        "auth": "3fa4ee58ecca428ee97488067960f648",
        "id": 1}
    data = json.dumps(data).encode()
    list_item = requests.post(url=url, data=data, headers=header, verify=False)
    return list_item.json()

def group_get():
    data = {
        "method": "hostgroup.get",
        "params": {
            "sortorder": "groupid"
        },
        "jsonrpc": "2.0",
        "auth": "fbb8ae26d69fa2cd2733af3a23bc6631",
        "id": 1
}
    data = json.dumps(data).encode()
    list_group = requests.post(url=url, data=data, headers=header, verify=False)
    return list_group.json()

if __name__ == "__main__":

    lista_host = host_get()['result']
    list_item = list_get()['result']
    # lista_group = group_get()['result']

    for obj in lista_host:
        for obj2 in list_item:
            if obj['hostid'] == obj2['hostid']:
                print("ID: ", obj['hostid'], "Nome do host: ", obj['name'], "Trigger monitorada: ", obj2['name'])
