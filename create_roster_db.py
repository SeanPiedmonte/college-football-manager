# Helper script to just create the roster data. Will not be called outside of
# in development

import sqlite3

db = sqlite3.connect("rosters.db")
cur = db.cursor()

# create the players table if it does not exist
create_players_stmt = """CREATE TABLE IF NOT EXISTS players(playerid INTEGER PRIMARY KEY,
                                    name TEXT,
                                    position TEXT,
                                    hometown TEXT,
                                    homestate TEXT,
                                    star_rating INTEGER,
                                    year INTEGER,
                                    redshirt INTEGER,
                                    dealbreaker TEXT,
                                    number INTEGER,
                                    height INTEGER,
                                    weight INTEGER,
                                    speed INTEGER,
                                    throwing_ability INTEGER,
                                    strength INTEGER,
                                    catching INTEGER,
                                    blocking INTEGER,
                                    tackling INTEGER,
                                    coverage INTEGER,
                                    pass_rush INTEGER)"""
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
#playerid,name,position,hometown,homestate,star_rating,year,redshirt,dealbreaker,number,height,weight,speed,throwing_ability,strength,catching,blocking,tackling,coverage,pass_rush
ironwood_state_roster = [
    (0, "Carter Malone", "QB", "Scottsdale", "AZ", 4, 2, false, "scheme_fit", 12, 76, 225, 87, 81, 83, 17, 10, 10, 5, 5),
    (1, "Julian Barnes", "QB", "Bowling Green", "KY", 3, 1, true, "playing_time", 14, 74, 210, 74, 69, 75, 13, 10, 6, 3, 3),
    (2, "Elijah Cooke", "QB", "Chattanooga", "TN", 3, 3, false, "program_tradition", 8, 75, 215, 75, 84, 74, 20, 12, 10, 5, 5),
    (3, "Jace Hollowell", "QB", "Sioux Falls", "SD", 2, 0, true, "distance_to_home", 16, 73, 195, 67, 49, 62, 10, 8, 3, 1, 2),
]

cur.executemany("INSERT INTO players VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", ironwood_state_roster)
db.commit()
