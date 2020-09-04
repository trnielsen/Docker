FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    curl \
    tzdata

RUN DEBIAN_FRONTEND=noninteractive apt-get --yes install keyboard-configuration


# McStas release. E.g. 2.6.1 (August 2020)
RUN curl http://packages.mccode.org/debian/mccode.list > /etc/apt/sources.list.d/mccode.list

RUN apt-get update && apt-get install -y \
    coreutils \
    emacs \
    firefox \
    fonts-liberation \
    libgl1-mesa-glx \
    libnexus1 \
    libnexus-dev \
    libopenmpi-dev \
    libosmesa6 \
    mcstas-suite-python \
    mcstas-suite-perl \
    mesa-utils \
    openmpi-bin \
    python3-pip \
    vim \
    xbase-clients \
    xdg-utils 


# McStas build tools
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    texlive \
    gcc \
    gfortran \
    flex \
    bison \
    build-essential \
    poppler-utils \
    texlive-latex-extra \
    texlive-bibtex-extra \
    texlive-pstricks \
    texlive-science equivs



# Create a non-root user
ARG username=docker
ARG uid=1000
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
RUN git clone https://github.com/McStasMcXtrace/McCode


# HOW TO TEST 
#
# Use user docker \ 
# Pull McStas from github \
# Build locally \
# cd McStas 
# git pull
# ./build_debs_mcstas 2.7-beta
#
# To test the container - login as root 
# Install mcstas*2.7-beta-deb64.deb
# dpkg -i *.deb 
# 
# Go back to docker user and test new enviorment 
# mcstas-2.7-beta-environment
# mcstas --version





