# Conda constructor for the IKON20 Scipp dev container


## Conda constructor
* https://github.com/conda/constructor
* https://github.com/conda/constructor/blob/master/CONSTRUCT.md
* conda install constructor



## Docker
* Ubuntu 20.04 baseed
* See https://github.com/trnielsen/Docker/tree/master/jhub37_dram_ikon20
* https://github.com/trnielsen/Docker/commit/1cc93f04a68056f6b2b3b9abd2285935d1b9ebe8

## Background
* Sometime packages can not be found at anaconda (not inf memory depth)
* Use conda constructor to pack all conda packages into one sh script
* This can then be used to intall the Jhub IKON20 Scipp dev off line
* Pypi (pip) packages can not be put into the conda shell script
* Pypi (pip) packages can be downloaded and saved
* The script from_pip/download.sh will download the Pypi packages


## How-to use
* make constructor.ymal file
* use enviroment.yml file as base
* source activate base [Docker containers use base env]
* conda env export > enviroment.yml
* constructor .


