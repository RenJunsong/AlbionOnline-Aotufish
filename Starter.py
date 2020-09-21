from pynput.keyboard import Key, Listener
import time
import threading
import inspect
import ctypes
import Albion


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
 
 
def game_run():
    Albion.fish()
def on_press(key):
    pass


def on_release(key):
    all_key.append(str(key))
    global t
    
    if "Key.f8" in all_key:
        Albion.small_game()
        all_key.clear()

    if "Key.f9" in all_key:
        if (not t.is_alive()):
            print("Fish start")
            t.start()
        all_key.clear()

    if "Key.f10" in all_key:
        if (t.is_alive()):
            print("Fish cause")
            stop_thread(t)
            t = threading.Thread(target=game_run)
        all_key.clear()
    try:
        if all_key[-1] == 'Key.ctrl_l':
            time1 = time.time()
            while True:
                if time.time() - time1 >= 1:
                    all_key.clear()
                    break
    except:
        pass
    if key == Key.f11:
        return False


if __name__ == '__main__':
    t = threading.Thread(target=game_run)
    all_key = []    
    with Listener(on_press=None, on_release=on_release) as listener:
        listener.join()
