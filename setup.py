import os

# Base directory for the structured data folders
base_directory = "Bareilly_LLM/data/Structured_Data"

# Function to create a .json file in each folder
def create_json_files(base_dir):
    try:
        # Iterate over all subdirectories in the base directory
        for folder_name in os.listdir(base_dir):
            folder_path = os.path.join(base_dir, folder_name)
            # Check if it's a directory
            if os.path.isdir(folder_path):
                # Define the JSON file name
                json_file_path = os.path.join(folder_path, f"{folder_name}.json")
                # Create the JSON file if it doesn't exist
                if not os.path.exists(json_file_path):
                    with open(json_file_path, 'w') as json_file:
                        json_file.write("{}")  # Initialize the file with an empty JSON object
                    print(f"Created JSON file: {json_file_path}")
                else:
                    print(f"JSON file already exists: {json_file_path}")
    except Exception as e:
        print(f"Error while creating JSON files: {e}")

# Call the function
create_json_files(base_directory)
