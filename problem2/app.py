# TODO: build FastAPI service

import os
import uvicorn
from fastapi import FastAPI, Query
from object import schema
from typing import Optional, List
from problem2.utilities.tools import DataProcess
from starlette.concurrency import run_in_threadpool


tags_metadata = [
    {
        "name": "Description",
        "description": "Set up criteria to filter posts. If no criteria is specified, we'll return the last 10 posts parsed."

    }
]

app = FastAPI(
    title="MongoDB API",
    description="Fetching data in MongoDB by FastAPI",
    openapi_tags=tags_metadata
)


@app.get('/', tags=['home'])
async def home():
    return 'Ready to fetch data by MongoDB API!'


@app.get('/posts', tags=['selection'], response_model=List[schema.Post])
async def select_posts(location: str = Query("不限", enum=["不限", "台北市", "新北市"]),
                       landlord_last_name: Optional[str] = None,
                       landlord_gender: str = Query("不限", enum=["不限", "限男性", "限女性"]),
                       landlord_identity: str = Query("不限", enum=["不限", "屋主", "非屋主"]),
                       contact_number: Optional[str] = None,
                       current_status: Optional[str] = None,
                       house_type: Optional[str] = None,
                       renter_gender: str = Query("不限", enum=["不限", "男性可", "女性可"])):

    return await run_in_threadpool(DataProcess().select_posts,
                                   location=location,
                                   landlord_last_name=landlord_last_name,
                                   landlord_gender=landlord_gender,
                                   landlord_identity=landlord_identity,
                                   contact_number=contact_number,
                                   current_status=current_status,
                                   house_type=house_type,
                                   renter_gender=renter_gender)


if __name__ == "__main__":
    uvicorn.run("app:app", host=os.getenv("api_host"), port=int(os.getenv("api_port")), reload=True, debug=True)
