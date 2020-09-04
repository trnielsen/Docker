# Ordering of Docker layers
## McStas is the base line
* Here we assume the McStas release cycle is changing faster than Mantid
* In other words we do not need the bleading edge of Mantid/Scipp


## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  |  Jhub |   |  Dockerfile_jhub_py37 |   |  trnielsen/jhub37_mantid |   |
| 2.  | Mantid/Scipp  |   | Dockerfile_jhub_py37_mantid  |   |  trnielsen/jhub37_mantid_mantid |   |
| 3.  | McStas  |   | Dockerfile_jhub_py37_mcstas |   | trnielsen/jhub37_mantid_mcstas  |   |
| 4.  | McStasScript  |   |  Dockerfile_jhub_py37_mcstasscript |   |  trnielsen/jhub37_mantid_mcstasscript |   |
| 5.  | SasView  |   |  Dockerfile_jhub_py37_sasview |   | trnielsen/jhub37_mantid_sasview  |   |
| 6  |  NB ext |   |  Dockerfile_jhub_py37_nbextensions |   |  trnielsen/jhub37_mantid_nbextensions |   |
| 7.  | Notebooks  |   |  Dockerfile_jhub_py37_notebooks |   | trnielsen/jhub37_mantid_notebooks  |   |

# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub37_mantid | latest   | 52214742e6b4  | 47 hours ago  | 671MB   |   |
| 2.  |  trnielsen/jhub37_mantid_mantid | latest   | 667118378d44 |  47 hours ago | 1.37GB  |   |
| 3.  |  trnielsen/jhub37_mantid_mcstas | latest   | d25a2eaf21ac  | 46 hours ago  | 4.2GB  |   |
| 4.  |  trnielsen/jhub37_mantid_mcstasscript | latest   | 045c07bc01a  | 46 hours ago |  4.21GB |   |
| 5.  |  trnielsen/jhub37_mantid_sasview | latest   | 04dde0a1af39  | 46 hours ago |  4.32GB |   |
| 6.  |  trnielsen/jhub37_mantid_nbextensions | latest   | 0f323f61c1cd  | 46 hours ago  | 4.37GB  |   |
| 7.  | trnielsen/jhub37_mantid_notebooks  | latest   | 0c3b41270de1  | 46 hours ago  | 4.67GB  |   |

# Build
```console
$ time docker build -t trnielsen/jhub37_mantid_notebooks -f Dockerfile_jhub_py37_notebooks .
```

# Run
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it trnielsen/jhub37_mantid_notebooks
```
