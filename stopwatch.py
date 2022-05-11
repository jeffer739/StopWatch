#import time
import time


print("Press ENTER to start the stopwatch")
print("press Ctrl+C to stop the stopwatch")

while True:
    try:
        input()
        start_time = time.time()
        print("Stopwatch Started..")

        except KeyboardInterrupt:
            print("Stopwatch Stopped..")
            end_time = time.time()
            total = round(end_time - start_time, 2)

            print(f"Total time is : {total} seconds")

            break
        
