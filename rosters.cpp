/*
* This file is made to handle the instanciation of roster files upon launching
* a new league. Utilizes a sqlite database to hold player and team info.
*/
#include "rosters.h"

/*
* initialize_rosters
*
* parameters: struct *Team
*   pass in a pointer to a team array to handle store roster data in game
*
* return: int
*   returns an int to stand as an error code to the main game loop
*/
int initialize_rosters(struct Team *teams) {
    int status = sqlite3_open_v2("rosters.db",
                                 &db,
                                 SQLITE_OPEN_READONLY,
                                 NULL);

    if (status == SQLITE_OK) {
        printf("Database opened successfully!\n");
        sqlite3_close(db);
    } else {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        if (db) sqlite3_close(db);
    }

    return 0;
}
