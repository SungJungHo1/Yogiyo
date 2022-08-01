from flask import Flask, request
from Get_yogiyo import *
from flask_cors import CORS
import json
import ssl

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwXqtznqQcUI7ISyqGHfwkCg9Vky1bPxqOSZWruwJl+Q3NwYn
MCwPlMRJ81Y+A2ms9Yssg2SrxOWVm4zzhZlrg5Sq8ElyqtB99ODXl/Q5v1YGlyr4
0y7+LkBgHzDvX15w8Jy6pwZhhp9VLgHHDK97ST2RR9vnIgrgGP4m35Ax8R53xlVm
vO9tDHffxr/THHTZ/FsCqlX2n05rkU+aL57GSNocBTzWH3eEIH4y1vFdjzUzc0Da
oF8zbDIbDOUp5YYHH/x2cVMcRZjMZI+WpHYhzfjOaZ5Skkk1Co/eBZKUE/tUXkN4
87QaxMBPwnCJIeArWHhdNJmWcsqad95IcHg/GwIDAQABAoIBADA5cr7nX79LIc/Y
ASGOK6DS1s7+2a2rkJJkEvEQlieM05Jcb0IbiVqsPj5vvY8+NMUTBmpNml6+Vrbp
v/0Jy3mFgcHYnMMkqnBx5mrSjd46A/SD2ndQ3DwNAahkmxVrRb1DY2akOYTDjAim
msV3q8QKm36MuiSLD2ZLWscYeso9PedVjlfdk/KAZb7ZAtQPrS/6SLLV5FwYDOig
sQrD7FwT2XkTgsVTlXs+FfHi/thHkoSTjGDkPbFtxfhiJRDrkwfqs5gVZFuvM4Rk
fYQcGd3ajFWXznZFWfYT6vnHV7mGbGL6ZsOm7TPqUmayEH+JUo2bsd/XCHiny6WD
pEi+HPECgYEA40YqYcHG4XY5R1tYtQQPoGW8zdtOddUZXX4D5utoZqxkVfLobAKI
aDGmZH9dXsBRICER74/oiDtiUbsa4JLgbjHsEDpU+nJIj6nYTrHtR+1TrXGMDh0s
929mq9N4JRVgjqDKBg17LyI4UZv/LituaWmWQ56XzIq9BwL4XoFrWwMCgYEA2e8G
Dfhatr74Za+USfmztK4+aMJTaiDpzHJWEIXItyd7YCiZh6QxP1alArPG0swYRBbt
SP6eh161D0K2SDWIvwlGTXDigulW3P8LkNfyBn78s0ODdudsgiHo2LbOwwt8CpCP
6SCGy9bR7X2ePIzBjqvp1ZPMd9Z3Cv8uomrCBAkCgYEA4IN++KU5d56XhOM7JU7G
tRfrxJxBzOtfrFkBN8wTjWH9mF5mtdRmti9eBWdAcIqhWZDxq+tItdOcE8s3CORv
asxMO9ez/NiKz8jkExF3qpdLE0rZJVQzCJf3IAS+ajvM7/jsub/1kaFHa28kTZK/
9shElbYElR31EAkiHBHTYMsCgYB6/4gvQkgQc9/FpD7RMXjXNLBMd8CUWVca6Dzi
vl713/al4sQj5etVkBU5XTWNq1rWswng9LOMO0t8/W3beztedmGTO27b6832lIt2
iCo0uF7u3d/Ir/xxxamhBivTsRuk6soODSmGygtZOligW+CyIRysSepQiF5Peo5b
ZF1z4QKBgQDcpzF/3NOA6iN3o85/uodM5r7O2CqabFb160g7ra3SoS0ySK2Bf9xx
TKKSpBCVQ8NkgieZZnM0MBumzCZc/futkd0vKQAdrd9hwKXMTGFnx1GAAY7Tg7hz
G1dJEuEzMaeuhfOBF2JFqyKIA/1TSufXwkeHE7wEITeUdFu2S/RkGw==
-----END RSA PRIVATE KEY-----"""

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


@app.route('/search')
def Searchs():

    Search = request.args.get("keyword", "피자")
    page = request.args.get("page", "0")
    lat = request.args.get("latitude", "37.5347556106622")
    lng = request.args.get("longitude", "127.114906298514")
    data = Search_Category(Search, page, lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result

@app.route('/popularMenu')
def popularMenu():

    lat = request.args.get("latitude", "36.969655961906")
    lng = request.args.get("longitude", "127.244958777736")
    data = Find_Top(lat, lng)
    result = json.dumps(data, ensure_ascii=False)
    return result

@app.route('/translate')
def translate():
    from_lan = request.args.get("from", "ko")
    to = request.args.get("to", "th")
    text = request.args.get("text", "태국어 번역 테스트")
    data = Google_translate(from_lan,to,text)
    result = json.dumps(data, ensure_ascii=False)
    return result

if __name__ == '__main__':

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='certificate.pem', keyfile='private.key')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)
    # app.run(host="0.0.0.0", debug=True, port=80)