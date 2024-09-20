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
class User1a_cls(BaseModel): # resolve #3
    u1a_score_attr: Optional[int] = None
    u1a_weapons_attr: Optional[List[str]] = None
class User1_cls(User1a_cls):
    u1_login_attr: int
    u1_country_attr: Optional[str] = None


# Routes
@app.get("/")
def root_fn():
    return "G'day mate 🦘🦘🦘!"




##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  


# DONE [2] Build Root GET endpoint ("/") #2
# DONE  [3] Create U1 and U1a User classes (pydantic models) #3
# TODO [4] Create U1 and U1a User sample data (userid=0) #4
# TODO [5] Build Default User Get endpoint with ("/user/0", pydantic response model) #5
# TODO [6] Build Path Parameter User Get endpoint ("/user/{userid}") #6