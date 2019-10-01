#!/bin/sh

docker cp ./writefreecanal.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /writefreecanal.sql" radius
docker cp ./writecanal.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /writecanal.sql" radius
docker cp ./writemac.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /writemac.sql" radius
docker cp ./beforeauth.sql freeradiusdb:/
docker exec -it freeradiusdb mysql -ufreeradius -pfreeradius -Dradius -e "source /beforeauth.sql" radius
