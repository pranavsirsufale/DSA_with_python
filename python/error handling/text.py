import json 


def list_all_videos(videos):
    print('\n')
    print('*'*70)
    for index,video in enumerate(videos,start=1):
        print(f"{index} and  is {video['name']} ,    Duration : {video['time']}")
    print('\n')
    print('*'*70)

def add_video(videos):
    name = input('Etner video name : ')
    time = input('Enter vide time : ')
    videos.append({
        'name':name,
        'time':time,
    })
    save_data_helper(videos)

def update_video(vide):
    pass

def delete_vidoe(videos):
    list_all_videos(videos)
    index = int(input('enter the video number to be deleted'))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else :
        print('invalid video index')

def load_data():
    try:
        with open('youtuve.txt','r') as file:
            test = json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        print('an empty file is returned')
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def main():
    videos = load_data()
    while True:
        print("\n Youtube manager | Choose an option")
        print("1. List the favourite video")
        print("2. Add a youtube video")
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input('Enter your choide : ')

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