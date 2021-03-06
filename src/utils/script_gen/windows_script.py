import re


def gen_script(content):
    m = re.search(r"\d", content)
    if not m:
        raise Exception("not match")
    return "dir /S \"*{}-{}*\"".format(content[:m.start()], content[m.start():])


def gen_windows_search(file_name):
    with open(file_name, 'r', encoding='UTF-8') as fp:
        content = fp.read()
        reg_ret = re.findall(r'[A-Z]{1,5}[0-9]{3}', content)
        ret = []
        for reg in reg_ret:
            if ret and reg == ret[-1]:
                continue
            ret.append(reg)
        ret = [gen_script(x) for x in ret]
    return ret


if __name__ == "__main__":
    print(*gen_windows_search('../../../data/files/cache.txt'), sep='\n', end='\n')
