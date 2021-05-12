# gestures2anything

Use your webcam to identify gestures and trigger any script

[![Gestures identification website](imgs/website.jpg)](https://gestos.mathigatti.com/)

# How do you use it?

[This](http://gestos.mathigatti.com/) website identifies 6 basic gestures and sends a MIDI message. You can use tools like LoopMidi in Windows or IAC driver in OSX to create a MIDI port and connect the website to Ableton or any other DAW.

If you are familiar with Python you can also catch the MIDI with `midi_example.py`, it's a simple script that receives the messages and prints them. You can replace the print statement for anything else you want.

For more details about the website development check [this repository](https://github.com/mathigatti/GesturesController).

## Python script usage

1. Install required python modules

```python -m pip install requirements.txt```

2. Run the script

```python midi_example.py```

3. Go to [the website](http://gestos.mathigatti.com/) and modify the selection bar in order to choose the midi output (Instead of `None`).

![Sample script output](imgs/sample_script.jpg)

## Support my work

If you want to help me to keep going developing and maintaining open-source projects you can contribute buying me some [ko-fi](https://ko-fi.com/mathigatti).
