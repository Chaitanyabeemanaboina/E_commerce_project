FROM python:3.10.8-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    gcc \
    python3-dev \
    default-libmysqlclient-dev

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
LABEL name=chaitanyabeemanaboina_ecommerce
#RUN set -ex \
##    && python manage.py migrate --verbosity 3 || exit 1
#COPY create_superuser.py .
#RUN python create_superuser.py
ENV mysql_config=/usr/bin/mysql_config

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#FROM python:3.10.8-slim
#
## Install system dependencies
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    default-libmysqlclient-dev \
#    gcc \
#    pkg-config \
#    python3-dev \
#    wget
#
## Set the working directory in the container
#WORKDIR /app
#
## Copy the requirements file into the container
#COPY requirements.txt .
#
## Install Python dependencies
#RUN pip install --upgrade pip && pip install -r requirements.txt
#
## Copy the rest of the application code into the container
#COPY . .
#
## Copy the wait_for_db.py script into the container
#COPY wait_for_db.py .
#
## Specify the command to run on container start
#CMD ["sh", "-c", "python wait_for_db.py && python manage.py runserver 0.0.0.0:8000"]
