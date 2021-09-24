FROM amazonlinux
RUN yum install -y python3 python3-pip 
COPY app.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "./app.py" ]
