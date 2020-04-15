#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import sys
import argparse
import os
import datetime
import shutil

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--source', required=True)
    parser.add_argument ('--days', type=int, required=True)
    parser.add_argument ('--size', type=int, required=True)
         
    return parser

def date (file):
    t = os.path.getmtime(os.path.join(namespace.source,file))
    return datetime.datetime.fromtimestamp(t)

def size (file):
    return os.stat(os.path.join(namespace.source,file)).st_size    
    

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
     
    print (namespace)

    today = datetime.datetime.now()
    files = os.walk(namespace.source).__next__()[2]
    [print('{} t: {} s: {}b delta: {}'
           .format(f, date(f), size(f),(today - date(f)).days)) for f in files]
    small = [f for f in files if size(f) < namespace.size]
    arch = [f for f in files if (today - date(f)).days > namespace.days]

    if small:
        try:
            print('Files {} will be moved to ..\\Small\\'.format(small))
            if (not os.path.exists(os.path.join(namespace.source,'Small'))):
                os.mkdir(os.path.join(namespace.source,'Small'))
            [shutil.copy(os.path.join(namespace.source,s),
                        os.path.join(namespace.source,'Small',s))
             for s in small]
        except OSError(args): 
            print('Smth get wrong. ', args)
        else:
            print('Files was moved successfully')
        
    if arch:
        try:
            print('Files {} will be moved to ..\\Archive\\'.format(arch))
            if (not os.path.exists(os.path.join(namespace.source,'Archive'))):
                os.mkdir(os.path.join(namespace.source,'Archive'))
            [shutil.copy(os.path.join(namespace.source,a),
                        os.path.join(namespace.source,'Archive',a))
             for a in arch]
        except OSError as err: 
            print('Smth get wrong. ', err.args)
        else:
            print('Files was moved successfully')
            
    try:
        allfiles2delete = small + [f for f in arch if not(f in small)]
        
        if allfiles2delete:
            print('Files {} will be deleted from {}'
                            .format(allfiles2delete,namespace.source))
            [os.remove(os.path.join(namespace.source,f)) for f in allfiles2delete]
            print('Files removed successfully')
    except (IOError, OSError) as er:
        print('Smth get wrong. ', er.args)
        