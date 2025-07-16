#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

/*
 * error_message
 *
 * parameters
 * string message: Error message to be sent
 *
 * return: void
 *
 * Basic Error message for memory allocations
 *
 */
void error_message(string message) {
    cout << message << endl;
}


/*
* Player is a struct looking to handle the creation of players for teams in
* the context of college football manager. Player will have the following
* attributes.
*
* name: This is the first and last name of the player
* pos : Player Position
* hgt : Player Height
* wgt : Player Weight
* num : Player Number
* spd : Player Speed
* thr : Player Passing Rating
* str : Player Strength
* cth : Player Catching
* tck : Player Tackling Rating
* cov : Player Coverage Rating
* prh : Player Pass Rushing Rating
* blk : Player Blocking Rating
*/
struct Player {
    std::string name;
    std::string pos;
    int num;
    int hgt;
    int wgt;
    int spd;
    int thr;
    int str;
    int cth;
    int blk;
    int tck;
    int cov;
    int prh;
};

/*
* create_base_roster
* parameters: None
* returns: struct *Player
*
* Create base roster creates an initialized array of 0 overall players
* Use to overwrite with valid players
*/
struct Player *create_base_roster() {
    struct Player base_player = {"John Doe", "P", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    struct Player *base_roster = (struct Player*)malloc(sizeof(struct Player) * 10);
    if (base_roster == NULL) {
        error_message("func::create_base_roster, Could Not Allocate base_roster");
        return NULL;
    }
    
    for (int i = 0; i < 10; i++) {
         base_roster[i] = base_player;
    }

    return base_roster;
}

/*
* create_player
* parameters: std::string, std::string, int, int, int, int, int, int, int, int, int, int, int
*
* returns struct Player
*
* Creates a player with all of the parameters needed to create a valid player
* struct. Use to append players to rosters.
*/
struct Player *create_player(string name, string pos, int num, int hgt, int wgt,
                             int spd, int thr, int str, int blk, int cth, int tck, 
                             int cov, int prh) 
{
    struct Player *new_player = (struct Player *)malloc(sizeof(struct Player));
    if (new_player == NULL) {
        error_message("func::create_player, could not allocate new_player");
        return NULL;
    }
    new_player->name = name;
    new_player->pos = pos;
    new_player->hgt = hgt;
    new_player->wgt = wgt;
    new_player->num = num;
    new_player->spd = spd;
    new_player->thr = thr;
    new_player->str = str;
    new_player->cth = cth;
    new_player->tck = tck;
    new_player->cov = cov;
    new_player->prh = prh;
    new_player->blk = blk;

    return new_player;
}

/*
* The Team struct will seek to create and manage our team. This will have the
* team names, location, roster, and prestige.
*
* id: int
* name: std::string
* mascot: std::string
* city: std::string
* state: std::string
* prestige: int
* roster: struct Player[10]
*/
struct Team {
    int id;
    string name;
    string mascot;
    string city;
    string state;
    int prestige;
    struct Player roster[10];
};

/*
* create_teams
*
* parameters: None
*
* returns: struct Team *
*
* creates a generic set of teams
*/
struct Team *create_teams() {
    struct Team *teams = (struct Team *)malloc(sizeof(struct Team) * 10);
    if (teams == NULL) {
        error_message("func::create_teams, could not allocate the teams array");
        return NULL;
    }
    struct Team team0 = {0, "Ironwood State", "ThunderHawks", "Ironwood Falls",
                         "MT", 7, {}};
    team0.roster[0] = {"Colt Masters", "QB", 12, 74, 228, 78, 92, 72, 65, 58, 35, 30, 25};
    team0.roster[1] = {"DeShawn Rucker", "RB", 25, 70, 210, 91, 45, 68, 79, 62, 38, 25, 25};
    team0.roster[2] = {"Wyatt Hagan", "WR", 87, 71, 207, 89, 42, 60, 85, 45, 30, 28, 18};
    team0.roster[3] = {"Boone Callahan", "OL", 70, 80, 335, 60, 30, 88, 50, 90, 40, 22, 20};
    team0.roster[4] = {"Eli Tupuola", "OL", 74, 78, 315, 58, 28, 92, 47, 91, 42, 20, 22};
    team0.roster[5] = {"Trent Moore", "DL", 91, 77, 274, 72, 30, 90, 35, 40, 87, 55, 89};
    team0.roster[6] = {"Jalen Bass", "DL", 96, 73, 307, 74, 33, 85, 40, 42, 84, 52, 86};
    team0.roster[7] = {"Tyrese Vann", "LB", 52, 72, 244, 82, 35, 75, 65, 48, 78, 72, 75};
    team0.roster[8] = {"Quincy Starks", "CB", 24, 73, 180, 90, 34, 67, 70, 41, 65, 88, 45};
    team0.roster[9] = {"Lane Hollowell", "CB", 29, 68, 203, 87, 31, 66, 73, 40, 63, 85, 48};
    
