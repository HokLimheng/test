from multiprocessing.sharedctypes import Value


pablo_info = {
    "firstname": "pablo",
    "lastname": "escobar",
    "email": "pablo_mx@gmail.com"
}

# pablo_info_str = ', '.join(pablo_info)
# print(pablo_info_str)


for keys, value in pablo_info.items():
    print(keys + ' = ' + value)


# pablo_name = pablo_info["firstname"]
# print(pablo_name)


#### dictionary in list form #####

# user_info = [
#     {
#         "firstname": "joe",
#         "lastname": "chea",
#         "email": "s.chea@aupp.edu.kh"
#     },
#     {
#         "firstname": "raksmey",
#         "lastname": "chea",
#         "email": "cheasingh@gmail.com"
#     }
# ]

# for info in user_info:
#     print(info["firstname"])


# loop in dictionary form
# for info in pablo_info.values():
#     print(info)

# loop in dictionary to get both key and value
# for keys, values in pablo_info.items():
#     print(keys, values)
