import os
import instaloader
from colorama import Fore, Style

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
    print(Fore.RED + "  _____               _            _   ")
    print(" |  __ \             | |          | |  ")
    print(" | |__) |___  ___  __| |_   _  ___| |_ ")
    print(" |  _  // _ \/ _ \/ _` | | | |/ __| __|")
    print(" | | \ \  __/  __/ (_| | |_| | (__| |_ ")
    print(" |_|  \_\___|\___|\__,_|\__,_|\___|\__|")
    print(Style.RESET_ALL)  # Reset color
    
    print("This tool is written by @ERROR1099\n")

    while True:
        username = input("Enter Instagram username (or 'exit' to quit): ")
        if username.lower() == 'exit':
            break
        get_profile_info(username)
