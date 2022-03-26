# coding=utf-8
import time

def check_addup(inlist, k):
    for i in range(len(inlist)-1):
        deduction = k - inlist[i]
        for j in range(i+1, len(inlist)):
            if deduction== inlist[j]:
                print('True')
                return True
                exit()
            else:
                pass
    print('Fasle')
    return False

if __name__=='__main__':
    inlist = list(map(int, input().strip().split()))

    k = int(input().strip())

    start_time = time.time()
    check_addup(inlist, k)
    print("----%s seconds----" % (time.time() - start_time))
        
