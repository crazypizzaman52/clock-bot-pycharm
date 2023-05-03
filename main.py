import discord
from discord import app_commands
from discord.ext import commands, tasks
import sqlite3
import datetime
import requests
import html
import random
from subprocess import check_output
from scrambleconvert import scrambler, solve
import logging


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = "!", intents=intents, case_insensitive=True)
client.remove_command('help')

logging.getLogger("discord").setLevel(logging.ERROR)
logging.basicConfig(filename="./logger.txt",level=logging.INFO,format="%(asctime)s:%(message)s")

connection = sqlite3.connect("./database.db")
cursor = connection.cursor()

# add a table for records to sqlite3

cursor.execute("""
CREATE TABLE IF NOT EXISTS clockbot (
comp_id VARCHAR(255) PRIMARY KEY,
comp_name VARCHAR(255),
location VARCHAR(255),
iso VARCHAR(8),
start_date VARCHAR(255),
end_date VARCHAR(255),
rounds INTEGER,
competitors TEXT
)
""")

@client.event
async def on_ready():
  print("Bot is online!")
  await client.get_channel(774133192536883203).send("piss")
  task_loop.start()
  logging.info("Bot is online")


@client.hybrid_command(description="lists upcoming clock competitions and sub 6 competitors going to each")
async def comps(ctx):
  logging.info("!comps")
  d1=datetime.date.today()
  d2=datetime.date.today() + datetime.timedelta(6) if datetime.date.today().weekday() == 0 else datetime.date.today() + datetime.timedelta(5)
  final=f"clock comps from {d1} to {d2}:\n"
  for i in cursor.execute("SELECT comp_name,iso,rounds,competitors FROM clockbot WHERE start_date BETWEEN ? AND ? OR end_date BETWEEN ? AND ? ORDER BY start_date, end_date",(d1, d2, d1, d2)).fetchall():
    final+=(f"{i[0]} :flag_{i[1]}: ({i[2]})\n")
    final+= "        *error fetching competitors*\n" if i[3] == None else i[3]+"\n" if i[3] != "" else ""
  final=final.strip('\n')
  if len(final)<2000:
    await ctx.send(final)
  else:
    index=final[:2000].rindex('\n')
    await ctx.send(final[:index])
    await ctx.send(final[index+1:])

# Gets new competitions from wca
@tasks.loop(seconds=900)
async def task_loop():
  try:
    r=requests.get("https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&event_ids%5B%5D=clock&region=all&search=&year=all+years&state=by_announcement&from_date=&to_date=&delegate=&display=list")
    comp_ids=[i.split('">')[0] for i in r.text.split('<a href="/competitions/')][2:]
    for i in comp_ids:
      if cursor.execute("SELECT * FROM clockbot WHERE comp_id = ?", (i,)).fetchall() == []:
        name = r.text.split(i)[1].split('">')[1].split("</a>")[0]
        location = r.text.split(i)[1].split('<div class="location">\n          <strong>')[1].split("</strong")[0]
        if location=="United States":
          location=r.text.split(i)[1].split("United States")[1].split(", ")[2].split("\n")[0]+", United States"
        iso = r.text.split(i)[0].split("fi-")[-1].split('"')[0]
        date = r.text.split(i)[0].split("</i>\n        ")[-1].split("\n")[0]
        date1 = datetime.datetime.strptime(" ".join(date.split(" ")[:2]).strip(",") + ", " + date.split(", ")[1][:4] if " - " in date else date, "%b %d, %Y").strftime("%Y-%m-%d")
        date2 = datetime.datetime.strptime(date if not "-" in date else date.split("- ")[1] if date.split("- ")[1][1].isalpha() else date.split(" ")[0] + date.split("-")[1], "%b %d, %Y").strftime("%Y-%m-%d")
        rounds = int(requests.get(f"https://www.worldcubeassociation.org/competitions/{i}#competition-events").text.split("clock-r")[-1][0])

        cursor.execute("INSERT INTO clockbot VALUES(?, ?, ?, ?, ?, ?, ?,NULL)", (i, html.unescape(name), location, iso, date1, date2, rounds))
        connection.commit()
        channel = client.get_channel(774133192536883203)
        await channel.send(f"{html.unescape(name)} was just announced in {location} :flag_{iso}: with {rounds} {'round' if rounds==1 else 'rounds'} of clock!")
        logging.info("competition just found: " + html.unescape(name))
    logging.info("updated comps")
  except:
    logging.info("comps update fail")

