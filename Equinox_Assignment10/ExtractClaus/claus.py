from dataloadingPackage.data_loading import *

data = data_loading_function()

def get_url_organization(index):
    print("url"+data[index]["remote_url"])
    print("organization"+data[index]["organization"])


