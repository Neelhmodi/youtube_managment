import sqlite3

connection = sqlite3.connect('youtube_videos.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def List_videos():
    
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def Add_videos(name , time):
    
    cursor.execute("INSERT INTO videos (name , time) VALUES(? , ?)",(name , time))
    connection.commit()

def Update_videos(video_id , name , time):
    
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(video_id , name , time))
    connection.commit()

def Delete_videos(video_id):
    
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    connection.commit()

def main():
    while True:
    
        print("\nYoutube manager with database : ")
        print("(1) List videos")
        print("(2) Add videos")
        print("(3) Update videos")
        print("(4) Delete videos")
        print("(5) Exite videos")

        choice = input("Enter Your Choice : ")

        match choice:

            case '1':

                List_videos()

            case '2':

                name = input("Enter the video name : ")
                time = input("Enter the video time : ")
                Add_videos(name , time)

            case '3':

                video_id = input("Enter the video id to update : ")
                name = input("Enter the video name : ")
                time = input("Enter the video time : ")
                Update_videos(video_id , name , time)

            case '4':

                video_id = input("Enter the video id to delete : ")
                Delete_videos(video_id)

            case '5':

                break

            case _:

                print("Invalid Choice ")

    connection.close()

if __name__ == "__main__":
    main()