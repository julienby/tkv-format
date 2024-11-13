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
