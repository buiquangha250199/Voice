import librosa
import soundfile as sf
import sounddevice as sd
import time
import keyboard

def sync_record(filename, duration, fs, channels):
 print('Recording...')
 myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
 sd.wait()
 sf.write(filename, myrecording, fs)
 print('Done recording!')


print('################################################################')
print('Please press SPACE to start recording!')
print('################')

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('space'):  # if key 'q' is pressed 
            sync_record('sync_record.wav', 10, 16000, 1)
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break