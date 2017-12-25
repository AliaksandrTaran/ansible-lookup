#!/bin/sh
sudo docker build -t test -f Dockerfile .
sudo docker run --name lookup -it -v $(pwd):/ansible/playbooks test
