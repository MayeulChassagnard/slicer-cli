# Slicer CLIs Item Tasks

Provides a docker image ready to be ingested by the item_tasks plugin from girder.


-----
## Getting started

Use the [Vagrantfile](https://github.com/girder/girder/tree/master/plugins/item_tasks/devops) from girder to provide a virtual machine configured to test the item_tasks plugin (`vagrant up`).

### Quick use

* go to [localhost:9080](http://localhost:9080)

* register and create an item

* configure task

* Use the image pushed on docker hub (mayeulchassagnard/slicer-cli) as the Docker image identifier and **["GaussianFilter"]** as the arguments to container for listening CLI and *RUN* it.

* Go to *Tasks*, then *slicer-cli* and provide a .nrrd file for instance.

### Developer use

* ssh to the vagrant box:
```sh
vagrant ssh
```

* Pull the image or build it from source
```sh
docker pull mayeulchassagnard/slicer-cli
```
```sh
git clone https://github.com/MayeulChassagnard/slicer-cli
docker build -t mayeulchassagnard/slicer-cli .
```

* Follow the [*Quick use* step](#quick-use) and uncheck *Pull image from Docker Hub prior to running*

