import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            time TEXT NOT NULL
)
"""
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    print("\n" + "*" * 70)
    for video in videos:

        print(f"\n{video[0]}. Title: {video[1]} - Duration: {video[2]}")

    print("\n" + "*" * 70)


def add_video(title, time):
    cursor.execute("INSERT INTO videos (title, time) VALUES (?, ?)", (title, time))
    print("\nVideo added successfully!")
    con.commit()


def update_video(video_id, title, time):
    cursor.execute(
        "UPDATE videos SET title = ?, time = ? WHERE id = ?", (title, time, video_id)
    )
    print("\nVideo updated successfully!")
    con.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    print("\nVideo deleted successfully!")
    con.commit()


def main():
    while True:
        print("\n Welcome to the YouTube Manager 2.0")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                title = input("Enter the title of the video: ")
                time = input("Enter the time of the video: ")
                add_video(title, time)
            case "3":
                list_videos()
                video_id = input("Enter the id of the video: ")
                title = input("Enter the title of the video: ")
                time = input("Enter the time of the video: ")
                update_video(video_id, title, time)
            case "4":
                list_videos()
                video_id = input("Enter the id of the video: ")
                delete_video(video_id)
            case "5":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice")

    con.close()


if __name__ == "__main__":
    main()
