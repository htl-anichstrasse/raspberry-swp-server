FROM python:3

MAINTAINER Joshua Winkler "josh@bemoty.dev"
WORKDIR /home/swp

COPY src .

CMD ["python", "server.py"]