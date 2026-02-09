FROM docker.io/library/mysql:9.6.0-oraclelinux9

RUN microdnf update -y && \
    microdnf install systemd glibc-langpack-ja langpacks-ja -y && \
    microdnf clean all && \
    mkdir /setup

ENV LANG=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:ja \
    LC_ALL=ja_JP.UTF-8

COPY my.cnf /etc/mysql/conf.d/my.cnf

COPY /setup/ /setup/

