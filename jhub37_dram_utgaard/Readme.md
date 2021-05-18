# Docker files for AMOR test May 2021
* on 10. network 

# Ordering of Docker layers
## McStas is the base line
* Here we assume the Scipp release cycle is changing faster than McStas
* Here we have both Scipp and Mantid

Plan for layers
* Jhub
* NeXus
* McStas
* SasView
* McStasScript
* Scipp and Mantid
* nbextenstion



## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  | Jhub         |   | Dockerfile_jhub_py37_base              |   | trnielsen/jhub37_dram_base               |   |
| 2.  | ScippMantid  |   | Dockerfile_jhub_py37_nexus             |   | trnielsen/jhub37_dram_base_nexus   |   |
| 3.  | Nexius       |   | Dockerfile_jhub_py37_mcstas            |   | trnielsen/jhub37_dram_base_mcstas         |   |
| 4.  | McStas       |   | Dockerfile_jhub_py37_sasview           |   | trnielsen/jhub37_dram_base_sasview        |   |
| 5.  | McStasScript |   | Dockerfile_jhub_py37_mcstasscript      |   | trnielsen/jhub37_dram_base_mcstasscript  |   |
| 6.  | SasView      |   | Dockerfile_jhub_py37_scippmantid       |   | trnielsen/jhub37_dram_base_scippmantid      |   |
| 7.  | NB ext       |   | Dockerfile_jhub_py37_nbextensions      |   | trnielsen/jhub37_dram_base_nbextensions  |   |


# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub37_base                   | latest   | bb82833b5cd  | 47 hours ago  | 654MB    |   |
| 2.  |  trnielsen/jhub37_dram_base_nexus        | latest   | 22f0533130b0  | 47 hours ago  | 1.06GB   |   |
| 3.  |  trnielsen/jhub37_dram_base_mcstas       | latest   | 34afda8dac31  | 46 hours ago  | 2.85GB   |   |
| 4.  |  trnielsen/jhub37_dram_base_sasview      | latest   | b6158e2584bc  | 46 hours ago  | 3.18GB   |   |
| 5.  |  trnielsen/jhub37_dram_base_mcstasscript | latest   | 2a107daf7738  | 46 hours ago  |  3.25GB  |   |
| 6.  |  trnielsen/jhub37_dram_base_scippmantid  | latest   | f3e7c5dcfb01  | 46 hours ago  |  5.01GB  |   |
| 7.  |  trnielsen/jhub37_dram_base_nbextensions | latest   | bfab68bd53ff  | 46 hours ago  | 5.15GB   |   |

# Dependencies 
* Scipp : from master
* Scippneutron : form dev

# Build
```console
$ time docker build -t trnielsen/jhub37_dram_base_scippmantid -f Dockerfile_jhub_py37_scippmantid .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub37_dram_base_nbextensions
```

# Docker Hub
* May  03 2021 (plus/minus a few days) 
* Tag: trnielsen/jhub37_dram_base_nbextensions -> trnielsen/jhub_py37_dram
* Pushed trnielsen/jhub_py37_dram to docker hub
* https://hub.docker.com/r/trnielsen/jhub_py37_dram

```console
$ docker pull trnielsen/jhub_py37_dram
```


# Notes
* Dockerfile_jhub_py37_new_Ubuntu
* Dockerfile_jhub_py37
* Are just different test version of the base image. Not used. Only included here to show what can be inclued/excluded
* Auto updates, etc.
