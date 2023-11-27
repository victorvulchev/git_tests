from multiprocessing import Process, current_process
import time

def print_info():
    process = current_process()
    print(f"Process Name: {process.name}, ID: {process.pid}")

if __name__ == "__main__":
    # Create a process
    my_process = Process(target=print_info)

    # Start the process
    my_process.start()

    # Wait for the process to finish
    my_process.join()
