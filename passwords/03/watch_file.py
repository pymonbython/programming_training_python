from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
path_abs = os.path.expanduser("~/pycamp/passwords/03")

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == os.path.join(path, "text.txt"):
            print(f"Plik {event.src_path} został zmodyfikowany!")

# Monitorowanie katalogu
path = "/home/szymurai/pycamp/passwords/03"
observer = Observer()
event_handler = FileChangeHandler()
observer.schedule(event_handler, path=path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
