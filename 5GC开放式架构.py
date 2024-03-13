import requests
import AMFIP_tac
import AMFIP_get   
import Phone_get_loc
import os
#获取网元注册信息
def get_check(nrf_ip):
    response = requests.get(f"http://{nrf_ip}:7777/nnrf-nfm/v1/nf-instances/", timeout=5)
    if response.status_code == 200:
        print("网元参数信息：")
        print(response.json())
        print()
    else:
        print("错误", "无法连接到指定的nrfIP,请检查输入是否正确。")







def display_menu():
    print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print("║请选择操作选项：                          ")
    print("║   1. 获取网元参数信息                    ")
    print("║   2. 查询AMF网元IP                      ")
    print("║   3. 查询TAC                            ")
    print("║   4. 手机定位并调用百度地图              ")
    print("║   5. 退出                               ")
    print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    choice = input("请输入选项数字：")
    return choice


def main():
  

    nrf_ip = input("请输入nrf网元IP:")
    try:
        response = requests.get(f"http://{nrf_ip}:7777/nnrf-nfm/v1/nf-instances/", timeout=5)
        if response.status_code == 200:
            while True:
                choice = display_menu()
                if choice == '1':
                    get_check(nrf_ip)
                    pass
                elif choice == '2':
                    AMFIP_get.Amfip_get(nrf_ip)
                    pass
                elif choice == '3':
                    AMFIP_tac.tac_get(nrf_ip)
                    pass
                elif choice == '4':
                    Phone_get_loc.get_loc()
                    pass
                elif choice == '5':
                    break
                else:
                    print("无效的选项，请重新输入。")
    except :
        print("连接超时,请检查网络连接或者目标NRF地址是否正确。")

if __name__ == "__main__":
    main()




