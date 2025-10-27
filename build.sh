#!/bin/bash

mkdir -p build
pushd build
c++ ../main.cpp -o cfbmanager -g -I/usr/include/SDL2 -D_REENTRANT -L/usr/lib/x86_64-linux-gnu -lSDL2
popd
