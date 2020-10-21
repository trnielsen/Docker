FROM trnielsen/jhub37_mantid_sasview:latest

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    cmake \
    libgsl-dev \
    libfftw3-dev \
    libtiff5-dev \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-regex-dev \
    libboost-iostreams-dev \
    qt5-default \
    libqt5designercomponents5 \
    qttools5-dev \
    libqt5svg5-dev \
    libqt5opengl5-dev \
    libcerf-dev \
    python3-dev \
    python3-numpy \
    python3-matplotlib \
    pkg-config \
    libeigen3-dev

# Create a non-root user
ARG username=docker
ARG uid=1001
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER 

USER $USER
WORKDIR /home/$USER
USER $USER
WORKDIR /home/$USER
RUN git clone --recurse-submodules https://github.com/scgmlz/BornAgain.git




# Build BA
# See https://www.bornagainproject.org/documentation/getting-started/installation/linux-detailed/build-and-install/
# 

# mkdir BA
# cd BA
# git pull
# mkdir Build_01
# cd Build_01
# cmake ../
# make -j6
# sudo make install
