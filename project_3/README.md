####  Handcrafting a Container Image

<h6>Create a lightsail server</h6>

- Create a Lightsail server with Ubuntu OS

<h6> Get and Run the Base Image</h6>

* Get the httpd from docker hub
> docker pull htttpd:2.4

* Run the container
> docker run  --name web_template -d httpd:2.4 

* Check the container is running
> docker ps

* Log into the container to make change
> docker exec -it web_template bash

* Install Git 
> apt update && apt install git

* Clone a repository to web_factory
>  git clone https://github.com/pyEdwin/web.git /temp/web_factory

* Check the files
> ls -l /temp/web_factory

* Remove the index.html from apache
> rm /htdocs/index.html