data1 = {
    "id": 1,
    "name": "hong kildong",
    "email": "hong@mail.com",
    "hp_num": "010-2343-9870"}
data2 = {
    "id": 2,
    "name": "lee soonsin",
    "email": "lee@mail.com",
    "hp_num": "010-3333-5555"}
data3 = {
    "id": 3,
    "name": "jang youngsil",
    "email": "jang@mail.com",
    "hp_num": "010-7777-1234"}
data4 = {
    "id": 4,
    "name": "king sejong",
    "email": "king@mail.com",
    "hp_num": "010-4567-0987"}

data = [data1, data2, data3, data4]

for d in data:
    for k, v in d.items():
        print("Key: ", k)
        print("Value: ", v)