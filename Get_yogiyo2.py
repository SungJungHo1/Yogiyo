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

def Push_Message(UserId,UserName,delivery_fee,OrderData,cart):
    Line_tokens = "Bearer LPoD2xZWE8Yz/OiZvghUhnuVRWqijmXiziipqaGKLbr30u9nEYmn3gcXM+U41brU6fKNWFMEcEyAQi/KiDaHHLHB/CJBbRphNIJLAYgmNJ6R18csA3uCr/IlGOGNZZIOsHmjTgH2gF4wSSI5/NRROQdB04t89/1O/w1cDnyilFU="
    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"
    }
    text2 = f"배달비 : {delivery_fee}"
    options_fee = 0
    totals = 0
    Menu_Data = []
    for idx,i in enumerate(cart):
        menu = i['menu']
        
        if (len(i['options']) == 0):
            MDs = [{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "음식이름",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": menu['menu_name'],
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "wrap": True
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "가격",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": format(int(menu['price']), ',d') + ' ￦',
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "갯수",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": str(i['quantity']) + "개",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "총 가격",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": format(int(i['totalPrice']), ',d') + ' ￦',
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            }]
            Make_dics(Menu_Data,MDs)
            totals = totals + i['totalPrice']
        else:
            MDs = [{
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "음식이름",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": menu['menu_name'],
                    "size": "sm",
                    "color": "#111111",
                    "align": "end",
                    "wrap": True
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "가격",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": format(int(menu['price']), ',d') + ' ￦',
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "갯수",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": str(i['quantity']) + "개",
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "text",
                    "text": "총 가격",
                    "size": "sm",
                    "color": "#555555"
                },
                {
                    "type": "text",
                    "text": format(int(i['totalPrice']), ',d') + ' ￦',
                    "size": "sm",
                    "color": "#111111",
                    "align": "end"
                }
                ]
            },
            {
                "type": "separator",
                "margin": "lg"
            },]
            Make_dics(Menu_Data,MDs)
            totals = totals + i['totalPrice']
            for x in i['options']:
                Option_Data = [{
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "옵션메뉴",
                        "size": "sm",
                        "color": "#1DB446"
                    },
                    {
                        "type": "text",
                        "text": x['optionName'],
                        "align": "end",
                        "size": "sm",
                        "color": "#111111",
                        "wrap": True
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "옵션명",
                        "size": "sm",
                        "color": "#1DB446"
                    },
                    {
                        "type": "text",
                        "text": x['subOptionName'],
                        "size": "sm",
                        "color": "#111111",
                        "align": "end",
                        "wrap": True
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "가격",
                        "size": "sm",
                        "color": "#1DB446"
                    },
                    {
                        "type": "text",
                        "text": format(x['subOptionPrice'], ',d') + ' ￦',
                        "size": "sm",
                        "color": "#111111",
                        "align": "end"
                    }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "lg"
                },]
                Make_dics(Menu_Data,Option_Data)
                options_fee = options_fee + x['subOptionPrice']
            # text3 = text3 + f"\n\n메뉴 갯수 : {i['quantity']}\n옵션 총 가격 : {format(options_fee, ',d')}\n메뉴당 가격 : {format(int(menu['price']), ',d')}\n총가격 : {format(int(i['totalPrice']), ',d')}"
            # text2 = text2 + text3
    datas = {
        "to": UserId,
        "messages":[
            {
                "type": "flex",
                "altText": "주문정보",
                "contents": {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "FastFood",
                                "weight": "bold",
                                "color": "#1DB446",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "고객정보",
                                "weight": "bold",
                                "size": "xxl",
                                "margin": "md"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "separator",
                                    "margin": "xxl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "주문자명",
                                        "size": "sm",
                                        "color": "#555555"
                                    },
                                    {
                                        "type": "text",
                                        "text": UserName,
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "wrap": True
                                    }
                                    ],
                                    "margin": "xxl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "주소",
                                        "size": "sm",
                                        "color": "#555555"
                                    },
                                    {
                                        "type": "text",
                                        "text": OrderData['address'] + ' ' + OrderData['addressDetail'],
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "wrap": True
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "1층 비밀번호",
                                        "size": "sm",
                                        "color": "#555555"
                                    },
                                    {
                                        "type": "text",
                                        "text": OrderData['firstFloorEntranceCode'],
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "wrap": True
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "주문사항",
                                        "size": "sm",
                                        "color": "#555555"
                                    },
                                    {
                                        "type": "text",
                                        "text": OrderData['deliveryMessage'],
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "wrap": True
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "전화번호",
                                        "size": "sm",
                                        "color": "#555555"
                                    },
                                    {
                                        "type": "text",
                                        "text": OrderData['phone'],
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                        "wrap": True
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "주문번호",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "#743289384279",
                                    "color": "#aaaaaa",
                                    "size": "xs",
                                    "align": "end"
                                }
                                ]
                            }
                            ]
                        },
                        "styles": {
                            "footer": {
                            "separator": True
                        }
                    }
                },
            },
            {
                "type": "flex",
                "altText": "주문정보",
                "contents":
                {
                    "type": "bubble",
                    "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "FastFood",
                                "weight": "bold",
                                "color": "#1DB446",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "주문정보",
                                "weight": "bold",
                                "size": "xxl",
                                "margin": "md"
                            },
                            {
                                "type": "separator",
                                "margin": "none"
                            },
                            {
                                "type": "text",
                                "text": cart[0]['storeName'],
                                "size": "md",
                                "align": "center",
                                "gravity": "center",
                                "margin": "lg",
                                "weight": "bold",
                                "wrap": True
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "separator",
                                    "margin": "lg"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "contents":Menu_Data},########################메뉴명
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "옵션가격",
                                        "color": "#555555",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": format(options_fee, ',d') + ' ￦',
                                        "align": "end",
                                        "color": "#111111",
                                        "size": "sm"
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "총 가격",
                                        "color": "#555555",
                                        "size": "sm"
                                    },
                                    {
                                        "type": "text",
                                        "text": format(totals, ',d') + ' ￦',
                                        "align": "end",
                                        "color": "#111111",
                                        "size": "sm"
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "주문번호",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "#743289384279",
                                    "color": "#aaaaaa",
                                    "size": "xs",
                                    "align": "end"
                                }
                                ]
                            }
                            ]
                        },
                        "styles": {
                            "footer": {
                            "separator": True
                            }
                        }
                    }
            }
        ]
    }
    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header,data= json.dumps(datas))
    template_Test(UserId,int(totals),int(delivery_fee))
    Get_json = response.json()
    return Get_json

