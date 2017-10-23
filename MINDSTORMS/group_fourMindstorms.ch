/* Control multiple robots simultaneously using the CMindstormsGroup class*/

#include <mindstorms.h>
CMindstorms robot1, robot2, robot3, robot4;
CMindstormsGroup group;

double radius = 1.1; // radius of the wheels (inches)
double trackWidth = 4.54; // track width of the robots (inches)

/* add the four robots as members of the group */
group.addRobot(robot1);
group.addRobot(robot2);
group.addRobot(robot3);
group.addRobot(robot4);

group.driveDistance(5, radius); // drive robots forward 5 inches
group.turnLeft(90, radius, trackWidth); // turn robots left 90 degrees
group.driveDistance(10, radius); //drive robots forward 10 inches
