#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import sys
import argparse
import os
import subprocess 
from pathlib import Path
#import ffmpeg

mus_ext = ['.mp3','.wav','.aif','.mid']

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--source',     '-s', required=True)
    parser.add_argument ('--destination','-d', default='mix.mp3')
    parser.add_argument ('--count',      '-c', default=-1, type=int)
    parser.add_argument ('--frame',      '-f', default=10, type=int)
    parser.add_argument ('--log',        '-l', action='store_const',const=True)
    parser.add_argument ('--extended',   '-e', action='store_const',const=True)
          
    return parser

def log (message):
    if args.log:
        print(message)

def mus_file():
    files = os.walk(args.source).__next__()[2]
    i = args.count if args.count != -1 else len(files)
    for f in files:
        if (i>0) and (Path(f).suffix.lower() in mus_ext):
            i -= 1
            yield f

def commands(i,m):
    name = 'temp{:05}.mp3'.format(i)
    rndm_start = '00:00:30'
    durat = '{2:02}:{1:02}:{0:02}'.format(args.frame%60,(args.frame//60)%60,
                                          args.frame//3600)    
    if args.extended:
        return ['ffmpeg', '-ss', rndm_start, '-t', durat,
                '-i', os.path.join(args.source, m), '-af',
                'afade=t=in:st=0:d={0:01},afade=t=out:st={1:01}:d={0:01}'.format(
                    args.frame*0.3,args.frame*(1-0.3)),    
                os.path.join(args.source, name)]
    else:
        return ['ffmpeg', '-ss', rndm_start, '-t', durat,
                '-i', os.path.join(args.source, m), '-acodec','copy',    
                os.path.join(args.source, name)]


def cut (musics):
    tempor = []
    for i,m in enumerate(musics):
        #print(commands(i,m))
        stdout, stderr = subprocess.Popen(commands(i,m), stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT).communicate()
        #print(stdout)

        #subprocess.Popen(cmnd, stdout=subprocess.PIPE,
         #                stderr=subprocess.STDOUT)
        log('--- processing file {}: {}'.format(i+1,m))
        tempor.append('temp{:05}.mp3'.format(i))
    return tempor

def glue(musics):
    log('--- mergering the frames...')
    with open('files.txt','w') as f:
        f.write('\n'.join(["file '{}'".format(
                            os.path.join(args.source, m)) for m in musics]))
        
    cmnd = ['ffmpeg','-f','concat','-safe','0',
            '-i', 'files.txt', '-acodec', 'copy',
            os.path.join(args.source, args.destination)]
    stdout, stderr = subprocess.Popen(cmnd, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT).communicate()
    #print(stdout)
    os.remove('files.txt')

def delete(musics):
    log('--- deleting temporary files...')
    for m in musics:
        os.remove(os.path.join(args.source, m))

if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    if not (os.path.exists(os.path.join(args.source,args.destination)) and
            input('File {} already exists. Override? [y/n]'.format(
            os.path.join(args.source,args.destination))) in 'nN') :
        try:
            os.remove(os.path.join(args.source,args.destination))
        except:
            pass
        try:
            music2cut = [m for m in mus_file()]
            #print(music2cut)
            pieces = cut(music2cut)
            glue(pieces)
            delete(pieces)
            log('--- done')
        except OSError as err:
            print('Smth get wrong.', err.args)
