"""Tuang Air"""
print ("Tuang Air")
def open_water_valve(seconds):
    return seconds * 100
# print(open_water_valve(3))


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
    seconds = target_fill // 100
    return seconds

seconds = fill_bucket(300)
# print(f"need {seconds} seconds to fill 300ml")


def heat_water(target_temp=77, current_temp=25):
    seconds =  (target_temp - current_temp) //5
    return seconds
seconds = heat_water(80, 60)
print(f"need {seconds} seconds to heat from 25c to 80c")


def mantain_temperature(current_temp, target_temp=77):
    if current_temp < target_temp:
        return "panaskan"
    if current_temp > target_temp:
        return "dinginkan"
    else:
        return "jaga suhu"
# print(f"suhu 70", mantain_temperature(70, 77))
# print(f"suhu 85", mantain_temperature(85, 77))
# print(f"suhu 77", mantain_temperature(77, 77))


def cook_noodle(cooking_seconds):
    cooking_time = 120
    if cooking_seconds >= cooking_time:
        return "READY"
    else:
        return "COOKING"
    
# print(f"waktu masak 100 detik", cook_noodle(100))
# print(f"waktu masak 120 detik", cook_noodle(120))
# print(f"waktu masak 150 detik", cook_noodle(150))


def dispense_all_seasoning(ketchup_ml=3, sausage_ml=2, powder_ml=3):
    seasoning = add_seasoning(ketchup_ml, sausage_ml, powder_ml)
    return seasoning
seasoning = dispense_all_seasoning()
print(seasoning)


#complete machine 

class WaterSystem:
    def __init__(self):
        self.tank = 5000
        self.bucket = 0
        self.current_temp = 25

    def open_valve(self, seconds):
        water = seconds * 100
        self.bucket += water
        self.tank -= water
        
    def close_valve(self):
        if self.bucket > 0:
            self.bucket = 300
        else:
            self.bucket = 0
    
    def heat_up(self, seconds):
        self.current_temp += seconds * 5
        if self.current_temp > 100:
            self.current_temp = 100
            
    def cool_down(self, seconds):
        self.current_temp -= seconds * 50
        if self.current_temp < 25:
            self.current_temp = 25        

    def empty_bucket(self):
        self.bucket = 0
        
    def check_water_level(self):
        if self.tank >= 500:
            warning_messages = "Water level ok"
        else:
            warning_messages = "Water level low"
        return warning_messages

water_system = WaterSystem()
# water_system.open_valve(3)
# print(f"water di bucket", water_system.bucket)
# print(f"water di tank", water_system.tank)

water_system.close_valve()
# print(f"water setelah isi bucket ", water_system.bucket)
# print(f"water di tank setelah isi bucket", water_system.tank)

water_system.heat_up(11)
# 
# print(f"temperatur air setelah dipanaskan ", water_system.current_temp)

water_system.cool_down(1)
# print(f"temperatur air setelah didinginkan", water_system.current_temp)

def get_water_status(water_system):
        return f"bucket: {water_system.bucket}ml\ntank: {water_system.tank}ml\ntemp: {water_system.current_temp}C\nmessage: {water_system.check_water_level()}"
# print(f"status water system", get_water_status(water_system))

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


class NoodleMachine:
    def __init__(self):
        self.water_system = WaterSystem()
        self.disipensers = Dispenser("ketchup", capacity=1000)
        self.disipensers = Dispenser("sausage", capacity=1000)
        self.disipensers = Dispenser("powder", capacity=1000)
        self.disipensers = Dispenser("noodle", capacity=50)
        self.noodle_made = 0
        
    def get_machine_status(self):
        water_status = get_water_status(self.water_system)
        ketchup_status = get_dispenser_status(ketchup)
        sausage_status = get_dispenser_status(sausage)
        powder_status = get_dispenser_status(powder)
        noodle_status = get_dispenser_status(noodle)
        return f"💧{water_status}\n🍅{ketchup_status}\n🌭{sausage_status}\n🧂{powder_status}\n🍜{noodle_status}\nNoodle made: {self.noodle_made}"
        
    def make_noodle(self):
        print ("💧 add water 500ml")
        self.water_system.open_valve(5)
        
        print("🔥 memanasakan air 80C")
        self.water_system.heat_up(11)
        
        print("🍝 masukan mie 1")
        self.takaran_mie = noodle.trigger(1)
        
        print("⏰ memasak mie 2menit")
        self.cooking_status = cook_noodle(120)  
        
        print("🍅 menambahkan ketchup 3ml")
        self.takaran_ketchup = ketchup.trigger(3)
        
        print("🌭 menambahkan sausage 2")
        self.takaran_sausage = sausage.trigger(2)
        
        print("🧂 menambahkan powder 3ml")
        self.takaran_powder = powder.trigger(3)
        
        print("✅ mie ayam siap disajikan!")
        self.noodle_made += 1
        
        print("🧹 bucket")
        self.water_system.empty_bucket()


machine = NoodleMachine()
print("🍜 INSTANT NOODLE MAKER MACHINE")
print("="*50)

print("\n📊 INITIAL STATUS:")
print(machine.get_machine_status())
print()
print("="*50)

print("\n" + "="*50)
print("🍜 MAKING NOODLE #1...")
print("="*50)
machine.make_noodle()
print("="*50)

print("\n" + "="*50)
print("🍜 MAKING NOODLE #2...")
print("="*50)
machine.make_noodle()
print("="*50)

print("\n" + "="*50)
print("🍜 MAKING NOODLE #3...")
print("="*50)
machine.make_noodle()
print("="*50)

print("\n📊 FINAL STATUS:")
print(machine.get_machine_status())