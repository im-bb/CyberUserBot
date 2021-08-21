# Sürətli və rahat qurulum üçün ;)

FROM gengkapak/impish:userbot

RUN git clone -b master https://github.com/FaridDadashzade/CyberUserBot /home/gengkapak/dclxvi/
RUN mkdir /home/gengkapak/dclxvi/bin/
WORKDIR /home/gengkapak/dclxvi/

EXPOSE 80 443

CMD ["python3","-m","userbot"]
