import requests
import Phone_get_loc

#

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

def tac_get(nrf_ip):
    phonenumber=input("请输入手机号")
    suffix=Phone_get_loc.imsi_get(phonenumber)
    amfip = Amfip_get(nrf_ip)
    url = f"http://{amfip}:7777/namf-comm/v1/ue-contexts/imsi-{suffix}/tac_list"

    # 发送GET请求
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code!=200:
        print("状态码有误，无法查询")
        return
    tac1 = response.json()
    print("TAC:",tac1)

if __name__ == "__main__":
    tac_get(input("请输入nef_ip"))

