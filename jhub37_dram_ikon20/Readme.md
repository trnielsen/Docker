# Ordering of Docker layers
## Mantid is the base line
* Here we assume the McStas release cycle is changing faster than Mantid
* In other words we do not need the bleading edge of Mantid/Scipp


## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  | Jhub         |   | Dockerfile_jhub_py37              |   | trnielsen/jhub37_ikon20               |   |
| 2.  | ScippMantid  |   | Dockerfile_jhub_py37_scippmantid  |   | trnielsen/jhub37_ikon20_scippmantid   |   |
| 3.  | Nexius       |   | Dockerfile_jhub_py37_nexus        |   | trnielsen/jhub37_ikon20_nexus         |   |
| 4.  | McStas       |   | Dockerfile_jhub_py37_mcstas       |   | trnielsen/jhub37_ikon20_mcstas        |   |
| 5.  | McStasScript |   | Dockerfile_jhub_py37_mcstasscript |   | trnielsen/jhub37_ikon20_mcstasscript  |   |
| 6.  | SasView      |   | Dockerfile_jhub_py37_sasview      |   | trnielsen/jhub37_ikon20_sasview       |   |
| 7.  | BornAgain    |   | Dockerfile_jhub_py37_bornagain    |   | trnielsen/jhub37_ikon20_bornagain     |   |
| 8   |  NB ext      |   | Dockerfile_jhub_py37_nbextensions |   | trnielsen/jhub37_ikon20_nbextensions  |   |


# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub37_ikon                | latest   | 3db760435235  | 47 hours ago  | 678MB    |   |
| 2.  |  trnielsen/jhub37_ikon_scippmantid    | latest   | d04fc1498f88  | 47 hours ago  | 1.49GB   |   |
| 3.  |  trnielsen/jhub37_ikon_nexus          | latest   | 0173353cb74b  | 46 hours ago  | 1.92GB   |   |
| 4.  |  trnielsen/jhub37_ikon_mcstas         | latest   | a4161b213ccf  | 46 hours ago  | 3.71GB   |   |
| 5.  |  trnielsen/jhub37_ikon_mcstasscript   | latest   | ab307e88e767  | 46 hours ago  |  3.72GB  |   |
| 6.  |  trnielsen/jhub37_ikon_sasview        | latest   | 4c564f0c8773  | 46 hours ago  |  3.85GB  |   |
| 7.  |  trnielsen/jhub37_ikon_bornagain      | latest   | 8234e8c8de3c  | 46 hours ago  |  4.16GB  |   |
| 8.  |  trnielsen/jhub37_ikon_nbextensions   | latest   | 4572c3e9a8d1  | 46 hours ago  | 4.21GB   |   |

# Dependencies 
* We use a build of BornAgain

# Build
```console
$ time docker build -t trnielsen/jhub37_ikon20_scippmantid -f Dockerfile_jhub_py37_scippmantid .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub37_ikon20_nbextensions
```

# Docker Hub
* Feb. 14 2021 (plus/minus a few days) 
* Tag: trnielsen/jhub37_ikon20_nbextensions -> trnielsen/jhub37_dram_ikon20
* Pushed trnielsen/jhub37_dram_ikon20 to docker hub
* https://hub.docker.com/repository/docker/trnielsen/jhub37_dram_ikon20

```console
$ docker pull trnielsen/jhub37_dram_ikon20
```
