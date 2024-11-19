import requests
url = "https://mhw-db.com/weapons/17"
param = {
    'fields': 'name,id,type'
}
array = requests.get("https://mhw-db.com/weapons")
array2 = requests.get(url)
data = array2.json()

print(data)

