import json 
from src.logger import log_info , log_err
def open_and_update_json(file_path, month):
    try:
        # Open the file and load its content
        with open(file_path, 'r') as file:
            data = json.load(file)

        data["month"].append(month)

        # Step 4: Write back the updated data to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        log_info("Data added successfully!")

    except Exception as e:
        log_err(f"An error occurred: {e}")

def load_month_data(file_path):
    data = None 
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data["Month"]