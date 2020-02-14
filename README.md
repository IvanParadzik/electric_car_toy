# electric_car_toy
Electric Car Toy

This is small home project of making electric toy car. For making this electric car I use four DC motors which are controlled with
two L298n motor drivers. Motors are connected to Raspberry Pi and code is written in Python. Electric car is controlled with laptop
trought TCP(Transmission Control Protocol). Interface is made in PyGame because at start my plan was to make it to look like game. 
When car is moving forward camera on car displays on PyGame Window. I used Raspberry Pi Camera modul. Camera is controlled with 
servo motor and it can be rotated for 120 degrees. Camera position is shown on Pygame window. 
On interface window there is label which is showing movement speed  of car . Movement speed of is measured with rotation 
sensor LM393. 
When car is moving backward there is radar displayed on Pygame window showing us distance of objects behind the car. If car is 
too close to object it stops. 
In front of car there is robot arm with four servo motors. The arm has finger with witch we can grab small and light objects. 
