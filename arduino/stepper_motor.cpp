# include <stepper.h>;
const int a = 2048
stepper b = stepper(a,8,10,9,11)
void setup(){
    b.setspeed(20);
}
void loop(){
    b.setp(a);
}