def template_Test(userId,Total_pay, deliver_fee):
    Line_tokens = "Bearer LPoD2xZWE8Yz/OiZvghUhnuVRWqijmXiziipqaGKLbr30u9nEYmn3gcXM+U41brU6fKNWFMEcEyAQi/KiDaHHLHB/CJBbRphNIJLAYgmNJ6R18csA3uCr/IlGOGNZZIOsHmjTgH2gF4wSSI5/NRROQdB04t89/1O/w1cDnyilFU="
    Total_Count = Total_pay + deliver_fee + 3000
    header = {
        "Authorization": Line_tokens,
        "Content-Type": "application/json"
    }
    datas = {
        "to": userId,
        "messages":[
            {
                "type": "flex",
                "altText": "주문이 완료되었습니다!",
                "contents": {############### 시작
                     "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "FASTFOOD",
                                "weight": "bold",
                                "color": "#000000",
                                "size": "sm"
                            },
                            {
                                "type": "text",
                                "text": "주문금액",
                                "weight": "bold",
                                "size": "xxl",
                                "margin": "md",
                                "color": "#1DB446"
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "xxl",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "총 가격",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": format(Total_pay, ',d')  + ' ￦',
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end",
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "배송비",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": format(deliver_fee, ',d')  + ' ￦',
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "서비스요금",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "3,000 ￦",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                    ]
                                },
                                {
                                    "type": "separator",
                                    "margin": "xxl"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "총 금액",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "text",
                                        "text": '￦ ' + format(Total_Count, ',d'),
                                        "align": "end",
                                        "weight": "bold",
                                        "color": "#1DB446"
                                    }
                                    ]
                                },
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "margin": "xxl",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "계좌번호",
                                        "size": "sm",
                                        "color": "#111111"
                                    },
                                    {
                                        "type": "text",
                                        "text": "1000-10120-2130921",
                                        "size": "sm",
                                        "color": "#037bfc",
                                        "align": "end"
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "은행명",
                                        "size": "sm",
                                        "color": "#111111"
                                    },
                                    {
                                        "type": "text",
                                        "text": "우리은행",
                                        "size": "sm",
                                        "color": "#037bfc",
                                        "align": "end"
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "예금주",
                                        "size": "sm",
                                        "color": "#111111"
                                    },
                                    {
                                        "type": "text",
                                        "text": "홍길동",
                                        "size": "sm",
                                        "color": "#037bfc",
                                        "align": "end"
                                    }
                                    ]
                                }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin": "xxl"
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "margin": "md",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "주문번호",
                                    "size": "xs",
                                    "color": "#aaaaaa",
                                    "flex": 0
                                },
                                {
                                    "type": "text",
                                    "text": "#743289384279",
                                    "color": "#aaaaaa",
                                    "size": "xs",
                                    "align": "end"
                                }
                                ]
                            }
                            ]
                        },
                        "styles": {
                            "footer": {
                            "separator": True
                            }
                        }
                }############### 끝

            }
        ]
    }
    url = f"https://api.line.me/v2/bot/message/push"
    response = requests.post(url, headers=header,data= json.dumps(datas))
    Get_json = response.json()
    return Get_json