    teams[0] = team0;
    struct Team team1 {1, "Lakeview Maritime", "Tridents", "Lakeview Shores", 
                       "ME", 5, {}
                      };
    team1.roster[0] = {"Silas Mercer", "QB", 9, 77, 202, 76, 86, 68, 62, 58, 32, 25, 20};
    team1.roster[1] = {"Niko Santiago", "RB", 21, 69, 215, 88, 44,  64, 74,  59, 35, 20, 18};
    team1.roster[2] = {"Blake Carson", "WR", 11, 74, 195, 84, 41, 61, 81, 44, 28, 25, 22};
    team1.roster[3] = {"Marcus Van Fleet", "OL", 68, 77, 297, 59, 30, 84, 50, 88, 39, 20, 24};
    team1.roster[4] = {"Finn Malachy", "OL", 72, 78, 299, 61, 28, 79, 48, 83, 39, 21, 24};
    team1.roster[5] = {"Dmitri Kalani", "DL", 98, 78, 285, 70, 30, 81, 42, 40, 79, 50, 78};
    team1.roster[6] = {"Logan Bremmer", "DL", 94, 78, 262, 66, 32, 77, 38, 42, 74, 52, 75};
    team1.roster[7] = {"Cairo Willis", "LB", 43, 71, 224, 78, 36, 72, 53, 50, 72, 66, 64};
    team1.roster[8] = {"Jace Lowenthal", "CB", 8, 73, 176, 85, 34, 65, 69, 41, 61, 80, 42};
    team1.roster[9] = {"Shane Kealoha", "CB", 29, 72, 191, 88, 33, 63, 67, 39, 60, 78, 40};
    teams[1] = team1;
    
    struct Team team2 {2, "Red Ridge Tech", "Vortex", "Red Ridge", "NV", 8, {}};
    team2.roster[0] = {"Daxen Reyes", "QB", 5, 77, 224, 80, 90, 74, 68, 62, 38, 32, 28};
    team2.roster[1] = {"Zahir Moreland", "RB", 22, 73, 220, 92, 46, 72, 78, 66, 41, 28, 25};
    team2.roster[2] = {"Elias Holt", "WR", 11, 70, 181, 89, 40, 67, 87, 50, 34, 30, 22};
    team2.roster[3] = {"Royce Daley", "OL", 71, 80, 310, 63, 40, 91, 54, 93, 47, 25, 30};
    team2.roster[4] = {"Koen Toma", "OL", 77, 76, 306, 66, 29, 89, 51, 90, 45, 24, 28};
    team2.roster[5] = {"Malik Durham", "DL", 97, 74, 269, 75, 34, 87, 44, 45, 86, 62, 88};
    team2.roster[6] = {"Jonah Gentry", "DL", 92, 78, 266, 72, 33, 86, 43, 46, 82, 60, 84};
    team2.roster[7] = {"Tyshon Renner", "LB", 44, 76, 228, 84, 38, 78, 61, 58, 81, 74, 72};
    team2.roster[8] = {"Kyrie Nesbit", "CB", 3, 72, 178, 91, 35, 70, 76, 46, 70, 89, 50};
    team2.roster[9] = {"Cruz Whitman", "CB", 6, 71, 175, 88, 32, 68, 67, 42, 68, 87, 52};
    teams[2] = team2;

