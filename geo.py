import requests


def get_Add(lat, lng):
    # 좌표 (경도, 위도)
    coords = f"{lat},{lng}"
    output = "json"
    orders = 'roadaddr'
    endpoint = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
    url = f"{endpoint}?coords={coords}&output={output}&orders={orders}"

    # 헤더
    headers = {
        "X-NCP-APIGW-API-KEY-ID": '16u37tq6w1',
        "X-NCP-APIGW-API-KEY": 'eYHr7Q6EQb0X8e8UZyED0SIqfq6CbEFeBb8dXEgL',
    }

    # 요청
    res = requests.get(url, headers=headers)
    data = res.json()
    # addrres = data['results'][0]
    # print(addrres['land'])
    # print(addrres)
    print(data)
    return data


if __name__ == "__main__":
    get_Add(127.244327, 36.9646706)
