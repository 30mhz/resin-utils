#!/bin/bash

docker build -t resin-utils .
docker run -it resin-utils