    struct Team team3 = {3, "Praire Forge", "Miners", "Praire Forge", "KS", 6, {}};
    team3.roster[0] = {"Silas Mercer", "QB", 9, 77, 203, 76, 86, 68, 62, 58, 32, 25, 20};
    team3.roster[1] = {"Niko Santiago", "RB", 21, 74, 223, 88, 44, 64, 74, 59, 35, 20, 18};
    team3.roster[2] = {"Blake Carson", "WR", 11, 73, 217, 84, 41, 63, 82, 46, 29, 26, 20};
    team3.roster[3] = {"Marcus Bellamy", "OL", 65, 76, 290, 60, 29, 85, 52, 89, 42, 23, 26};
    team3.roster[4] = {"Xavier Hicks", "OL", 75, 75, 292, 58, 28, 83, 50, 86, 42, 23, 24};
    team3.roster[5] = {"Cole Vickers", "DL", 93, 78, 300, 71, 31, 82, 41, 43, 77, 56, 80};
    team3.roster[6] = {"Malik Crowder", "DL", 99, 76, 293, 69, 32, 80, 40, 45, 75, 56, 78};
    team3.roster[7] = {"Javon Redding", "LB", 48, 71, 244, 80, 35, 74, 57, 53, 73, 63, 69};
    team3.roster[8] = {"Kyler Benson", "CB", 23, 72, 193, 87, 33, 66, 62, 44, 63, 81, 44};
    team3.roster[9] = {"Jalen Cross", "CB", 19, 68, 185, 89, 34, 64, 60, 41, 61, 79, 42};
    teams[3] = team3;

    struct Team team4 = {4, "Midland Covenant", "Crusaders", "Midland Springs", "IN", 4, {}};
    team4.roster[0] = {"Tanner McElroy", "QB", 14, 75, 209, 74, 83, 66, 61, 55, 31, 26, 20};
    team4.roster[1] = {"Malik Sorrell", "RB", 27, 69, 193, 85, 42, 61, 71, 57, 34, 21, 18};
    team4.roster[2] = {"RJ Burton", "WR", 88, 71, 192, 81, 40, 60, 79, 42, 27, 23, 22};
    team4.roster[3] = {"Dante Greer", "OL", 67, 75, 295, 56, 27, 80, 48, 84, 38, 21, 24};
    team4.roster[4] = {"Noah Kealani", "OL", 78, 78, 316, 57, 26, 78, 45, 82, 35, 22, 24};
    team4.roster[5] = {"Micah St. James", "DL", 90, 72, 300, 66, 30, 78, 39, 40, 72, 51, 78};
    team4.roster[6] = {"Jonah Elridge", "DL", 95, 72, 294, 64, 31, 75, 37, 42, 70, 50, 75};
    team4.roster[7] = {"Ellis McCray", "LB", 41, 75, 233, 77, 33, 70, 56, 48, 70, 66, 64};
    team4.roster[8] = {"Nolan DeWitt", "CB", 1, 73, 194, 84, 32, 62, 58, 40, 59, 77, 39};
    team4.roster[9] = {"Trent Solano", "CB", 7, 72, 186, 82, 31, 60, 56, 38, 58, 74, 38};
    teams[4] = team4;

    struct Team team5 = {5, "Northshore Institute", "Sabercats", "Northshore", "MN", 9, {}};
    team5.roster[0] = {"Jett Corbin", "QB", 12, 75, 235, 90, 93, 77, 71, 64, 40, 34, 28};
    team5.roster[1] = {"Tylan Nwoko", "RB", 24, 69, 205, 94, 48, 76, 82, 71, 45, 30, 26};
    team5.roster[2] = {"Devon Lattimore", "WR", 18, 72, 183, 98, 42, 71, 90, 56, 37, 34, 25};
    team5.roster[3] = {"Jeremiah Ricks", "OL", 74, 80, 308, 75, 32, 93, 58, 95, 51, 30, 32};
    team5.roster[4] = {"Beau Chevallier", "OL", 79, 75, 326, 68, 32, 90, 55, 93, 49, 30, 32};
    team5.roster[5] = {"Roman Maddox", "DL", 96, 76, 261, 78, 35, 89, 47, 48, 88, 68, 91};
    team5.roster[6] = {"Jahil Copeland", "DL", 92, 73, 291, 86, 36, 87, 46, 49, 85, 66, 88};
    team5.roster[7] = {"Chance Hollaway", "LB", 52, 75, 260, 86, 39, 82, 69, 62, 84, 79, 76};
    team5.roster[8] = {"Da'Ron Silas", "CB", 9, 69, 205, 93, 36, 72, 74, 50, 74, 91, 56}; 
    team5.roster[9] = {"KJ Ramsey", "CB", 1, 69, 177, 91, 35, 70, 72, 48, 71, 89, 54};
    teams[5] = team5;

