# list 안 dict 구성

# key : value(여러 변수 종류 가능)
dict_carinfor_mustang = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "price": 30000
}

dict_carinfor_sonata = {
    "brand": "Hyundai",
    "model": "Sonata",
    "year": 2020,
    "color": "Black",
    "price": 30000
}

list_carinfor = [dict_carinfor_mustang, dict_carinfor_sonata]

list_carinfor = [
    {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "price": 30000,
    },
    {
        "brand": "Hyundai",
        "model": "Sonata",
        "year": 2020,
        "color": "Black",
        "price": 30000
    }
        ]

dict_carinfor_k5 = {
    "brand": "Kia",
    "model": "K5",
    "year": 2021,
    "color": "White",
    "price": 28000
    }

list_carinfor.append(dict_carinfor_k5)

# list_carinfor안에 있는 index 0번에 있는 "model" : "Mustang" 접근 방법
# dict_carinfor_index_first = list_carinfor[0]
# dict_carinfor_index_first['model']
# pass
# list_carinfor[0]['model']
# pass

# for로 각 dict 정보 출력
for dict_carinfor in list_carinfor:
    brand = dict_carinfor['brand']
    model = dict_carinfor['model']
    print('브랜드 : {}, 모델 : {}'.format(brand, model))
    pass