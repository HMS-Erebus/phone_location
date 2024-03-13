import requests
def maps_open(lng,lat):
    # API
    url = "https://api.map.baidu.com/reverse_geocoding/v3"
    ak = "hxG9V22HDBAZ4wiBzLQy62eX6TzXLC7v"
    
    #lng=106.57741202706583
    #lat=29.494640044733433
    data = {
        "ak": ak,
        "output": "json",
        "coordtype": "wgs84ll",
        "extensions_poi": "0",
        "location": f"{lat},{lng}"
    }

    response = requests.get(url=url, params=data)
    is_data = response.json()

    formatted_address = is_data['result']['formatted_address']
    print("根据地址,获取位置在:", formatted_address)