    struct Team team6 = {6, "Echo Valley", "Wranglers", "Echo Valley", "WY", 3, {}};
    team6.roster[0] = {"Colt Abernathy", "QB", 16, 73, 223, 71, 79, 64, 58, 52, 29, 24, 19};
    team6.roster[1] = {"Shane Fenwick", "RB", 28, 73, 220, 82, 40, 58, 66, 54, 32, 19, 18};
    team6.roster[2] = {"Theo Coltrane", "WR", 83, 71, 199, 84, 39, 57, 74, 40, 24, 21, 17};
    team6.roster[3] = {"Brody Callahan", "OL", 66, 75, 308, 54, 26, 75, 45, 79, 35, 20, 18};
    team6.roster[4] = {"Wyatt Holt", "OL", 73, 74, 314, 55, 25, 73, 43, 76, 32, 20, 18};
    team6.roster[5] = {"Hunter Gage", "DL", 94, 77, 305, 62, 29, 73, 36, 38, 66, 46, 70};
    team6.roster[6] = {"Kyle Riggins", "DL", 98, 74, 302, 61, 28, 72, 35, 38, 65, 44, 69};
    team6.roster[7] = {"Reece Donnelly", "LB", 45, 76, 255, 74, 31, 66, 53, 45, 64, 54, 58};
    team6.roster[8] = {"Jaire Wardell", "CB", 20, 70, 204, 80, 29, 56, 55, 37, 52, 70, 34};
    team6.roster[9] = {"Camdin Fox", "CB", 6, 69, 190, 78, 29, 55, 54, 35, 51, 68, 32};
    teams[6] = team6;

    struct Team team7 = {7, "Cobalt Hills", "Aviators", "Cobalt Hills", "CO", 7, {}};
    team7.roster[0] = {"Byce Kavanagh", "QB", 11, 74, 200, 78, 89, 72, 67, 60, 36, 30, 26};
    team7.roster[1] = {"Amir Lockhart", "RB", 21, 70, 214, 98, 45, 70, 79, 67, 41, 28, 24};
    team7.roster[2] = {"Kael Thompkins", "WR", 82, 74, 182, 92, 41, 65, 85, 52, 33, 29, 22};
    team7.roster[3] = {"Nolan Jeffries", "OL", 68, 77, 308, 62, 29, 87, 53, 91, 45, 25, 27};
    team7.roster[4] = {"Victor Manzano", "OL", 76, 74, 290, 64, 28, 85, 50, 89, 42, 24, 26};
    team7.roster[5] = {"Cole Drummond", "DL", 93, 72, 269, 73, 32, 83, 42, 44, 81, 60, 84};
    team7.roster[6] = {"Elijah Boone", "DL", 97, 75, 300, 70, 31, 82, 41, 45, 79, 58, 82};
    team7.roster[7] = {"Taj Middleton", "LB", 47, 76, 245, 82, 36, 76, 65, 55, 77, 68, 70};
    team7.roster[8] = {"Dorian Westfall", "CB", 4, 73, 185, 88, 34, 67, 69, 46, 66, 85, 48};
    team7.roster[9] = {"Marcus Devine", "CB", 29, 72, 190, 86, 33, 65, 67, 44, 64, 83, 47};
    teams[7] = team7;

