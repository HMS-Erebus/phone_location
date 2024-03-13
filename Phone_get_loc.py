import requests
import pandas as pd
import MAP
amfip = '10.88.13.63'
def imsi_get(suffix):
    phone_imsi={
        "177":"4604000",
        "189":"4664000",
        "159":"4600000"
    }
    #手机号
 
    #18900000001
    prefix=suffix[:3]

    #这个地方对phone_imsi字典使用get 可以进行键值查找，自动查找有没有符合prefix的，如果没有则返回no
    imsi_prefix=phone_imsi.get(prefix,"no")
    print(imsi_prefix)
    #这个地方和上面对应，根据返回值是否为no，判断查找是否成功。
    if imsi_prefix != "no":
        suffix=imsi_prefix+suffix[3:]#数字合成
        print("转换完成")
        return suffix
    else:
        print("运行商表里不存在此PLMN")

#下面是接入tac获取流程
def tac_get(ismi):
    url = f"http://{amfip}:7777/namf-comm/v1/ue-contexts/imsi-{ismi}/tac_list"
    # 发送GET请求
    response = requests.get(url)
    # 检查响应状态码
    if response.status_code==200:
        tac1 = response.json()
        print(tac1)
        return tac1
    else:
        print("状态码有误，无法查询")
        print(f"status_code:{response.status_code}")

def loc_get():
    tac=81
    is_tac=tac
    df=pd.read_excel('data.xlsx')

    row=df.loc[df['tac']==is_tac].index
    if len(row)>0:
        print("查找结果为")
        for idx in row:
            lng=df['经度'][idx]
            lat=df['纬度'][idx]
            info=MAP.get_location_info(lat,lng)
            print(f"位置是:{info}")
            MAP.open_map_in_browser(lat,lng)

def get_loc():
    suffix=input("请输入手机号以便转换\n")
    ismi=imsi_get(suffix)
    print(f"imsi:{ismi}\n")
    #tac_get(ismi)
    loc_get()
    

if __name__ == "__main__":
    get_loc()
