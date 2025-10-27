#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <SDL.h>
#include "SDL_render.h"
#include "SDL_video.h"
#include "rosters.h"

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
    int id;
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
    struct Player base_player = {0, "John Doe", "P", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
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
void create_player(struct Player *new_player, int id, string name, string pos, int num, int hgt, int wgt,
                             int spd, int thr, int str, int blk, int cth, int tck, 
                             int cov, int prh) 
{
    new_player->id = id;
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
* Utilizes a round robin algorithm to create the matchups with teams getting
* a bye in the final week designated by -1
*/
void create_schedule(schedule sch) {
    srand(time(0));
    int anchor = rand() % 10;
    int team_ptr = anchor + 1;
    printf("anchor: %d, team_ptr: %d\n", anchor, team_ptr);
    if (team_ptr == 10)
    {
        team_ptr = 0;
    }
    for (int week = 0; week < 10 && team_ptr != anchor; week++) {
        if (team_ptr == 10) {
            team_ptr = 0 == anchor ? 1 : 0;
        }
        sch[anchor][week] = team_ptr;
        sch[team_ptr][week] = anchor;
        printf("team_ptr: %d\n", team_ptr);
        int ptr1 = team_ptr + 1 > 9 ? 0 : team_ptr + 1;
        int ptr2 = team_ptr - 1 < 0 ? 9 : team_ptr - 1;
        for (int tm = 0; tm < 5; tm++) {
            if (ptr1 == anchor) {
                ptr1 += 1;
            }
            if (ptr1 >= 10) {
                ptr1 -= 10;
            }
            if (ptr2 == anchor) {
                ptr2 -= 1;
            }
            if (ptr2 < 0) {
                ptr2 += 10;
            }
            sch[ptr1][week] = ptr2;
            sch[ptr2][week] = ptr1;
            ptr1 += 1;
            ptr2 -= 1;
        }
        team_ptr += 1;
    }
    for (int i = 0; i < 10; i++) {
        sch[i][9] = -1;
    }
    for (int i = 0; i < 10; i++) {
        printf("%d: ", i);
        for (int j = 0; j < 10; j++) {
            printf("%d, ", sch[i][j]);
        }
        printf("\n");
    } 
}

bool HandleEvent(SDL_Event *Event) {
    bool ShouldQuit = false;
    switch(Event->type) {
        case SDL_QUIT:
        {
            printf("SDL_QUIT\n");
            ShouldQuit = true;
        } break;

        case SDL_WINDOWEVENT:
        {
            switch(Event->window.event)
            {
                case SDL_WINDOWEVENT_RESIZED:
                {
                    printf("SDL_WINDOWEVENT_RESIZED (%d, %d)\n", Event->window.data1, Event->window.data2);
                }break;
                case SDL_WINDOWEVENT_FOCUS_GAINED:
                {
                    printf("SDL_WINDOWEVENT_FOCUS_GAINED\n");
                }break;
                case SDL_WINDOWEVENT_EXPOSED:
                {
                    SDL_Window *Window = SDL_GetWindowFromID(Event->window.windowID);
                    SDL_Renderer *Renderer = SDL_GetRenderer(Window);
                    static bool IsWhite = true;
                    if (IsWhite == true) {
                        SDL_SetRenderDrawColor(Renderer, 255, 255, 255, 255);
                        IsWhite = false;
                    } else {
                        SDL_SetRenderDrawColor(Renderer, 0, 0, 0, 255);
                        IsWhite = true;
                    }
                    SDL_RenderClear(Renderer);
                    SDL_RenderPresent(Renderer);
                }break;
            }
        }break;
    }
    return(ShouldQuit);
}

int main(int argc, char *argv[]) {
    //struct Team teams[10] = {0}; 
    //schedule sch = {0};
    //create_schedule(sch);
    //SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, "College Football Manager",
    //                         "This is College Football Manager", 0);
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        // SDL didnt work
    }
    SDL_Window *Window;
    Window = SDL_CreateWindow("College Football Manager",
                              0,
                              0,
                              /*SDL_WINDOWPOS_UNDEFINED,
                              SDL_WINDOWPOS_UNDEFINED,*/
                              640,
                              480,
                              SDL_WINDOW_RESIZABLE);
    if (Window) {
        SDL_Renderer *Renderer = SDL_CreateRenderer(Window,
                                                    -1,
                                                    0);
        if (Renderer) {
            for(;;)
            {
                SDL_Event Event;
                SDL_WaitEvent(&Event);
                if (HandleEvent(&Event))
                {
                    break;
                }
            }
        } else {
        }
    } else {
    }
    SDL_Quit();
    return(0);
}
