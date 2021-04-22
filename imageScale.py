#!/usr/bin/python
# -*-coding:utf-8-*-
# !python
import os, sys
import shutil
from PIL import Image

scale = 0.5

currentPath = os.getcwd()
input = os.path.join(currentPath, "input")
outPath = os.path.join(currentPath, "output")
if os.path.exists(outPath):
    shutil.rmtree(outPath)
os.makedirs(outPath)

# 匹配字符串末尾是包含某个字符串
def endWith(s, *endstring):
    # endswith()匹配字符串的开头或末尾是否包含一个字符串。匹配开头是startswith()
    # map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False

def get_recursive_file_list(path):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        if endWith(full_file_name, '.png') or endWith(full_file_name, '.jpg'):
            all_files.append(full_file_name)
        if os.path.isdir(full_file_name):
            next_level_files = get_recursive_file_list(full_file_name)
            all_files.extend(next_level_files)
    return all_files


if __name__ == '__main__':
    allPngArray = get_recursive_file_list(input)
    for png in allPngArray:
        if os.path.exists(png):
            print(png)
            dir, file = os.path.split(png)
            pathPart = dir.split(input + os.sep)
            outdir = os.path.join(outPath, pathPart[1])
            if not os.path.exists(outdir):
                os.makedirs(outdir)
            print("scaling   " + png)
            with Image.open(png) as im:
                width, height = im.size
                new_width = int(scale * width)
                new_height = int(scale * height)
                resized_im = im.resize((new_width, new_height))
                resized_im.save(os.path.join(outdir, file))
    print("scaling done!!!")
