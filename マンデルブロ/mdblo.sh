#!/bin/sh

echo "set term png;
set output \"mtest2.png\";
set grid;
set pm3d map;
set size square;
set terminal png size 48000, 36000;
splot \"mtest.png.data\"" | gnuplot

#openはmacで使える

exit 0
