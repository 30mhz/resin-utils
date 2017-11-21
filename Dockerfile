# Make shure docker is running, then execute:
# docker build -t resin-utils .
# docker run -it resin-utils

FROM python:2

RUN pip install git+https://github.com/resin-io/resin-sdk-python.git

COPY . /resin-utils

CMD ["python", "/resin-utils/start.py"]
