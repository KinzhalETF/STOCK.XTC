import os
import sys
import win32com.client

def create_website_shortcut(url, shortcut_name):
    # Ensure that the URL starts with "http://" or "https://"
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        # Create a shortcut object
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(os.path.join(os.path.expanduser("~\\Desktop"), f"{shortcut_name}.lnk"))

        # Set the properties of the shortcut
        shortcut.TargetPath = url
        shortcut.Save()

        print(f"Shortcut to '{url}' created on the desktop as '{shortcut_name}.lnk'")
    except Exception as e:
        print(f"Error creating shortcut: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_shortcut.py <URL> <ShortcutName>")
        sys.exit(1)

    url = sys.argv[1]
    shortcut_name = sys.argv[2]

    create_website_shortcut(url, shortcut_name)
