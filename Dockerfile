FROM scratch
ADD https://downloads.openwrt.org/chaos_calmer/15.05.1/x86/generic/openwrt-15.05.1-x86-generic-Generic-rootfs.tar.gz /
EXPOSE 80

RUN mkdir /var/lock && \
    opkg update && \
    opkg install python && \
    opkg install ca-certificates && \
    opkg install nano && \
    opkg install python-pip && \
    pip install autobahn incremental constantly zope.interface twisted
ENV SKY_ID=aabbxxbbaaaa
ADD ./agent.py /agent.py
CMD ["python", "/agent.py"]