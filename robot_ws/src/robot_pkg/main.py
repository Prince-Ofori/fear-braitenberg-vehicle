# -*- coding: utf-8 -*-
import rospy
from cv2 import destroyAllWindows
from behaviourv3 import behaviour
 
def main():
    rospy.init_node('wandering', anonymous=True)
    behaviour()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    destroyAllWindows()
   

if __name__ == "__main__":main()