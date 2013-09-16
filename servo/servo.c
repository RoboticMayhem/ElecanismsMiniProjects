#include <p24FJ128GB206.h>
#include "config.h"
#include "common.h"
#include "ui.h"
#include "timer.h"
#include "pin.h"
#include "oc.h"
#include "uart.h"
#include "stdio.h"

int16_t main(void) {
    init_timer();
    init_clock();

    init_pin();
    pin_analogIn(&A[0]);
    pin_digitalOut(&D[0]);

    uint16_t pot;
    uint16_t pos;

    init_oc();

    init_uart();

    /*uint16_t in_min = 64;
    uint16_t in_max = 5632;
    double out_min = 800;
    double out_max = 2200;*/

    oc_servo(&oc1, &D[0], &timer1, 20e-3, 0.8e-3, 2.2e-3, 0);
    while(1){
        //Loop works, need to play with oc_servo range to get full 180 degrees
        pot = pin_read(&A[0]);
        //range of pot = 0 - 5632
        //pos = (pot * (1e-3/5632)) + 1e-3;
        //pos = (pot- in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
        pos = pot;
        printf("we're sending the servo %d \n",pos);
        pin_write(&D[0],pos);
    }
}