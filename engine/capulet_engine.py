from engine.Engine import Engine

CapuletEngineMileage = 30000

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.mileage = CapuletEngineMileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.mileage
