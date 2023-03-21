


fname = input('enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

count = 0
for line in fh:
    
    if 'Fri, 04 Jan' in line:
        count = count + 1
        
        print (line)

print (count)