# Gets new (clock) records from wca
@tasks.loop(seconds=900)
async def records_loop():
  try:
    r=requests.get("https://www.worldcubeassociation.org/competitions?utf8=%E2%9C%93&event_ids%5B%5D=clock&region=all&search=&year=all+years&state=by_announcement&from_date=&to_date=&delegate=&display=list")
    comp_ids=[i.split('">')[0] for i in r.text.split('<a href="/competitions/')][2:]
    for i in comp_ids:
      if cursor.execute("SELECT * FROM clockbot WHERE comp_id = ?", (i,)).fetchall() == []:
        name = r.text.split(i)[1].split('">')[1].split("</a>")[0]
        location = r.text.split(i)[1].split('<div class="location">\n          <strong>')[1].split("</strong")[0]
        if location=="United States":
          location=r.text.split(i)[1].split("United States")[1].split(", ")[2].split("\n")[0]+", United States"
        iso = r.text.split(i)[0].split("fi-")[-1].split('"')[0]
        date = r.text.split(i)[0].split("</i>\n        ")[-1].split("\n")[0]
        date1 = datetime.datetime.strptime(" ".join(date.split(" ")[:2]).strip(",") + ", " + date.split(", ")[1][:4] if " - " in date else date, "%b %d, %Y").strftime("%Y-%m-%d")
        date2 = datetime.datetime.strptime(date if not "-" in date else date.split("- ")[1] if date.split("- ")[1][1].isalpha() else date.split(" ")[0] + date.split("-")[1], "%b %d, %Y").strftime("%Y-%m-%d")
        rounds = int(requests.get(f"https://www.worldcubeassociation.org/competitions/{i}#competition-events").text.split("clock-r")[-1][0])

        cursor.execute("INSERT INTO clockbot VALUES(?, ?, ?, ?, ?, ?, ?,NULL)", (i, html.unescape(name), location, iso, date1, date2, rounds))
        connection.commit()
        channel = client.get_channel(774133192536883203)
        await channel.send(f"{html.unescape(name)} was just announced in {location} :flag_{iso}: with {rounds} {'round' if rounds==1 else 'rounds'} of clock!")
        logging.info("competition just found: " + html.unescape(name))
    logging.info("updated comps")
  except:
    logging.info("comps update fail")

@client.hybrid_command(description="generates a random clock scramble")
async def scramble(ctx):
  logging.info("!scramble")
  moves=["0+","1+","2+","3+","4+","5+","6+","1-","2-","3-","4-","5-"]
  pinstates=["UR DR DL UL", "UR DR DL", "UR DR UL", "UR DL UL", "DR DL UL", "UR DR", "DR DL", "DL UL", "UL UR", "UR DL", "DR UL", "UR", "UL", "DR", "DL", ""]
  await ctx.send(f"UR{random.choice(moves)} DR{random.choice(moves)} DL{random.choice(moves)} UL{random.choice(moves)} U{random.choice(moves)} R{random.choice(moves)} D{random.choice(moves)} L{random.choice(moves)} ALL{random.choice(moves)} y2 U{random.choice(moves)} R{random.choice(moves)} D{random.choice(moves)} L{random.choice(moves)} ALL{random.choice(moves)} {random.choice(pinstates)}")

@client.hybrid_command(description="finds the optimal solution")
async def optclock(ctx, *, scramble):
  logging.info("!optclock " + scramble)
  if scramble=="help":
    await ctx.send("""Do '!optclock' followed by the scramble to use. In the solution, a lowercase pin such as 'dr' means to put up every pin except for that pin. '/' means URDL and '\' means ULDR. Ping/DM Josh M#3108 if you need more help. This program uses optclock which was made by Michael Gottlieb.""")
  else:
    try:
      await ctx.send("searching for optimal solution...")
      if all(str(ele).isdigit() for ele in scramble.split(" ")):
        if len(scramble.split(" "))==14:
          out=check_output(["./path to clockbot"], input=f"{scramble}\nq\n", encoding="utf-8")
          await ctx.channel.send(out.split("solutions.\n")[1].split('\n')[0]+"\n"+solve(out.split("is optimal:\n")[1].split("\nOptimal solution")[0],"y2"))
        else:
          await ctx.channel.send(f'Error: It appears you tried to enter the dial positions manually. This requires 14 numbers separated by spaces and you have {len(message.split(" "))}.')
          logging.info("bad input: len error")
      else:
        out=check_output(["./path to clockbot"], input=f"{scrambler(scramble)}\nq\n", encoding="utf-8")
        await ctx.channel.send(out.split("solutions.\n")[1].split('\n')[0]+"\n"+solve(out.split("is optimal:\n")[1].split("\nOptimal solution")[0],message))
    except:
       await ctx.channel.send('error. please check to make sure you entered the scramble correctly. use "!optclock help" to learn how to use.')
       logging.info("bad input")