    struct Team team8 = {8, "Frostpine University","Yetis", "Frostpine", "AK", 2, {}};
    team8.roster[0] = {"Travis Kinloch", "QB", 13, 77, 207, 70, 77, 62, 56, 50, 28, 22, 18};
    team8.roster[1] = {"Colby Harvin", "RB", 32, 68, 203, 80, 39, 56, 64, 51, 30, 18, 17};
    team8.roster[2] = {"Javon Flint", "WR", 84, 72, 188, 84, 37, 55, 72, 39, 23, 20, 16};
    team8.roster[3] = {"Tyler Deacon", "OL", 60, 80, 292, 52, 25, 73, 44, 77, 34, 20, 16};
    team8.roster[4] = {"Clay Dunst", "OL", 71, 80, 300, 53, 24, 71, 42, 75, 32, 18, 16};
    team8.roster[5] = {"Ridge Temple", "DL", 92, 73, 298, 60, 27, 70, 34, 35, 63, 43, 67};
    team8.roster[6] = {"Makoa Velez", "DL", 99, 72, 270, 59, 27, 69, 33, 36, 61, 42, 66};
    team8.roster[7] = {"Hunter Fife", "LB", 44, 70, 237, 72, 30, 64, 52, 42, 62, 50, 55};
    team8.roster[8] = {"Isaiah Treadwell", "CB", 3, 73, 180, 78, 28, 54, 54, 34, 50, 68, 33};
    team8.roster[9] = {"Nickei Lawton", "CB", 25, 74, 190, 76, 28, 53, 52, 33, 49, 66, 32};
    teams[8] = team8;

    struct Team team9 = {9, "Western Bluffs", "Stormcallers", "Western Bluffs", "OR", 6, {}};
    team9.roster[0] = {"Eli Weatherford", "QB", 10, 73, 231, 76, 87, 70, 65, 58, 35, 29, 24};
    team9.roster[1] = {"Damien Lovette", "RB", 26, 69, 215, 88, 44, 67, 76, 63, 39, 26, 22};
    team9.roster[2] = {"Zaylen Branch", "WR", 85, 75, 212, 89, 40, 63, 83, 48, 31, 27, 21};
    team9.roster[3] = {"Trent Halvorsen", "OL", 63, 80, 294, 60, 28, 83, 50, 87, 41, 23, 24};
    team9.roster[4] = {"Marcus Calloway", "OL", 72, 78, 321, 61, 28, 82, 49, 86, 40, 22, 24};
    team9.roster[5] = {"DeAndre Kincaid", "DL", 90, 72, 278, 69, 30, 80, 39, 42, 76, 55, 79};
    team9.roster[6] = {"Ethan Strong", "DL", 95, 72, 278, 68, 30, 79, 38, 43, 74, 53, 77};
    team9.roster[7] = {"Holden Knight", "LB", 53, 76, 259, 80, 34, 72, 63, 51, 74, 63, 66};
    team9.roster[8] = {"Jarius Harper", "CB", 7, 70, 175, 86, 32, 61, 68, 42, 60, 80, 44};
    team9.roster[9] = {"Silas Van Dorn", "CB", 22, 74, 186, 84, 31, 60, 66, 41, 58, 78, 42};
    teams[9] = team9;

    return teams;
}

typedef int schedule[10][10];
/*
* create_schedule
*
* parameters: None
*
* returns: schedule*
*
* creates a 10 week schedule for 10 teams
* and returns a 2d array pointer to the matchups
*/
schedule *create_schedule() {
    // to do
    return NULL;
}

int main(void) {
    struct Team *teams = create_teams();

    for (int j = 0; j < 10; j++) {
        cout << "city: " << teams[j].city << ", ";
        cout << "id: " << teams[j].id << ", ";
        cout << "mascot: " << teams[j].mascot << ", ";
        cout << "name: " << teams[j].name << ", ";
        cout << "state: " << teams[j].state << ", ";
        cout << "prestige " << teams[j].prestige << endl;
        for (int i = 0; i < 10; i++) {
            cout << "name: " << teams[j].roster[i].name << ", ";
            cout << "pos: " << teams[j].roster[i].pos << ", ";
            cout << "hgt: " << teams[j].roster[i].hgt << ", ";
            cout << "wgt: " << teams[j].roster[i].wgt << ", ";
            cout << "spd: " << teams[j].roster[i].spd << ", ";
            cout << "thr: " << teams[j].roster[i].thr << ", ";
            cout << "str: " << teams[j].roster[i].str << ", ";
            cout << "cth: " << teams[j].roster[i].cth << ", ";
            cout << "blk: " << teams[j].roster[i].blk << ", ";
            cout << "tck: " << teams[j].roster[i].tck << ", ";
            cout << "cov: " << teams[j].roster[i].cov << ", ";
            cout << "prh: " << teams[j].roster[i].prh << endl;
        }
    }
}
