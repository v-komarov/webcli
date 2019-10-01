FROM ubuntu:latest
COPY ./src/ /
RUN apt-get update \
 && apt-get install python -y \
 && apt-get install python-pip -y \
 && apt-get install python-mysqldb -y \
 && pip install bottle \
 && pip install beaker \
 && pip install gunicorn \
 && pip install pytest
CMD ["gunicorn","-b","0.0.0.0:8000","--workers", "5", "webcli:app"]
