iFROM redhat/ubi8

RUN yum install -y python3 && \
    yum install -y python3-pip

RUN pip3 install Flask

COPY app.py .

CMD ["python3", "/app.py"]
