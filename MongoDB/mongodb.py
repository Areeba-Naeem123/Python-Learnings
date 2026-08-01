from  pymongo import MongoClient
from bson import ObjectId 

# not a good practice to add password and username in link 
client= MongoClient("mongodb+srv://youtubepy:Areeba069@cluster0.yvtfftv.mongodb.net/")

db = client["ytmanager"]
video_collection=db["videos"]
print(video_collection)



def add_video(name,time):
        video_collection.insert_one({"name":name,"time":time}) 
def update_video(videoid,name,time):
        video_collection.update_one(
                {'_id':ObjectId(videoid)},# what to find
                {'$set': {"name":name,"time":time}})
def delete_video(videoid):
        video_collection.delete_one({"_id":ObjectId(videoid)})

def list_videos():
        for video in video_collection.find():
                print(f"ID:{video['_id']}, Name: {video['name']}, Duration : {video['time']}")

        

def main (): 
    while True:
        print ("\n YOUTUBE MANAGER | Choose and Option ")
        print ("1. List Youtube video ")
        print ("2. Add a Youtube video ")
        print ("3. Update a Youtube video ")
        print ("4. Delete a Youtube video ")
        print ("5. Exit the App ")
        choice=input("Enter your Choice: ")
        match choice:
            case "1":
                        list_videos()
            case "2":
                        name=input("Enter the name of the video you want to add: ")
                        time=input("Enter the duration of the video: ")
                        add_video(name,time)
            case "3":
                        id= input("Enter the ID of the video you want to update: ")
                        name=input("Enter the name of the video you want to update: ")
                        time=input("Enter the duration of the video: ")
                        update_video(id,name,time)
            case "4":
                        id= input("Enter the id  of the video you want to Delete : ")
                        
                        delete_video(id)
            case "5":
                        break
            case _:
                        print ("invalid choice")
                # print (videos)




if __name__=="__main__":
    main()
