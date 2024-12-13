import datetime
import pandas as pd


def read_tkv(file_path):
    """
    Reads a TKV file and returns a list of dictionaries.

    Parameters:
    - file_path (str): Path to the TKV file.

    Returns:
    - list of dict: List where each dictionary represents a line in the TKV file with
      the timestamp and sensor data.
    """
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            # Remove any extra whitespace and split the line by " ; "
            parts = line.strip().split(" ; ")

            # First part is the timestamp
            timestamp_str = parts[0]
            try:
                timestamp = datetime.datetime.fromisoformat(timestamp_str)
            except ValueError:
                raise ValueError(f"Invalid timestamp format: {timestamp_str}")

            # Initialize a dictionary for this line with the timestamp
            entry = {"timestamp": timestamp}

            # Parse each sensor:value pair
            for sensor_data in parts[1:]:
                # Split each sensor data into key and value
                try:
                    key, value = sensor_data.split(":")

                    # Try to convert the value to float, if possible
                    try:
                        # Try converting to float if the value looks like a number
                        value = float(value)
                    except ValueError:
                        # If it's not a number, leave the value as a string
                        pass

                    # Add the key and value to the entry dictionary
                    entry[key] = value

                except ValueError:
                    raise ValueError(f"Invalid sensor data format: {sensor_data}")

            # Append the entry dictionary to the data list
            data.append(entry)

    return data

def tkv_to_df(data):
    """
    Converts the list of dictionaries from read_tkv into a pandas DataFrame.

    Parameters:
    - data (list of dict): List of dictionaries where each dictionary represents
      a line in the TKV file with timestamp and sensor data.

    Returns:
    - pd.DataFrame: A pandas DataFrame with timestamp as a datetime index and each sensor as a column.
    """
    # Create DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Set the timestamp column as the DataFrame index
    df.set_index("timestamp", inplace=True)

    return df


def write_tkv(file_path, data):
    """
    Writes a list of dictionaries to a TKV file.

    Parameters:
    - file_path (str): Path to the output TKV file.
    - data (list of dict): List where each dictionary represents a line in the TKV file
      with 'timestamp' as a key and other key-value pairs for each sensor.
    """
    with open(file_path, 'w') as file:
        for entry in data:
            # Extract the timestamp and ensure it is a string in ISO format
            timestamp = entry.get("timestamp")
            if isinstance(timestamp, (str, datetime.datetime)):
                timestamp = timestamp.isoformat() if isinstance(timestamp, datetime.datetime) else timestamp
            else:
                raise ValueError("Each entry must contain a valid 'timestamp' in ISO format.")

            # Build the sensor data as "key:value" pairs
            sensor_data = " ; ".join(f"{key}:{value}" for key, value in entry.items() if key != "timestamp")

            # Write the line in TKV format
            file.write(f"{timestamp} ; {sensor_data}\n")
