################## Program Written by: Tony Phung (AU 2024) ##################
from tony_files.tony_helper_fns import print_start_info, print_end_info, logging
logger = logging.getLogger(__name__)

print_start_info(__file__)
##############################################################################
############################## START CODE HERE ###############################
##############################################################################


from fastapi import FastAPI, Request  
from app.routes.users import user_router
from exceptions import CustomException
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(user_router)

@app.exception_handler(CustomException)
def custom_exception_handler(req: Request, exc: CustomException):
  return JSONResponse(
    status_code=418,
    content={"message":f"Something happened! {exc}"} #exc.name needs inse.name attribute
  )


##############################################################################
############################## END CODE HERE #################################
##############################################################################
print_end_info(__file__)