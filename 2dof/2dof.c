#include <p24FJ128GB206.h>
#include "config.h"
#include "common.h"
#include "ui.h"
#include "timer.h"
#include "pin.h"
#include "oc.h"
#include "uart.h"
#include "stdio.h"
#include "math.h"
#include "string.h"

int16_t main(void) {
    // blink ///////////////////////////////////////////////////////
    init_clock();
    init_ui();
    init_timer();

    led_on(&led1);
    timer_setPeriod(&timer2, 1);
    timer_start(&timer2);
    timer_time(&timer3);

    // servo ///////////////////////////////////////////////////////
    init_pin();
    ////pin_analogIn(&A[0]);
    pin_digitalOut(&D[2]);
    pin_digitalOut(&D[3]);

    ////uint16_t pot;
    uint16_t posHoriz;
    uint16_t posVert;

    init_oc();
    init_uart();

    /*uint16_t in_min = 64;
    uint16_t in_max = 5632;
    double out_min = 800;
    double out_max = 2200;*/

    oc_servo(&oc1, &D[2], &timer1, 20e-3, 0.6e-3, 2.55e-3, 0);
    oc_servo(&oc2, &D[3], &timer1, 20e-3, 0.6e-3, 2.55e-3, 0);

    // communication ///////////////////////////////////////////////
    uint8_t string[40];
    uint8_t compare[40];

    // MAIN LOOP ///////////////////////////////////////////////////
    while (1) {

        // Blink ///////////////////////////////////////////////////
        if (timer_flag(&timer2)) {
            timer_lower(&timer2);
            led_toggle(&led1);
        }
        led_write(&led2, !sw_read(&sw2));
        led_write(&led3, !sw_read(&sw3));

        // Servo ///////////////////////////////////////////////////
    // This function expects the loop to run continuously
        //Loop works, need to play with oc_servo range to get full 180 degrees
        //pot = pin_read(&A[0]);
        //pos = pot;

        printf("we're sending the Horizontal servo %u \n",posHoriz);
        printf("we're sending the Vertical   servo %u \n",posVert);
        pin_write(&D[2],posHoriz);
        pin_write(&D[3],posVert);

        // communication ///////////////////////////////////////////
    // This funciton expects the loop to stop here
        printf(">> ");
        uart_gets(&uart1, string, 40);
        printf("'%s'\n", string);

        if (strcmp(string, "w") == 0){
            printf("W - Up \n");
            posVert = posVert + 1;
        }
        else if (strcmp(string, "s") == 0){
            printf("S - Down \n");
            posVert = posVert - 1;
        }
        else if (strcmp(string, "a") == 0){
            printf("A - Left \n");
            posHoriz = posHoriz + 1;
        }
        else if (strcmp(string, "d") == 0){
            printf("D - Right \n");
            posHoriz = posHoriz - 1;
        }
        else if (strcmp(string, "r") == 0){
            printf("R - Reset \n");
            posHoriz = 0;
            posVert = 0;
        }
        else{
            printf("NA \n");
        }
    }
}
