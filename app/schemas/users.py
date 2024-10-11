from typing import Optional, List
from pydantic import BaseModel
# Schemas
class U4_UsersId_cls(BaseModel): #35
    u4_userid: int
class User1a_cls(BaseModel): # [3]
    u1a_score_attr: Optional[int] = None
    u1a_weapons_attr: Optional[List[str]] = None
class User1_cls(User1a_cls, U4_UsersId_cls):
    u1_login_attr: str
    u1_country_attr: Optional[str] = None
class User2_cls(BaseModel): #12
    u2_userid_attr: int
    u2_users_attr: int
class U3_Users_cls(BaseModel): #35
    u3_users_attr: List[User1_cls]