#!/usr/bin/env python3
#//==========================================================================//
#// Copyright (c) 2012 Wen-Han Gu. All rights reserved.
#//
#// Author: Nowar Gu (Wen-Han Gu)
#// E-mail: wenhan.gu <at> gmail.com
#//
#// Any advice is welcome. Thank you!
#//==========================================================================//

import getopt
import tkinter
import sys

import Generator
import MainFrame

def showUsage():
  print("OVERVIEW: {0} ID Generator".format(sys.argv[0]), file=sys.stderr)
  print("USAGE: {0} [options]".format(sys.argv[0]), file=sys.stderr)
  print("OPTIONS:", file=sys.stderr)
  print("  -n, --no-window               do not show window",
        file=sys.stderr)


if __name__ == "__main__":
  try:
    OptList, Args = getopt.getopt(sys.argv[1:],
                                  "hn", ("help", "no-window=false"))
  except getopt.GetoptError as Err:
    print(Err, file=sys.stderr)
    print(file=sys.stderr)
    showUsage()
    sys.exit(2)

  FlagNoWindow = False

  for Opt, Answer in OptList:
    if Opt in ("-n", "--no-window"):
      FlagNoWindow = True
    else:
      showUsage()
      sys.exit(1)

  if (FlagNoWindow):
    print(Generator.Generator().gen())
    sys.exit(0)

  Master = tkinter.Tk(className="ID Generator")
  Gen = Generator.Generator()
  IDGenerator = MainFrame.MainFrame(Master, Gen)
  IDGenerator.mainloop()
