from app.schemas.users import User1_cls, User2_cls, U3_Users_cls

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
class User_Service:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    async def calc_nbr_of_users()->int:
        return len(u1_dicts)

    @staticmethod
    async def get_u1_instance_fn(userid: int=0)->User1_cls:
        if userid not in u1_dicts:
            raise CustomException
        user_u1_dict = u1_dicts[userid]     #29
        user_u1a_dict = u1a_dicts[userid]   #29
        user_u4_dict = u4_dicts[userid]   #39
        user_u1u1au4_dict = {**user_u1_dict,**user_u1a_dict,**user_u4_dict} #unpack dictionary in a function allocated arguments to fields
        # print(user_u1u1au4_dict)
        u1_instance = User1_cls(**user_u1u1au4_dict)
        return u1_instance

    @staticmethod
    async def create_new_update_u1_user_fn(u1_postbodyrequest:User1_cls,
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

    def get_u3_users_fn(self, start: int, limit: int)->U3_Users_cls: #13
        u1_users_list = []
        n_users = len(u1_dicts) # 1
        for userid in range(n_users):  # [0,1,2]
            if userid<start: 
                continue
            else:
                u1_instance = self.get_u1_instance_fn(userid)
                u1_users_list.append(u1_instance)
                if len(u1_users_list)==limit:
                    break
        return u1_users_list

    @staticmethod
    async def delete_u1_user_fn(userid: int):
        print(f"[Inside UserService.delete_fn]: [{userid}]")
        if userid not in u1_dicts:
            raise CustomException
        # print(f"__file__: [{__file__}]")
        # print(f"__ca  ched__: [{__cached__}]")
        del u1_dicts[userid]
        del u1a_dicts[userid]
        del u4_dicts[userid]
        return None

    # async def delete_u1v2_user_fn(self, userid: int):
    #     print(f".......inside delete_u1_fn with argument userid: {userid}")
    #     if userid in u1_dicts:
    #         del u1_dicts[userid]
    #         print(f"Successfully deleted {userid} from u1_dicts")
    #         del u1a_dicts[userid]
    #         print(f"Successfully deleted {userid} from u1a_dicts")
    #         del u4_dicts[userid]
    #         print(f"Successfully deleted {userid} from u4_dicts")
    #     return None