from os import walk
from shutil import copyfile
path = '/home/arturo/Documentos/cancerCNN/Dataset/DataSet/maligno'
# f = []
# dirpath, dirnames, filenames = walk(path)

# print(dirpath)
dst = '/home/arturo/Documentos/cancerCNN/Dataset/'
for (dirpath, dirnames, filenames) in walk(path):
    # f.extend(filenames)
    for name in filenames:
        # print(name)
        elements = name.split('-')
        zoom = elements[3]
        num = elements[4]
        # print(dirpath+'/'+name)
        # print('zoom = {} num={}'.format(zoom, num))
        # print(dst+zoom+'x/'+name)
        copyfile(dirpath+'/'+name, dst+zoom+'x/maligno/'+name)

        # break

print('Finish!!')
