# import personnel
# print(personnel.data)
from personnel import data
# print(data)
# for info in data:
#     if "Comedy" in info['movie_gen']:
#         print (info["first_name"])


print("welcome to our list: ")


user_input = input("What do you want to check?: " )
result = 0
if user_input.lower() == "female": 
    # result = 0
    for info in data:
        if "F" in info["gender"]:
            result += 1
            print(info["first_name"])
            # print(f'There are {result} females')
    print(f'There are {result} females')

elif user_input.lower() == "comedy":
    for info in data:
        if "Comedy" in info["movie_gen"]:
            result += 1
            print(info["first_name"])
    print(f'There are {result} people who love comedy genre')


elif user_input.lower() == "email":
    put_name = int(input("put ID of the person you want to check: "))
    if put_name == 2:
        for info in data:
            if info["id"] == 2:
                print(f'{info["first_name"]} email is {info["email"]}')
    elif put_name == 1:
        for info in data:
            if info["id"] == 1:
                print(f'{info["first_name"]} email is {info["email"]}')    

elif user_input.lower() == "info":    
    input = int(input("put iD: "))
    if input == 1:
        for info in data:
            if info["id"] == 1:
                for keys, value in info.items():
                    print(keys + ' = ' + str(value))
    if input == 2:
        for info in data:
            if info["id"] == 2:
                for keys, value in info.items():
                    print(keys + ' = ' + str(value))
    if input == 3:
        for info in data:
            if info["id"] == 3:
                for keys, value in info.items():
                    print(keys + ' = ' + str(value))
