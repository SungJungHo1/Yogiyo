import requests
from datetime import datetime
import googletrans
import json

translator = googletrans.Translator()

def get_Yogiyo(category, lat, lng):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}

    url = f"https://www.yogiyo.co.kr/api/v1/restaurants-geo/?category={category}&items=60&lat={lat}&lng={lng}&order=rank&page=0&search="
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json


def get_Menu(id):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}

    url = f"https://www.yogiyo.co.kr/api/v1/restaurants/{id}/menu/?add_photo_menu=android&add_one_dish_menu=true&order_serving_type=delivery"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json

def getItemReviews(id,page,count,menu_id):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}
    url = f"https://www.yogiyo.co.kr/api/v1/reviews/{id}/?page={page}&count={count}&sort=time&type=&sort_order=desc&menu_id={menu_id}"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json

def get_Review(id,count,page):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}

    # url = f"https://www.yogiyo.co.kr/api/v1/reviews/{id}/?count=10&only_photo_review=false&page=1&sort=time"
    url = f"https://www.yogiyo.co.kr/api/v1/reviews/{id}/?count={count}&only_photo_review=false&page={page}&sort=time"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json


def Search_Category(Search, page, lat, lng):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}

    url = f"https://www.yogiyo.co.kr/api/v1/restaurants-geo/search/?items=60&lat={lat}&lng={lng}&order=rank&page={page}&search={Search}"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json

def Find_Top(lat, lng):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}

    url = f"https://www.yogiyo.co.kr/api/v1/restaurants-geo/?items=60&lat={lat}&lng={lng}&order=review_avg&page=0&search="
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json

def Find_User_Profile(UserId):
    Line_tokens = "Bearer LPoD2xZWE8Yz/OiZvghUhnuVRWqijmXiziipqaGKLbr30u9nEYmn3gcXM+U41brU6fKNWFMEcEyAQi/KiDaHHLHB/CJBbRphNIJLAYgmNJ6R18csA3uCr/IlGOGNZZIOsHmjTgH2gF4wSSI5/NRROQdB04t89/1O/w1cDnyilFU="
    header = {
            "Authorization": Line_tokens
        }
    url = f"https://api.line.me/v2/bot/profile/{UserId}"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json

def Google_translate(from_lan : str,to : str,text : str):

    result = translator.translate(text,src= from_lan, dest=to)
    return result.text

def Push_Message(UserId,UserName,OrderData,cart):
    Line_tokens = "Bearer LPoD2xZWE8Yz/OiZvghUhnuVRWqijmXiziipqaGKLbr30u9nEYmn3gcXM+U41brU6fKNWFMEcEyAQi/KiDaHHLHB/CJBbRphNIJLAYgmNJ6R18csA3uCr/IlGOGNZZIOsHmjTgH2gF4wSSI5/NRROQdB04t89/1O/w1cDnyilFU="
    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"
    }
    text1 = f"주문자명: {UserName}\n주소 : {OrderData['address'] + ' ' + OrderData['addressDetail']}\n1층비밀번호 : {OrderData['firstFloorEntranceCode']}\n주문사항 : {OrderData['deliveryMessage']}\n전화번호 : {OrderData['phone']}"
    text2 = ""
    for idx,i in enumerate(cart):
        menu = i['menu']
        if idx == 0:
            text2 = text2 + f"음식점 이름 : {i['storeName']}\n메뉴명 : {menu['menu_name']}\n갯수 : {i['quantity']}\n개당가격 : {menu['price']}\n총가격 : {i['totalPrice']}"
        else:
            text2 = text2 + f"\n\n음식점 이름 : {i['storeName']}\n메뉴명 : {menu['menu_name']}\n갯수 : {i['quantity']}\n개당가격 : {menu['price']}\n총가격 : {i['totalPrice']}"
    datas = {
        "to": UserId,
        "messages":[
            {
                "type":"text",
                "text":text1
            },
            {
                "type":"text",
                "text":text2
            }
        ]
    }
    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header,data= json.dumps(datas))
    Get_json = response.json()
    return Get_json

if __name__ == "__main__":
    #  print(get_Yogiyo('1인분주문', 36.969655961906, 127.244958777736))
    # print(Find_User_Profile("Uad859360a7e2589c8c213b3b47fc27a2"))
    orderdata = {'address': 'asdas', 'addressDetail': 'asdasd', 'firstFloorEntranceCode': 'asdasd', 'addressPhoto': {}, 'deliveryMessage': '기본', 'phone': 'asdasd'}
    cart = [
            {
                'menu': 
                {
                    'menu_name': '순두부국밥（특）', 
                    'menuId': '568040348', 
                    'price': '10500'
                }, 
                'options': [], 
                'quantity': 7, 
                'totalPrice': 73500, 
                'basePrice': 73500, 
                'storeId': '1111759', 
                'storeName': '더진국-가락점'
            }, 
            {
                'menu': 
                {
                    'menu_name': '직화물냉면（보통）', 
                    'menuId': '568040350', 
                    'price': '9000'
                    }, 
                'options': [], 
                'quantity': 8, 
                'totalPrice': 72000, 
                'basePrice': 72000, 
                'storeId': '1111759', 
                'storeName': '더진국-가락점'
            }
        ]
    data = Push_Message("Uad859360a7e2589c8c213b3b47fc27a2",'크턱',orderdata,cart)
    print(data)
    # print(get_Menu(468686))
    # print(get_Review(468686))
    # print(Search_Category("치킨", 0, "36.969655961906", "127.244958777736"))
