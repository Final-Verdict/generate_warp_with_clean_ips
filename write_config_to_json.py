import json
import os
def write_json_config(data, filename):
  """Writes the provided data to a JSON file.

  Args:
    data: The data to be written, as a dictionary.
    filename: The name of the JSON file to create.
  """

  try:
    if not os.path.isfile(filename):
            with open(filename, "w") as f:
                json.dump({}, f)  # Create an empty JSON file if it doesn't exist
    with open(filename, "w") as f:
      json.dump(data, f, indent=4)  # Indent for readability
      f.write("\n")
    print(f"JSON config written to {filename}")
  except Exception as e:
    print(f"Error writing JSON file: {e}")

def append_diff_to_json(data, filename):
    """Appends the differences between the provided data and existing JSON data to a JSON file.
    Args:
        data: The data to be compared and appended, as a dictionary.
        filename: The name of the JSON file to append to.
    """
    try:
        if not os.path.isfile(filename):
            with open(filename, "w") as f:
                json.dump({}, f)  # Create an empty JSON file if it doesn't exist

        with open(filename, "r+") as f:
            existing_data = json.load(f)
            diff_data = {k: v for k, v in data.items() if k not in existing_data or v != existing_data[k]}
            existing_data.update(diff_data)
            f.seek(0)
            json.dump(existing_data, f, indent=4)
        print(f"Differences appended to {filename}")
    except Exception as e:
        print(f"Error appending differences to JSON file: {e}")