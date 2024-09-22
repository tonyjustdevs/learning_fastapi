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
class User1a_cls(BaseModel): # [3]
    u1a_score_attr: Optional[int] = None
    u1a_weapons_attr: Optional[List[str]] = None
class User1_cls(User1a_cls):
    u1_login_attr: str
    u1_country_attr: Optional[str] = None
class User2_cls(BaseModel): #12
    u2_userid_attr: int
    u2_users_attr: int
    
# DB
u1_dicts = {
    0:{
        'u1_login_attr':"default user",
        'u1_country_attr':'Australia',
        }
}

u1a_dicts = {
    0:{
        'u1a_score_attr':100,
        'u1a_weapons_attr': ['pike','ninja sword','wand']
        }
}    

# Service
def calc_nbr_of_urs()->int:
    return len(u1_dicts)

def get_u1_instance_fn(userid: int=0)->User1_cls:
    user_u1_dict = u1_dicts[userid]     #29
    user_u1a_dict = u1a_dicts[userid]   #29
    user_u1u1a_dict = {**user_u1_dict,**user_u1a_dict} #unpack dictionary in a function allocated arguments to fields
    print(user_u1u1a_dict)
    u1_instance = User1_cls(**user_u1u1a_dict)
    return u1_instance

def create_new_u1_user_fn(u1_postbodyrequest:User1_cls)-> User2_cls:
    # get user info
    u1_country_attr     = u1_postbodyrequest.u1_country_attr
    u1_login_attr       = u1_postbodyrequest.u1_login_attr
    u1a_score_attr      = u1_postbodyrequest.u1a_score_attr  
    u1a_weapons_attr    = u1_postbodyrequest.u1a_weapons_attr

    # create new userid
    new_userid = len(u1_dicts) #26
    
    # create new user u1 (from postbodyreq) #27
    u1_dicts[new_userid] =  {
            'u1_login_attr':u1_login_attr,
            'u1_country_attr':u1_country_attr,
    }
    u1a_dicts[new_userid] = {
            'u1a_score_attr':u1a_score_attr,
            'u1a_weapons_attr': u1a_weapons_attr
    }
    
    return new_userid # return new_userid

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
    new_userid = create_new_u1_user_fn(u1_postbodyrequest) #25
    users = calc_nbr_of_urs()
    u2_instance = User2_cls(u2_userid_attr=new_userid,
                            u2_users_attr=users)
    return u2_instance #28


##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  


#TODO [#11 Build Simple Fast API App]  [#12/fastapi]
#TODO [#13 Build Query Parameters GET endpoint ({start},{limit},"/user/{userid}")]  [#11/fastapi]
#TODO [#14 Build PUT endpoint ("/user/{userid}")]  [#11/fastapi]
#TODO [#15 Build DELETE endpoint ("/user/{userid}")]  [#11/fastapi]
#TODO [#16 Refactor to Async Functions]  [#11/fastapi]
#TODO [#17 Refactor App Directory Structure]  [#11/fastapi]
#TODO [#18 Add API Routers]  [#11/fastapi]
#TODO [#19 Add HTTP Exception]  [#11/fastapi]
#TODO [#20 Add Exception Class]  [#11/fastapi]
#TODO [#21 Add Logging]  [#11/fastapi]
#TODO [#22 Add Custom Exception Handlers]  [#11/fastapi]
#TODO [#23 Add Headers and Dependencies]  [#11/fastapi]



# DZONE [2] Build Root GET endpoint ("/") #2
# DZONE [3] Create U1 and U1a User classes (pydantic models) #3
# DZONE [4] Create U1 and U1a User sample data (userid=0) #4
# DZONE [5] Build Default User Get endpoint with ("/user/0", pydantic response model) #5
# DZONE [6] Build Path Parameter User Get endpoint ("/user/{userid}") #6
# zDONE [#12 Create U2 POST Response class (pydantic model)]  [#11/fastapi]
    #zDONE [#24 1. Accepts post body request (u1 class) [#12]]  [#12/fastapi]
    #zDONE [#25 2. create new user of U1 class [#12]]  [#12/fastapi]
    #zDONE [#26 2a. creates new user id [#12]]  [#12/fastapi]
    #zDONE [#27 2b. creates new user in sample dicts [#12]]  [#12/fastapi]
    #zDONE [#28 3. return u2 class post response [#12]]  [#12/fastapi]
    #zDONE [#29 bug fix]