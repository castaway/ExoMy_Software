# Base image
FROM ros:jazzy 

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Basic tools
RUN apt-get update && \
    apt-get install vim nano git tmux wget curl python3-pip net-tools iputils-ping -y

# Install additional ros packages
RUN apt-get update && apt-get install ros-jazzy-rosbridge-server ros-jazzy-joy -y
RUN pip install --break-system-packages adafruit-pca9685


# Install packages for web application
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get update && \
    apt-get install nodejs -y
RUN npm install http-server -g

# Install packages for camera use
RUN apt-get update && \
    apt-get install ros-jazzy-web-video-server -y
#    ros-jazzy-camera-ros -y

# Install libcamera/camera_ros separately:

# # create workspace
# RUN mkdir -p ~/camera_ws/src
# RUN cd ~/camera_ws/src

# # check out libcamera
# RUN  apt -y install python3-colcon-meson python3-jinja2 python3-ply

# # Option A: official upstream
# # git clone https://git.libcamera.org/libcamera/libcamera.git
# # Option B: raspberrypi fork with support for newer camera modules
# RUN git clone https://github.com/raspberrypi/libcamera.git

# # check out this camera_ros repository
# RUN git clone https://github.com/christianrauch/camera_ros.git

# # resolve binary dependencies and build workspace
# RUN . /opt/ros/jazzy/setup.bash
# RUN cd ~/camera_ws/
# RUN rosdep install -y --from-paths src --ignore-src --rosdistro jazzy --skip-keys=libcamera
# RUN colcon build --event-handlers=console_direct+
# Program python3 (jinja2, yaml, jinja2, ply) found: NO modules: jinja2, yaml, jinja2
# RUN cd ..

# Add ros sourcing to bashrc
RUN echo ". /opt/ros/jazzy/setup.bash" >> ~/.bashrc

# Create Ros workspace
ENV EXOMY_WS=/root/exomy_ws
RUN mkdir -p $EXOMY_WS/src

WORKDIR /root

COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
