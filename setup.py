#!/usr/bin/python

import os
import re

CONFIG_FILES=[('bin/activate', 'HOME_DIR="%s"'),
                ('bin/activate.csh', 'setenv HOMEDIR "%s"'),
                ('bin/activate.fish', 'set -gx HOME_DIR "%s"')]
def setup():
    _path = os.path.dirname(os.path.abspath(__file__))

    for f_name,pat in CONFIG_FILES:
        f = open("%s/%s" % (_path, f_name), "r")
        lines = map(lambda x: x.rstrip(), f.readlines())
        f = open("%s/%s" % (_path, f_name), "w+")
        re_pat = "^(.*)%s.*" % (pat[:pat.find("%s")],)
        print re_pat
        for l in lines:
            if re.search(re_pat, l) != None:
                print re.search(re_pat, l).groups()
                f.write("%s%s\n" % (re.search(re_pat, l).groups()[0], pat % (_path,)))
            else:
                f.write("%s\n" % (l,))
        f.close()

if __name__ == "__main__":
    setup()
