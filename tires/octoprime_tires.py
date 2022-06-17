from tires.Tires import Tires

octoprimeTiresNetWearValue = 3

class OctoprimeTires(Tires):
    def __init__(self, tire_readings):
        self.tire_readings = tire_readings
        self.netwearValue = 3

    def needs_service(self):
        return sum(self.tire_readings) >= self.netwearValue