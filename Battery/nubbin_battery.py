from Battery.battery import Battery

NubbinBatteryLife = 4

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.lastServiceDate = last_service_date
        self.currentDate = current_date

    def needs_service(self):
        return self.lastServiceDate.replace(year=self.lastServiceDate.year+NubbinBatteryLife) < self.currentDate