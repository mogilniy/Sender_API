FROM ubuntu
RUN  apt-get update
RUN yes| apt-get install pip    
#RUN apt install ubuntu-desktop -y
#RUN  pip install python 
#RUN   apt-get install default-jre -y 
RUN pip install flask 
RUN pip install requests
COPY * /home/myapp/
COPY  ./dop_code /home/myapp/




