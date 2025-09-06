# 基础镜像（ROS Humble 桌面完整版）
FROM osrf/ros:humble-desktop-full

# 用户参数
ARG USERNAME=yutou
ARG USER_UID=1000
ARG USER_GID=$USER_UID


RUN apt-get update && \
    apt-get install -y \
        wget \
        git \
        pip \
        xterm \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y \
        fish \           
        gedit \
        ros-humble-foxglove-bridge \
        # ros-humble-teleop-twist-keyboard \
        nautilus \
        curl \
        sudo \             
        && \
    pip install rosbags && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  # sudo已在上一步安装

USER $USERNAME
WORKDIR /home/$USERNAME

ENV ROS_DISTRO=humble
ENV ROS_SETUP_BASH="/opt/ros/humble/setup.bash"

# 为bash用户自动加载ROS环境
RUN echo "source $ROS_SETUP_BASH" >> /home/$USERNAME/.bashrc && \
    echo "source /home/yutou/ros2_ws/install/setup.bash" >> /home/$USERNAME/.bashrc

# # 为fish用户配置ROS环境（可选）
# RUN echo 'bass source /opt/ros/humble/setup.bash' >> /home/$USERNAME/.config/fish/config.fish && \
#     echo 'bass source ~/ros2_ws/install/setup.bash' >> /home/$USERNAME/.config/fish/config.fish && \
#     echo 'source ~/ros2_ws/.config/fish/completions/ros2.fish' >> /home/$USERNAME/.config/fish/config.fish

# ------------------------------
# 设置工作目录和默认命令
# ------------------------------
WORKDIR /home/$USERNAME

# 默认启动命令
CMD ["/usr/bin/bash"]