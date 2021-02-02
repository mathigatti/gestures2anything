from rtmidi.midiutil import open_midiinput

port = 0
midi_in, port_name = open_midiinput(port)

last_gestures = []
last_gesture = None

while True:
    msg = midi_in.get_message()
    if msg:
        message, deltatime = msg
        gesture = message[1]
        last_gestures.append(gesture)
        last_gestures = last_gestures[-10:]
        if last_gesture != gesture and last_gestures.count(gesture) > 5:
        	last_gesture = gesture
        	print(gesture)