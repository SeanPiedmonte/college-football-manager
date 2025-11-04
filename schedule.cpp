#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "schedule.h"

void create_schedule(schedule sch, int teams, int weeks) {
    int anchor = 0;
    int home_ptr = 1;
    int away_ptr = 9;
    int anchor_pair = 5;
    for (int i = 1; i < 10; i++) {
        printf("anchor: %d, anchor_pair: %d, home_ptr: %d, away_ptr: %d\n", anchor, anchor_pair, home_ptr, away_ptr);
        sch[anchor][i-1] = anchor_pair;
        sch[anchor_pair][i-1] = anchor;
        int in_ptr_h = home_ptr;
        int in_ptr_a = away_ptr;
        printf("%d:\n", i);
        for (int j = 0; j < teams/2-1; j++) {
            printf("in_ptr_h: %d, in_ptr_a: %d\n", in_ptr_h, in_ptr_a);
            sch[in_ptr_h][i-1] = in_ptr_a;
            sch[in_ptr_a][i-1] = in_ptr_h;
            in_ptr_h++;
            in_ptr_a--;
            if (in_ptr_a < 1) {
                in_ptr_a = 9;
            }
            if (in_ptr_h > 9) {
                in_ptr_h = 1;
            }
        }
        home_ptr++;
        away_ptr = anchor + i;
        anchor_pair++;
        if (anchor_pair > 9) {
            anchor_pair = 1;
        }
    }
    for (int i = 0; i < 10; i++) {
        sch[i][weeks-1] = -1;
    }
}
