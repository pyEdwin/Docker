#Base
FROM python:3.11.3
#add app.py to the container
ADD app.py .
#install depedencies
RUN pip install requests

CMD [ "python" , "./app.py"]