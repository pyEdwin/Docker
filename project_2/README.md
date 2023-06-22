#### Lauch a Flask app with Docker

<h6> Environment setup</h6>

* mdkir project_2

* cd project_2

* pip install virtualenv

* virtualenv env

* env\Scripts\activate.bat 

* pip install flask

* insatll pastman

* Build the image

> docker image build -t project_2 .30

* Run the image

>  docker run -p 3000:3000 -d project_2