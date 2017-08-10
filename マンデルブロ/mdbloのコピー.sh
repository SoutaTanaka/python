#!/bin/sh

echo "set term png;
set output \"mtest2.png\";
set grid;
set pm3d map;
set size square;
splot \"mtest.png.data\"" | gnuplot


exit 0


