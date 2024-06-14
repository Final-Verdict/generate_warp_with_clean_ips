import csv

def get_and_remove_first_ip_port(csv_file_path):
    ip_port = None

    try:
        with open(csv_file_path, "r") as file:
            rows = list(csv.reader(file))
            if len(rows) > 1:
                ip_port_row = rows[1]
                ip_port = ip_port_row[0]  # Extract IP:Port from the first row

                # Remove the first row from the CSV file
                with open(csv_file_path, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows[2:])
            else:
                print("CSV file contains less than 2 rows. No row removed.")
    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")

    return ip_port