import sqlite3 as db

conn = db.connect('youtube_videos.db')


cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')

def list_videos():
    cursor.execute('select * from videos')
    
    for row in cursor.fetchall():
        print(row)
        if (row == ''):
            print('No Data Found !!!!1')
            break



def add_video(name,time):
    cursor.execute('insert into videos (name,time) values (?,?)',(name,time))
    conn.commit()


def update_video(vid,new_name,new_time):
    cursor.execute('update videos set name = ?, time = ? where id = ?  ',(new_name,new_time,vid))
    conn.commit()



def delete_video(vid):
    cursor.execute('delete from videos where id=?',(vid,))
    conn.commit()

def main():
    while True:
        print('\n Youtube manager app with DB')
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Videos')
        print('4. Delete Videos')
        print('5. Exit app')
        choice = input('Enter your choice : ')

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('enter the video name : ')
            time = input('enter the video time : ')
            add_video(name, time)
        elif choice == '3':
            vid = input('Enter video ID :')
            name = input('Enter the video name : ')
            time = input('Enter the Video time : ')
            update_video(vid,name,time)
        elif choice == '4':
            vid = input('Enter the video ID : ')
            delete_video(vid)
        elif choice == '5' : 
            break
        else : 
            print('Invalid Choice ')
    conn.close()






if __name__ == '__main__':
    main()
