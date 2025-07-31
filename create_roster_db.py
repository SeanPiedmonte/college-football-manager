# Helper script to just create the roster data. Will not be called outside of
# in development

import sqlite3
import csv

player_id = -1
ironwood_roster_file = open("ironwood.csv", "r")
ironwoodcsv = csv.reader(ironwood_roster_file)

db = sqlite3.connect("rosters.db")
cur = db.cursor()
# create the players table if it does not exist
create_players_stmt = """CREATE TABLE IF NOT EXISTS players(playerid INTEGER PRIMARY KEY,
                                    name TEXT,
                                    number INTEGER,
                                    position TEXT,
                                    star_rating INTEGER,
                                    year INTEGER,
                                    redshirt INTEGER,
                                    height INTEGER,
                                    weight INTEGER,
                                    speed INTEGER,
                                    throwing_power INTEGER,
                                    throwing_accuracy INTEGER,
                                    catching INTEGER,
                                    blocking INTEGER,
                                    pass_rush INTEGER,
                                    block_shedding INTEGER,
                                    tackling INTEGER,
                                    coverage INTEGER,
                                    strength INTEGER,
                                    football_iq INTEGER,
                                    ball_carrier_vision INTEGER,
                                    carrying INTEGER,
                                    dev_trait INTEGER,
                                    dealbreaker TEXT,
                                    hometown TEXT,
                                    homestate TEXT)"""
cur.execute(create_players_stmt)

create_teams_stmt = """CREATE TABLE IF NOT EXISTS teams(teamid INTEGER PRIMARY KEY,
                                  name TEXT,
                                  mascot TEXT,
                                  city TEXT,
                                  state TEXT,
                                  prestige INTEGER)"""

cur.execute(create_teams_stmt)

create_roster_stmt = """CREATE TABLE IF NOT EXISTS roster(teamid INTEGER NOT NULL,
                                           playerid INTEGER NOT NULL,
                                           PRIMARY KEY (teamid, playerid),
                                           FOREIGN KEY (teamid) REFERENCES team(teamid),
                                           FOREIGN KEY (playerid) REFERENCES player(playerid))"""
cur.execute(create_roster_stmt)
    
team_data = [
    (0, "Ironwood State", "ThunderHawks", "Ironwood Falls","MT", 7),
    (2, "Red Ridge Tech", "Vortex", "Red Ridge", "NV", 8),
    (3, "Praire Forge", "Miners", "Praire Forge", "KS", 6),
    (4, "Midland Covenant", "Crusaders", "Midland Springs", "IN", 4),
    (5, "Northshore Institute", "Sabercats", "Northshore", "MN", 9),
    (6, "Echo Valley", "Wranglers", "Echo Valley", "WY", 3),
    (7, "Cobalt Hills", "Aviators", "Cobalt Hills", "CO", 7),
    (8, "Frostpine University","Yetis", "Frostpine", "AK", 2),
    (9, "Western Bluffs", "Stormcallers", "Western Bluffs", "OR", 6),
]

cur.executemany("INSERT INTO teams VALUES(?,?,?,?,?,?)", team_data)
db.commit()

true = 1
false = 0
tup_list = []
for line in ironwoodcsv:
    if player_id == -1:
        player_id+=1
        continue
    line.insert(0, str(player_id))
    player_id+=1
    tup_list.append(tuple(line))

cur.executemany("""INSERT INTO players(playerid, name, number, position, 
                       star_rating, year, redshirt, height, weight, speed,
                       throwing_power, throwing_accuracy, catching, blocking, 
                       pass_rush, block_shedding, tackling, coverage, strength, 
                       football_iq, ball_carrier_vision, carrying, dev_trait, 
                       dealbreaker, hometown, homestate) 
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", tup_list)
db.commit()
