# import library for multiprocessing
import multiprocessing

def power(x,y):
    print("pow({}, {}): {}".format(x, y, x**y))

def average(x,y):
    print("Average({}, {}): {}".format(x, y, (x+y)/2))

if __name__ == '__main__':
    # Create different Process for each task
    process1 = multiprocessing.Process(target = power, args = (2,3,))
    process2 = multiprocessing.Process(target = average, args = (2,3,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Done!")