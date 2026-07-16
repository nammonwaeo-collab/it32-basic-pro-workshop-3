shop = int(input("ระบุจำนวนร้าน : "))
bank = 0

for i in range(shop):
    money = float(input("ระบุจำนวณเงิน :"))
    bank += money
print(bank)