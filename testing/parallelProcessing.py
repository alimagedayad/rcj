from multiprocessing import Pool
from greenTiles import colorSensorGreen

def p1(a):
    x = 1
    print('F1 start!')
    while(True):
        x += 1

if __name__ == '__main__':
    with Pool(processes=2) as pool:
        r1 = pool.apply_async(p1, (1,))
        r2 = pool.apply_async(p1, (2,))
        print(r1.get(timeout=1))
        print(r2.get(timeout=1))