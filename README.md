# TKV Time Key Value -> tkv-format

## Description

**TKV Time Key Value** is a simplified data format for storing time-series sensor data with associated values. Each line represents a timestamped record with timezone information, followed by `key:value` pairs for each sensor. This format is easy to read, compact, and suited for applications that require structured and timestamped sensor records.

## Data Format

Each record consists of a timestamp with timezone information, followed by `key:value` pairs for each sensor. The general format is as follows:

```
timestamp ; sensor1:value1 ; sensor2:value2 ; ...
```

The recommended timestamp format follows the **ISO 8601** standard, including the timezone, as shown:

```
YYYY-MM-DDTHH:MM:SS±HH:MM
```

### Example

```
2024-11-12T14:32:45+01:00;temperature:22.5;humidity:45.0;pressure:1013
```

In this example:
- `timestamp` is the recording time with timezone (here, `+01:00`).
- `temperature`, `humidity`, and `pressure` are keys representing different sensors.
- `22.5`, `45.0`, and `1013` are values associated with each sensor at the time of recording.

## Project Structure

```
- TKV/
    - src/                # Project source code
        - parser.py       # Script to read and parse TKV files
        - writer.py       # Script to generate and write TKV files
    - README.md           # Project documentation
```

## Installation

Ensure you have **Python 3.8** or later. To install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Parsing a TKV File

The `parser.py` script reads a TKV file and loads the data into a Python structure.

Example usage:

```python
from src.parser import parse_tkv

data = read_tkv("yourfile.tkv")
print(data)
```

### Creating a TKV File

The `writer.py` script allows you to create a new TKV file from data in dictionary format.

Example usage:

```python
from src.writer import write_tkv

data = [
    {"timestamp": "2024-11-12T14:32:45+01:00","temperature": 22.5,"humidity" :45.0, "pressure": 1013},
    {"timestamp": "2024-11-12T14:33:00+01:00","temperature": 22.4,"humidity" :44.8, "pressure": 1012},
]

write_tkv("data/new_file.tkv", data)
```

## Contribution

1. Fork the project.
2. Create a branch for your feature (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add my feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

- **Julien Baudry** - Project Creator

---

This README is structured in Markdown for improved readability on GitHub and other platforms.
