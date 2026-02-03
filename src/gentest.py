import random


with open("gentest.txt", "w", encoding="utf-8") as f:
    """Sinh testcase theo yêu cầu vào file gentest.txt"""
    
    # test1: 1_000_000 số nguyên tăng dân
    arr = sorted([random.randint(-100_000, 100_000) for _ in range(1_000_000)])
    f.write(" ".join(map(str, arr)) + "\n")
    
    # test2: 1_000_000 số nguyên giảm dần
    arr = sorted([random.randint(-100_000, 100_000) for _ in range(1_000_000)], reverse=True)
    f.write(" ".join(map(str, arr)) + "\n")
    
    # test3, 4, 5: 1_000_000 số nguyên ngẫu nhiên
    for _ in range(3):
        arr = [random.randint(-100_000, 100_000) for _ in range(1_000_000)]
        f.write(" ".join(map(str, arr)) + "\n")
        

    # test6: 1_000_000 số thực tăng dần
    arr = sorted([random.uniform(-100_000, 100_000) for _ in range(1_000_000)])
    f.write(" ".join(map(str, arr)) + "\n")
    # f.write(" ".join(format(x, ".3f") for x in arr) + "\n")
    
    # test7: 1_000_000 số thực giảm dần
    arr = sorted([random.uniform(-100_000, 100_000) for _ in range(1_000_000)], reverse=True)
    f.write(" ".join(map(str, arr)) + "\n")
    
    # test8, 9, 10: 1_000_000 số thực ngẫu nhiên
    for _ in range(3):
        arr = [random.uniform(-100_000, 100_000) for _ in range(1_000_000)]
        f.write(" ".join(map(str, arr)) + "\n")


