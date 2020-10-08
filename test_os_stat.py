import os
from time import sleep
from pathlib import Path
from loguru import logger


@logger.catch
def print_timestamps(tf):
    print(f'Path.stat().st_mtime: {tf.stat().st_mtime}')
    print(f'Path.stat().st_atime: {tf.stat().st_atime}')
    print(f'Path.stat().st_ctime: {tf.stat().st_ctime}')        
    print(f'os.stat(f).st_mtime: {os.stat(tf).st_mtime}')
    print(f'os.stat(f).st_atime: {os.stat(tf).st_atime}')
    print(f'os.stat(f).st_ctime: {os.stat(tf).st_ctime}')        
    print(f'os.path.getmtime(f): {os.path.getmtime(tf)}')
    print()
    return


@logger.catch
def main():
    tf = Path(Path.cwd(), "os_stat_test.tmp")
    print("Creating new file.")
    with open(tf, "w") as f:
        f.writelines("test")
    print_timestamps(tf)

    for q in range(2):
        print("Write another line to the file.")
        with open(tf, "a") as f:
            f.writelines("test")
        print_timestamps(tf)

        for i in range(3):
            print("Access the file")
            with open(tf, "r") as f:
                lns = f.readlines()
            print_timestamps(tf)
            sleep(2)

        sleep(2)
    return


main()
