from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input of the file is %r bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
raw_input("Ready, hit RETURN to continue or CTRL-C to abrort.")

out_file = open(to_file, 'w').write(indata)

print "Alrigth, all done."
