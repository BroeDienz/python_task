import time
import threading

"""Tuang Air"""
# print ("Tuang Air")
def open_water_valve(water_system, seconds):
    water_added = 0
    time_elapsed = 0
    
    while time_elapsed < seconds:
        water_added += 100  # Add 100ml per second
        water_system["bucket"] += 100
        water_system["tank"] -= 100
        time_elapsed += 1
        # print(f"opening valve... bucket: {water_system['bucket']}ml")
        # print(f"tank: {water_system['tank']}ml")
    
    # print(f"valve open {seconds} seconds, total water added: {seconds * 100}ml")  
    return water_added
# print(f"valve open 5 seconds", 
    #   open_water_valve(water_system={"bucket":0, "tank":5000}, seconds=5))


def close_water_valve(water_system, target_fill=500):
    while water_system["bucket"] > target_fill:
        water_system["bucket"] -= 100
        # print(f"closing valve, bucket now: {water_system['bucket']}ml")
        
    if water_system["bucket"] > 0:
        water_system["bucket"] = target_fill
    else:
        water_system["bucket"] = 0
        
    # print (f"closed valve closed, bucket amounted to: {water_system['bucket']}ml")

    return water_system["bucket"]
# print(f"valve close whit targe fill", 
    #   close_water_valve(water_system={"bucket":800, "tank":5000}, target_fill=500))
    


"""masak air"""
def is_temperature_ok(current_temp):
    return 75 <= current_temp <= 80
# print(is_temperature_ok(90))
# print(is_temperature_ok(78))
# print (is_temperature_ok(60))

"""mie"""
def added_nodle(noodle_pcs):
    return noodle_pcs == 1
# print(added_nodle(1))

"""bumbu mie ayam"""
def add_ketchup(ketchup_ml):
    return (ketchup_ml == 3)

def add_sausage(sausage_pcs):
    return (sausage_pcs ==2)

def add_powder(powder_ml):
    return (powder_ml ==3)

# print(add_ketchup(3), add_sausage(2), add_powder(3))
# print(add_ketchup(3), add_sausage(2), add_powder(1))
# print(add_ketchup(3), add_sausage(3), add_powder(1))
# print(add_ketchup(13), add_sausage(22), add_powder(34))

# PART 2 Machine Control

"""isi air di ember"""
def fill_bucket(target_fill):
    total_filled =  0
    seconds = 0
    while total_filled < target_fill:
        total_filled += 100
        seconds += 1
    return seconds

seconds = fill_bucket(500)
# print(f"need {seconds} seconds to fill 500ml")

"""panaskan air"""
def heat_water(target_temp):
    current_temp = 25
    seconds =  0
    while current_temp < target_temp:
        current_temp += 5
        seconds += 1
    return seconds

seconds = heat_water(80)
# print(f"need {seconds} seconds to heat from 25c to 80c")


"""jaga temperatur air"""
def mantain_temperature(current_temp, target_temp):
    seconds = 0
    while current_temp != target_temp:
        if current_temp < target_temp:
            current_temp += 5
            seconds += 1
        elif current_temp > target_temp:
            current_temp -= 5
            seconds += 1
        time.sleep(0.5)
        # print(f"maintain temperature from {current_temp} to {target_temp}")
    return seconds 

# seconds = mantain_temperature(current_temp=50, target_temp=80)
# print(f"final temperature after maintain {seconds}C")


"""masak mie"""
def cook_noodle(cooking_seconds):
    cooking_time = 0
    seconds = 0
    while cooking_time < cooking_seconds:
        cooking_time += 1
        seconds += 1
        print (f"cooking... {seconds}s")
        time. sleep(0.5)
    return seconds
    
    
# cooking_time = 120
# seconds = cook_noodle(cooking_time)
# print(f"waktu masak  {cooking_time}detik, mie {seconds}")    


