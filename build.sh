#!/bin/bash

mkdir -p build
pushd build
c++ ../main.cpp -o cfbmanager -g
popd
