from glob2 import glob


def search():
    f = glob(r'**/CX-P.exe')  # glob.glob表示glob模块下的glob函数
    print(f)


if __name__ == "__main__":
    search()
