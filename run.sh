#!/bin/sh
docker build --rm --label  skywifipro/vap:${1} -q .