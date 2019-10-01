#!/bin/sh

docker cp ./writefreecanal.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /writefreecanal.sql" radius
docker cp ./writecanal.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /writecanal.sql" radius
#docker cp ./iptvpackets.sql freeradiusdb:/
#docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /iptvpackets.sql" radius
