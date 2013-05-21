#!/bin/bash


octave --eval "jellyfishTopoGenerator(350)" &
appid=$!
sleep 2
kill $appid
