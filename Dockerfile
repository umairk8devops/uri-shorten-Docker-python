FROM python:3.6
COPY cleanuri.py  sourcelist.txt /tmp/
RUN apt update && apt install -y jq &&  pip3 install requests 
