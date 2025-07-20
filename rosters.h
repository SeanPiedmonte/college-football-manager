/*
* Header file for intializing the rosters on new league start
*/

#include <stdio.h>
#include <sqlite3.h>

sqlite3 *db;

int initialize_rosters(struct Team *teams);
