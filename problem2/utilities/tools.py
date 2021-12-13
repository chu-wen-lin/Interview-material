# TODO: define methods to MongoDB

from problem2.datapool import json_data
from typing import List, Dict, Union
from problem2.object.database import get_db
from collections import ChainMap


class DataProcess:
    def __init__(self):
        self.collection = get_db()

    def insert_posts(self, data: List[Dict[str, Union[str, int]]]) -> str:
        result = self.collection.insert_one(dict(data))
        return result

    def select_posts(self,
                     location: str,
                     landlord_gender: str,
                     landlord_identity: str,
                     renter_gender: str,
                     **kwargs) -> str:

        conditions = {k: v for k, v in kwargs.items() if v is not None}

        if location != "不限":
            conditions["location"] = location

        if landlord_gender == "限男性":
            conditions["landlord_gender"] = 1
        elif landlord_gender == "限女性":
            conditions["landlord_gender"] = 0

        if landlord_identity == "屋主":
            conditions["landlord_identity"] = landlord_identity
        elif landlord_identity == "非屋主":
            conditions["landlord_identity"] = {"$ne": "屋主"}

        if renter_gender == "男性可":
            conditions['renter_gender'] = {"$ne": 2}  # 非限女
        elif renter_gender == "女性可":
            conditions['renter_gender'] = {"$ne": 1}  # 非限男

        print(conditions)
        if conditions:
            results = self.collection.find(conditions)
            print(results.count())

        else:
            results = self.collection.find().sort("parse_time", -1).limit(10)

        for result in results:
            yield result


condition1 = {"location": "新北市", "renter_gender": {"$ne": 2}}

condition2 = {"contact_number": "0979032622"}

condition3 = {"landlord_identity": {"$ne": "屋主"}}

condition4 = {"location": "台北市",
              "landlord_gender": 0,
              "landlord_last_name": "吳"}


# process = DataProcess()
# # 1. insert posts
# for data in json_data:
#     process.insert_posts(data)

