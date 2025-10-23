import time

"""Tuang Air"""
print ("Tuang Air")
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


"""bumbu mie ayam"""
def add_seasoning(ketchup_ml, sausage_ml, powder_ml):
    return (ketchup_ml == 3 and sausage_ml ==2 and powder_ml ==3)
# print(add_seasoning(3,2,3))
# print (add_seasoning(2,2,3))
# print (add_seasoning(4,2,3))


#machine control

def fill_bucket(target_fill):
    total_filled =  0
    seconds = 0
    while total_filled < target_fill:
        total_filled += 100
        seconds += 1
    return seconds

seconds = fill_bucket(500)
# print(f"need {seconds} seconds to fill 500ml")

def heat_water(target_temp):
    current_temp = 25
    seconds =  0
    while current_temp < target_temp:
        current_temp += 5
        seconds += 1
    return seconds

seconds = heat_water(80)
# print(f"need {seconds} seconds to heat from 25c to 80c")


def mantain_temperature(current_temp, target_temp):
    while current_temp != target_temp:
        if current_temp < target_temp:
            current_temp += 5
        elif current_temp > target_temp:
            
            current_temp -= 50
    # print(f"maintain temperature at {target_temp}")
    return current_temp 

# print (f"maintain temperature", mantain_temperature(90, 80))


def cook_noodle(cooking_seconds):
    cooking_time = 120
    seconds = 0
    
    while seconds < cooking_seconds:
        seconds += 1
    if seconds >= cooking_time:
        return "READY"
    else:
        return "COOKING"
    
seconds = cook_noodle(120)
# print(f"waktu masak 120 detik", seconds)    


def dispense_all_seasoning(ketchup_ml=3, sausage_ml=2, powder_ml=3):
    add_ketchup = 0
    add_sausage = 0
    add_powder = 0
    
    while add_ketchup < ketchup_ml:
        add_ketchup += 1
        print(f"adding ketchup {add_ketchup}ml")
    
    while add_sausage < sausage_ml:
        add_sausage += 1
        # print(f"adding sausage {add_sausage}pcs")
    
    while add_powder < powder_ml:
        add_powder += 1
        # print(f"adding powder {add_powder}gr")
    
    sesasoning = add_seasoning(add_ketchup, add_sausage, add_powder)
    time.sleep(1)
    return sesasoning                            
print(f"dispense all seasoning", dispense_all_seasoning())

#complete machine 

class WaterSystem:
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
        return seconds
            
    def cool_down(self, target_temp):
        seconds = 0
        while target_temp < self.current_temp:
            self.current_temp -= 5
            seconds += 1
            print(f"cooling... current temp: {self.current_temp}C (cooled for {seconds}s)")      

    def empty_bucket(self):
        self.bucket = 0
        
    def check_water_level(self):
        if self.tank >= 500:
            warning_messages = "Water level ok"
        else:
            warning_messages = "Water level low"
        return warning_messages

water_system = WaterSystem()

seconds_needed = water_system.fill_bucket(500)
print(f"water di bucket setelah diisi  {water_system.bucket}ml selama {seconds_needed} detik")

seconds_needed = water_system.heat_water(80)
print(f"suhu air sekarang { water_system.current_temp}C setelah dipanaskan selama {seconds_needed} detik")

seconds_needed = water_system.cool_down(1)
# print(f"temperatur air setelah didinginkan {water_system.current_temp}")

def get_water_status(water_system):
        return f"bucket: {water_system.bucket}ml\ntank: {water_system.tank}ml\ntemp: {water_system.current_temp}C\nmessage: {water_system.check_water_level()}"
print(f"status water system", get_water_status(water_system))

class Dispenser: 
    def __init__(self, name, capacity, ml_per_trigger=1):
        self.name = name        
        self.capacity_ml = capacity
        self.current_amount = capacity
        self.ml_per_trigger = ml_per_trigger

    def trigger(self, times):
        used = times * self.ml_per_trigger
        self.current_amount -= used
        return used
        
        
ketchup = Dispenser("ketchup", capacity=1000, ml_per_trigger=1)
# takaran_ketchup = ketchup.trigger(0)
# print(f"dispensed ketchup:", takaran_ketchup)
# print(f"stock ketchup", ketchup.current_amount)

