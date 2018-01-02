# Make shure docker is running, then execute:
# docker build -t resin-utils .
# docker run -it resin-utils

FROM python:2

RUN pip install git+https://github.com/resin-io/resin-sdk-python.git@v1.6.3

RUN pip install readchar

COPY . /resin-utils

CMD ["python", "/resin-utils/start.py"]
