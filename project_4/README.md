#### Use Docker for building a Node/Express app with a Mongo & Redis database
-------------------------------------------------------------------------
<h5>Workflow for running the app with Node on the local machine</h5>

- Create a directory NODE-DOCKER
> mkdir NODE-DOCKER

- Get JSON file package
> npm init -y

- Install Express
> npm install express

- Create index.js file

- Start the app
> node index.js

#### Containerize the app
-------------------------------------------------------------------------
- Create a custom image ( Dockerfile )
> docker build . / docker image build -t node_app_image .

- Check the image
> docker image ls

- Delete the image
> docker image rm  

- Run the image
> docker run -d --name node_app node_app_image / docker run -p 3000:3000 -d --name node_app node_app_iamge

- Check running containers
> docker ps

- Delete the container
> docker rm node_app -f

- Enter a container 
> docker exec -it node_app bash

- Exit the container
> exit

Create a .dockerignore file
