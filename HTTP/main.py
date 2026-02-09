import requests

user = "akhil2006"
token = "akhil2006token"

url = f"https://pixe.la/v1/users/{user}/graphs/graph1"

graph = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "KM",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
} 

values = {
    "date" : "20251226",
    "quantity" : "6.69",

}
response = requests.post(url=url, json=values, headers=headers)
print(response.text)
