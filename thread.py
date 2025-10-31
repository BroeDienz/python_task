import threading
import time


class CookingTry(threading.Thread):
    def __init__(self, fill_target, heat_target, ketchup_ml):
        threading.Thread.__init__(self)
        self.fill_target = fill_target
        self.heat_target = heat_target
        self.ketchup_ml = ketchup_ml
        self.current_temp = 20

        # Threads will be created in the run() method
    
    
    def fill_bucket(self, target_fill):
        total_filled =  0
        seconds = 0
        while total_filled < target_fill:
            total_filled += 100
            seconds += 1
            print(f"Filling bucket: {total_filled}ml, {seconds} seconds")
            time.sleep(1)
        return seconds


    def heat_water(self, target_temp):
        current_temp = 20
        seconds_needed = 0
        while current_temp < target_temp:
            current_temp += 1
            seconds_needed += 1
            print(f"Current temperature: {current_temp}C, {seconds_needed} seconds")
            time.sleep(1)
        return seconds_needed
        

    def dispense_ketchup(self, ketchup_ml):
        ketchup_current = 0
        seconds_to_add = 0
        while ketchup_current < ketchup_ml:
            ketchup_current += 1
            seconds_to_add += 1
            print(f"Adding ketchup: {ketchup_current}ml, {seconds_to_add} seconds")
            time.sleep(1)
        return seconds_to_add


    def run(self):
        t1 = threading.Thread(target=self.fill_bucket, args=(self.fill_target,), daemon=True)
        t2 = threading.Thread(target=self.heat_water, args=(self.heat_target,), daemon=False)
        t3 = threading.Thread(target=self.dispense_ketchup, args=(self.ketchup_ml,), daemon=True)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

cooker = CookingTry(fill_target=500, heat_target=30, ketchup_ml=3)
cooker.start()



## Example of simple threading with join()
# class Kiki(threading.Thread):
#     def __init__(self, time):
#         super(Kiki, self).__init__()
#         self.time = time
#         self.start()

#     def run(self):
#         print (self.time, " seconds start!")
#         for i in range(0,self.time):
#             time.sleep(1)
#             print ("1 sec of ", self.time)
#         print (self.time, " seconds finished!")


# t1 = Kiki(3)
# t2 = Kiki(2)
# t3 = Kiki(1)
# t1.join()
# print ("t1.join() finished")
# t2.join()
# print ("t2.join() finished")
# t3.join()
# print ("t3.join() finished")