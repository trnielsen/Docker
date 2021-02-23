# Ordering of Docker layers
## ScippMantid is the base line
* Here we assume the McStas release cycle is changing faster than ScippMantid
* In other words we do not need the bleading edge of Mantid/Scipp


## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  | Jhub         |   | Dockerfile_jhub_py37                |   | trnielsen/jhub37_ikon20                        |   |
| 2.  | ScippMantid  |   | Dockerfile_jhub_py37_scippmantid    |   | trnielsen/jhub37_ikon20_scipp_dev              |   |
| 3.  | NeXus        |   | Dockerfile_jhub_py37_nexus          |   | trnielsen/jhub37_ikon20_scipp_dev_nexus        |   |
| 4.  | McStas       |   | Dockerfile_jhub_py37_mcstas         |   | trnielsen/jhub37_ikon20_scipp_dev_mcstas       |   |
| 5.  | McStasScript |   | Dockerfile_jhub_py37_mcstasscript   |   | trnielsen/jhub37_ikon20_scipp_dev_mcstasscript |   |
| 6.  | SasView      |   | Dockerfile_jhub_py37_sasview        |   | trnielsen/jhub37_ikon20_scipp_dev_sasview      |   |
| 7.  | Notebooks    |   | Dockerfile_jhub_py37_nbextensions   |   | trnielsen/jhub37_ikon20_scipp_dev_nbextensions |   |
 
# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub37_ikon20                        | latest   | 3db760435235  | 47 hours ago  | 678MB   |   |
| 2.  |  trnielsen/jhub37_ikon20_scipp_dev              | latest   | 308bc8a0aa98  | 47 hours ago  | 3.04GB  |   |
| 3.  |  trnielsen/jhub37_ikon20_scipp_dev_nexus        | latest   | 46ba256ad165  | 46 hours ago  | 3.47GB  |   |
| 4.  |  trnielsen/jhub37_ikon20_scipp_dev_mcstas       | latest   | 752f13f4ecab  | 46 hours ago  | 4.72GB  |   |
| 5.  |  trnielsen/jhub37_ikon20_scipp_dev_mcstasscript | latest   | 57d77c29315d  | 46 hours ago  | 4.72GB  |   |
| 6.  |  trnielsen/jhub37_ikon20_scipp_dev_sasview      | latest   | 1548764f8683  | 46 hours ago  | 4.86GB  |   |
| 7.  |  trnielsen/jhub37_ikon20_scipp_dev_nbextensions | latest   | 643d1b09b30e  | 46 hours ago  | 4.91GB  |   |


# Dependencies 
* BornAgain is not included
* Sipp dev seems to restrict numpy to 1.15 (leads to conflict with BA)

# Build
```console
$ time docker build -t trnielsen/jhub37_ikon20_scipp_dev_nbextensions -f Dockerfile_jhub_py37_nbextensions .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub37_ikon20_scipp_dev_nbextensions
```
# Tag
* Remember to avoide name clash
* E.i. tagging should use a new name
```console
$ docker tag 643d1b09b30e trnielsen/jhub37_dram_ikon20_scipp_dev:latest
```

# Push
* Update repo on DockerHub
```console
$ docker push  trnielsen/jhub37_dram_ikon20_scipp_dev:latest
```
# Docker Hub
* Feb. 11 2021 
* Pushed jhub37_dram_ikon20_scipp_dev to docker hub
* https://hub.docker.com/r/trnielsen/jhub37_dram_ikon20_scipp_dev



```console
$ docker pull trnielsen/jhub37_dram_ikon20_scipp_dev
```
