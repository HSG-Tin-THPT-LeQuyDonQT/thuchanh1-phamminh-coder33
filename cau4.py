cannang = float(input(" cân nặng là "))
chieucao = float(input(" chiều cao là "))
BMI = cannang / (chieucao ** 2)
print("BMI của bạn là ",BMI)
if BMI < 18.5:
 print("Gầy")
if 18.5 <= BMI < 25:
 print("Bình Thường")
if BMI > 25:
 print("Thừa cân")
