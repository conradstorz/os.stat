import os
from time import sleep
from pathlib import Path
from loguru import logger


@logger.catch
def main():
    tf = Path(Path.cwd(), "os_stat_test.tmp")
    print("Creating new file.")
    with open(tf, "w") as f:
        f.writelines("test")
    print(tf.stat())
    print(os.stat(tf))
    print()
    
    for q in range(2):
        print("Write another line to the file.")
        with open(tf, "a") as f:
            f.writelines("test")
        print(tf.stat())
        print(os.stat(tf))
        print()

        for i in range(3):
            print("Access the file")
            with open(tf, "r") as f:
                lns = f.readlines()
            print(tf.stat())
            print(os.stat(tf))                
            print()
            sleep(2)

        sleep(2)
    return


main()
