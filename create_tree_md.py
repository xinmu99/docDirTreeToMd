#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
'''
##creat md contents :

- [1.1. .temp.userdb](/.temp.userdb)
- [1.2. build](/build)
    - [1.2.1. bopomofo.prism.bin](/build\bopomofo.prism.bin)
    - [1.2.2. bopomofo.schema.yaml](/build\bopomofo.schema.yaml)
    - [1.2.3. bopomofo_tw.prism.bin](/build\bopomofo_tw.prism.bin)
    - [1.2.4. bopomofo_tw.schema.yaml](/build\bopomofo_tw.schema.yaml)
'''

import os
import codecs


def filedir_tree(_path, md_strs, filter_f=None, root=None, lev=0, index="1."):
    root = root or _path

    dirs = os.listdir(_path)
    if filter_f:
        dirs = filter(filter_f, dirs)

    for i, file_name in enumerate(dirs):

        file_path = os.path.join(_path, file_name)
        rel_p = os.path.relpath(file_path, root)
        ste = formatstr.format(space=' '*4*lev,
                               ordrn=index + "%d. " % (i+1),
                               name=file_name,
                               path=rel_p
                               )
        md_strs.append(ste)

        if os.path.isdir(file_path):
            dirs[i] = filedir_tree(
                file_path, md_strs,
                root=root, lev=lev+1,
                index=index + "%d." % (i+1)
            )

    return dirs


def creat_contens(path=None, format=None, filter_f=None):
    filter_f = filter_f or filter_f_d
    if not path:
        path = os.getcwd()

    md_strs = []
    filedir_tree(path, md_strs, filter_f=filter_f)
    md_strs = "\n".join(md_strs)

    with codecs.open(path+"/sidebar.md", 'w', encoding='utf8') as f:
        f.write(md_strs)
    return md_strs


formatstr = '''{space}- [{ordrn}{name}](/{path})'''

def filter_f_d(x): return x.split('.')[-1] not in {"py"}

if __name__ == '__main__':
    md_strs = creat_contens()
    print(md_strs)
