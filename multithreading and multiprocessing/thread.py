import threading
from datetime import datetime
import time


def read_files(file_path):
    time.sleep(3)
    with open(file_path, "r") as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}")


def main():
    file_p1 = 'file_1.txt'
    file_p2 = 'file_2.txt'
    file_p3 = 'file_3.txt'
    file_p4 = 'file_4.txt'

    thread_1 = threading.Thread(target=read_files, args=(file_p1,))
    thread_2 = threading.Thread(target=read_files, args=(file_p2,))
    thread_3 = threading.Thread(target=read_files, args=(file_p3,))
    thread_4 = threading.Thread(target=read_files, args=(file_p4,))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    print("Main thread continues execution.")


if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())