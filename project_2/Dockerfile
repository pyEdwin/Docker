FROM ubuntu:20.04
RUN apt update
RUN apt install python3 -y
RUN apt -y install python3-pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["flask" , "run" ,"--host=0.0.0.0"]