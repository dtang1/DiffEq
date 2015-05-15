import math
import sys
def euler(points,step,end,input):
	#x=2
	#y=1
	pts = points.split(',')
	x = float(pts[0])
	y = float(pts[1])
	t=0
	dt= float(step)
	end = int(end)
	#end = 4
	n=((end-x)/dt)
	#dydt = 'x^2-y^2'
	dydt = input
	dd = ''
	j = 0
	while j < len(dydt) + 1:
		tmp = dydt[j:j+1]
		print(tmp)
		if tmp not in '+-/*1234567890':
			if tmp not in 'xy':
				sys.exit("Syntax Error")
			elif(dydt[j+1:j+2] == '^'):
				dd+='pow(' + tmp + "," + dydt[j+2:j+3] + ")"
				j+=3
			else: 
				dd+=tmp
				j+=1
			#if (dydt[j:j+1] == 'l' && dydt[j:j+2] == 'n')
		else:
			dd += dydt[j:j+1]
			j+=1
		print(dd)

	output = ''
	for p in range(0, int(n)+1):
		output += "t"+str(p)+":" + str(t) + "\tx: "+ str(x) + "\ty: " + str(y)+"\n"
		y+=dt*(eval(dd))
		x+=dt
	print(output +' test')
	return output
