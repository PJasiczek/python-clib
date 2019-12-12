#include <stdio.h>
#include <math.h>
#define M_PI 3.14159265358979323846

double get_y_block(double distance, double length, double height, double angle, double radius) {

    double counter_position_y = (height - (sin(angle)*radius))*(distance - (cos(angle)*radius));
    double denominator_position_y = sqrt(pow(length,2) - pow((height-(sin(angle)*radius)),2));

    double position_y = (sin(angle) * radius) + (counter_position_y/denominator_position_y);

    return position_y;
}

double speed_block(double start_x, double start_y, double end_x, double end_y, double time) {

    double road = sqrt(pow((end_x - start_x),2) + pow((end_y - start_y),2));
    double speed = road/time;

    return speed;
}

double acceleration_of_the_block(double start_speed, double end_speed, double time) {

    double acceleration = (end_speed - start_speed)/time;
    return acceleration;
}