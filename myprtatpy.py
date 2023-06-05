x = "1234567890"

print(len(x)) #字串長度
print(pow(2,10)) #2的10次方
print(int(x)) #強制轉型 int 整數類
print(float(x))#強制轉型 float 浮點數類
print(str(x)) #強制轉換 str 字串類

name = 'Loli'

print(name.upper()) #強制轉換 大寫
print(name.lower()) #強制轉換 小寫

name.upper()
print('name:'+name) #python of the methods(模組) doesn't change the value

name2=name.upper()

print('name2:'+name2)
print(name.isupper())
print(name.islower())

print(name.lower().islower()) #method chaining 模組串連

print(name.lower().replace('l','h'))

sentence = 'AN apple a day keep the doctor away'
print(sentence.split(" ")) #根據空格切割字串
print(sentence.split("a")) #根據a(a不算入)切割字串

print(list(sentence)) #將字串轉乘陣列

print("{},{},{}".format("100","杯","鐵觀音拿鐵"))

countnum = 10

print(f"現在掉落 {countnum} 個沙漏")

layer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(layer[10:])


