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
pass
dict_carinfor_k5 = {
    "brand": "Kia",
    "model": "K5",
    "year": 2021,
    "color": "White",
    "price": 28000
    }

list_carinfor.append(dict_carinfor_k5)