"""dispense mie dan bumbu"""
def dispense_nodle(noodle_pcs=1):
        add_noodle = 0
        while add_noodle < noodle_pcs:
            add_noodle += 1
            time.sleep(1)
            print(f"adding noodle {add_noodle}pcs")
        
        noodle = added_nodle(add_noodle)    
        return noodle
# print(f"dispense noodle", dispense_nodle())


def dispense_ketchup(ketchup_ml=3):
    added_ketchup = 0
    
    while added_ketchup < ketchup_ml:
        added_ketchup += 1
        print(f"adding ketchup {added_ketchup}ml")
        time.sleep(0.5)
    
    sesasoning1 = add_ketchup(added_ketchup)
 
    return sesasoning1
# print(f"dispense ketchup", dispense_ketchup(3))


def dispense_sausage(sausage_pcs=2):
    added_sausage = 0
    
    while added_sausage < sausage_pcs:
        added_sausage += 1
        print(f"adding sausage {added_sausage}pcs")
        time.sleep(0.5)
    
    sesasoning2 = add_sausage(added_sausage)
 
    return sesasoning2
# print(f"dispense sausage", dispense_sausage())


def dispense_powder(powder_t_spoon=3):
    added_powder = 0
    
    while added_powder < powder_t_spoon:
        added_powder += 1
        print(f"adding powder {added_powder}gr")
        time.sleep(0.5)
    
    sesasoning3 = add_powder(added_powder)
 
    return sesasoning3
# print(f"dispense powder", dispense_powder())


#PART 3 Complete Machine 

class WaterSystem:    #✅
    def __init__(self):
        self.tank = 5000
        self.bucket = 0
        self.current_temp = 25

    def open_water_valve(self, seconds):
        water_added = 0
        time_elapsed = 0
    
        while time_elapsed < seconds:
            water_added += 100  # Add 100ml per second
            self.bucket += 100
            self.tank -= 100
            time_elapsed += 1
            # print(f"opening valve... bucket: {self.bucket}ml")
            # print(f"tank: {self.tank}ml")
    
        # print(f"valve open {seconds} seconds, total water added: {seconds * 100}ml")  
        return water_added
        
    def close_water_valve(self, target_fill=500):
        while self.bucket > target_fill:
            self.bucket -= 100
            # print(f"closing valve, bucket now: {self.bucket}ml")
        
        if self.bucket > 0:
            self.bucket = target_fill
        else:
            self.bucket = 0
        
        # print (f"closed valve closed, bucket amounted to: {self.bucket}ml")

        return self.bucket
    
    
    def fill_bucket(self, target_ml):
        if self.bucket >= target_ml:
            print(f"bucket already {self.bucket}ml, (target {target_ml}ml)")
            return 0
        
        seconds= 0    
        standart_filled = self.bucket
        while standart_filled < target_ml:
            if self.tank >= 100:
                standart_filled += 100
                self.bucket += 100
                self.tank -= 100
                seconds += 1
                print(f"filling... bucket: {self.bucket}ml (filled for {seconds}s)")
                time.sleep(1)
            else:
                print("isi water tank dulu")
                self.tank += 5000
                print(f"isi water tank sampai {self.tank}ml")
        
        if self.bucket > target_ml:
            self.close_water_valve(target_fill=target_ml)
        return seconds

    
    def heat_water(self, target_temp):
        seconds =  0
        while self.current_temp < target_temp:
            self.current_temp += 5
            seconds += 1
            print(f"heating... current temp: {self.current_temp}C (tuned for {seconds}s)")
            time.sleep(1)
        return seconds
        
            
    def cool_down(self, target_temp):
        seconds = 0
        while target_temp < self.current_temp :
            self.current_temp -= 5
            seconds += 1
            print(f"cooling... current temp: {self.current_temp}C (cooled for {seconds}s)")
            time.sleep(2)
        return seconds


    def empty_bucket(self):
        self.bucket = 0
        time.sleep(1)
        return self.bucket

        
    def check_water_level(self):
        if self.tank >= 500:
            warning_messages = "Water level ok"
        else:
            warning_messages = "Water level low"
        return warning_messages

