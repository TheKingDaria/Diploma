import sys
import re

testfile = sys.argv[1]
filename_out = sys.argv[2]

f = open(testfile, 'r')
datafile = ''.join(f.readlines())
f.close()
data = [ '{} {} 1\n'.format(cit[9:], ind[6:]) for cit, ind in 
        zip(re.findall(r'#citation\d+', datafile),
            re.findall(r'#index\d+', datafile))]
f = open(filename_out, 'w')
f.writelines(data)
f.close()

