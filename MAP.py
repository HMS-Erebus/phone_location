import requests
import webbrowser
api_key = "hxG9V22HDBAZ4wiBzLQy62eX6TzXLC7v"
def get_location_info(lat, lng):
    
    url = f"http://api.map.baidu.com/reverse_geocoding/v3/?ak={api_key}&output=json&coordtype=wgs84ll&extensions_poi=0&location={lat},{lng}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 0:
        formatted_address = data['result']['formatted_address']
        return formatted_address
    else:
        return "状态码错误,不为0"

def open_map_in_browser(latitude, longitude, zoom=15):
    base_url = "http://api.map.baidu.com/staticimage/v2?"
    center = f"{longitude},{latitude}"
    markers = f"{longitude},{latitude}"
    params = {
        "ak": api_key,
        "center": center,
        "markers": markers,
        "width": 1024,
        "height": 800,
        "zoom": zoom
    }
    url = base_url + "&".join([f"{key}={value}" for key, value in params.items()])
    webbrowser.open(url)


