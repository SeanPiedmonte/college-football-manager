use std::fmt;
use rand::Rng;

/*
* Player is a struct looking to handle the creation of players for teams in
* the context of the college football manager. Player will have the following
* attributes.
* name: This is the name of a player
* num: This is the player's number
* spd: Speed of the player
* thr: The throwing ability of the player (Goal is to have this broken out in more detail) str: The strength of the player cth: The catching ability of the player tck: The tackling ability of the player
* cov: The coverage ability of the player
* prh: The pass rushing ability of the player
*/
#[derive(Default, Copy, Clone)]
pub struct Player {
    name: &'static str,
    pos : &'static str,
    hgt :i32,
    wgt :i32,
    num :i32,
    spd :i32,
    thr :i32,
    str :i32,
    cth :i32,
    tck :i32,
    cov :i32,
    prh :i32,
    blk: i32,
}

/*
* This is our display trait to allow us to log and print our player sturcts
*/
impl std::fmt::Display for Player {
    fn fmt(&self, fmt: &mut std::fmt::Formatter<'_>) -> fmt::Result {
        write!(fmt, "Player {{ name: {}, pos: {}, num: {}, hgt: {}, wgt: {}, spd: {}, thr: {}, str: {}, cth: {}, tck: {}, cov: {}, prh: {}, blk: {} }}",
        self.name, self.pos, self.num, self.hgt, self.wgt, self.spd, self.thr, self.str, self.cth, self.tck, self.cov, self.prh, self.blk)
    }
}

/*
* create_base_roster
* parameters: None
* returns: [Player; 10]
*
* Create base roster is the function that seeks to create an array for teams
* to use to store players. (Might Remove)
*/
pub fn create_base_roster() -> [Player; 10] {
    let arr = [Player::default(); 10];
    arr
}

/*
* create_player
* parameters: &'static str, i32, i32, i32, i32, i32, i32, i32, i32
* returns: Player
*
* Creates a player with all of the parameters needed to create a valid Player
* struct. Use to append Players to rosters.
*/
pub fn create_player(name: &'static str, pos: &'static str, num : i32, spd : i32, thr : i32, 
        str : i32, cth : i32, tck : i32, cov : i32, prh : i32, blk : i32, hgt: i32, wgt: i32) -> Player {
    let new_player = Player {
        name,
        num,
        pos,
        hgt,
        wgt,
        spd,
        thr,
        str,
        cth,
        tck,
        cov,
        prh,
        blk,
    };
    new_player
}

/*
* The Team struct will seek to create and manager our team. This will have
* The team names, location, roster, prestige
*/
#[derive(Default, Copy, Clone)]
pub struct Team {
    id: i32,
    name: &'static str,
    mascot: &'static str,
    city: &'static str,
    state: &'static str,
    prestige: i8,
    pub roster: [Player; 10],
}

