FROM python:3.9.18-bookworm
RUN apt update
RUN apt install -y tcpdump
RUN apt install -y inetutils-tools
RUN apt install -y traceroute
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
ENV PORT 8080
ENV DEBUG_MODE 1
CMD ["gunicorn", "main:app", "--config=config.py"]