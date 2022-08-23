from flask import Flask, request
from Get_yogiyo import *
from flask_cors import CORS
import json
import ssl

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
    OrderData = json.loads(request.form['OrderData'])
    cart = json.loads(request.form['cart'])
    code = Push_Message(userId, userName, delivery_fee, OrderData, cart)

    return code


@app.route('/AddData', methods=['GET'])
def AddData():
    Code = request.args.get("Code", "66")

    return Code


@app.route('/getIMG', methods=['POST'])
def getIMG():

    # userId = request.args.get("userId", "66")
    # fileName = request.args.get("fileName", "66")
    userId = request.form['userIds']
    fileName = request.form['fileNames']

    IMG_Test(userId, fileName)

    return "Yes"


if __name__ == '__main__':

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(
        certfile='certificate.pem', keyfile='private.key')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)
