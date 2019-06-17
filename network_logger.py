import time
import psutil
from db import NetworkSlice
from datetime import datetime
from pony.orm import db_session
from enum import Enum

class Interval(float, Enum):
    HOUR = 3600.
    MINUTE = 60.
    SECOND = 1.
    MILLISECOND = .001


class TrafficMonitor:

    def __init__(self):
        # set initial cached usage
        self.prev = psutil.net_io_counters()

    def poll(self, interval = Interval.SECOND):
        time.sleep(interval)

        usage = psutil.net_io_counters()
        timestamp = datetime.now()
        
        up = usage.bytes_sent - self.prev.bytes_sent
        down = usage.bytes_recv - self.prev.bytes_recv
        
        # update cached usage
        self.prev = usage

        # log to database
        self.log(up, down, timestamp)

        return up, down, timestamp

    @db_session
    def log(self, up, down, timestamp):
        return NetworkSlice(down=down, up=up, timestamp=timestamp)


if __name__ == '__main__':
    #print("\n////Initializing Network Tracking////\n")

    try:
        monitor = TrafficMonitor()
        while True:
            monitor.poll()

    except (KeyboardInterrupt, SystemExit):
        pass
