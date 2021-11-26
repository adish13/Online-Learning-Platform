#!/usr/bin/bash
g++ -c mandelbrot.cpp
g++ mandelbrot.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system
./sfml-app