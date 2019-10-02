FROM ubuntu:latest
COPY ./src/ /
RUN apt-get update \
 && apt-get install tcpdump -y \
 && apt-get install python -y \
 && apt-get install python-pip -y \
 && apt-get install python-mysqldb -y \
 && pip install bottle \
 && pip install beaker \
 && pip install pytest
EXPOSE 5000

CMD ["python","webcli.py"]
