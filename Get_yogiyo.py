import requests
import json
from Ordersdatas import *
from Make_Datas import *
from DBMaker import *
from AccessToken import *
import time


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


def getItemReviews(id, page, count, menu_id):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}
    url = f"https://www.yogiyo.co.kr/api/v1/reviews/{id}/?page={page}&count={count}&sort=time&type=&sort_order=desc&menu_id={menu_id}"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json


def get_Review(id, count, page):
    header = {"x-apikey": 'iphoneap',
              "x-apisecret": 'fe5183cc3dea12bd0ce299cf110a75a2'}
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
    Line_tokens = f"Bearer {Access_Token}"
    header = {
        "Authorization": Line_tokens
    }
    url = f"https://api.line.me/v2/bot/profile/{UserId}"
    response = requests.get(url, headers=header)
    Get_json = response.json()
    return Get_json


def Push_Message(UserId, UserName, delivery_fee, OrderData, cart, lan, lng):
    # Line_tokens = f"Bearer {Access_Token}"
    # header = {
    #     "Authorization": Line_tokens,
    #     "Content-Type": "application/json"
    # }

    Order_Code = Insert_Data(
        UserName, UserId, delivery_fee, OrderData, cart, lan, lng)

    options_fee = 0
    totals = 0
    Menu_Data = []
    for i in cart:
        menu = i['menu']

        if (len(i['options']) == 0):
            MDs = Set_Dics(menu, i)
            Make_dics(Menu_Data, MDs)
            totals = totals + i['totalPrice']
        else:
            MDs = Set_Dics(menu, i)
            Make_dics(Menu_Data, MDs)
            totals = totals + i['totalPrice']
            for x in i['options']:
                Option_Data = Set_Options(x)
                Make_dics(Menu_Data, Option_Data)
                options_fee = options_fee + x['subOptionPrice']

    # datas = Make_OrderList(UserId, UserName, OrderData,
    #                        cart, Menu_Data, options_fee, totals, Order_Code)
    # url = f"https://api.line.me/v2/bot/message/push"
    # response = requests.post(url, headers=header, data=json.dumps(datas))
    template_Test(UserId, UserName, int(totals), int(delivery_fee), Order_Code)
    # Get_json = response.json()
    return Order_Code


def template_Test(userId, UserName, Total_pay, deliver_fee, Order_Code):
    time.sleep(0.5)
    Line_tokens = f"Bearer {Access_Token}"
    Total_Count = Total_pay + deliver_fee + 3000
    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"
    }
    datas = Make_DD(userId, Total_pay, deliver_fee,
                    Total_Count, UserName, Order_Code)
    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header, data=json.dumps(datas))
    Get_json = response.json()
    return Get_json


def IMG_Test(UserId, file_Name):
    Line_tokens = f"Bearer {Access_Token}"

    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"

    }
    datas = {
        "to": UserId,
        "messages": [
            {
                "type": "image",
                "originalContentUrl": file_Name,
                "previewImageUrl": file_Name,
            }
        ]
    }

    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header, data=json.dumps(datas))
    Get_json = response.json()
    return Get_json


if __name__ == "__main__":

    # delivery_fee = 3000
    # data = Push_Message("U812329a68632f4237dea561c6ba1d413",
    #                     '크턱', 3000, orderdata, cart2)
    # print(data)
    print(get_Menu(351360))
    # print(data)
    # IMG_Test("Uad859360a7e2589c8c213b3b47fc27a2")
    # get_Menu()
    # get_Menu(1109037)
