#!/bin/bash


octave --eval "jellyfishTopoGenerator(400)" &
appid=$!
sleep 2
kill $appid
