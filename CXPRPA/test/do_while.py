# 当次循环正常结束的时候才会执行else中的语句（如果当次循环执行了break，那么else不会执行）。
    # 注意：for j的else中的continue是对for i起作用的，而不是for j。
    # for i in range(1, 10):
    #     logger.info("i:   " + str(i))
    #     for j in range(1, 10):
    #         logger.info("j:   " + str(j))
    #         if j == 2:
    #             break
    #     else:
    #         continue
    #     break