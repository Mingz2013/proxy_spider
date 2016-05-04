# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import pymongo
import datetime
import time
import threading

from settings import MONGO_URI, MONGO_DATABASE

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_DATABASE]


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items.find()

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsValidDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_valid.find()

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_valid.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_valid.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsJdDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_jd.find()

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_jd.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_jd.remove({"ip": item['ip'], "port": item['port']})