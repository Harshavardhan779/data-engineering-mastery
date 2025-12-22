import os
import shutil

# Define the folder structure we want
FOLDERS = {
    "scripts": [".py", ".java", ".class"],
    "data": [".csv", ".json", ".db"],
    "notes": [".md", ".txt"]
}

def organize_workspace():
    print("🧹 Starting Workspace Cleanup...")
    
    # Get current directory
    current_dir = os.getcwd()
    
    for folder_name, extensions in FOLDERS.items():
        # Create folder if it doesn't exist
        target_path = os.path.join(current_dir, folder_name)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
            print(f"📁 Created folder: {folder_name}/")

        # Move files
        for file in os.listdir(current_dir):
            if any(file.endswith(ext) for ext in extensions) and file != "Day14_Organizer.py":
                source = os.path.join(current_dir, file)
                destination = os.path.join(target_path, file)
                
                # Only move if it's a file
                if os.path.isfile(source):
                    shutil.move(source, destination)
                    print(f"   -> Moved {file} to {folder_name}/")

    print("✅ Cleanup Complete! Your workspace is structured.")

if __name__ == "__main__":
    organize_workspace()