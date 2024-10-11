################## Program Written by: Tony Phung (AU 2024) ##################
from tony_files.tony_helper_fns import print_start_info, print_end_info, logging
logger = logging.getLogger(__name__)

print_start_info(__file__)
##############################################################################
############################## START CODE HERE ###############################
##############################################################################

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from app.routes.users import user_router

app = FastAPI()
app.include_router(user_router)

def delete_u1_user_fn(userid: int):
    if userid in u1_dicts:
        del u1_dicts[userid]
        del u1a_dicts[userid]
        del u4_dicts[userid]
    return None

@app.delete("/user/{userid}") #15
def delete_u1_endpoint_fn(userid:int): 
    delete_u1_user_fn(userid=userid) 


##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  


# aTODO [#11 Build Simple Fast API App]  [#12/fastapi]
# aTODO [#14 Build PUT endpoint ("/user/{userid}")]  [#11/fastapi]


# aTODO [#15 Build DELETE endpoint ("/user/{userid}")]  [#11/fastapi]
# aTODO [#16 Refactor to Async Functions]  [#11/fastapi]
# aTODO [#17 Refactor App Directory Structure]  [#11/fastapi]
# aTODO [#18 Add API Routers]  [#11/fastapi]
# aTODO [#19 Add HTTP Exception]  [#11/fastapi]
# aTODO [#20 Add Exception Class]  [#11/fastapi]
# aTODO [#21 Add Logging]  [#11/fastapi]
# aTODO [#22 Add Custom Exception Handlers]  [#11/fastapi]
# aTODO [#23 Add Headers and Dependencies]  [#11/fastapi]



#zDONE [2] Build Root GET endpoint ("/") #2
#zDONE [3] Create U1 and U1a User classes (pydantic models) #3
#zDONE [4] Create U1 and U1a User sample data (userid=0) #4
#zDONE [5] Build Default User Get endpoint with ("/user/0", pydantic response model) #5
#zDONE [6] Build Path Parameter User Get endpoint ("/user/{userid}") #6
#zDONE [#24 1. Accepts post body request (u1 class) [#12]]  [#12/fastapi]
#zDONE [#25 2. create new user of U1 class [#12]]  [#12/fastapi]
#zDONE [#26 2a. creates new user id [#12]]  [#12/fastapi]
#zDONE [#27 2b. creates new user in sample dicts [#12]]  [#12/fastapi]
#zDONE [#28 3. return u2 class post response [#12]]  [#12/fastapi]
#zDONE [#29 bug fix]
#zDONE [#12 Create U2 POST Response class (pydantic model)]  [#11/fastapi]
#zDONE [#13 Build Query Parameters GET endpoint ({start},{limit},"/user/{userid}")]  [#11/fastapi]
#zDONE [#33 create new query_parameters endpoint u3_endpt [13]]  [#13/fastapi]
#zDONE [#34 create start and limit parameters  [13]]  [#13/fastapi]
#zDONE [#35 create new u3 class - list of u1 [13]]  [#13/fastapi]
#zDONE [#36 create u3_endpt return u3_class [13]]  [#13/fastapi]
#zDONE [#41 update function [create_new_u1_user_fn] to optionally input [userid] (#14)]  [#14/fastapi]
#zDONE [#42 create user: if user not exist [userid] (#14)]  [#14/fastapi]
#zDONE [#43 update user: if user exists (dicts) (#14)]  [#14/fastapi]
#zDONE [#44 update PUT endpoint (#14)]  [#14/fastapi]