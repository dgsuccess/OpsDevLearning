

def readfilerev(fd):
    buff = 256
    fd.seek(0,2)
    size = fd.tell()
    rem = size % buff
    line = ''
    pos = -1
    while fd.tell() >0:
        fd.seek(pos,1)
        d = fd.read(1)
        if fd.tell() == 1:
            fd.seek(-1,1)
            yield d + line
        else:
            pos = -2
            if d != '\n':
                line = d + line
            else:
                yield line
                line = d

print [l for l in readfilerev(open('data'))]
 