water_system = WaterSystem()

# seconds_needed = water_system.fill_bucket(500)
# print(f"water di bucket setelah diisi  {water_system.bucket}ml selama {seconds_needed} detik")
# print("="*50, "\n")

# print("="*15, "panaskan air", "="*15) 
# seconds_needed = water_system.heat_water(25)
# print(f"suhu air sekarang { water_system.current_temp}C setelah dipanaskan selama {seconds_needed} detik")
# print("="*50, "\n")

# print("="*15, "dinginkan air", "="*15) 
# seconds_needed = water_system.cool_down(25)
# print(f"temperatur air setelah didinginkan {water_system.current_temp}c selama {seconds_needed} detik")
# print("="*50, "\n")

# print("="*15, "water system status", "="*15) 
def get_water_status(water_system):
        time. sleep(0.5)
        return f"bucket: {water_system.bucket}ml\ntank: {water_system.tank}ml\ntemp: {water_system.current_temp}C\nmessage: {water_system.check_water_level()}"
# print(f"status water system", get_water_status(water_system))
# print("="*50, "\n")

class Dispenser:     #✅
    def __init__(self, name, capacity, ml_per_trigger=1):
        self.name = name        
        self.capacity_ml = capacity
        self.current_amount = capacity
        self.ml_per_trigger = ml_per_trigger

    
    def trigger(self, added):
        if self.current_amount >= added:
            self.current_amount -= added
            return added
        else:
            dispensed = self.current_amount
            self.current_amount = 0
            return dispensed                           
        
ketchup = Dispenser("ketchup", capacity=1000, ml_per_trigger=1)
takaran_ketchup = ketchup.trigger(0)
# print(f"dispensed ketchup:", takaran_ketchup)
# print(f"stock ketchup", ketchup.current_amount)

sausage = Dispenser("sausage", capacity=1000, ml_per_trigger=1)
takaran_sausage = sausage.trigger(0)
# print(f"dispensed sausage:", takaran_sausage)
# print(f"stock sausage", sausage.current_amount)

powder = Dispenser("powder", capacity=1000, ml_per_trigger=1)
takaran_powder = powder.trigger(0)
# print(f"dispensed powder:", takaran_powder)
# print(f"stock powder", powder.current_amount)

noodle = Dispenser("noodle", capacity= 50 , ml_per_trigger=1)
takaran_mie = noodle.trigger(0)
# print(f"dispensed noodle:", takaran_mie)
# print(f"stock noodle", powder.current_amount)

def get_dispenser_status(dispenser):
        time.sleep(0.5)
        return f"{dispenser.name} stock: {dispenser.current_amount} ml"

# print(f"status stock di mesin", get_dispenser_status(ketchup))
# print(f"status stock di mesin", get_dispenser_status(sausage))
# print(f"status stock di mesin", get_dispenser_status(powder))
# print(f"status stock di mesin", get_dispenser_status(noodle))

