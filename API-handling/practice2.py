import requests

def fetch_data():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data :
        jokes= data["data"]["data"]
        for joke in jokes :
            print (f'id: {joke["id"]}')
            print (f'category: {joke["categories"]}')
            print (f'content: {joke["content"]}')
    else:
         raise Exception ("API RESPONSE FAILED!! ")

    return jokes



def main ():
    fetch_data()

if __name__=="__main__":
    main()

    

