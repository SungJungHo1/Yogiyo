from pymongo import MongoClient
from Ordersdatas import *
from datetime import *
from random import *
from datetime import datetime, timedelta, timezone

client = MongoClient('mongodb://fastfood:fastfood@43.200.202.12', 27017)

mydb = client['FastFoodDB']
mycol = mydb['OrderDatas']
errcol = mydb['Errors']


def Insert_Data(UserName, UserId, Delivery_Fee, Order_Data, Cart):
    z = randrange(0, 900)
    Order_Code = str(datetime.now().hour) + str(datetime.now().month) + str(datetime.now().year) + \
        str(datetime.now().day) + \
        str(int(datetime.now().microsecond / 1000)) + str(z)[-1]

    timezone_kst = timezone(timedelta(hours=9))
    datetime_utc2 = datetime.now(timezone_kst)

    format = '%Y-%m-%d %H:%M:%S'
    str_datetime = datetime.strftime(datetime_utc2, format)

    mycol.insert_one({"Order_Code": Order_Code, "UserName": UserName, "UserId": UserId,
                     "delivery_fee": Delivery_Fee, "Order_Data": Order_Data, "Cart": Cart, "Order_End": True, 'Del_End': False, "Memo": "음식 문앞에두고 꼭 전화한번 주세요!", "Rider": "", "Order_Time": str(str_datetime)})
    return Order_Code


def Insert_Err(Errors):
    timezone_kst = timezone(timedelta(hours=9))
    datetime_utc2 = datetime.now(timezone_kst)

    format = '%Y-%m-%d %H:%M:%S'
    str_datetime = datetime.strftime(datetime_utc2, format)

    errcol.insert_one({"Errors": Errors, "Time": str(str_datetime)})


def Edit_Data(Code, Ur):
    mycol.update_one({"Order_Code": str(Code)}, {
                     '$set': {'Addres_Url': str(Ur)}})


def Drop_Users():
    mycol.drop()


if __name__ == "__main__":
    # Insert_Data("Uad859360a7e2589c8c213b3b47fc27a2",'크턱',orderdata,cart)
    # Drop_Users()
    # z = randrange(0,900)
    # Order_Code = str(datetime.now().hour) + str(datetime.now().month) + str(datetime.now().year) + str(datetime.now().day) + str(int(datetime.now().microsecond / 1000)) + str(z)[-1]
    # print('Order_Code')
    x = mycol.find()
    for i in x:
        print(i)
    # Insert_Err("sdsdsdsdsds")
    # Edit_Data("1382022238380", "https://ibb.co/r22bKFs")
