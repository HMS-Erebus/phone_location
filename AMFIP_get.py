import requests

def Amfip_get(nrf_ip):
    nf_types = 'AMF'
    headers = {'Content-Type': 'application/json'}
    nrf_api_url = f'http://{nrf_ip}:7777/nnrf-nfm/v1'
    nf_instances_list = []
    url = f'{nrf_api_url}/nf-instances'
    if nf_types:
        url += f'?nf-type={nf_types}'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            nf_instances = response.json()
            items = nf_instances["_links"]["items"]
            for item in items:
                href = item["href"]
                responses2 = requests.get(href, headers=headers)
                nf_instances2 = responses2.json()
                nf_instances_list.append(nf_instances2) 
                ipv4_address = nf_instances2['ipv4Addresses'][0]
                print(f"AMF_IP:{ipv4_address}")
                return ipv4_address
                #print(url)
                #print(nf_instances)
                #print(nf_instances2)