import time
import os
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
from transcribe import transcribe

class Handler(FileSystemEventHandler):
    def on_created(self, event: FileSystemEvent):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            transcribe(os.path.join("inFiles", file_name))

# Set up the event handler and observer
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, "inFiles", recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping observer...")
finally:
    observer.stop()
    observer.join()