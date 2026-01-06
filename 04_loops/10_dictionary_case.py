users = [
    {"id": 1, "total": 1200, "coupon": "P20"},
    {"id": 2, "total": 850, "coupon": "F10"},
    {"id": 3, "total": 1500, "coupon": "P50"}
]

discounts = {
    "P20" : (0.2,0),
    "P50" : (0.5,0),
    "F10" : (0,50)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent +fixed

    print(f"{user["id"]} paid {user["total"]} and got discount of {discount}")