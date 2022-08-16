def Make_dics(get_List,lists):
    for i in lists:
        get_List.append(i)
    return get_List

def Set_Options(x):
    datas = [{
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

    return datas

def Set_Dics(menu,i):
    data = [{
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
    return data

def Make_OrderList(UserId,UserName,OrderData,cart,Menu_Data,options_fee,totals,Order_Code):
    datas = {
        "to": UserId,
        "messages":[
            {
                "type": "flex",
                "altText": "주문정보",
                "contents": {
                    "type": "carousel",
                    "contents": [
                    {######flax1
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
                                        "text": str(Order_Code),
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
                    },######flax1
                    {#######flax2
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
                                        "text": str(Order_Code),
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
                        }############flax2
                    ]
                    }
            }
        ]
    }
    return datas

def Make_DD(userId,Total_pay,deliver_fee,Total_Count,UserName,Order_Code):
    datas = {
        "to": userId,
        "messages":[
            {
                "type": "flex",
                "altText": "주문이 완료되었습니다!",
                "contents": {
                    "type": "carousel",
                    "contents": [
                    {############### 시작
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
                                        "text": str(Order_Code),
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
                    },############### 끝
                    {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "maxHeight": "300px",
                            "contents": [
                            {
                                "type": "text",
                                "text": "❤FASTFOOD❤",
                                "wrap": True,
                                "align": "center",
                                "gravity": "center"
                            },
                            {
                                "type": "text",
                                "text": f"\n위 계좌번호로 입금 해주세요🙏🏻\n\n입금 확인후 {UserName}님 에게  음식 배달을 시작합니다🥰  \n\n🍝🍲🍤🦪🍙🎂🍕🍟🌮🥘🍰🍱🍣🥟🍜🍦🧁🍿🧋🌭🍔🌯",
                                "wrap": True,
                                "align": "center",
                                "gravity": "center"
                            }
                            ]
                        },
                        "styles": {
                            "footer": {
                            "separator": True
                            }
                        }
                    }
                    ]
                }

            }
        ]
    }
    return datas
