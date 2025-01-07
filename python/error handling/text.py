def list_all_videos(vide):
    pass

def add_video(video):
    pass

def update_video(vide):
    pass

def delete_vidoe(video):
    pass


def main():
    videos = []
    while True:
        print("\n Youtube manager | Choose an option")
        print("1. List the favourite video")
        print("2. Add a youtube video")
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input('Enter your choide')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_vidoe(videos)
            case '5':
                break
            case _:
                print('wrong input')


#! the double underscore called dunder >>>
if __name__ == '__main__':
    main()
