#!/usr/bin/env python

import re
import sys
import exrex
import random
import string
import json
from subprocess import call


prog = "./tests/test_rand"

if len(sys.argv) < 2:
  print("")
  print("usage: %s pattern [nrepeat]" % sys.argv[0])
  print("  where [nrepeat] is optional")
  print("")
  sys.exit(-1)

own_prog = sys.argv[0]
pattern = sys.argv[1]
if len(sys.argv) > 2:
  ntests = int(sys.argv[2])
else:
  ntests = 10
nfails = 0
repeats = ntests


try:
  repeats = int(sys.argv[2])
except:
  pass

r = 50
while r < 0:
  try:
    g = exrex.generate(pattern)
    break
  except:
    pass


sys.stdout.write("%-35s" % ("  pattern '%s': " % pattern))


while repeats >= 0:
  try:
    repeats -= 1
    example = exrex.getone(pattern)
    #print("%s %s %s" % (prog, pattern, example))
    ret = call([prog, "\"%s\"" % pattern, "\"%s\"" % example])
    if ret != 0:
      escaped = repr(example) # escapes special chars for better printing
      print("    FAIL : doesn't match %s as expected [%s]." % (escaped, ", ".join([("0x%02x" % ord(e)) for e in example]) ))
      nfails += 1

  except:
    #import traceback
    #print("EXCEPTION!")
    #raw_input(traceback.format_exc())
    ntests -= 1
    repeats += 1
    #nfails += 1

sys.stdout.write("%4d/%d tests succeeded \n" % (ntests - nfails, ntests))
#print("")

