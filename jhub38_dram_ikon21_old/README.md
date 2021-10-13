# Docker files for DRAM py38 September 2021 (IKON21 Python workshop)

# Two versions
* Jupyter notebook classic
* Jupyter lab
 

# From docker-stacks
* https://github.com/jupyter/docker-stacks/tree/master/base-notebook

# Ordering of Docker layers


## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.  | Jhub         |   | Dockerfile_from_docker_stacks_py38         |   | trnielsen/jhub38_dram_sep2021_ds              |   |
| 2.  | ScippMantid  |   | Dockerfile_jhub_py38_sep2021_scippmantid   |   | trnielsen/jhub38_dram_sep2021_ds_scipp        |   |
| 3.  | Nexus        |   | Dockerfile_jhub_py38_sep2021_nexus         |   | trnielsen/jhub38_dram_sep2021_ds_nexus        |   |
| 4.  | Voila        |   | Dockerfile_jhub_py38_sep2021_voila         |   | trnielsen/jhub38_dram_sep2021_ds_volia        |   |
| 5.  | McStas       |   | Dockerfile_jhub_py38_sep2021_mcstas        |   | trnielsen/jhub38_dram_sep2021_ds_mcstas       |   |
| 6.  | McStasScript |   | Dockerfile_jhub_py38_sep2021_mcstasscript  |   | trnielsen/jhub38_dram_sep2021_ds_mcstasscript |   |
| 7.  | McXtrace     |   | Dockerfile_jhub_py38_sep2021_mcxtrace      |   | trnielsen/jhub38_dram_sep2021_ds_mcxtrace     |   |
| 8.  | SasView      |   | Dockerfile_jhub_py38_sep2021_sasview       |   | trnielsen/jhub38_dram_sep2021_ds_sasview      |   |


## Docker layers and services: Jupyter notebook classic
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 9a.  | NB ext       |   | Dockerfile_jhub_py38_sep2021_nbextensions     |   | trnielsen/jhub38_dram_sep2021_ds_nbextensions    |   |

## Docker layers and services: Jupyter lab
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 9b.  | Lab          |   | Dockerfile_jhub_py38_sep2021_nbgitpuller      |   | trnielsen/jhub38_dram_sep2021_ds_nbgitpuller    |   |



# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.  |  trnielsen/jhub38_dram_sep2021_ds                    | latest   | bb82833b5cd   | 47 hours ago  | 667MB    |   |
| 2.  |  trnielsen/jhub38_dram_sep2021_ds_scipp              | latest   | 22f0533130b0  | 47 hours ago  | 3.01GB   |   |
| 3.  |  trnielsen/jhub38_dram_sep2021_ds_nexus              | latest   | 34afda8dac31  | 46 hours ago  | 3.43GB   |   |
| 4.  |  trnielsen/jhub38_dram_sep2021_ds_volia              | latest   | b6158e2584bc  | 46 hours ago  | 3.73GB   |   |
| 5.  |  trnielsen/jhub38_dram_sep2021_ds_mcstas             | latest   | 2a107daf7738  | 46 hours ago  | 5.54GB   |   |
| 6.  |  trnielsen/jhub38_dram_sep2021_ds_mcstasscript       | latest   | f3e7c5dcfb01  | 46 hours ago  | 5.55GB   |   |
| 7.  |  trnielsen/jhub38_dram_sep2021_ds_mcxtrace           | latest   | bfab68bd53ff  | 46 hours ago  | 5.61GB   |   |
| 8.  |  trnielsen/jhub38_dram_sep2021_ds_sasview            | latest   | e191bdb2f372  | 46 hours ago  | 5.74GB   |   |
| 9a. |  trnielsen/jhub38_dram_sep2021_ds_nbextensions       | latest   | 268135670089  | 46 hours ago  | 5.80GB   |   |
| 9b. |  trnielsen/jhub38_dram_sep2021_ds_nbgitpuller        | latest   | c81ddd5d688c  | 46 hours ago  | 5.75GB   |   |


# Dependencies 
* Scipp : from master
* Scippneutron : from master
* Mantid : from scipp/label/dev

# Build
```console
$ time docker build --no-cache -t trnielsen/jhub38_dram_sep2021_ds_scippmantid -f Dockerfile_jhub_py38_sep2021_scipp .
```

# Run Jupyter classical 
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it  trnielsen/jhub38_dram_sep2021_ds_nbextensions
```

# Run Jupyter lab 
```console
$ docker run --name test_notebooks -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v  ~/Desktop:/Desktop -it trnielsen trnielsen/jhub38_dram_sep2021_ds_nbgitpuller
```


# Docker Hub
* Sep  17 2021 (plus/minus a few days) 
* Tag: trnielsen/jhub38_dram_sep2021_ds_nbextensions -> trnielsen/jhub_py38_ikon21_nb
* Pushed trnielsen/jhub_py38_ikon21_nb to docker hub
* https://hub.docker.com/r/trnielsen/jhub_py38_ikon21_nb

```console
$ docker pull trnielsen/jhub_py38_ikon21_nb
```