/*
* Create a generic team that has no qualities
*/
pub fn create_teams() -> [Team; 10] {
    let team0 = Team {
        id: 0,
        name: "Ironwood State",
        mascot: "Thunderhawks",
        city: "Ironwood Falls",
        state: "MT",
        prestige: 7,
        roster: [Player{name: "Colt Masters", pos: "QB", num: 12, hgt: 74, wgt: 228, spd: 78, thr: 92, str: 72, cth: 65, blk: 58, tck: 35, cov: 30, prh: 25},
                Player{name: "DeShawn Rucker", pos: "RB", num: 25, hgt: 70, wgt: 210, spd: 91, thr: 45, str: 68, cth: 79, blk: 62, tck: 38, cov: 25, prh: 25},
                Player{name: "Wyatt Hagan", pos: "WR", num: 87, hgt: 71, wgt: 207, spd: 89, thr: 42, str: 60, cth: 85, blk: 45, tck: 30, cov: 28, prh: 18},
                Player{name: "Boone Callahan", pos: "OL", num: 70, hgt: 80, wgt: 335, spd: 60, thr: 30, str: 88, cth: 50, blk: 90, tck: 40, cov: 22, prh: 20},
                Player{name: "Eli Tupuola", pos: "OL", num: 74, hgt: 78, wgt: 315, spd: 58, thr: 28, str: 92, cth: 47, blk: 91, tck: 42, cov: 20, prh: 22},
                Player{name: "Trent Moore", pos: "DL", num: 91, hgt: 77, wgt: 274, spd: 72, thr: 30, str: 90, cth: 35, blk: 40, tck: 87, cov: 55, prh: 89},
                Player{name: "Jalen Bass", pos: "DL", num: 96, hgt: 73, wgt: 307, spd: 74, thr: 33, str: 85, cth: 40, blk: 42, tck: 84, cov: 52, prh: 86},
                Player{name: "Tyrese Vann", pos: "LB", num: 52, hgt: 72, wgt: 244, spd: 82, thr: 35, str: 75, cth: 65, blk: 48, tck: 78, cov: 72, prh: 75},
                Player{name: "Quincy Starks", pos: "CB", num: 24, hgt: 73, wgt: 180, spd: 90, thr: 34, str: 67, cth: 70, blk: 41, tck: 65, cov: 88, prh: 45},
                Player{name: "Lane Hollowell", pos: "CB", num: 29, hgt: 68, wgt: 203, spd: 87, thr: 31, str: 66, cth: 73, blk: 40, tck: 63, cov: 85, prh: 48}],
    };
    let team1 = Team {
        id: 1,
        name: "Lakeview Maritime",
        mascot: "Tridents",
        city: "Lakeview Shores",
        state: "ME",
        prestige: 5,
        roster: [Player{name: "Silas Mercer", pos: "QB", num: 9, hgt: 77, wgt: 202, spd: 76, thr: 86, str: 68, cth: 62, blk: 58, tck: 32, cov: 25, prh: 20},
                Player{name: "Niko Santiago", pos: "RB", num: 21, hgt: 69, wgt: 215, spd: 88, thr: 44, str: 64, cth: 74, blk: 59, tck: 35, cov: 20, prh: 18},
                Player{name: "Blake Carson", pos: "WR", num: 11, hgt: 74, wgt: 195, spd: 84, thr: 41, str: 61, cth: 81, blk: 44, tck: 28, cov: 25, prh: 22},
                Player{name: "Marcus Van Fleet", pos: "OL", num: 68, hgt: 77, wgt: 297, spd: 59, thr: 30, str: 84, cth: 50, blk: 88, tck: 39, cov: 20, prh: 24},
                Player{name: "Finn Malachy", pos: "OL", num: 72, hgt: 78, wgt: 299, spd: 61, thr: 28, str: 79, cth: 48, blk: 83, tck: 39, cov: 21, prh: 24},
                Player{name: "Dmitri Kalani", pos: "DL", num: 98, hgt: 78, wgt: 285, spd: 70, thr: 30, str: 81, cth: 42, blk: 40, tck: 79, cov: 50, prh: 78},
                Player{name: "Logan Bremmer", pos: "DL", num: 94, hgt: 78, wgt: 262, spd: 66, thr: 32, str: 77, cth: 38, blk: 42, tck: 74, cov: 52, prh: 75},
                Player{name: "Cairo Willis", pos: "LB", num: 43, hgt: 71, wgt: 224, spd: 78, thr: 36, str: 72, cth: 53, blk: 50, tck: 72, cov: 66, prh: 64},
                Player{name: "Jace Lowenthal", pos: "CB", num: 8, hgt: 73, wgt: 176, spd: 85, thr: 34, str: 65, cth: 69, blk: 41, tck: 61, cov: 80, prh: 42},
                Player{name: "Shane Kealoha", pos: "CB", num: 29, hgt: 72, wgt: 191, spd: 88, thr: 33, str: 63, cth: 67, blk: 39, tck: 60, cov: 78, prh: 40}],
    };
    let team2 = Team {
        id: 2,
        name: "Red Ridge Tech",
        mascot: "Vortex",
        city: "Red Ridge",
        state: "NV",
        prestige: 8,
        roster: [Player{name: "Daxen Reyes", pos: "QB", num: 5, hgt: 77, wgt: 224, spd: 80, thr: 90, str: 74, cth: 68, blk: 62, tck: 38, cov: 32, prh: 28},
                Player{name: "Zahir Moreland", pos: "RB", num: 22, hgt: 73, wgt: 220, spd: 92, thr: 46, str: 72, cth: 78, blk: 66, tck: 41, cov: 28, prh: 25},
                Player{name: "Elias Holt", pos: "WR", num: 11, hgt: 70, wgt: 181, spd: 89, thr: 40, str: 67, cth: 87, blk: 50, tck: 34, cov: 30, prh: 22},
                Player{name: "Royce Daley", pos: "OL", num: 71, hgt: 80, wgt: 310, spd: 63, thr: 40, str: 91, cth: 54, blk: 93, tck: 47, cov: 25, prh: 30},
                Player{name: "Koen Toma", pos: "OL", num: 77, hgt: 76, wgt: 306, spd: 66, thr: 29, str: 89, cth: 51, blk: 90, tck: 45, cov: 24, prh: 28},
                Player{name: "Malik Durham", pos: "DL", num: 97, hgt: 74, wgt: 269, spd: 75, thr: 34, str: 87, cth: 44, blk: 45, tck: 86, cov: 62, prh: 88},
                Player{name: "Jonah Gentry", pos: "DL", num: 92, hgt: 78, wgt: 266, spd: 72, thr: 33, str: 86, cth: 43, blk: 46, tck: 82, cov: 60, prh: 84},
                Player{name: "Tyshon Renner", pos: "LB", num: 44, hgt: 76, wgt: 228, spd: 84, thr: 38, str: 78, cth: 61, blk: 58, tck: 81, cov: 74, prh: 72},
                Player{name: "Kyrie Nesbit", pos: "CB", num: 3, hgt: 72, wgt: 178, spd: 91, thr: 35, str: 70, cth: 76, blk: 46, tck: 70, cov: 89, prh: 50},
                Player{name: "Cruz Whitman", pos: "CB", num: 6, hgt: 71, wgt: 175, spd: 88, thr: 32, str: 68, cth: 67, blk: 42, tck: 68, cov: 87, prh: 52}],
    };
    let team3 = Team {
        id: 3,
        name: "Praire Forge",
        mascot: "Miners",
        city: "Praire Forge",
        state: "KS",
        prestige: 6,
        roster: [Player{name: "Silas Mercer", pos: "QB", num: 9, hgt: 77, wgt: 203, spd: 76, thr: 86, str: 68, cth: 62, blk: 58, tck: 32, cov: 25, prh: 20},
                Player{name: "Niko Santiago", pos: "RB", num: 21, hgt: 74, wgt: 223, spd: 88, thr: 44, str: 64, cth: 74, blk: 59, tck: 35, cov: 20, prh: 18},
                Player{name: "Blake Carson", pos: "WR", num: 11, hgt: 73, wgt: 217, spd: 84, thr: 41, str: 63, cth: 82, blk: 46, tck: 29, cov: 26, prh: 20},
                Player{name: "Marcus Bellamy", pos: "OL", num: 65, hgt: 76, wgt: 290, spd: 60, thr: 29, str: 85, cth: 52, blk: 89, tck: 42, cov: 23, prh: 26},
                Player{name: "Xavier Hicks", pos: "OL", num: 75, hgt: 75, wgt: 292, spd: 58, thr: 28, str: 83, cth: 50, blk: 86, tck: 42, cov: 23, prh: 24},
                Player{name: "Cole Vickers", pos: "DL", num: 93, hgt: 78, wgt: 300, spd: 71, thr: 31, str: 82, cth: 41, blk: 43, tck: 77, cov: 56, prh: 80},
                Player{name: "Malik Crowder", pos: "DL", num: 99, hgt: 76, wgt: 293, spd: 69, thr: 32, str: 80, cth: 40, blk: 45, tck: 75, cov: 56, prh: 78},
                Player{name: "Javon Redding", pos: "LB", num: 48, hgt: 71, wgt: 244, spd: 80, thr: 35, str: 74, cth: 57, blk: 53, tck: 73, cov: 63, prh: 69},
                Player{name: "Kyler Benson", pos: "CB", num: 23, hgt: 72, wgt: 193, spd: 87, thr: 33, str: 66, cth: 62, blk: 44, tck: 63, cov: 81, prh: 44},
                Player{name: "Jalen Cross", pos: "CB", num: 19, hgt: 68, wgt: 185, spd: 89, thr: 34, str: 64, cth: 60, blk: 41, tck: 61, cov: 79, prh: 42}],
    };
    let team4 = Team {
        id: 4,
        name: "Midland Covenant",
        mascot: "Crusaders",
        city: "Midland Springs",
        state: "IN",
        prestige: 4,
        roster: [Player{name: "Tanner McElroy", pos: "QB", num: 14, hgt: 75, wgt: 209, spd: 74, thr: 83, str: 66, cth: 61, blk: 55, tck: 31, cov: 26, prh: 20},
                Player{name: "Malik Sorrell", pos: "RB", num: 27, hgt: 69, wgt: 193, spd: 85, thr: 42, str: 61, cth: 71, blk: 57, tck: 34, cov: 21, prh: 18},
                Player{name: "RJ Burton", pos: "WR", num: 88, hgt: 71, wgt: 192, spd: 81, thr: 40, str: 60, cth: 79, blk: 42, tck: 27, cov: 23, prh: 22},
                Player{name: "Dante Greer", pos: "OL", num: 67, hgt: 75, wgt: 295, spd: 56, thr: 27, str: 80, cth: 48, blk: 84, tck: 38, cov: 21, prh: 24},
                Player{name: "Noah Kealani", pos: "OL", num: 78, hgt: 78, wgt: 316, spd: 57, thr: 26, str: 78, cth: 45, blk: 82, tck: 35, cov: 22, prh: 24},
                Player{name: "Micah St. James", pos: "DL", num: 90, hgt: 72, wgt: 300, spd: 66, thr: 30, str: 78, cth: 39, blk: 40, tck: 72, cov: 51, prh: 78},
                Player{name: "Jonah Elridge", pos: "DL", num: 95, hgt: 72, wgt: 294, spd: 64, thr: 31, str: 75, cth: 37, blk: 42, tck: 70, cov: 50, prh: 75},
                Player{name: "Ellis McCray", pos: "LB", num: 41, hgt: 75, wgt: 233, spd: 77, thr: 33, str: 70, cth: 56, blk: 48, tck: 70, cov: 66, prh: 64},
                Player{name: "Nolan DeWitt", pos: "CB", num: 1, hgt: 73, wgt: 194, spd: 84, thr: 32, str: 62, cth: 58, blk: 40, tck: 59, cov: 77, prh: 39},
                Player{name: "Trent Solano", pos: "CB", num: 7, hgt: 72, wgt: 186, spd: 82, thr: 31, str: 60, cth: 56, blk: 38, tck: 58, cov: 74, prh: 38}],
    };
    let team5 = Team {
        id: 5,
        name: "Northshore Institute",
        mascot: "Sabercats",
        city: "Northshore",
        state: "MN",
        prestige: 9,
        roster: [Player{name: "Jett Corbin", pos: "QB", num: 12, hgt: 75, wgt: 235, spd: 90, thr: 93, str: 77, cth: 71, blk: 64, tck: 40, cov: 34, prh: 28},
                Player{name: "Tylan Nwoko", pos: "RB", num: 24, hgt: 69, wgt: 205, spd: 94, thr: 48, str: 76, cth: 82, blk: 71, tck: 45, cov: 30, prh: 26},
                Player{name: "Devon Lattimore", pos: "WR", num: 18, hgt: 72, wgt: 183, spd: 98, thr: 42, str: 71, cth: 90, blk: 56, tck: 37, cov: 34, prh: 25},
                Player{name: "Jeremiah Ricks", pos: "OL", num: 74, hgt: 80, wgt: 308, spd: 75, thr: 32, str: 93, cth: 58, blk: 95, tck: 51, cov: 30, prh: 32},
                Player{name: "Beau Chevallier", pos: "OL", num: 79, hgt: 75, wgt: 326, spd: 68, thr: 32, str: 90, cth: 55, blk: 93, tck: 49, cov: 30, prh: 32},
                Player{name: "Roman Maddox", pos: "DL", num: 96, hgt: 76, wgt: 261, spd: 78, thr: 35, str: 89, cth: 47, blk: 48, tck: 88, cov: 68, prh: 91},
                Player{name: "Jahil Copeland", pos: "DL", num: 92, hgt: 73, wgt: 291, spd: 86, thr: 36, str: 87, cth: 46, blk: 49, tck: 85, cov: 66, prh: 88},
                Player{name: "Chance Hollaway", pos: "LB", num: 52, hgt: 75, wgt: 260, spd: 86, thr: 39, str: 82, cth: 69, blk: 62, tck: 84, cov: 79, prh: 76},
                Player{name: "Da'Ron Silas", pos: "CB", num: 9, hgt: 69, wgt: 205, spd: 93, thr: 36, str: 72, cth: 74, blk: 50, tck: 74, cov: 91, prh: 56}, 
                Player{name: "KJ Ramsey", pos: "CB", num: 1, hgt: 69, wgt: 177, spd: 91, thr: 35, str: 70, cth: 72, blk: 48, tck: 71, cov: 89, prh: 54}],
    };
    let team6 = Team {
        id: 6,
        name: "Echo Valley",
        mascot: "Wranglers",
        city: "Echo Valley",
        state: "WY",
        prestige: 3,
        roster: [Player{name: "Colt Abernathy", pos: "QB", num: 16, hgt: 73, wgt: 223, spd: 71, thr: 79, str: 64, cth: 58, blk: 52, tck: 29, cov: 24, prh: 19},
                Player{name: "Shane Fenwick", pos: "RB", num: 28, hgt: 73, wgt: 220, spd: 82, thr: 40, str: 58, cth: 66, blk: 54, tck: 32, cov: 19, prh: 18},
                Player{name: "Theo Coltrane", pos: "WR", num: 83, hgt: 71, wgt: 199, spd: 84, thr: 39, str: 57, cth: 74, blk: 40, tck: 24, cov: 21, prh: 17},
                Player{name: "Brody Callahan", pos: "OL", num: 66, hgt: 75, wgt: 308, spd: 54, thr: 26, str: 75, cth: 45, blk: 79, tck: 35, cov: 20, prh: 18},
                Player{name: "Wyatt Holt", pos: "OL", num: 73, hgt: 74, wgt: 314, spd: 55, thr: 25, str: 73, cth: 43, blk: 76, tck: 32, cov: 20, prh: 18},
                Player{name: "Hunter Gage", pos: "DL", num: 94, hgt: 77, wgt: 305, spd: 62, thr: 29, str: 73, cth: 36, blk: 38, tck: 66, cov: 46, prh: 70},
                Player{name: "Kyle Riggins", pos: "DL", num: 98, hgt: 74, wgt: 302, spd: 61, thr: 28, str: 72, cth: 35, blk: 38, tck: 65, cov: 44, prh: 69},
                Player{name: "Reece Donnelly", pos: "LB", num: 45, hgt: 76, wgt: 255, spd: 74, thr: 31, str: 66, cth: 53, blk: 45, tck: 64, cov: 54, prh: 58},
                Player{name: "Jaire Wardell", pos: "CB", num: 20, hgt: 70, wgt: 204, spd: 80, thr: 29, str: 56, cth: 55, blk: 37, tck: 52, cov: 70, prh: 34},
                Player{name: "Camdin Fox", pos: "CB", num: 6, hgt: 69, wgt: 190, spd: 78, thr: 29, str: 55, cth: 54, blk: 35, tck: 51, cov: 68, prh: 32}],
    };
    let team7 = Team {
        id: 7,
        name: "Cobalt Hills",
        mascot: "Aviators",
        city: "Cobalt Hills",
        state: "CO",
        prestige: 7,
        roster: [Player{name: "Byce Kavanagh", pos: "QB", num: 11, hgt: 74, wgt: 200, spd: 78, thr: 89, str: 72, cth: 67, blk: 60, tck: 36, cov: 30, prh: 26},
                Player{name: "Amir Lockhart", pos: "RB", num: 21, hgt: 70, wgt: 214, spd: 98, thr: 45, str: 70, cth: 79, blk: 67, tck: 41, cov: 28, prh: 24},
                Player{name: "Kael Thompkins", pos: "WR", num: 82, hgt: 74, wgt: 182, spd: 92, thr: 41, str: 65, cth: 85, blk: 52, tck: 33, cov: 29, prh: 22},
                Player{name: "Nolan Jeffries", pos: "OL", num: 68, hgt: 77, wgt: 308, spd: 62, thr: 29, str: 87, cth: 53, blk: 91, tck: 45, cov: 25, prh: 27},
                Player{name: "Victor Manzano", pos: "OL", num: 76, hgt: 74, wgt: 290, spd: 64, thr: 28, str: 85, cth: 50, blk: 89, tck: 42, cov: 24, prh: 26},
                Player{name: "Cole Drummond", pos: "DL", num: 93, hgt: 72, wgt: 269, spd: 73, thr: 32, str: 83, cth: 42, blk: 44, tck: 81, cov: 60, prh: 84},
                Player{name: "Elijah Boone", pos: "DL", num: 97, hgt: 75, wgt: 300, spd: 70, thr: 31, str: 82, cth: 41, blk: 45, tck: 79, cov: 58, prh: 82},
                Player{name: "Taj Middleton", pos: "LB", num: 47, hgt: 76, wgt: 245, spd: 82, thr: 36, str: 76, cth: 65, blk: 55, tck: 77, cov: 68, prh: 70},
                Player{name: "Dorian Westfall", pos: "CB", num: 4, hgt: 73, wgt: 185, spd: 88, thr: 34, str: 67, cth: 69, blk: 46, tck: 66, cov: 85, prh: 48},
                Player{name: "Marcus Devine", pos: "CB", num: 29, hgt: 72, wgt: 190, spd: 86, thr: 33, str: 65, cth: 67, blk: 44, tck: 64, cov: 83, prh: 47}],
    };
    let team8 = Team {
        id: 8,
        name: "Frostpine University",
        mascot: "Yetis", 
        city: "Frostpine",
        state: "AK",
        prestige: 2,
        roster: [Player{name: "Travis Kinloch", pos: "QB", num: 13, hgt: 77, wgt: 207, spd: 70, thr: 77, str: 62, cth: 56, blk: 50, tck: 28, cov: 22, prh: 18},
                Player{name: "Colby Harvin", pos: "RB", num: 32, hgt: 68, wgt: 203, spd: 80, thr: 39, str: 56, cth: 64, blk: 51, tck: 30, cov: 18, prh: 17},
                Player{name: "Javon Flint", pos: "WR", num: 84, hgt: 72, wgt: 188, spd: 84, thr: 37, str: 55, cth: 72, blk: 39, tck: 23, cov: 20, prh: 16},
                Player{name: "Tyler Deacon", pos: "OL", num: 60, hgt: 80, wgt: 292, spd: 52, thr: 25, str: 73, cth: 44, blk: 77, tck: 34, cov: 20, prh: 16},
                Player{name: "Clay Dunst", pos: "OL", num: 71, hgt: 80, wgt: 300, spd: 53, thr: 24, str: 71, cth: 42, blk: 75, tck: 32, cov: 18, prh: 16},
                Player{name: "Ridge Temple", pos: "DL", num: 92, hgt: 73, wgt: 298, spd: 60, thr: 27, str: 70, cth: 34, blk: 35, tck: 63, cov: 43, prh: 67},
                Player{name: "Makoa Velez", pos: "DL", num: 99, hgt: 72, wgt: 270, spd: 59, thr: 27, str: 69, cth: 33, blk: 36, tck: 61, cov: 42, prh: 66},
                Player{name: "Hunter Fife", pos: "LB", num: 44, hgt: 70, wgt: 237, spd: 72, thr: 30, str: 64, cth: 52, blk: 42, tck: 62, cov: 50, prh: 55},
                Player{name: "Isaiah Treadwell", pos: "CB", num: 3, hgt: 73, wgt: 180, spd: 78, thr: 28, str: 54, cth: 54, blk: 34, tck: 50, cov: 68, prh: 33},
                Player{name: "Nickei Lawton", pos: "CB", num: 25, hgt: 74, wgt: 190, spd: 76, thr: 28, str: 53, cth: 52, blk: 33, tck: 49, cov: 66, prh: 32}],
    };
    let team9 = Team {
        id: 9,
        name: "Western Bluffs",
        mascot: "Stormcallers",
        city: "Western Bluffs",
        state: "OR",
        prestige: 6,
        roster: [Player{name: "Eli Weatherford", pos: "QB", num: 10, hgt: 73, wgt: 231, spd: 76, thr: 87, str: 70, cth: 65, blk: 58, tck: 35, cov: 29, prh: 24},
                Player{name: "Damien Lovette", pos: "RB", num: 26, hgt: 69, wgt: 215, spd: 88, thr: 44, str: 67, cth: 76, blk: 63, tck: 39, cov: 26, prh: 22},
                Player{name: "Zaylen Branch", pos: "WR", num: 85, hgt: 75, wgt: 212, spd: 89, thr: 40, str: 63, cth: 83, blk: 48, tck: 31, cov: 27, prh: 21},
                Player{name: "Trent Halvorsen", pos: "OL", num: 63, hgt: 80, wgt: 294, spd: 60, thr: 28, str: 83, cth: 50, blk: 87, tck: 41, cov: 23, prh: 24},
                Player{name: "Marcus Calloway", pos: "OL", num: 72, hgt: 78, wgt: 321, spd: 61, thr: 28, str: 82, cth: 49, blk: 86, tck: 40, cov: 22, prh: 24},
                Player{name: "DeAndre Kincaid", pos: "DL", num: 90, hgt: 72, wgt: 278, spd: 69, thr: 30, str: 80, cth: 39, blk: 42, tck: 76, cov: 55, prh: 79},
                Player{name: "Ethan Strong", pos: "DL", num: 95, hgt: 72, wgt: 278, spd: 68, thr: 30, str: 79, cth: 38, blk: 43, tck: 74, cov: 53, prh: 77},
                Player{name: "Holden Knight", pos: "LB", num: 53, hgt: 76, wgt: 259, spd: 80, thr: 34, str: 72, cth: 63, blk: 51, tck: 74, cov: 63, prh: 66},
                Player{name: "Jarius Harper", pos: "CB", num: 7, hgt: 70, wgt: 175, spd: 86, thr: 32, str: 61, cth: 68, blk: 42, tck: 60, cov: 80, prh: 44},
                Player{name: "Silas Van Dorn", pos: "CB", num: 22, hgt: 74, wgt: 186, spd: 84, thr: 31, str: 60, cth: 66, blk: 41, tck: 58, cov: 78, prh: 42}],
    };
    let teams = [team1, team2, team3, team4, team5, team6, team7, team8, team9, team0];
    teams 
}

