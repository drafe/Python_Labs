import argparse
import os
import struct
import sys
import binascii

class SoundFile(object):
    def __init__(self, tag_="", name_="", artist_="", album_="", year_="", comment_="", genre_=""):
        self.tag = tag_
        self.name = name_
        self.artist = artist_
        self.album = album_
        self.year = year_
        self.comment = comment_
        self.genre = genre_
        
class ID3v1Decoder(object):
    def __init__(self, path, d_):
        self.__tracks = []
        self.__files = os.listdir(path)
        self.__d = d_
        if d_:
            self.__hex = []
            self.__hexdecode()
        self.__decode()
    
    def __decode(self):
        for file in self.__files:
            with open(os.path.join(path, file), 'rb') as mp3:
                mp3.seek(-128, 2)
                tag = mp3.read()
                sf = SoundFile()
                sf.tag, sf.name, sf.artist, sf.album, sf.year, sf.comment, sf.genre = struct.unpack("!3s30s30s30s4s30sb", tag)
                self.__tracks.append(sf)
        
    def __hexdecode(self):
        for file in self.__files:
            val = bytearray()
            with open(os.path.join(path, file), 'rb') as mp3:
                mp3.seek(-128, 2)
                while True:
                    current_byte = mp3.read(1)
                    if (not current_byte):
                        break
                    val += current_byte
            self.__hex.append(binascii.hexlify(val))
        
    def show(self):
        i = 0
        for track in self.__tracks:
            if self.__d:
                print (self.__hex[i])
                i += 1
            print('[ ' + track.artist.decode('windows-1251').rstrip('\x00') + " ]  -  [ " +
                track.name.decode('windows-1251').rstrip('\x00') + " ]  -  [ " +
                track.album.decode('windows-1251').rstrip('\x00') + " ]")
                  
if __name__ == '__main__':
    path = sys.argv[1]
    d = False
    if sys.argv[-1] == '-d':
        d = True
    idv3 = ID3v1Decoder(path, d)
    idv3.show()