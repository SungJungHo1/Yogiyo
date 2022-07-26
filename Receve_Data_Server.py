from flask import Flask, jsonify, make_response, flash, request, redirect, render_template, url_for
from Get_yogiyo import *
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/getStores')
def getStores():
    category = request.args.get("category", "1인분주문")
    latitude = request.args.get("latitude", "37.5347556106622")
    longitude = request.args.get("longitude", "127.114906298514")

    data = get_Yogiyo(category, latitude, longitude)
    result = json.dumps(data, ensure_ascii=False)
    # res = make_response(result)
    return result


@app.route('/getMenus')
def getMenus():
    id = request.args.get("id", "468686")
    data = get_Menu(id)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/getReviews')
def getReviews():
    id = request.args.get("id", "468686")
    data = get_Review(id)
    result = json.dumps(data, ensure_ascii=False)
    return result


@app.route('/Search')
def Searchs():

    Search = request.args.get("Search", "피자")
    page = request.args.get("page", "0")
    lat = request.args.get("latitude", "37.5347556106622")
    lng = request.args.get("longitude", "127.114906298514")
    data = Search_Category(Search, page, lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result

@app.route('/Find_Top')
def Find_Top():

    lat = request.args.get("latitude", "36.969655961906")
    lng = request.args.get("longitude", "127.244958777736")
    data = Find_Top(lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result

if __name__ == '__main__':

    app.run(host="0.0.0.0", debug=True, port=80)
