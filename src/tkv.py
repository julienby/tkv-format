import datetime
import pandas as pd

def is_valid_timestamp(timestamp_str):
    """Check if a timestamp string is in ISO 8601 format."""
    try:
        return datetime.datetime.fromisoformat(timestamp_str)
    except ValueError:
        return None


def parse_sensor_data(sensor_data):
    """Parse sensor data in the format 'sensor:value'."""
    try:
        key, value = sensor_data.split(":")
        # Try to convert value to float
        try:
            value = float(value)
        except ValueError:
            pass  # Keep as string if conversion fails
        return key, value
    except ValueError:
        return None, None


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

    def process_line(line):
        """Process a single line and return a dictionary or None if invalid."""
        parts = line.strip().split(" ; ")

        # Ensure the line has at least a timestamp and one sensor:value pair
        if len(parts) < 2:
            return None

        # Validate timestamp
        timestamp_str = parts[0]
        timestamp = is_valid_timestamp(timestamp_str)
        if not timestamp:
            return None

        # Initialize a dictionary for this line with the timestamp
        entry = {"timestamp": timestamp}

        # Parse sensor data
        if not parse_sensor_entries(parts[1:], entry):
            return None

        return entry

    def parse_sensor_entries(sensor_parts, entry):
        """Parse multiple sensor data entries and update the entry dictionary."""
        for sensor_data in sensor_parts:
            key, value = parse_sensor_data(sensor_data)
            if key is None or value is None:
                return False  # Invalid sensor data
            entry[key] = value
        return True

    with open(file_path, 'r') as file:
        for line in file:
            entry = process_line(line)
            if entry:
                data.append(entry)  # Append only valid entries

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
