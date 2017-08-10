#!/bin/sh
#引数チェック
if [ $# -ne 8 ]; then
	echo "Usage: $0 filname minReal maxReal minImage maxImage step loop emission" 1>&2
	exit 1
fi

#pythonによるマンデルブロ集合データ出力
python mandel.py $1.data $2 $3 $4 $5 $6 $7 $8

# #gnuplotによるプロット
echo "set term png;
set output \"$1\";
set grid;
set pm3d map;
set size square;
set terminal png size 48000, 36000;
splot \"$1.data\"" | gnuplot

#openはmacで使える
open $1

exit 0
