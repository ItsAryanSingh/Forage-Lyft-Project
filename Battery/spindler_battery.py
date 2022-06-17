from Battery.battery import Battery

SpindlerBatteryLife = 2

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.lastServiceDate = last_service_date
        self.currentDate = current_date

    def needs_service(self):
        return self.lastServiceDate.replace(year=self.lastServiceDate.year+SpindlerBatteryLife) < self.currentDate

