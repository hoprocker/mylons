#!/usr/bin/python

import os
import re
import sys

CONFIG_FILES=[('bin/activate', 'HOMEDIR="%s"'),
                ('bin/activate.csh', 'setenv HOMEDIR "%s"'),
                ('bin/activate.fish', 'set -gx HOME_DIR "%s"')]

def setup():
    setup_bootstrap()
    setup_links()

def setup_bootstrap():
    _path = os.path.dirname(os.path.abspath(__file__))

    for f_name,pat in CONFIG_FILES:
        f = open("%s/%s" % (_path, f_name), "r")
        lines = map(lambda x: x.rstrip(), f.readlines())
        f = open("%s/%s" % (_path, f_name), "w+")
        re_pat = "^(.*)%s.*" % (pat[:pat.find("%s")],)
        for l in lines:
            if re.search(re_pat, l) != None:
                f.write("%s%s\n" % (re.search(re_pat, l).groups()[0], pat % (_path,)))
            else:
                f.write("%s\n" % (l,))
        f.close()

def setup_links():
    _path = os.path.dirname(os.path.abspath(__file__))
    search_paths = ["/usr/bin/python", "/usr/local/bin/python", "/sw/bin/python"]
    os.remove(os.path.join(_path, "bin/python"))
    for p in search_paths:
        if os.path.exists(p):
            print "linking %s -> %s" % (os.path.join(_path, "bin/python"), p)
            os.symlink(p, os.path.join(_path, "bin/python"))
            return

    print "couldn't find python!!! searched %s" % (search_paths,)
    sys.exit(-1)

if __name__ == "__main__":
    ## TODO : allow specification of path-to-python-bin
    setup()
