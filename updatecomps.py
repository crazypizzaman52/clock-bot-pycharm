# Updates the !comps competitors and times. This is run automatically with crontab every Sunday, Tuesday, and Thursday night with the following crontab line:
# 30 23 * * 0,2,4 python3 /{path to file}/updatecomps.py &

import requests
import sqlite3
import time
import datetime
import logging
import html

connection = sqlite3.connect("./database.db")
cursor = connection.cursor()

logging.basicConfig(filename="path to log file", level=logging.INFO, format="%(asctime)s:%(message)s")

complete = False

while complete == False:
    try:
        for i in cursor.execute("SELECT comp_id FROM clockbot WHERE start_date BETWEEN ? AND ?",
                                (datetime.date.today(), datetime.date.today() + datetime.timedelta(8))).fetchall():
            r = requests.get(
                f"https://www.worldcubeassociation.org/competitions/{i[0]}/registrations/psych-sheet/clock")
            times = [x.split("</td>")[0] for x in r.text.split('class="average">')[2:] if
                     x.split("</td>")[0] and ":" not in x.split("</td>")[0] and float(x.split("</td>")[0]) < 6]
            competitors = [html.unescape(x.split("</td>")[0]) for x in r.text.split('class="name">')[2:2 + len(times)]]
            final = "\n".join([f"        __**{competitors[x]} - {times[x]}**__" if float(
                times[x]) < 4 else f"        **{competitors[x]} - {times[x]}**" if float(
                times[x]) < 5 else f"        *{competitors[x]} - {times[x]}*" for x in range(len(times))])
            cursor.execute("UPDATE clockbot SET competitors = ? WHERE comp_id = ?", (final, i[0]))
            connection.commit()
        complete = True
        print("done")
        logging.info("!comps update success")
    except:
        logging.info("!comps update failed. retrying in 5 minutes")
        time.sleep(300)
