import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--set", nargs=2, help="display a square", type=str)

args = parser.parse_args()


def diff_dif_file(path):
    # 读取愿文件夹下面的所有的文件和文件夹
    file_dir = os.listdir(path)

    _dir = []
    _file = []

    # 文件家和文件和文件夹分类
    for df in file_dir:
        if os.path.isfile(path + "/" + df):
            _file.append(df)
        elif df == '.git' or df == '.idea':
            pass
        else:
            _dir.append(df)

    return [_dir, _file]


def recursive_write(src, tar):
    file_dir = diff_dif_file(src)

    file = file_dir[1]
    dir = file_dir[0]

    if len(file) == 0 and len(dir) == 0:
        return

    for sub_file in file:
        with open(src + "/" + sub_file, "r") as file_object:
            tar_file = open(tar + "/" + sub_file, 'w')
            lines = file_object.readlines()
            for line in lines:
                tar_file.write(line)

    # 建立文件夹
    for sub_dir in dir:
        tar_file_path = tar + "/" + sub_dir
        if not os.path.exists(tar_file_path):
            os.mkdir(tar_file_path)
        recursive_write(src + "/" + sub_dir, tar + "/" + sub_dir)


with open("setting.txt", 'r+') as file:
    if args.set:
        # 向设置文件中写入内容
        file.write(args.set[0] + "\n")
        file.write(args.set[1])
        print("\033[1;35m 成功设置用户搬运起始目标地址 \033[0m!")
    else:
        file = open("setting.txt", 'r')
        paths = file.readlines()
        recursive_write(paths[0].rstrip(), paths[1].rstrip())
