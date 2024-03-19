The iplocation.py tool can also be used from inside a docker container

to use this command perform the following steps.

from inside this folder type:

### build docker container
docker build . -t iplocation
### run docker container in detached mode
docker run -d iplocation
### To run the iplocation command you will need to know the name of the container that is now running
export container=`docker ps | grep iplocation | awk '{print $1}'`
### connect to shell inside new container
docker exec -ti $container /bin/sh
### run command from inside container
python ./iplocation.py -i <IP_ADDRESS> -a <API_KEY>
### exit container
exit
### close container
docker stop $container