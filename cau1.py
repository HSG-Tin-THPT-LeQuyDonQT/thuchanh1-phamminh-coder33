tong = 0
n = int(input("Nhập số n: "))
tong = tong + n % 10
n = n // 10
tong = tong + n % 10
n = n // 10
tong = tong + n % 10
n = n // 10
tong = tong + n % 10
n = n // 10
print("Tổng là ",tong)
