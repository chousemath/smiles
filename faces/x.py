import os

for fname in [x for x in os.listdir('.') if 'jpg' in x]:
    new_fname = fname.replace(' ', '').replace('.', 'xx').replace('(', '').replace(')', '') + '.jpg'
    os.rename(fname, new_fname)
