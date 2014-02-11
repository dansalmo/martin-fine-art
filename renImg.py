import os, sys, glob

path = os.path.split(sys.argv[1])[0]
for n, infile in enumerate(glob.glob(sys.argv[1])):
    try:
        newfile = '{}\\{:03}.jpg'.format(path, n)
        os.rename(infile, newfile)
        print newfile
    except IOError:
        print "cannot rename '%s'" % infile
            
