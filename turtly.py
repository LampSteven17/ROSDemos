#from turtlesimy import main

import rospy 
from geometry_msgs.msg import Twist 
import sys 
from turtlesim.msg import Pose 
import time
from std_srvs.srv import Empty

#SERIOUSLY A GLOBAL
yertleRots = 0
flaggy = False

def main():
	turtle_circle(float(2.0))


def countRotations():
	global yertleRots
	global flaggy 

	if flaggy: 
		yertleRots += 1
		rospy.loginfo("ROTS INCREASED TO: %f", yertleRots)
	flaggy = not flaggy

def yertle_pos(pose):
	if(round(pose.theta, 2) <= 0.01 and round(pose.theta, 2) >= -0.01):
		rospy.loginfo("YERTLE'S AT: X:%f Y:%f Z:%f", pose.x, pose.y, pose.theta)
		countRotations()
		time.sleep(3)



def turtle_circle(radius):
	global yertleRots

	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)

	rospy.Subscriber('/turtle1/pose', Pose, yertle_pos)

	rate = rospy.Rate(10)
	vel = Twist()

	clear_bg = rospy.ServiceProxy('reset', Empty)
	clear_bg()

	while (not rospy.is_shutdown()) and yertleRots < 3:
		vel.linear.x = radius
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1

		#rospy.loginfo("Radius = %f", radius)

		pub.publish(vel)
		rate.sleep()



if __name__ == '__main__':
    main()