@client.hybrid_command(description="sends all optimal solutions that optclock finds")
async def optclockall(ctx, *, scramble):
  logging.info("!optclockall " + scramble)
  if scramble=="help":
    await ctx.send("""do '!optclockall' followed by the scramble to use. in the solution, a lowercase pin such as 'dr' means to put up every pin except for that pin. this program uses optclock which was made by Michael Gottlieb""")
  else:
    try:
      await ctx.send("searching for optimal solutions...")
      if all(str(ele).isdigit() for ele in scramble.split(" ")):
        if len(scramble.split(" "))==14:
          out=check_output(["./path to optclock all"], input=f"{scramble}\nq\n", encoding="utf-8")
          optimal=out.split("solutions.\n")[1].split(" moves")[0]
          final=""
          for c,v in enumerate(out.split("\n")):
            if "Found solution of length "+optimal in v:
              final+=solve(out.split("\n")[c+1].split("Found")[0].split("Checked")[0],"y2")+"\n"
        else:
          await ctx.channel.send(f'Error: It appears you tried to enter the dial positions manually. This requires 14 numbers separated by spaces and you have {len(message.split(" "))}.')
          logging.info("bad input: len error")
          return
      else:
        out=check_output(["./path to optclock all"], input=f"{scrambler(scramble)}\nq\n", encoding="utf-8")
        optimal=out.split("solutions.\n")[1].split(" moves")[0]
        final=""
        for c,v in enumerate(out.split("\n")):
          if "Found solution of length "+optimal in v:
            final+=solve(out.split("\n")[c+1].split("Found")[0].split("Checked")[0],scramble)+"\n"
      if len(final)>1950:
        final_lines = final.splitlines()
        result = [final_lines[i] for i in range(len(final_lines)) if sum(len(line) for line in final_lines[:i+1]) < 1900]
        final = "\n".join(result) +"\nSome solutions were removed to avoid discord's message size limit"
      await ctx.channel.send(out.split("solutions.\n")[1].split('\n')[0]+"\n"+final)
    except:
       await ctx.channel.send('error. please check to make sure you entered the scramble correctly. use "!optclock help" to learn how to use.')
       logging.info("bad input")

#syncs the slash commands
@client.command()
@commands.is_owner()
async def synccommands(ctx):
  await client.tree.sync()
  await ctx.send("cool")
  logging.info("commands synced")

#Updates the competition list. This is done automatically but this is here just in case.
@client.command()
@commands.is_owner()
async def updatecomps(ctx):
  logging.info("!updatecomps")
  await ctx.channel.send("updating...")
  for i in cursor.execute(f"SELECT comp_id FROM clockbot WHERE start_date BETWEEN '{datetime.date.today()}' AND '{datetime.date.today()+datetime.timedelta(7)}'").fetchall():
    r=requests.get(f"https://www.worldcubeassociation.org/competitions/{i[0]}/registrations/psych-sheet/clock")
    times=[x.split("</td>")[0] for x in r.text.split('class="average">')[2:] if (x.split("</td>")[0] and ":" not in x.split("</td>")[0] and float(x.split("</td>")[0]) < 6)]
    competitors=[html.unescape(x.split("</td>")[0]) for x in r.text.split('class="name">')[2:2+len(times)]]
    final = "\n".join([f"        __**{competitors[x]} - {times[x]}**__" if float(times[x]) < 4 else f"        **{competitors[x]} - {times[x]}**" if float(times[x]) < 5 else f"        *{competitors[x]} - {times[x]}*" for x in range(len(times))])
    cursor.execute("UPDATE clockbot SET competitors = ? WHERE comp_id = ?", (final,i[0]))
    connection.commit()
  await ctx.channel.send(cursor.execute(f"SELECT competitors FROM clockbot WHERE start_date BETWEEN '{datetime.date.today()}' AND '{datetime.date.today()+datetime.timedelta(5)}'").fetchall())

client.run("OTE4NjE1NjM3NDE5NTAzNjI2.Gz-E4x.ux-vU0AwMkWoj5AQXVMF9FW88KZ42xf7lE7Oco",log_handler=None)
