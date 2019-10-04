FROM ubuntu:latest
COPY ./src/ /
RUN apt-get update \
 && apt-get install tcpdump -y \
 && apt-get install python -y \
 && apt-get install python-pip -y \
 && apt-get install python-mysqldb -y \
 && pip install bottle \
 && pip install gunicorn \
 && pip install beaker \
 && pip install pytest
EXPOSE 5000

CMD ["gunicorn", "-w 5", "-b 0.0.0.0:5000", "webcli:app"]
