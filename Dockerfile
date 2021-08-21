# Sürətli və rahat qurulum üçün ;)

FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git -y curl ffmpeg python3-pip opus-tools
RUN python3.9 -m pip install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN git clone https://github.com/FaridDadashzade/CyberUserBot /root/CyberUserBot
WORKDIR /root/CyberUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
