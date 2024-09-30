################## Program Written by: Tony Phung (AU 2024) ##################
from tony_files.tony_helper_fns import print_start_info, print_end_info, logging
logger = logging.getLogger(__name__)

print_start_info(__file__)
##############################################################################
############################## START CODE HERE ###############################
##############################################################################

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
app = FastAPI()

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
    
# DB
u1_dicts = {
    0:{
        'u1_login_attr':"default human",
        'u1_country_attr':'Earth'
        }
}

u1a_dicts = {
    0:{
        'u1a_score_attr':100,
        'u1a_weapons_attr': ['pike','ninja sword','wand']
        }
}    

u4_dicts = {
    0:{
    'u4_userid': 0
    }       
}

# Service
def calc_nbr_of_urs()->int:
    return len(u1_dicts)

def get_u1_instance_fn(userid: int=0)->User1_cls:
    user_u1_dict = u1_dicts[userid]     #29
    user_u1a_dict = u1a_dicts[userid]   #29
    user_u4_dict = u4_dicts[userid]   #39
    user_u1u1au4_dict = {**user_u1_dict,**user_u1a_dict,**user_u4_dict} #unpack dictionary in a function allocated arguments to fields
    print(user_u1u1au4_dict)
    u1_instance = User1_cls(**user_u1u1au4_dict)
    return u1_instance

def create_new_update_u1_user_fn(u1_postbodyrequest:User1_cls,
                                 userid: int=None)-> User2_cls: #41
    
    if not userid in u1_dicts: #42 
        userid = len(u1_dicts) #26 # create new userid
    
    u1_country_attr     = u1_postbodyrequest.u1_country_attr
    u1_login_attr       = u1_postbodyrequest.u1_login_attr
    u1a_score_attr      = u1_postbodyrequest.u1a_score_attr  
    u1a_weapons_attr    = u1_postbodyrequest.u1a_weapons_attr

    # create new user #27 or update #42 
    u1_dicts[userid] =  {
            'u1_login_attr':u1_login_attr,
            'u1_country_attr':u1_country_attr
    }
    u1a_dicts[userid] = {
            'u1a_score_attr':u1a_score_attr,
            'u1a_weapons_attr': u1a_weapons_attr
    }
    u4_dicts[userid] = {
            'u4_userid':userid
    }
    
    return userid # return new_userid

def get_u3_users_fn(start: int, limit: int)->U3_Users_cls: #13
    u1_users_list = []
    n_users = len(u1_dicts) # 1
    for userid in range(n_users):  # [0,1,2]
        if userid<start: 
            continue
        else:
            u1_instance = get_u1_instance_fn(userid)
            u1_users_list.append(u1_instance)
            if len(u1_users_list)==limit:
                break
    return u1_users_list

# Routes
@app.get("/")
def root_endpoint_fn():
    return "G'day mate 🦘🦘🦘!"

@app.get("/user/0",response_model=User1_cls)
def default_user_endpoint_fn():
    u1_instance = get_u1_instance_fn()
    return u1_instance

@app.get("/user/{userid}",response_model=User1_cls)
def userid_endpoint_fn(userid:int):
    u1_instance = get_u1_instance_fn(userid)
    return u1_instance

@app.post("/user",response_model=User2_cls) 
def post_u1_endpoint_fn(u1_postbodyrequest:User1_cls): #24
    new_userid = create_new_update_u1_user_fn(u1_postbodyrequest) #25
    users = calc_nbr_of_urs()
    u2_instance = User2_cls(u2_userid_attr=new_userid,
                            u2_users_attr=users)
    return u2_instance #28

@app.get("/user/",response_model=U3_Users_cls) #33
def userid_endpoint_fn(start:int=0, limit:int=2): #34
    u1_users_list = get_u3_users_fn(start, limit)
    u3_instance = U3_Users_cls(u3_users_attr=u1_users_list)
    return u3_instance #36

##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  

#DONE [#13 Build Query Parameters GET endpoint ({start},{limit},"/user/{userid}")]  [#11/fastapi]
#DONE [#33 create new query_parameters endpoint u3_endpt [13]]  [#13/fastapi]
#DONE [#34 create start and limit parameters  [13]]  [#13/fastapi]
#DONE [#35 create new u3 class - list of u1 [13]]  [#13/fastapi]
#DONE [#36 create u3_endpt return u3_class [13]]  [#13/fastapi]

# aTODO [#11 Build Simple Fast API App]  [#12/fastapi]
# aTODO [#14 Build PUT endpoint ("/user/{userid}")]  [#11/fastapi]
        #TODO [#41 update function [create_new_u1_user_fn] to optionally input [userid] (#14)]  [#14/fastapi]
        #TODO [#42 create user: if user not exist [userid] (#14)]  [#14/fastapi]
        #TODO [#43 update user: if user exists (dicts) (#14)]  [#14/fastapi]
        #TODO [#44 update PUT endpoint (#14)]  [#14/fastapi]


# aTODO [#15 Build DELETE endpoint ("/user/{userid}")]  [#11/fastapi]
# aTODO [#16 Refactor to Async Functions]  [#11/fastapi]
# aTODO [#17 Refactor App Directory Structure]  [#11/fastapi]
# aTODO [#18 Add API Routers]  [#11/fastapi]
# aTODO [#19 Add HTTP Exception]  [#11/fastapi]
# aTODO [#20 Add Exception Class]  [#11/fastapi]
# aTODO [#21 Add Logging]  [#11/fastapi]
# aTODO [#22 Add Custom Exception Handlers]  [#11/fastapi]
# aTODO [#23 Add Headers and Dependencies]  [#11/fastapi]



# DZONE [2] Build Root GET endpoint ("/") #2
# DZONE [3] Create U1 and U1a User classes (pydantic models) #3
# DZONE [4] Create U1 and U1a User sample data (userid=0) #4
# DZONE [5] Build Default User Get endpoint with ("/user/0", pydantic response model) #5
# DZONE [6] Build Path Parameter User Get endpoint ("/user/{userid}") #6
#zDONE [#24 1. Accepts post body request (u1 class) [#12]]  [#12/fastapi]
#zDONE [#25 2. create new user of U1 class [#12]]  [#12/fastapi]
#zDONE [#26 2a. creates new user id [#12]]  [#12/fastapi]
#zDONE [#27 2b. creates new user in sample dicts [#12]]  [#12/fastapi]
#zDONE [#28 3. return u2 class post response [#12]]  [#12/fastapi]
#zDONE [#29 bug fix]
# zDONE [#12 Create U2 POST Response class (pydantic model)]  [#11/fastapi]