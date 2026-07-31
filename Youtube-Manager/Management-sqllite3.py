import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor=conn.cursor()
cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT OT NULL,
                time TEXT NOT NULL
                )
''')






global input_file
input_file = "youtube.txt"



def load_data():
    rows = cursor.execute( "SELECT *FROM videos") # cursor holds the result of query
    if not rows :
        print ("NO DATA TO SHOW ")
    else :
        for row in cursor.fetchall():
            print(row )





def list_all_videos(videos):
    rows = cursor.execute( "SELECT *FROM videos") # cursor holds the result of query
    if not rows :
        print ("NO DATA TO SHOW ")
    else :
        for row in cursor.fetchall():
            print(row )


def add_video(name, time):
        cursor.execute(
            "INSERT INTO videos (name , time ) VALUES (?,?) ",(name,time)
        )
        conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute(
        "UPDATE videos SET name =?, time=? WHERE id=? ", (new_name,new_time,video_id)

)
    conn.commit()


def delete_video(video_id ):
    cursor.execute(
    "DELETE FROM videos WHERE id =? ",(video_id, ) # only tuple is acceptable thats why we added one extra comma ti make it tuple 
    )
    conn.commit()

             



def main ():
    videos=load_data()

    while True:
        print ("\n YOUTUBE MANAGER | Choose and Option ")
        print ("1. List Youtube video ")
        print ("2. Add a Youtube video ")
        print ("3. Update a Youtube video ")
        print ("4. Delete a Youtube video ")
        print ("5. Exit the App ")
        choice=input("Enetr your Choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
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
     
    conn.close()


if __name__=="__main__":
    main()
