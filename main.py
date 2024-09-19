################## Program Written by: Tony Phung (AU 2024) ##################
from tony_files.tony_helper_fns import print_start_info, print_end_info, logging
logger = logging.getLogger(__name__)

print_start_info(__file__)
##############################################################################
############################## START CODE HERE ###############################
##############################################################################

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_fn():
    return "G'day mate 🦘🦘🦘!"




##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)  
