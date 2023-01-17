from os.path import join, abspath

tpath = join('.', 'Data', 'sudoky3.txt')
print(tpath)
tpath = abspath(tpath)
print(tpath)
with open(tpath, 'rt', encoding = 'utf-8') as src:
    for line in src:
        print(line)