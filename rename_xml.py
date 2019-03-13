import os

path_xml = "BCCD/Annotations/"
for fn in os.listdir(path_xml):
    if len(fn)>16:
        print(fn, fn[11:16])
        f_num = int(fn[11:16]) + 1
        src = path_xml + fn
        dst = path_xml + str(f_num) + ".xml"
        print(dst)
        os.rename(src,dst)
print('done')