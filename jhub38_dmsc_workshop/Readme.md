# Docker files for DMSC workshop May 2022
* 9 May - 10 May
* Only scipp

# Depends on
* See https://github.com/trnielsen/Docker/tree/master/jhub38_dram_ikon21
* See https://github.com/trnielsen/Docker/blob/master/jhub38_dram_ikon21/Dockerfile_from_docker_stacks_py38


# Build
```console
$ time docker build --no-cache -t trnielsen/dmsc_workshop_scipp -f Dockerfile_ikon21_scipp .
```

# Run Jupyter classical 
```console
$ docker run --name test_notebooks -p 8888:8888 -v  ~/Desktop:/Desktop -it  trnielsen/dmsc_workshop_scipp
```

# Run Jupyter lab 
* Not in this repo 
* Just added for showing how to start Lab.
```console
$ docker run --name test_notebooks -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v  ~/Desktop:/Desktop -it trnielsen/dmsc_workshop_scipp
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
* April 26 2022 
* Pushed trnielsen/jhub_py38_dmsc_workshop:latest to docker hub
* https://hub.docker.com/r/trnielsen/jhub_py38_dmsc_workshop

```console
$ docker pull trnielsen/jhub_py38_dmsc_workshop
```


