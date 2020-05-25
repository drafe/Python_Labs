#!/usr/bin/python
# -*- coding: UTF-8 -*-
import binascii
import io
import struct
import argparse
import os
from pathlib import Path


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', '-s', required=True)
    parser.add_argument('--dump', '-d', action='store_const', const=True)

    return parser


class MP3(object):
    __slots__ = ['__dump', '__header', '__title', '__artist', '__album', '__year', '__comment', '__zb', '__track',
                 '__genre']

    def __init__(self, atts, d=False):
        self.__header, self.__title, self.__artist, self.__album, self.__year, self.__comment, self.__zb, self.__track, self.__genre = atts
        self.__dump = d

    def __repr__(self):
        ret = "title['{}'], artist['{}'], album['{}'], year[{}]".format(
            self.__title.decode('windows-1251').rstrip('\x00\x20'),
            self.__artist.decode('windows-1251').rstrip('\x00\x20'),
            self.__album.decode('windows-1251').rstrip('\x00\x20'),
            self.__year.decode('windows-1251').rstrip('\x00\x20'))
        if not self.__dump:
            return ret
        return ret + ", dump[{}]".format(self.__dump)


class MP3_ID3v1(object):
    __slots__ = ['_path', '_files', '_dump', '__mp3s']
    mus_ext = ['.mp3']

    def __init__(self, source, dump):
        self.__mp3s = []
        if source[source.rfind('.'):] in self.mus_ext:
            self._path = ''.join(Path(source).parts[:-1])
            self._files = [Path(source).name, ]
        else:
            self._path = source
            self._files = self.__mus_files()
        pass
        for i in self._files:
            with open(os.path.join(self._path, i), 'rb') as mp3:
                mp3.seek(-128, io.SEEK_END)
                text = mp3.read()
                if text[:3] == b'TAG' and text[3:5] != b'\x00' * 2:
                    self.__mp3s.append(
                        MP3(struct.unpack('<3s30s30s30s4s28s1s1s1s', text), binascii.hexlify(text) if dump else False))

    def show_info(self):
        for m in self.__mp3s:
            print(m)

    def __mus_files(self):
        files = os.walk(args.source).__next__()[2]
        for f in files:
            if Path(f).suffix.lower() in self.mus_ext:
                yield f


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    try:
        if not (os.path.exists(args.source) or os.path.exists(os.path.abspath(args.source))):
            print('No such file or directory..')
            raise OSError
        id3 = MP3_ID3v1(args.source, args.dump)
        id3.show_info()
    except OSError:
        pass
    except Exception as e:
        print(e)