sausage = Dispenser("sausage", capacity=1000, ml_per_trigger=1)
# takaran_sausage = sausage.trigger(0)
# print(f"dispensed sausage:", takaran_sausage)
# print(f"stock sausage", sausage.current_amount)

powder = Dispenser("powder", capacity=1000, ml_per_trigger=1)
# takaran_powder = powder.trigger(0)
# print(f"dispensed powder:", takaran_powder)
# print(f"stock powder", powder.current_amount)

noodle = Dispenser("noodle", capacity= 50 , ml_per_trigger=1)
# takaran_mie = noodle.trigger(0)
# print(f"dispensed noodle:", takaran_mie)
# print(f"stock noodle", powder.current_amount)

def get_dispenser_status(dispenser):
        return f"{dispenser.name} stock: {dispenser.current_amount} ml"

# print(f"status stock di mesin", get_dispenser_status(ketchup))
# print(f"status stock di mesin", get_dispenser_status(sausage))
# print(f"status stock di mesin", get_dispenser_status(powder))
# print(f"status stock di mesin", get_dispenser_status(noodle))


# class NoodleMachine:
#     def __init__(self):
#         self.water_system = WaterSystem()
#         self.disipensers = Dispenser("ketchup", capacity=1000)
#         self.disipensers = Dispenser("sausage", capacity=1000)
#         self.disipensers = Dispenser("powder", capacity=1000)
#         self.disipensers = Dispenser("noodle", capacity=50)
#         self.noodle_made = 0
        
#     def get_machine_status(self):
#         water_status = get_water_status(self.water_system)
#         ketchup_status = get_dispenser_status(ketchup)
#         sausage_status = get_dispenser_status(sausage)
#         powder_status = get_dispenser_status(powder)
#         noodle_status = get_dispenser_status(noodle)
#         return f"💧{water_status}\n🍅{ketchup_status}\n🌭{sausage_status}\n🧂{powder_status}\n🍜{noodle_status}\nNoodle made: {self.noodle_made}"
        
#     def make_noodle(self, add_water=500):
#         print ("💧 add water with 500 ml")
#         if not self.water_system.fill_bucket_cooking(add_water):
#             print("❌ gagal membuat mie, air tidak cukup")
#             return
#         time.sleep(3)
        
#         print("🔥 memanasakan air 80C")
#         self.water_system.heat_up(11)
#         time.sleep(4)
        
#         print("🍝 masukan mie 1")
#         self.takaran_mie = noodle.trigger(1)
#         time.sleep(1)
        
#         print("⏰ memasak mie 2menit")
#         self.cooking_status = cook_noodle(120)
#         time.sleep(5)  
        
#         print("🍅 menambahkan ketchup 3ml")
#         self.takaran_ketchup = ketchup.trigger(3)
#         time.sleep(0.3)
        
#         print("🌭 menambahkan sausage 2")
#         self.takaran_sausage = sausage.trigger(2)
#         time.sleep(0.3)
        
#         print("🧂 menambahkan powder 3ml")
#         self.takaran_powder = powder.trigger(3)
#         time.sleep(0.3)
        
#         print("✅ mie ayam siap disajikan!")
#         self.noodle_made += 1
#         time.sleep(1)
        
#         print("🧹 bucket")
#         self.water_system.empty_bucket()
#         time.sleep(2)


# machine = NoodleMachine()
# print("🍜 INSTANT NOODLE MAKER MACHINE")
# print("="*50)

# print("\n📊 INITIAL STATUS:")
# print(machine.get_machine_status())
# print()
# print("="*50)

# print("\n" + "="*50)
# print("🍜 MAKING NOODLE #1...")
# print("="*50)
# machine.make_noodle()
# print("="*50)

# print("\n" + "="*50)
# print("🍜 MAKING NOODLE #2...")
# print("="*50)
# machine.make_noodle()
# print("="*50)

# print("\n" + "="*50)
# print("🍜 MAKING NOODLE #3...")
# print("="*50)
# machine.make_noodle()
# print("="*50)

# print("\n📊 FINAL STATUS:")
# print(machine.get_machine_status())