from flask import Flask, request
from Get_yogiyo import *
from flask_cors import CORS
import json
import ssl
from DBMaker import *
from geo import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/getStores', methods=['GET'])
def getStores():
    category = request.args.get("category", "1인분주문")
    latitude = request.args.get("latitude", "37.5347556106622")
    longitude = request.args.get("longitude", "127.114906298514")

    data = get_Yogiyo(category, latitude, longitude)
    result = json.dumps(data, ensure_ascii=False)
    # res = make_response(result)
    return result


@app.route('/getMenus', methods=['GET'])
def getMenus():
    id = request.args.get("id", "468686")
    data = get_Menu(id)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/getReviews', methods=['GET'])
def getReviews():
    id = request.args.get("id", "1048427")
    count = request.args.get("count", "1000")
    page = request.args.get("page", "1")
    data = get_Review(id, count, page)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/getItemReviews', methods=['GET'])
def getR():
    id = request.args.get("id", "1048427")
    count = request.args.get("count", "1000")
    page = request.args.get("page", "1")
    menu_id = request.args.get("menu_id", "314259651")
    data = getItemReviews(id, page, count, menu_id)
    result = json.dumps(data, ensure_ascii=False)

    return result


@app.route('/search', methods=['GET'])
def Searchs():

    Search = request.args.get("keyword", "피자")
    page = request.args.get("page", "0")
    lat = request.args.get("latitude", "37.5347556106622")
    lng = request.args.get("longitude", "127.114906298514")
    data = Search_Category(Search, page, lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/popularMenu', methods=['GET'])
def popularMenu():

    lat = request.args.get("latitude", "36.969655961906")
    lng = request.args.get("longitude", "127.244958777736")
    data = Find_Top(lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/profile', methods=['GET'])
def Profile():
    Id = request.args.get("id", "66")
    data = Find_User_Profile(Id)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/pushOrder', methods=['POST'])
def pushOrder():
    userId = request.args.get("userId", "66")
    userName = request.args.get("userName", "66")
    delivery_fee = request.args.get("delivery_fee", "66")
    Service_Money = request.args.get("Service_Money", "66")
    ImageIn = request.args.get("ImageIn", "66")
    lan = json.loads(request.form['lan'])
    lng = json.loads(request.form['lng'])
    OrderData = json.loads(request.form['OrderData'])
    cart = json.loads(request.form['cart'])
    IMG_URL = ""
    if ImageIn == "yes":

        image = request.files['image']

        IMG_URL = Upload_IMG(image.read())
    datas, Order_Code = Push_Message(userId, userName, delivery_fee,
                                     OrderData, cart, lan, lng, Service_Money)
    if ImageIn == "yes":
        Edit_Data(Order_Code, IMG_URL)

    return datas


@app.route('/service')
def Get_service():
    data = find_service()

    return str(data)


@app.route('/AddData', methods=['GET'])
def AddData():
    UserId = request.args.get("UserId", "66")
    Ad_Urls = request.args.get("Ad_Urls", "66")
    Edit_Data(UserId, Ad_Urls)
    return "yes"


@app.route('/getIMG', methods=['POST'])
def getIMG():

    # userId = request.args.get("userId", "66")
    # fileName = request.args.get("fileName", "66")
    userId = request.form['userIds']
    fileName = request.form['fileNames']

    IMG_Test(userId, fileName)

    return "Yes"


@app.route('/LogErr', methods=['POST'])
def LogErr():

    Errors = request.form['Errors']

    Insert_Err(Errors)

    return "Yes"


@app.route('/getAddres', methods=['GET'])
def getAddres():

    lat = request.args.get("lat", "66")
    lng = request.args.get("lng", "66")

    data = get_Add(lat, lng)
    result = json.dumps(data, ensure_ascii=False)

    return result


@app.route('/find_User_Data', methods=['GET'])
def find_User_Data():
    User_ID = request.args.get("User_ID", "66")
    User_Data = find_cust(User_ID)
    if User_Data != None:
        result = json.dumps(int(User_Data["Point"]), ensure_ascii=False)
    else:
        result = json.dumps(0, ensure_ascii=False)
    return result


if __name__ == '__main__':

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(
        certfile='certificate.pem', keyfile='private.key')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)
