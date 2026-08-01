import requests
def fetch_random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    # print (type(response))
    data = response.json()
    # print(data)
    if data["success"] and "data" in data :
        user_data=data ["data"]
        user_name=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return user_name, country 
    else:
        raise Exception("Failed to fetch user data ")


def main():
    try :
        username,country=fetch_random_user() 
        print( f"userName: {username} , country: {country}")
    except Exception as e :
        print (str(e))





if __name__=="__main__":
    main()
