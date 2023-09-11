from abc import ABC
from car import Car
from battery import battery, spindler_battery, nubbin_battery 
from engine import engine, capulet_engine, willoughby_engine, sternman_engine 

class CarFactory(Car, Engine, Battery):

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        calliope = Car.__init__(self, self.CapuletEngine.init(last_service_date, current_mileage, last_service_mileage), self.SpindlerBattery.init(last_service_date, current_date))
        return calliope
        
        
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        glissade = Car.__init__(self, self.WilloughbyEngine.init(last_service_date, current_mileage, last_service_mileage), self.SpindlerBattery.init(last_service_date, current_date))
        return glissade

    def create_palindrome(current_date, last_service_date, warning_light_on) -> Car:
        palindrome = Car.__init__(self, self.SternmanEngine.init(last_service_date, warning_light_on), self.SpindlerBattery.init(last_service_date, current_date))
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        rorschach = Car.__init__(self, self.WilloughbyEngine.init(last_service_date, current_mileage, last_service_mileage), self.NubbinBattery.init(last_service_date, current_date))
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        thovex = Car.__init__(self, self.CapuletEngine.init(last_service_date, current_mileage, last_service_mileage), self.NubbinBattery.init(last_service_date, current_date))
        return thovex