#include <time.h>
#include <stdlib.h>
#include <stdio.h>

typedef int schedule[10][10];

void create_schedule(schedule sch, int teams, int weeks) {
    int anchor = 0;
    int home_ptr = 1;
    int away_ptr = 9;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
        }
    }
}

int main(void) {
    schedule sch = {0};
    create_schedule(sch, 10, 10);
}
