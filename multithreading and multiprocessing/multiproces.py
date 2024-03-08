import multiprocessing
from datetime import datetime
import time


def write_to_file(file_path, data):
    time.sleep(3)
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"Data written to {file_path}")


def main():
    file_p1 = 'file_1.txt'
    file_p2 = 'file_2.txt'
    file_p3 = 'file_3.txt'
    file_p4 = 'file_4.txt'

    data1 = 'Hello from Process 1!'
    data2 = 'Greetings from Process 2!'
    data3 = 'Greetings from Process 3!'
    data4 = 'Greetings from Process 4!'

    process1 = multiprocessing.Process(target=write_to_file, args=(file_p1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_p2, data2))
    process3 = multiprocessing.Process(target=write_to_file, args=(file_p3, data3))
    process4 = multiprocessing.Process(target=write_to_file, args=(file_p4, data4))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print("Main process continues execution.")


if __name__ == "__main__":
    print(datetime.now().time())
    main()
    print(datetime.now().time())
