# first line: 1
@mem.cache
#load data
def get_data():
    data = load_svmlight_file("australian_scale.txt")
    return data[0], data[1]
