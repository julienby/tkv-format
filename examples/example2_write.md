### Example Usage

Suppose you have data structured like this:

```python
data = [
    {"timestamp": "2024-11-12T14:32:45+01:00", "temperature": 22.5, "humidity": 45.0, "pressure": 1013.0},
    {"timestamp": "2024-11-12T14:33:00+01:00", "temperature": 22.4, "humidity": 44.8, "pressure": 1012.0},
]
```

You can use `write_tkv` to save it to a file:

```python
write_tkv("data/output.tkv", data)
```

### Resulting `output.tkv` File

```
2024-11-12T14:32:45+01:00 ; temperature:22.5 ; humidity:45.0 ; pressure:1013.0
2024-11-12T14:33:00+01:00 ; temperature:22.4 ; humidity:44.8 ; pressure:1012.0
```

### Explanation

- **`timestamp.isoformat()`**: Ensures timestamps are in ISO format.
- **Joining sensor data**: Each key-value pair is joined by `" ; "` to match the required format.
  
This function should handle most data structures that match the expected format. If you need any adjustments, let me know!