#!/bin/bash

# """
# Part of update set for Resin used by 30MHz
#
# Plain script to easily build en start docker.
# Just to remember the commands ;)
#
# A: Fokko
# E: fokko@30MHz.com
# D: 20 Dec 2017
# """

docker build -t resin-utils .
docker run -it resin-utils
