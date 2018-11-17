def find_max_count_ip(fn):
    with open(fn, 'r', encoding='utf8') as f:
        for ip in f:
            print(ip, end='')
            # TODO:

if "__main__" == __name__:
    find_max_count_ip('ip')
    # 找到出现次数最多前N个IP
