import os

path_img = "BCCD/JPEGImages/"
for fn in os.listdir(path_img):
    if len(fn)>16:
        print(fn, fn[11:16])
        f_num = int(fn[11:16]) + 1
        src = path_img + fn
        dst = path_img + str(f_num) + ".jpg"
        print(dst)
        os.rename(src,dst)
print('done')