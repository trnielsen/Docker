# Docker files for DRAM py38 September 2021 (IKON21 Python workshop)
* Thursday 31 September - Friday 1 October


# Jupyter Notebook version
* Jupyter notebook classic

 

# From docker-stacks
* https://github.com/jupyter/docker-stacks/tree/master/base-notebook

# Ordering of Docker layers


## Docker layers and services
| Layer  | Service  |   | Dockerfile  |   | Docker image  |   |
|---|---|---|---|---|---|---|
| 1.   | Jhub         |   | Dockerfile_from_docker_stacks_py38         |   | trnielsen/jhub38_dram_ikon21_ds	         |   |
| 2.   | Scipp        |   | Dockerfile_jhub_py38_ikon21_scipp	       |   | trnielsen/jhub38_dram_ikon21_scipp          |   |
| 3.   | ScippExtra   |   | Dockerfile_jhub_py38_ikon21_scipp_extra    |   | trnielsen/jhub38_dram_ikon21_scipp_extra    |   |
| 4.   | Nexus        |   | Dockerfile_jhub_py38_ikon21_nexus          |   | trnielsen/jhub38_dram_ikon21_nexus          |   |
| 5.   | Voila        |   | Dockerfile_jhub_py38_ikon21_voila          |   | trnielsen/jhub38_dram_ikon21_volia          |   |
| 6.   | McStas       |   | Dockerfile_jhub_py38_ikon21_mcstas         |   | trnielsen/jhub38_dram_iokn21_mcstas         |   |
| 7.   | McStasScript |   | Dockerfile_jhub_py38_ikon21_mcstasscript   |   | trnielsen/jhub38_dram_ikon21_mcstasscript   |   |
| 8.   | McXtrace     |   | Dockerfile_jhub_py38_ikon21_mcxtrace       |   | trnielsen/jhub38_dram_ikon21_mcxtrace       |   |
| 9.   | SasView      |   | Dockerfile_jhub_py38_ikon21_sasview        |   | trnielsen/jhub38_dram_ikon21_sasview        |   |
| 10.  | ASE          |   | Dockerfile_jhub_py38_ikon21_ase_extra      |   | trnielsen/jhub38_dram_ikon21_ase_extra      |   |
| 11.  | NB ext       |   | Dockerfile_jhub_py38_ikon21_nbextensions   |   | trnielsen/jhub38_dram_ikon21_nbextensions   |   |
| 12.  | Updates      |   | Dockerfile_jhub_py38_ikon21_updates   	   |   | trnielsen/jhub38_dram_ikon21_updates        |   |
| 13.  | Update scipp |   | Dockerfile_jhub_py38_ikon21_updates_scipp  |   | trnielsen/jhub38_dram_ikon21_updates_scipp |   |





# Docker images and sizes
| Nr.  | Docker image  |  tag | ID image   |  CREATED | SIZE  |   |
|---|---|---|---|---|---|---|
| 1.   |  trnielsen/jhub38_dram_ikon21_ds                 | latest   | bb82833b5cd   | 47 hours ago  | 667MB    |   |
| 2.   |  trnielsen/jhub38_dram_ikon21_scipp              | latest   | 22f0533130b0  | 47 hours ago  | 905MB    |   |
| 3.   |  trnielsen/jhub38_dram_ikon21_scipp_extra        | latest   | 22f0533130b0  | 47 hours ago  | 3.13GB   |   |
| 4.   |  trnielsen/jhub38_dram_ikon21_nexus              | latest   | 34afda8dac31  | 46 hours ago  | 3.55GB   |   |
| 5.   |  trnielsen/jhub38_dram_ikon21_volia              | latest   | b6158e2584bc  | 46 hours ago  | 3.85GB   |   |
| 6.   |  trnielsen/jhub38_dram_ikon21_mcstas             | latest   | 2a107daf7738  | 46 hours ago  | 5.66GB   |   |
| 7.   |  trnielsen/jhub38_dram_ikon21_mcstasscript       | latest   | f3e7c5dcfb01  | 46 hours ago  | 5.67GB   |   |
| 8.   |  trnielsen/jhub38_dram_ikon21_mcxtrace           | latest   | bfab68bd53ff  | 46 hours ago  | 5.72GB   |   |
| 9.   |  trnielsen/jhub38_dram_ikon21_sasview            | latest   | e191bdb2f372  | 46 hours ago  | 5.86GB   |   |
| 10.  |  trnielsen/jhub38_dram_ikon21_ase_extra          | latest   | e191bdb2f372  | 46 hours ago  | 6.01GB   |   |
| 11.  |  trnielsen/jhub38_dram_ikon21_nbextensions       | latest   | 268135670089  | 46 hours ago  | 6.07GB   |   |
| 12.  |  trnielsen/jhub38_dram_ikon21_updates            | latest   | c81ddd5d688c  | 46 hours ago  | 6.08GB   |   |
| 13.  |  trnielsen/jhub38_dram_ikon21_updates_scipp      | latest   | e191bdb2f372  | 46 hours ago  | 6.12GB   |   |


# Dependencies 
* Scipp : from master
* Scippneutron : from master
* Mantid : 

# Build
```console
$ time docker build --no-cache -t trnielsen/jhub38_dram_ikon21_scipp -f Dockerfile_jhub_py38_ikon21_scipp .
```

# Run Jupyter classical 
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it  trnielsen/jhub38_dram_ikon21_updates_scipp
```

# Run Jupyter lab 
* Not in this repo 
* Just added for showing how to start Lab.
```console
$ docker run --name test_notebooks -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v  ~/Desktop:/Desktop -it trnielsen trnielsen/jhub38_dram_sep2021_ds_nbgitpuller
```


# Docker Hub
* Sep. 26 2021 (plus/minus a few days) 
* Tag: trnielsen/jhub38_dram_ikon21_updates_scipp -> trnielsen/jhub_py38_ikon21_nb
* Pushed trnielsen/jhub_py38_ikon21_nb to docker hub
* https://hub.docker.com/r/trnielsen/jhub_py38_ikon21_nb

```console
$ docker pull trnielsen/jhub_py38_ikon21_nb
```



