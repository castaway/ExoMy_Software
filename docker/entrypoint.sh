#!/bin/bash
if [[ $1 == "config" ]]
then
	cd /root/exomy_ws/src/exomy/scripts
	bash
elif [[ $1 == "autostart" ]]
then
	source /opt/ros/jazzy/setup.bash
	cd /root/exomy_ws
	colcon build
    . /root/camera_ws/install/local_setup.bash
    . /root/exomy_ws/install/local_setup.bash

	http-server src/exomy/gui -p 8000 &

	ros2 launch exomy exomy.launch.py

	bash
elif [[ $1 == "devel" ]]
then
	cd /root/exomy_ws
	source /opt/ros/jazzy/setup.bash
    . /root/camera_ws/install/local_setup.bash
    . /root/exomy_ws/install/local_setup.bash

	bash
else
	bash
fi