class Coocking(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def coock_noodle(self):
        #start cooking noodle for 120 seconds
        self.coock_status = cook_noodle(120)
            
    #dispense ketchup 3ml
    def add_ketchup(self):
        self.takaran_ketchup = ketchup.trigger(3)
        self.seasoning_added = dispense_ketchup(
            ketchup_ml=self.takaran_ketchup
        )
        
    #maintain temperature 75-80C
    def maintain_temp_up(self):
        self.matain_temp = mantain_temperature(
            current_temp=70, target_temp=80
        )
        
    #dispense sausage 2pcs
    def add_sausage(self):
        self.takaran_sausage = sausage.trigger(2)
        self.seasoning_added = dispense_sausage(
            sausage_pcs=self.takaran_sausage
        )
        
    #mantain temperature 95-80C
    def maintain_temp_down(self):
        self.mantain_temp = mantain_temperature(
            current_temp=100, target_temp=80)
        
    #dispense powder 3 gr
    def add_powder(self):
        self.takaran_powder = powder.trigger(3)
        self.seasoning_added = dispense_powder(
            powder_t_spoon=self.takaran_powder
        )
        
    def run(self):
        t1 = threading.Thread(target=self.coock_noodle, daemon=True)
        t2 = threading.Thread(target=self.add_ketchup, daemon=True)
        t3 = threading.Thread(target=self.maintain_temp_up, daemon=True)
        t4 = threading.Thread(target=self.add_sausage, daemon=True)
        t5 = threading.Thread(target=self.maintain_temp_down, daemon=True)
        t6 = threading.Thread(target=self.add_powder, daemon=True)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        
cooker = Coocking()
cooker.run()        

class NoodleMachine:
    def __init__(self):
        self.water_system = WaterSystem()
        self.dispensers = Dispenser("ketchup", capacity=1000)
        self.dispensers = Dispenser("sausage", capacity=1000)
        self.dispensers = Dispenser("powder", capacity=1000)
        self.dispensers = Dispenser("noodle", capacity=50)
        self.noodle_made = 0
        
    def get_machine_status(self):
        water_status = get_water_status(self.water_system)
        ketchup_status = get_dispenser_status(ketchup)
        sausage_status = get_dispenser_status(sausage)
        powder_status = get_dispenser_status(powder)
        noodle_status = get_dispenser_status(noodle)
        return f"💧{water_status}\n🍅{ketchup_status}\n🌭{sausage_status}\n🧂{powder_status}\n🍜{noodle_status}\nNoodle made: {self.noodle_made}"
        
    def make_noodle(self, add_water=500):
        print ("💧 add water with 500 ml")
        if not self.water_system.fill_bucket(add_water):
            print("❌ gagal membuat mie, air tidak cukup")
            return
        
        print("🔥 memanasakan air 80C")
        self.water_system.heat_water(80)
        
        print("🍝 masukan mie 1")
        self.takaran_mie = noodle.trigger(1)
        self.noodle_added = dispense_nodle(
            noodle_pcs=self.takaran_mie
        )
        
        print("⏰ memasak mie 2menit")
        self.cooking_status = cook_noodle(120)

        
        print("🍅 menambahkan ketchup 3ml")
        self.takaran_ketchup = ketchup.trigger(3)
        self.seasoning_added = dispense_ketchup(
            ketchup_ml=self.takaran_ketchup
        )
        
        print("🌭 menambahkan sausage 2pcs")
        self.takaran_sausage = sausage.trigger(2)
        self.seasoning_added = dispense_sausage(
            sausage_pcs=self.takaran_sausage
        )
        
        print("🧂 menambahkan powder 3gr")
        self.takaran_powder = powder.trigger(3)
        self.seasoning_added = dispense_powder(
            powder_t_spoon=self.takaran_powder
        )
        
        print("✅ mie ayam siap disajikan!")
        self.noodle_made += 1
        time.sleep(1)
        
        print("🧹clean bucket")
        self.water_system.empty_bucket()
        time.sleep(2)


# machine = NoodleMachine()
# print("🍜 INSTANT NOODLE MAKER MACHINE")
# print("="*50)
# time.sleep(1)

# print("\n📊 INITIAL STATUS:")
# print(machine.get_machine_status())
# print()
# print("="*50)

# print("\n" + "="*50)
# print("🍜 MAKING NOODLE #1...")
# print("="*50)
# machine.make_noodle()
# print("="*50)

# # print("\n" + "="*50)
# # print("🍜 MAKING NOODLE #2...")
# # print("="*50)
# # machine.make_noodle()
# # print("="*50)

# # print("\n" + "="*50)
# # print("🍜 MAKING NOODLE #3...")
# # print("="*50)
# # machine.make_noodle()
# # print("="*50)

# print("\n📊 FINAL STATUS:")
# print(machine.get_machine_status())