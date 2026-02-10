FROM postgres:18.1-trixie

RUN mkdir /setup && \
  localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8

ENV LANG=ja_JP.utf8

COPY /setup/ /setup/
