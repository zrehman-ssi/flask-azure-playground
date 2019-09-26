FROM ubuntu
RUN apt update && apt install -y build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    wget \
    && wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz \
    && tar -xf Python-3.7.4.tar.xz && cd Python-3.7.4 \
    && ./configure && make altinstall
ENV connection_string postgres://zeburrehman@rwhealthtech-srv:Netsolpk1!@rwhealthtech-srv.postgres.database.azure.com:5432/SIB_DB
WORKDIR /home/projects/flask-azure-playground
COPY . .
RUN python3.7 -m pip install --upgrade pip \
    && python3.7 -m venv venv 
CMD /home/projects/flask-azure-playground/venv/bin/pip3.7 install -r requirements.txt \
    && /home/projects/flask-azure-playground/venv/bin/uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app