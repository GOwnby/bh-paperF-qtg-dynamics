"""Compare a regenerated figure with the one shipped in the repository root: pixel dimensions (identical figure size and dpi), file sizes.
usage: python3 figcmp.py <regenerated.png> <shipped.png>      (pure Python, no imaging library)"""
import struct, sys, os

def dims(fn):
    with open(fn, 'rb') as f:
        h = f.read(24)
    assert h[:8] == b'\x89PNG\r\n\x1a\n', fn + ' is not a PNG file'
    return struct.unpack('>II', h[16:24])

a, b = sys.argv[1], sys.argv[2]
da, db = dims(a), dims(b)
print('%s  regenerated %dx%d px (%d bytes)   shipped %dx%d px (%d bytes)   dimensions %s' % (
    os.path.basename(a), da[0], da[1], os.path.getsize(a), db[0], db[1], os.path.getsize(b), 'identical' if da == db else 'DIFFERENT'))
