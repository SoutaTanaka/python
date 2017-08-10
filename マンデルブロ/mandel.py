# -*- coding: utf-8 -*-
import sys

def mandelbrot(c, K, LOOPMAX):
	#発散まで回したループ数を返す
	n = 0
	z = 0.0 + (0.0 * 1j)
	while (n<LOOPMAX and abs(z)<K):
		z = z**2 + c
		n += 1
	return n

def getArg():
	#コマンドライン引数用関数
	argv = sys.argv
	argc = len(argv)
	if (argc != 9):
		#引数がない場合は終了
		print ('Usage: python %s filename '
			'minReal maxReal minImage maxImage step loop emission') %argv[0]
		quit()
	return argv

def main():
	argv = getArg()

	writer = open(argv[1], 'w')

	loop = int(argv[7]); K = float(argv[8])

	step = float(argv[6])
	x_min = float(argv[2]); x_max = float(argv[3])
	y_min = float(argv[4]); y_max = float(argv[5])

	x = x_min
	while (x < x_max):
		y = y_min
		while (y < y_max):
			c = x + (y * 1j)
			n = mandelbrot(c, K, loop)
			writer.write(str(c.real)+'\t'+str(c.imag)+'\t'+str(n)+'\n')
			y += step
		writer.write('\n')
		x += step
	print x_max

if __name__ == '__main__':
	main()
