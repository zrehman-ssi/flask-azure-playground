FROM ubuntu
RUN apt update && apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget && wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz && tar -xf Python-3.7.4.tar.xz && cd Python-3.7.4 && ./configure && make altinstall
WORKDIR /home/projects/flask-azure-playground
COPY . .
RUN pip3.7 --version
RUN python3.7 -m venv venv && source /venv/Scripts/activate && pip3.7 install -r requirements.txt