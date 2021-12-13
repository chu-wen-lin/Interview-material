from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    post_id: str
    location: Optional[str] = None
    landlord: Optional[str] = None
    landlord_last_name: Optional[str] = None
    landlord_gender: Optional[int] = None
    landlord_identity: Optional[str] = None
    contact_number: Optional[str] = None
    house_type: Optional[str] = None
    current_status: Optional[str] = None
    renter_gender: Optional[int] = None
    parse_time: Optional[datetime] = None
