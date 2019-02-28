# # Список(Массивы)
# # Строки
# # Словари
# # Кортежи
# # Множества
#
#
#
# # m = [1,2,3,4]
# # n = m.copy()
# #
# # n[0] = 100
# #
# # print(m)
# # print(n)
# #
#
#
# #slice
#
# # m = [1,2,3,4,5,6,7,8,9,0,1]
# # print(m[::-1]) #reverse
#
# # print(m[4])
# # print(m[2:7])
# # print(m[2:])
# # print(m[:])
# # print(m[2:7:2])
#
# # print(m[-2])
#
#
# m = [1]*123
#
# print(m)
#
# print([5,6,7] + [1,2,3])


# s = "aliehfiuo34y2t78yo8surhgliuhrgilu"
#
#
# print(s[3])
# print(s[3:10])
# print(s[3:10:2])
# print(s[::-1])
#
#
# # s[4] = '3'
#
# print("dwadawd" + "awddaw" + "awawdwad")

# for i in s[5:10]:
#     print(i)

# s = "London is the capital of GB!"
#
# a = s.split(" ")
# print(a)
# print("***".join(a))


# num = input("Input number: ")
# s = 0
# for i in num:
#     s += int(i)
#
# print(s)


# print(len("awddawwda"))
# print(len([1,2,3,4,5]))
#
# a= 123
# b = 423
# c = 324
# d = 23
# import math
# print("a=" + str(a) + "; b=" + str(b) + "; c=" + str(c) + "; d=" + str(d))
# print(f"a={a**2}; b={b+a}; c={c}; d={math.sin(d)}")
#


# s = "Hello my name is Andrey! Buy, sell"
# # s = "Hello my name is Andrey!"
#
#
# if "buy" in s.lower():
#     print("Spam")
# else:
#     print("Not spam")
#
#
#
# m = [1,2,3,4]
#
#
# if 3 in m:
#     print("Yes")
# else:
#     print("No")
#

# кортеж
# tuple
# m = (1,2,3,4,5,6,7,8,9,0)
#
# for i in m:
#     print(i)
#
# print(m[2:])
# print(m[2])


# dict


#
# d = {
#     "Name": "Andrey",
#     "Surname": "Pak",
#     0:234,
#     23.3:23,
#     True:324,
#     None: {
#         "awd":243
#     },
#
#     (12,213,312): [234,56,7]
#
# }
#
#
# print(d[(12,213,312)])
#
# for k,v in d.items():
#     print(k,v)
#
# print(d.keys())
# print(d.values())


# if "Name" in d:
#
# text = "kw 34gowc m85c gmow4mh cgo 8xo85ygow478y gcogwyershgluieyhw378 o4t 8yesf uli ey r hlgi3y 4wo78g sy lie lie lie lie lie lie lie lie ylgie74ygur"
#
#
#
#
# stat = {}
#
# # stat["awaw"] = 234
#
# for i in text.split(" "):
#     if i not in stat:
#         stat[i] = 1
#     else:
#         stat[i] += 1
#
#
# for k,v in stat.items():
#     print(k,v)


# a = [] #list массив
# b = () #tuple кортеж
# c = dict() #dict set
# d = set() #dict set
# e = ''' awluidawiudl
#
#  awlduyawdkyg
#
#  awkydawd
#
#  awdyukadakwd
#
#  sfsefes
#  '''
#
#
# print(e)


# m = {1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2}
#
# print(m)
#
# m = [1,2,3,1,2,3,4,5,6,7,8,90,8,5]
#
# print(list(set(m)))


# a = {1, 2, 3, 4, 5}
#
# b = {4, 5, 6, 7, 8}
#
# c = {1, 2, 3, 6, 7, 8}
#
# print(a.difference(b).union(b.difference(a)))
# print(a & b)
# print(a | b)

# if and &&
#    or ||

# c = {4,7,8}
#
# print(a.difference(b))
#
# print(a.intersection(b).intersection(c))
#
# print(a.union(b))


# import requests
#
# r = requests.get("http://vk.com", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
#
# print(r.text)
#
#
# import bs4
#
#
# bs4.BeautifulSoup(r.text, "html.parser")
