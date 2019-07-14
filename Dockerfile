FROM ubuntu:18.04
RUN apt-get -y update  &&  apt-get install -y  iptables git python3-pip python3-dev build-essential  && apt-get autoremove -y
COPY example_app /app
COPY requirements.txt /app
RUN pip3 install -r app/requirements.txt
CMD ["python3", "app/api.py"]
