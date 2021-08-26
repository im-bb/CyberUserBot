# Sürətli və rahat qurulum üçün ;)

FROM cyberuserbot/cyberspaceaz:latest
RUN git clone https://github.com/FaridDadashzade/CyberUserBot/ /root/CyberUserBot/blob/cyberdev
WORKDIR /root/CyberUserBot/blob/cyberdev
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
