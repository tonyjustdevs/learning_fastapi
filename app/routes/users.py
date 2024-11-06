from app.schemas.users import User1_cls, User2_cls, U3_Users_cls
from app.services.users import User_Service
from fastapi import APIRouter, HTTPException

import logging
# Unable to remove existing handlers from the logger

logging.getLogger().handlers = [] # #BUG Issue#64 temp fix remove persistent cached tony_cool_logs.txt from being used

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)-6s %(name)-20s %(asctime)s.%(msecs)03d \n\t\t\t %(message)s",
    datefmt="%Y-%m-%d-%H:%M:%S",
    filename="log.txt")
logger.setLevel(logging.DEBUG) # [diwec]: [debug->info->warning->error->critical]
# ie if logging.ERROR->only error+critical logged

# print(f"[print]-{cached_str}")
# cached_str = f"__cached__: [{__cached__}]" # temp visibility
# logger.info(f"[LOGGER]-{cached_str}")


consoleHandler = logging.StreamHandler()
# logger.addHandler(consoleHandler)
full_logger = logging.getLogger("") #Dont understand what this actually does.
full_logger.addHandler(consoleHandler)

def create_user_router():
    
    user_router     = APIRouter(prefix="/custom_router_prefix_user", tags=["custom_users_tag"])
    user_service    = User_Service()

    @user_router.get("/0",response_model=User1_cls)
    async def default_user_endpoint_fn():
        u1_instance = await user_service.get_u1_instance_fn()
        return u1_instance

    @user_router.get("/{userid}",response_model=User1_cls)
    async def userid_endpoint_fn(userid:int):
        try:
            u1_instance = await user_service.get_u1_instance_fn(userid)
            return u1_instance
        except KeyError as e:
            keyerror_msg_str = f"User does not exist! [{userid}]. Please Try Again!" 
            logger.error(keyerror_msg_str)
            raise HTTPException(status_code=404, detail={'msg':keyerror_msg_str,
                                                         'user':userid}
                                )
    @user_router.post("/",response_model=User2_cls) 
    async def post_u1_endpoint_fn(u1_postbodyrequest:User1_cls): #24
        new_userid = await user_service.create_new_update_u1_user_fn(u1_postbodyrequest) #25
        users = user_service.calc_nbr_of_urs()
        u2_instance = User2_cls(u2_userid_attr=new_userid,
                                u2_users_attr=users)
        return u2_instance #28

    @user_router.get("/",response_model=U3_Users_cls) #33
    def userid_endpoint_fn(start:int=0, limit:int=2): #34
        u1_users_list = user_service.get_u3_users_fn(start, limit)
        u3_instance = U3_Users_cls(u3_users_attr=u1_users_list)
        return u3_instance #36

    @user_router.put("/{userid}") 
    async def post_u1_endpoint_fn(u1_postbodyrequest:User1_cls,userid:int): #24
        await user_service.create_new_update_u1_user_fn(u1_postbodyrequest=u1_postbodyrequest  , userid=userid) #25

    @user_router.delete("/{userid}/delete") #15
    async def delete_u1_endpoint_fn(userid:int): 
        logger.info(f"[LOGGER]:[Entered Delete Route for {userid}]")
        try:
            await user_service.delete_u1_user_fn(userid=userid) 
        except KeyError:
            # print("TP-KeyError caught in try-except!")
            # raise HTTPException(status_code=404, detail=f"User [{userid}] does not exist!")
            logger.error(f"[LOGGER]:[User does not exist: [{userid}]]")
            raise HTTPException(status_code=404, detail= {"msg": "[HTTPException]User does not exist!",
                                                          "userid": userid})
            
    # @user_router.delete("/{userid}/delete-v2") #15
    # async def delete_u1v2_endpoint_fn(userid:int): 
        # print(f"Attemping to delete {userid}via instance_method")
        # await user_service.delete_u1v2_user_fn(userid=userid) 

    return user_router


user_router = create_user_router()