def Make_dics(get_List,lists):
    for i in lists:
        get_List.append(i)
    return get_List


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
    cart2 = [
  {
    'menu': {
      'menu_name': '레전드 고기만 500g',
      'menuId': '314436161',
      'price': '16800'
    },
    'options': [
      {
        'optionName': '고기 선택',
        'subOptionName': '칼집장인 숙성 꽃삼겹 500g',
        'subOptionPrice': 2000
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '특제소스 양념갈비 400g',
        'subOptionPrice': 2000
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '고소한 숙성 우삼겹 400g',
        'subOptionPrice': 2000
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '프리미엄 소  고기 스테이크 400g',
        'subOptionPrice': 4000
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '숙성 프리미엄 삼겹 500g',
        'subOptionPrice': 1500
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '두툼한 목살구이 500g',
        'subOptionPrice': 500
      },
      {
        'optionName': '고기 선택',
        'subOptionName': '숙성 프리미엄 삼겹 250g＋두툼한 목살구이 250g',
        'subOptionPrice': 1500
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '숙성 프리미엄 삼겹 250g＋두툼한 목살구이 250g 추가',
        'subOptionPrice': 10500
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '숙성 프리미엄 삼겹 500g 추가',
        'subOptionPrice': 10500
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '칼집장인 숙성 꽃삼겹 500g 추가',
        'subOptionPrice': 11000
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '두툼한 목살구이 500g 추가',
        'subOptionPrice': 9000
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '특제소스 양념갈비 400g 추가',
        'subOptionPrice': 10000
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '고소한 숙성 우삼겹 400g 추가',
        'subOptionPrice': 11000
      },
      {
        'optionName': '고기 추가 선택',
        'subOptionName': '프리미엄 소고기 스테이크 400g 추가',
        'subOptionPrice': 13000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '레전드 매운 물냉면 추가',
        'subOptionPrice': 8600
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '레전드 매운 비빔냉면 추가',
        'subOptionPrice': 8600
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '레전드 물냉면 추가',
        'subOptionPrice': 8000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '레전드 비빔냉면 추가',
        'subOptionPrice': 8000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '모짜렐라 콘치즈 추가',
        'subOptionPrice': 3000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '살얼음 동동 묵사발 추가',
        'subOptionPrice': 4000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '품질좋은육 회 한접시 추가',
        'subOptionPrice': 4000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '매콤달달 떡볶이 추가',
        'subOptionPrice': 4000
      },
      {
        'optionName': '반찬 추가 선택',
        'subOptionName': '매콤달달 떡볶이＋모짜렐라치즈 추  가',
        'subOptionPrice': 5000
      }
    ],
    'quantity': 1,
    'totalPrice': 158500,
    'basePrice': 158500,
    'storeId': '1049420',
    'storeName': '레전드고기한상-암사점'
  }
]
    delivery_fee = 3000
    data = Push_Message("Uad859360a7e2589c8c213b3b47fc27a2",'크턱',delivery_fee,orderdata,cart)
    print(data)
    # print(template_Test(10000,3000))
    # print(get_Menu(468686))
    # print(get_Review(468686))
    # print(Search_Category("치킨", 0, "36.969655961906", "127.244958777736"))
