# import webbrowser
import pandas

# webbrowser.open('https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/'
#                 'about_data')

data = pandas.read_csv('squirrel_data.csv')
print(data, '\n', '-' * 175)
data_gray_count = len(data[data['Primary Fur Color'] == 'Gray'])  # 2473
data_cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])  # 392
data_black_count = len(data[data['Primary Fur Color'] == 'Black'])  # 103

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [data_gray_count, data_cinnamon_count, data_black_count]
}

pandas.DataFrame(data_dict).to_csv('squirrel_count')
