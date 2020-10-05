from pynput.keyboard import Key, Listener, Controller
import time

def on_press(key):
    if key == Key.f5:
        return False
    r='r'
    e='e'
    f='f'
    w='w'
    d='d'
    if str(key) == "'a'":
        keyboard.press(f)
        time.sleep(0.02)
        keyboard.release(f)
        time.sleep(0.5)
        keyboard.press(Key.space)
        time.sleep(0.02)
        keyboard.release(Key.space)
        time.sleep(0.02)
        keyboard.press(w)
        time.sleep(0.02)
        keyboard.release(w)
        time.sleep(0.6)
    if str(key) == "'s'":
        keyboard.press(d)
        time.sleep(0.02)
        keyboard.release(d)
        time.sleep(0.7)
        keyboard.press(r)
        time.sleep(0.02)
        keyboard.release(r)
        time.sleep(0.01)
        keyboard.press(r)
        time.sleep(0.02)
        keyboard.release(r)
        time.sleep(0.01)
        keyboard.press(r)
        time.sleep(0.02)
        keyboard.release(r)
        time.sleep(0.6)
        keyboard.press(e)
        time.sleep(0.02)
        keyboard.release(e)




if __name__ == '__main__':
    all_key = [] 
    keyboard = Controller()	
    with Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
