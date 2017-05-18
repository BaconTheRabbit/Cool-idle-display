import string
def show(chicken,linepos=0):
    while 1:
            print(chicken)
            if linepos < chicken.count('')-1:
                    chicken = chicken[:linepos] + string.ascii_lowercase[string.ascii_lowercase.find(chicken[linepos])+1] + chicken[linepos+1:]
                    linepos += 1
            elif linepos == chicken.count('')-1 and chicken[linepos-1] == 'z':
                    linepos = 0
                    while linepos < chicken.count('')-1:
                            chicken = chicken[:linepos] + 'a' + chicken[linepos+1:]
                            linepos += 1
                            if linepos != chicken.count('')-1:
                                    print(chicken)
    ##		chicken = aline(linepos)
    ##		linepos = 0
            else:
                    linepos = 0
                    chicken = chicken[:linepos] + string.ascii_lowercase[string.ascii_lowercase.find(chicken[linepos])+1] + chicken[linepos+1:]
                    linepos += 1

def aline(num):
	aline = ''
	for a in range(0,num):
		aline += 'a'
	return aline
num = int(input("How many characters should the super-cool show be in? "))
show(aline(num))
