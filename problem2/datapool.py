import json
from typing import List, Dict, Union
import datetime
import random

json_data = [{
    "post_id": "11845808",
    "location": "台北市",
    "landlord": "陳先生",
    "landlord_last_name": "陳",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0918304667",
    "house_type": "電梯大樓",
    "current_status": "獨立套房",
    "renter_gender": 0
},
{
    "post_id": "11845803",
    "location": "台北市",
    "landlord": "吳小姐",
    "landlord_last_name": "吳",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0933550262",
    "house_type": "電梯大樓",
    "current_status": "分租套房",
    "renter_gender": 0
},

{
    "post_id": "11845801",
    "location": "台北市",
    "landlord": "楊先生",
    "landlord_last_name": "楊",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0920666920",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 2
},

{
    "post_id": "11845786",
    "location": "台北市",
    "landlord": "歐先生",
    "landlord_last_name": "歐",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0925363226",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 2
},

{
    "post_id": "11845766",
    "location": "台北市",
    "landlord": "林太太",
    "landlord_last_name": "林",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0986346678",
    "house_type": "公寓",
    "current_status": "分租套房",
    "renter_gender": 0
},

{
    "post_id": "11845760",
    "location": "台北市",
    "landlord": "黃先生",
    "landlord_last_name": "黃",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0908999869",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845710",
    "location": "台北市",
    "landlord": "黃先生",
    "landlord_last_name": "黃",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0908999869",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11844991",
    "location": "台北市",
    "landlord": "值班人員",
    "landlord_last_name": "值",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0910001127",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845775",
    "location": "台北市",
    "landlord": "吳小姐",
    "landlord_last_name": "吳",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0921352986",
    "house_type": "電梯大樓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11845794",
    "location": "台北市",
    "landlord": "專案人員",
    "landlord_last_name": "專",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0910001127",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845679",
    "location": "台北市",
    "landlord": "戴先生",
    "landlord_last_name": "戴",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0933799553",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845668",
    "location": "台北市",
    "landlord": "李先生",
    "landlord_last_name": "李",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0928015328",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845700",
    "location": "台北市",
    "landlord": "許先生",
    "landlord_last_name": "許",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0987069889",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845684",
    "location": "台北市",
    "landlord": "吳小姐",
    "landlord_last_name": "吳",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0952102411",
    "house_type": "電梯大樓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11845677",
    "location": "台北市",
    "landlord": "戴先生",
    "landlord_last_name": "戴",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0933799553",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845824",
    "location": "台北市",
    "landlord": "許小姐",
    "landlord_last_name": "許",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0955875557",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845823",
    "location": "台北市",
    "landlord": "邱先生",
    "landlord_last_name": "邱",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0989374692",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845503",
    "location": "台北市",
    "landlord": "高先生",
    "landlord_last_name": "高",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0975656200",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845500",
    "location": "台北市",
    "landlord": "陳小姐",
    "landlord_last_name": "陳",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0981960184",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845494",
    "location": "台北市",
    "landlord": "郭小姐",
    "landlord_last_name": "郭",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0938521796",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 2
},

{
    "post_id": "11845469",
    "location": "台北市",
    "landlord": "許先生",
    "landlord_last_name": "許",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0932205621",
    "house_type": "公寓",
    "current_status": "分租套房",
    "renter_gender": 0
},

{
    "post_id": "11845478",
    "location": "台北市",
    "landlord": "陳先生",
    "landlord_last_name": "陳",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0933992468",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11845473",
    "location": "台北市",
    "landlord": "袁先生",
    "landlord_last_name": "袁",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0916768066",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 2
},

{
    "post_id": "11845422",
    "location": "台北市",
    "landlord": "唐媽媽",
    "landlord_last_name": "唐",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0905359891",
    "house_type": "公寓",
    "current_status": "雅房",
    "renter_gender": 2
},

{
    "post_id": "11845464",
    "location": "台北市",
    "landlord": "劉小姐",
    "landlord_last_name": "劉",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0937027562",
    "house_type": "公寓",
    "current_status": "分租套房",
    "renter_gender": 2
},

{
    "post_id": "11849601",
    "location": "新北市",
    "landlord": "吳媽媽",
    "landlord_last_name": "吳",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0912242680",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 2
},

{
    "post_id": "11834415",
    "location": "新北市",
    "landlord": "盧小姐",
    "landlord_last_name": "盧",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0932109160",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849579",
    "location": "新北市",
    "landlord": "顏先生",
    "landlord_last_name": "顏",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0939722338",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849572",
    "location": "新北市",
    "landlord": "家家",
    "landlord_last_name": "家",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0952538115",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849567",
    "location": "新北市",
    "landlord": "陳先生",
    "landlord_last_name": "陳",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0933736486",
    "house_type": "車位",
    "current_status": "平面式",
    "renter_gender": 0
},

{
    "post_id": "11849568",
    "location": "新北市",
    "landlord": "謝先生",
    "landlord_last_name": "謝",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0911206626",
    "house_type": "公寓",
    "current_status": "分租套房",
    "renter_gender": 0
},

{
    "post_id": "11849563",
    "location": "新北市",
    "landlord": "黎先生",
    "landlord_last_name": "黎",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0911206669",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849548",
    "location": "新北市",
    "landlord": "潘先生",
    "landlord_last_name": "潘",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0926889471",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849557",
    "location": "新北市",
    "landlord": "巫先生",
    "landlord_last_name": "巫",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0922118060",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849552",
    "location": "新北市",
    "landlord": "陳先生",
    "landlord_last_name": "陳",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0984499664",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849546",
    "location": "新北市",
    "landlord": "謝先生",
    "landlord_last_name": "謝",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0967370811",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849521",
    "location": "新北市",
    "landlord": "莊先生",
    "landlord_last_name": "莊",
    "landlord_gender": 1,
    "landlord_identity": "屋主",
    "contact_number": "0919377679",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849516",
    "location": "新北市",
    "landlord": "簡小姐",
    "landlord_last_name": "簡",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0958093809",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11849514",
    "location": "新北市",
    "landlord": "葉媽媽",
    "landlord_last_name": "葉",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0983233933",
    "house_type": "電梯大樓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11849504",
    "location": "新北市",
    "landlord": "楊小姐",
    "landlord_last_name": "楊",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0986851077",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849502",
    "location": "新北市",
    "landlord": "游小姐",
    "landlord_last_name": "游",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0937916580",
    "house_type": "透天厝",
    "current_status": "其他",
    "renter_gender": 0
},

{
    "post_id": "11849486",
    "location": "新北市",
    "landlord": "徐小姐",
    "landlord_last_name": "徐",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0922521508",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11849480",
    "location": "新北市",
    "landlord": "張小姐",
    "landlord_last_name": "張",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0933874066",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849330",
    "location": "新北市",
    "landlord": "林小姐",
    "landlord_last_name": "林",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0986851077",
    "house_type": "電梯大樓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11849469",
    "location": "新北市",
    "landlord": "林先生",
    "landlord_last_name": "林",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0936030211",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849457",
    "location": "新北市",
    "landlord": "蔡太太",
    "landlord_last_name": "蔡",
    "landlord_gender": 0,
    "landlord_identity": "屋主",
    "contact_number": "0986851077",
    "house_type": "公寓",
    "current_status": "雅房",
    "renter_gender": 0
},

{
    "post_id": "11849452",
    "location": "新北市",
    "landlord": "楊小姐",
    "landlord_last_name": "楊",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0960316901",
    "house_type": "電梯大樓",
    "current_status": "整層住家",
    "renter_gender": 0
},

{
    "post_id": "11849446",
    "location": "新北市",
    "landlord": "呂小姐",
    "landlord_last_name": "呂",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0958717529",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 0
},

{
    "post_id": "11849443",
    "location": "新北市",
    "landlord": "柯先生",
    "landlord_last_name": "柯",
    "landlord_gender": 1,
    "landlord_identity": "仲介",
    "contact_number": "0955026127",
    "house_type": "公寓",
    "current_status": "整層住家",
    "renter_gender": 0
},
{
    "post_id": "11849443",
    "location": "新北市",
    "landlord": "吳太太",
    "landlord_last_name": "吳",
    "landlord_gender": 0,
    "landlord_identity": "仲介",
    "contact_number": "0979032622",
    "house_type": "公寓",
    "current_status": "獨立套房",
    "renter_gender": 0
}]

for data in json_data:
    data['parse_time'] = datetime.datetime.now() + datetime.timedelta(seconds=random.randint(0,50))


# 0: 女性, 1: 男性
# 0: 男女性皆可; 1: 限男性: 2: 限女性

