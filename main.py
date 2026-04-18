def eng_yaqin_50(narx):
    return round(narx / 50) * 50

narxlar = [10, 23, 45, 67, 89, 101, 123, 145]
yangi_narxlar = [eng_yaqin_50(narx) for narx in narxlar]
print(yangi_narxlar)
