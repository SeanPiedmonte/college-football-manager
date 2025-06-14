use std::fmt;

/*
* Player is a file looking to handle the creation of players for teams in
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
        write!(fmt, "Player {{ name: {}, num: {}, spd: {}, thr: {}, str: {}, cth: {}, tck: {}, cov: {}, prh: {}, blk: {} }}",
        self.name, self.num, self.spd, self.thr, self.str, self.cth, self.tck, self.cov, self.prh, self.blk)
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
pub fn create_player(name: &'static str, num : i32, spd : i32, thr : i32, 
        str : i32, cth : i32, tck : i32, cov : i32, prh : i32, blk : i32) -> Player {
    let new_player = Player {
        name,
        num,
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


