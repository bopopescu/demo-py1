import zlib

tests= b'hey hello hey hello to him hello to all hello again'
print(len(tests))

comps = zlib.compress(tests)
print(len(comps))