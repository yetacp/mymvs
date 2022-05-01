#!/bin/bash
sudo mount -t tmpfs -o size=384m tmpfs ./shadows
df -h | grep shadows
