import os
import instaloader
from colorama import Fore, Style

def download_posts(username):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Retrieve profile metadata
        profile = instaloader.Profile.from_username(L.context, username)

        # Create folder with profile name if not exists
        profile_folder = os.path.join("profile_data", profile.username)
        os.makedirs(profile_folder, exist_ok=True)

        # Initialize a counter for downloaded posts
        downloaded_count = 0

        # Iterate over the profile's posts and download them
        for post in profile.get_posts():
            L.download_post(post, target=profile_folder)
            downloaded_count += 1

            # Display post details
            print(Fore.RED + "\nPost Details:")
            print(Fore.YELLOW + f"Caption: {post.caption}")
            print(f"Likes: {post.likes}")
            print(f"Comments: {post.comments}")
            print(Style.RESET_ALL)  # Reset color

            # Leave a space between post details and filenames
            print()

        # Display success message with the number of posts downloaded
        print(Fore.GREEN + "\nPosts downloaded successfully.")
        print(f"Total posts downloaded: {downloaded_count}")
        print(Style.RESET_ALL)  # Reset color

    except Exception as e:
        print(Fore.RED + "\nAn error occurred:", e)
        print(Style.RESET_ALL)  # Reset color

def get_profile_info(username):
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        profile_url = f"https://www.instagram.com/{username}/"
        profile_pic_url = profile.profile_pic_url
        profile_data = (
            f"Username: {profile.username}\n"
            f"Full Name: {profile.full_name}\n"
            f"Bio: {profile.biography}\n"
            f"Posts Count: {profile.mediacount}\n"
            f"Followers Count: {profile.followers}\n"
            f"Following Count: {profile.followees}\n"
            f"External URL: {profile.external_url}\n"
            f"Profile URL: {profile_url}\n"
            f"Profile Picture URL: {profile_pic_url}\n"
            f"Is Private: {'Yes' if profile.is_private else 'No'}\n"
            f"Is Verified: {'Yes' if profile.is_verified else 'No'}\n"
        )

        # Display profile information with colors on terminal
        print(Fore.RED + "Profile Information:")
        print(Fore.YELLOW + profile_data)
        print(Style.RESET_ALL)  # Reset color

        save_info = input("Do you want to save this profile information? (yes/no): ").lower() == 'yes'
        if save_info:
            # Create folder if not exists
            os.makedirs("profile_data", exist_ok=True)

            # Write data to a text file with UTF-8 encoding
            file_path = os.path.join("profile_data", f"{username}_profile.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(profile_data)
                print(Fore.GREEN + f"Profile information saved to {file_path}")
                print(Style.RESET_ALL)  # Reset color
    except instaloader.exceptions.ProfileNotExistsException:
        print(Fore.RED + "Profile not found.")
        print(Style.RESET_ALL)  # Reset color

if __name__ == "__main__":
    # Print banner
    print(Fore.RED + "  _____               _            _   ")
    print(" |  __ \             | |          | |  ")
    print(" | |__) |___  ___  __| |_   _  ___| |_ ")
    print(" |  _  // _ \/ _ \/ _` | | | |/ __| __|")
    print(" | | \ \  __/  __/ (_| | |_| | (__| |_ ")
    print(" |_|  \_\___|\___|\__,_|\__,_|\___|\__|")
    print(Style.RESET_ALL)  # Reset color

    while True:
        print(Fore.YELLOW + "1. Download Instagram Posts")
        print("2. Get Instagram Profile Information")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter Instagram username to download posts: ")
            download_posts(username)
        elif choice == '2':
            username = input("Enter Instagram username to get profile information: ")
            get_profile_info(username)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
             print("Invalid choice. Please enter a valid option (1/2/3).")
