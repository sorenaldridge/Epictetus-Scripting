import time
import os
import subprocess
from reports import slash_fill
from reports import dash_fill
from datetime import datetime
from pathlib import Path
from db import Torrent
from pony.orm import db_session

import slack
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirCreatedEvent, FileCreatedEvent

class SlackHandler(FileSystemEventHandler):
    def __init__(self):
        # instantiate Slack client
        self.client = slack.WebClient(os.environ.get('SLACK_BOT_TOKEN'))

    def on_created(self, event):
        path = Path(event.src_path)
        timestamp = datetime.now()
        msg = (
            f"```{slash_fill}\n"
            f"\n\t\t\tTORRENT COMPLETED\n\t\t {timestamp.strftime('%a, %b %d @ %I:%M %p')}\n\n"
            f"{dash_fill} \n\n -{path.name}\n\n"
            f"{slash_fill}```"
        )

        try:
            sp_result = subprocess.run(['du','s','-B1', path], capture_output=True, text=True)
            #print(sp_result)
            size = int(sp_result.stdout.split()[0])
        except:
            size = None

        #add torrent data to datbase
        self.create_row(path.name, timestamp, size)
        self.client.chat_postMessage(channel='#torrent-notifications', text=msg)

    @db_session
    def create_row(self, name, completed, size):
        t = Torrent(name=name, completed=completed, size=size)


if __name__ == '__main__':

    watch_dir = Path("/home/yeet/Documents/Completed Downloads")

    observer = Observer()
    observer.schedule(SlackHandler(), str(watch_dir), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    except Exception as e:
        print(e)
        observer.stop()

    observer.join()

