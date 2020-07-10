from gids import builder
from selenium import webdriver


config = {
    'driver_path': './chromedriver',
    'headless': True,
    'window-size': '720x480',
    'disable_gpu': False
}

first_item = {
    'keyword': 'Lion',
    'limit': 10,  # The number of images
    'download_context': './data',
    'path': 'animal'  # save in ./data/animal/img_01...10
}

second_item = {
    'keyword': 'Bamboo',
    'limit': 10,  # The number of images
    'download_context': './data',
    'path': 'plant'  # save in ./data/plant/img_01...10
}

items = [first_item, second_item]

downloader = builder.build(config)

downloader.download(items)
