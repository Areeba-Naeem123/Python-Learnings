import json

global input_file
input_file = "youtube.txt"



def load_data():
    try:
        with open (input_file) as file :
           test=json.load(file) # this line loads the file data and convert it into json
        #    print(test)
           return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(input_file,'w') as file :
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print ("*"*20)
    for index, video in enumerate(videos,start=1):
        print (f"{index}. {video['name']}, Duration :{video['time']} ") 
    print("\n")
    print ("*"*20)

def add_video(videos):
    name=input("Enter Videos Name:")
    time=input("Enter Videos Time:")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
def update_video(videos):
    list_all_videos(videos)
    index = int (input ("Enter the video number you want to update")
)
    if 1<=index<=len(videos):
        name=input("Enter the new video name:")
        time=input("Enter the new vudeo duration:")
        videos[index-1]={'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print ("INvalid video number ")
     

def delete_video(videos):
    list_all_videos(videos)
    index = int (input ("Enter the video number you want to delete")
    )
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos) 
    else:
        print ("INvalid video number ")
             



def main ():
    videos=load_data()

    while True:
        print ("\n YOUTUBE MANAGER | Choose and Option ")
        print ("1. List Youtube video ")
        print ("2. Add a Youtube video ")
        print ("3. Update a Youtube video ")
        print ("4. Delete a Youtube video ")
        print ("5. Exit the App")
        choice=input("Enetr your Choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print ("invalid choice")
        # print (videos)


if __name__=="__main__":
    main()
