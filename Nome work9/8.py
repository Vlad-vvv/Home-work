result = []
def divider(a, b):

   try:

       return a / b

   except ZeroDivisionError:
       print("Помилка!")
       return 0

   except TypeError:
       print("Помилка!")
       return 0

   except ValueError:
       print("Помилка!")
       return 0

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}



for key in data:
   res = divider(key, data[key])
   result.append(res)

print(result)

