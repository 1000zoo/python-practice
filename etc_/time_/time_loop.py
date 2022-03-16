import time

SEC=1
MIN=60*SEC
HOUR=60*MIN
DAY=24*HOUR

def main():
    start = time.time()
    while time.time() - start < MIN:
        pass
    print("end", time.time() - start)

if __name__ == '__main__':
    main()