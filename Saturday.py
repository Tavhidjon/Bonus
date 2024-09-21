# mashqi1
# def Maxx_minn( maxx=-9999999999, minn=99999999999):
#     my_list=[10, 15, 20, 2, 10, 6],
#     for i in my_list:
#         if i > maxx:
#             maxx = i
#     for i in my_list:
#         if i < minn:
#             minn = i
#     print(maxx-minn) 
# Maxx_minn()

# mashqi2 

# from random import randint, sample
# my_list = []
# for i in range(0, 100):
#     n = randint(1000000000, 9999999999)
#     my_list.append(n)
# a = sample(my_list, 2)
# print(a[0], a[1])

# mashqi 3
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def pirimetr(self):
#         pass
# class Rectengel(Shape):
#     def __init__(self, n, k):
#         self.n=n
#         self.k=k
#     def area(self):
#         print(self.n*self.k)

#     def pirimetr(self):
#         print(2*(self.n+self.k))
# class square(Shape):
#     def __init__(self, n):
#         self.n=n
#     def area(self):
#         print(self.n*4)

#     def pirimetr(self):
#         print(2*(self.n*8))
# obj = (5,3)
# obj1 = square(2)
# obj.area()
# obj.pirimetr()  
# obj1.area()
# obj1.pirimetr()



# mashqi 4
# class Staff:
#     def __init__(self, role, depertament, salary):
#         self.role=role
#         self._depertament=depertament
#         self._salary=salary

# class Teacher(Staff):
#     def show(self):
#         print(self.role, self._depertament, self._salary)
# obj1 = Teacher("Teacher", "Glavniy", 2000)
# obj1.show()
# n = int(input())
# with open("file.txt", "r") as file:
#     lines = file.readlines()

# print(lines[n-1])

# mashqi 5
# n = input()
# my_list=n.split()
# licct1 = []
# f = ""
# d =""
# for i in my_list:
#     if len(i) >= 5:
#         k = 0
#         f=""
#         while k < len(i):
#             f+="#"
#             k+=1
#         licct1.append(f)
#     else:
#         licct1.append(i)
# nm=""
# d=" ".join(licct1)
# print(d)

# mashqi 6

# n = input()
# my_list = n.split()
# dictionary = {
#     "int": [],
#     "str": [],
#     "bool": []
# }


# mashqi 7

# for i in my_list:
#     try:
#         n = int(i)
#         dictionary["int"].append(n)
#     except ValueError:
#         if i == "True" or i == "False":
#             dictionary["bool"].append(i)
#         else:
#             dictionary["str"].append(i)

# print(dictionary)