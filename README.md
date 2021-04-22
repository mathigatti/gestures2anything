# gestures2anything

Use your webcam to identify gestures and trigger any script

[![Gestures identification website](imgs/website.jpg)](https://gestos.mathigatti.com/)

# How it works?

[This](http://gestos.mathigatti.com/) website identifies 6 basic gestures and sends a MIDI message. To catch the MIDI you can use `midi_example.py`, it's a simple script that receives the messages and prints them. You can replace the print statement for anything else you want.

For more details about the website development check [this repository](https://github.com/mathigatti/GesturesController).

# Requirements

- Python 3
- Some python modules (Try something like `pip install -r requirements.txt`)

# Usage

1. Run the script.

```python midi_example.py```

2. Go to [the website](http://gestos.mathigatti.com/) and modify the selection bar in order to choose the midi output (Instead of `None`).

![Sample script output](imgs/sample_script.jpg)

## Support my work

If you want to help me to keep going developing and maintaining open-source projects you can contribute buying me some [ko-fi](https://ko-fi.com/mathigatti).
