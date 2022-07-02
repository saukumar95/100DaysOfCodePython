# with open('weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
# data = pd.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dic = data.to_dict()
# # print(data_dic)
# # temp_list = data["temp"].max()
# # print(temp_list)
#
# temp_in_c = int(data[data.day == "Monday"].temp)
#
# temp_in_f = (1.8 * temp_in_c) + 32
#
# print(f"{temp_in_f} F")
#
#
# # create a data frames using pandas
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

sq_data = pd.read_csv("Squirrel_Data.csv")
# print(sq_data["Primary Fur Color"].groupby(sq_data["Primary Fur Color"]).count().to_csv("squirrel_count.csv"))
squirrel_colors = ["Gray", "Cinnamon", "Black"]
gray_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": squirrel_colors,
    "count": [gray_count, cinnamon_count, black_count]
}

data = pd.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")




