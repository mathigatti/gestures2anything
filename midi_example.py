from rtmidi.midiutil import open_midiinput

port = 0
midi_in, port_name = open_midiinput(port)

while True:
    msg = midi_in.get_message()
    if msg:
        message, deltatime = msg
        print(message)
        #gesture = message[1]
        #print(gesture)