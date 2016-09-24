#!/usr/bin/env python
import rospy
from basics.msg import Complex

def data_received_cb(latest_msg):
    '''
    Triple the complex numbers published on the /complex topic and publish
    new values on /tripled topic 

    :param latest_msg: contains copy of last published data
    :type latest_msg: basics.msg.Complex class auto-generated by catkin
    :return: None
    '''
    latest_msg.real *= 3
    latest_msg.imaginary *= 3
    pub.publish(latest_msg)
    rospy.loginfo('tripled complex number is %f + %fi', latest_msg.real, latest_msg.imaginary)
    return


if __name__=='__main__':
    rospy.init_node('tripler')
    pub = rospy.Publisher('tripled', Complex, queue_size=1)
    rospy.Subscriber('complex', Complex, data_received_cb)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
