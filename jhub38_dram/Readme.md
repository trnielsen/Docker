# Docker files for DRAM py38 June 2021

# From docker-stacks
* https://github.com/jupyter/docker-stacks/tree/master/base-notebook

# Ordering of Docker layers




## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  | Jhub         |   | Dockerfile_from_docker_stacks              |   | trnielsen/jhub38_dram_june_ds               |   |
| 2.  | ScippMantid  |   | Dockerfile_jhub_py38_june_scippmantid      |   | trnielsen/jhub38_dram_june_ds_scippmantid   |   |
| 3.  | Nexius       |   | Dockerfile_jhub_py38_june_nexus            |   | trnielsen/jhub38_dram_june_ds_nexus         |   |
| 4.  | McStas       |   | Dockerfile_jhub_py38_june_mcstas           |   | trnielsen/jhub38_dram_june_ds_mcstas        |   |
| 5.  | McStasScript |   | Dockerfile_jhub_py38_june_mcstasscript     |   | trnielsen/jhub38_dram_june_ds_mcstasscript  |   |
| 6.  | SasView      |   | Dockerfile_jhub_py38_june_sasview          |   | trnielsen/jhub38_dram_june_ds_sasview       |   |
| 7.  | NB ext       |   | Dockerfile_jhub_py38_june_nbextensions     |   | trnielsen/jhub38_dram_june_ds_nbextensions  |   |


# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub38_dram_june_ds                   | latest   | bb82833b5cd   | 47 hours ago  | 674MB    |   |
| 2.  |  trnielsen/jhub38_dram_june_ds_scippmantid       | latest   | 22f0533130b0  | 47 hours ago  | 2.83GB   |   |
| 3.  |  trnielsen/jhub38_dram_june_ds_nexus             | latest   | 34afda8dac31  | 46 hours ago  | 3.24GB   |   |
| 4.  |  trnielsen/jhub38_dram_june_ds_mcstas            | latest   | b6158e2584bc  | 46 hours ago  | 5.03GB   |   |
| 5.  |  trnielsen/jhub38_dram_june_ds_mcstasscript      | latest   | 2a107daf7738  | 46 hours ago  | 5.04GB   |   |
| 6.  |  trnielsen/jhub38_dram_june_ds_sasview           | latest   | f3e7c5dcfb01  | 46 hours ago  | 5.18GB   |   |
| 7.  |  trnielsen/jhub38_dram_june_ds_nbextensions      | latest   | bfab68bd53ff  | 46 hours ago  | 5.23GB   |   |

# Dependencies 
* Scipp : from master
* Scippneutron : from master
* Mantid : from scipp/label/dev

# Build
```console
$ time docker build --no-cache -t trnielsen/jhub38_dram_june_ds_scippmantid -f Dockerfile_jhub_py38_june_scippmantid .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub38_dram_june_ds_nbextensions
```

# Docker Hub
* June  15 2021 (plus/minus a few days) 
* Tag: trnielsen/jhub38_dram_june_ds_nbextensions -> trnielsen/jhub_py38_dram
* Pushed trnielsen/jhub_py38_dram to docker hub
* https://hub.docker.com/r/trnielsen/jhub_py38_dram

```console
$ docker pull trnielsen/jhub_py38_dram
```



