import time
import threading

import pyperclip


def is_url_but_not_bitly(url):
    if url.startswith("http://") and not "bit.ly" in url:
        return True
    return False


def print_to_stdout(clipboard_content):
    print("Found url: %s" % str(clipboard_content))


class ClipboardWatcher(threading.Thread):
    def __init__(self, predicate, callback, pause=5.):
        super(ClipboardWatcher, self).__init__()
        self._predicate = predicate
        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                if self._predicate(recent_value):
                    self._callback(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True


def main():
    watcher = ClipboardWatcher(is_url_but_not_bitly, print_to_stdout, 5.)
    watcher.start()
    while True:
        try:
            print("Waiting for changed clipboard...")
            time.sleep(10)
        except KeyboardInterrupt:
            watcher.stop()
            break


if __name__ == "__main__":
    main()