impl std::fmt::Display for Team {
    fn fmt(&self, fmt: &mut std::fmt::Formatter<'_>) -> fmt::Result {
        write!(fmt, "Team: {}, ({}, {}), {}",
        self.name, self.city, self.state, self.prestige)
    }
}

fn create_schedule() -> [[i32; 10]; 10] {
    let mut schedule : [[i32; 10]; 10] = [[0; 10]; 10];
    let num_teams = 10;
    let mut rng = rand::rng();
    //let anchor = rng.random_range(0..10);
    let anchor = 0;
    let mut team_ptr = anchor + 1;
    println!("{anchor}");
    println!("{team_ptr}");
    let week = 0;
    //for week in 0..9 {
        //if team_ptr == (anchor as i32) {
        //    continue;
        //} 
        if team_ptr == 10 {
            team_ptr = 0;
        }
        schedule[anchor as usize][week] = team_ptr;
        schedule[team_ptr as usize][week] = anchor as i32;
        let mut ptr1 = team_ptr + 1;
        let mut ptr2 = team_ptr - 1;
        for i in 0..5 {
            if ptr1 >= 10 {
                ptr1 = ptr1 - 10;
            }
            if ptr1 == anchor {
                ptr1 = if (anchor == 9) { 0 } else {ptr1 + 1};
            }
            if ptr2 <= -1 {
                ptr2 = 10 + ptr2;
                //println!("hit under 0: {ptr2}");
            }
            if ptr2 == anchor {
                ptr2 = if anchor == 0 { 9 } else { ptr2 - 1 };
                //println!("hit ptr2 == anchor: {ptr2}");
            }
            print!("ptr1: {ptr1}, ptr2: {ptr2} ");
            schedule[ptr1 as usize][week] = ptr2;    
            schedule[ptr2 as usize][week] = ptr1;
            ptr1 += i;
            ptr2 -= i;
        }
        println!("");
        team_ptr += 1;
    //} 
    schedule
}

fn main() {
    let teams = create_teams();
    let mut i = 0;
    let schedule = create_schedule();
    for e in schedule {
        print!("{i} ");
        for elem in e {
            print!("{elem}, ");
        }
        println!("");
        i += 1;
    }
    i = 0;
    for e in teams {
        println!("{i}: {e}");
        i+=1;
    }
}
