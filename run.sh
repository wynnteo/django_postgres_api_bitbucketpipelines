#!/bin/sh

cd /home/ec2-user 

aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 975049996552.dkr.ecr.ap-southeast-1.amazonaws.com 
docker-compose down &&
docker-compose pull &&
docker-compose build && 
docker-compose up -d