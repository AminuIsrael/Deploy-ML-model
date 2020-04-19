FROM python:3.7

MAINTAINER aminu israel <aminuisrael2@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /src/app

# copy requirements.txt
COPY ./requirements.txt /src/app/requirements.txt

# install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# Generate pikle file
WORKDIR /src/app/ML_Model
RUN python model.py

# set work directory
WORKDIR /src/app

# set app port
EXPOSE 5001

ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 