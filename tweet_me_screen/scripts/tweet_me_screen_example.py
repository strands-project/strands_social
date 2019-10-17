#! /usr/bin/env python

import rospy
import roslib
import os

import strands_webserver.client_utils
from tweet_me_screen import create_tweet_me_page

if __name__ == '__main__':
    rospy.init_node("tweet_me_screen_example")

    # The display to publish on, defaulting to all displays
    display_no = rospy.get_param("~display", 0) 

    image_topic = rospy.get_param('~image_topic') 
    image_host = rospy.get_param('~image_host', 'localhost') 

    print('image_topic', image_topic)
    print('image_host', image_host)

    # set http root to be this package
    http_root = os.path.join(roslib.packages.get_pkg_dir('tweet_me_screen'), 'data')
    strands_webserver.client_utils.set_http_root(http_root)

    # generate the page 
    file_name = 'tweet_me.html'
    sayings = []
    create_tweet_me_page(os.path.join(http_root, file_name), image_topic, '<span class="lead">Have your image tweeted by</span> @BobStrands', sayings, image_host=image_host)

    # show the page
    strands_webserver.client_utils.display_relative_page(display_no, file_name)

