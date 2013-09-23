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

    // servo ///////////////////////////////////////////////////////
    init_pin();
    pin_digitalOut(&D[2]);
    pin_digitalOut(&D[3]);

    uint16_t posHoriz = 0;
    uint16_t posVert = 65535;

    init_oc();
    init_uart();

    oc_servo(&oc1, &D[2], &timer1, 20e-3, 0.6e-3, 2.55e-3, posHoriz);
    oc_servo(&oc2, &D[3], &timer1, 20e-3, 0.6e-3, 2.55e-3, posVert);

    // Servo ///////////////////////////////////////////////////
    for (posHoriz <= 65535) {
        pin_write(&D[2],posHoriz);
        for (posVert > 0) {
            posVert = posVert - 100;
            pin_write(&D[3],posVert);
        }
    posVert = 65535;
    posHoriz = posHoriz + 1000;
    }
}
