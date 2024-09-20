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
    u1_login_attr: int
    u1_country_attr: Optional[str] = None

# Service
def get_u1_instance(userid: int=0)->User1_cls:
    u1_dicts = {
        0:{
            'u1_login_attr':0,
            'u1_country_attr':'Australia',
          }
    }
    
    u1a_dicts = {
        0:{
            'u1a_score_attr':100,
            'u1a_weapons_attr': ['pike','ninja sword','wand']
          }
    }    
    
    return None

# Routes
@app.get("/")
def root_fn():
    return "G'day mate 🦘🦘🦘!"

@app.get("/user/0",response_model=User1_cls)
def root_fn():
    u1_instance = get_u1_instance()
    return u1_instance


##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  


# DONE [2] Build Root GET endpoint ("/") #2
# DONE [3] Create U1 and U1a User classes (pydantic models) #3
# DONE [4] Create U1 and U1a User sample data (userid=0) #4
# TODO [5] Build Default User Get endpoint with ("/user/0", pydantic response model) #5
# TODO [6] Build Path Parameter User Get endpoint ("/user/{userid}") #6