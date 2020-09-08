# Ordering of Docker layers
## McStas is the base line
Here we assume the Mantid release cycle is changing faster the McStas

## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  |  Jhub |   |  Dockerfile_jhub_py37 |   |  trnielsen/jhub37_mcstas |   |
| 2.  | McStas  |   | Dockerfile_jhub_py37_mcstas  |   |  trnielsen/jhub37_mcstas_mcstas |   |
| 3.  | Mantid/Scipp  |   | Dockerfile_jhub_py37_mantid |   | trnielsen/jhub37_mcstas_mantid  |   |
| 4.  | McStasScript  |   |  Dockerfile_jhub_py37_mcstasscript |   |  trnielsen/jhub37_mcstas_mcstasscript |   |
| 5.  | SasView  |   |  Dockerfile_jhub_py37_sasview |   | trnielsen/jhub37_mcstas_sasview  |   |
| 6  |  NB ext |   |  Dockerfile_jhub_py37_nbextensions |   |  trnielsen/jhub37_mcstas_nbextensions |   |
| 7.  | Notebooks  |   |  Dockerfile_jhub_py37_notebooks |   | trnielsen/jhub37_mcstas_notebooks  |   |

# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub37_mcstas | latest   | 52214742e6b4  | 46 hours ago  | 671MB2   |   |
| 2.  |  trnielsen/jhub37_mcstas_mcstas | latest   | 19f2f783f0c2 |  35 hours ago | 3.5GB  |   |
| 3.  |  trnielsen/jhub37_mcstas_mantid | latest   | e2f5faaef7f0  | 35 hours ago  | 4.2GB  |   |
| 4.  |  trnielsen/jhub37_mcstas_mcstasscript | latest   | 1ea9dba9395b  | 35 hours ago |  4.21GB |   |
| 5.  |  trnielsen/jhub37_mcstas_sasview | latest   | 32a3c40372ba  | 35 hours ago |  4.31GB |   |
| 6.  |  trnielsen/jhub37_mcstas_nbextensions | latest   | 01c121fa8c2e  | 35 hours ago  | 4.37GB  |   |
| 7.  | trnielsen/jhub37_mcstas_nnotebooks  | latest   | 74dda8c95fd5  | 35 hours ago  | 4.66GB  |   |


# Build
```console
$ time docker build -t trnielsen/jhub37_mcstas_notebooks -f Dockerfile_jhub_py37_notebooks .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub37_mcstas_notebooks
```

# Docker Hub
* Sep. 08 2020 
* Pushed jhub37_mcstas_mcstas to docker hub
* https://hub.docker.com/repository/docker/trnielsen/jhub_mcstas

```console
$ docker pull trnielsen/jhub_mcstas:latest
```

