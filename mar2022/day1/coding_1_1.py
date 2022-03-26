# coding=utf-8
import time

def check_addup(inlist, k):
    residual_set = set()

    for i in range(len(inlist)-1):
        deduction = k - inlist[i]
        residual_set.add(deduction)
        if inlist[i+1] in residual_set:
            print('True')
            return True
            exit()
        else:
            pass
    print('False')
    return False


if __name__=='__main__':
    inlist = list(map(int, input().strip().split()))

    k = int(input().strip())

    start_time = time.time()
    check_addup(inlist, k)
    print("----%s seconds----" % (time.time() - start_time))
        
