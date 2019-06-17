import time
import sys
import os
import slack
from datetime import datetime, timedelta
from db import Torrent, NetworkSlice
from pony.orm import *
from dateutil.relativedelta import relativedelta
from math import log
unit_list = list(zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2]))
slash_fill = "///////////////////////////////////////"
dash_fill = "---------------------------------------"

class Reporter:
    def __init__(self):
        # instantiate Slack client
        self.client = slack.WebClient(os.environ.get('SLACK_BOT_TOKEN'))
    
    def weekly_reporter(self):     
        weekly_report = (
            f"```{slash_fill}\n\n\t\t\tWEEKLY REPORT\n\t for {datetime.today().date() - relativedelta(weeks=1)} to {datetime.today().date()}\n\n{dash_fill}"
            f"\n  TOTAL WEEK DOWN: {self.sizeof_fmt(week_down)}"
            f"\n  TOTAL WEEK UP: {self.sizeof_fmt(week_up)}\n{dash_fill}\n"
            f"\n{self.format_torrents(week_torrent)}"
            f"\n\n{slash_fill}\n```"
        )
        self.client.chat_postMessage(channel='#torrent-notifications', text=weekly_report)

    def monthly_reporter(self):     
        monthly_report = (
            f"```{slash_fill}\n\n\t\t\tMONTHLY REPORT\n\t for {datetime.today().date() - relativedelta(months=1)} to {datetime.today().date()}\n\n{dash_fill}"
            f"\n  TOTAL MONTH DOWN: {self.sizeof_fmt(month_down)}"
            f"\n  TOTAL MONTH UP: {self.sizeof_fmt(month_up)}\n{dash_fill}\n"
            f"\n{self.format_torrents(week_torrent)}"
            f"\n\n{slash_fill}\n```"
        )
        self.client.chat_postMessage(channel='#torrent-notifications', text=monthly_report)

    @staticmethod 
    def format_torrents(torrents):
        return "\n".join([f" -{t[:32]}..." for t in torrents])

    @staticmethod
    def sizeof_fmt(num):
        """Human friendly file size"""
        if num > 1:
            exponent = min(int(log(num, 1000)), len(unit_list) - 1)
            quotient = float(num) / 1000**exponent
            unit, num_decimals = unit_list[exponent]
            format_string = '{:.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)
        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'


with db_session:
    network_activity = NetworkSlice.select(lambda ns: ns.timestamp >= datetime.now() - timedelta(minutes=2))[:]
    network_activity = select(ns for ns in NetworkSlice if ns.timestamp >= datetime.now() - timedelta(minutes=2))[:]

    week_up = sum(ns.up for ns in NetworkSlice if ns.timestamp >= datetime.now() - relativedelta(weeks=1))
    week_down = sum(ns.down for ns in NetworkSlice if ns.timestamp >= datetime.now() - relativedelta(weeks=1))
    week_torrent = select(t.name for t in Torrent if t.completed >= datetime.now() - relativedelta(weeks=1))[:]

    month_up = sum(ns.up for ns in NetworkSlice if ns.timestamp >= datetime.now() - relativedelta(months=1))
    month_down = sum(ns.down for ns in NetworkSlice if ns.timestamp >= datetime.now() - relativedelta(months=1))
    month_torrent = select(t.name for t in Torrent if t.completed >= datetime.now() - relativedelta(months=1))[:]


if __name__ == '__main__':
    #create instance of reporter
    reporter = Reporter()
    #if command line passes w as arg push weekly report to slack
    if sys.argv[1] == 'w':
        reporter.weekly_reporter()
    #if command line passes m as arg push monthly report to slack
    elif sys.argv[1] == 'm':
        reporter.monthly_reporter()
    else:
        print("Invalid Arg")
    
    

    