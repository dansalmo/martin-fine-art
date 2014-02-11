import os, sys, glob
import Image

size = 640, 640
for infile in glob.glob(sys.argv[1]):
    outfile = os.path.splitext(infile)[0] + ".lrg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
            
