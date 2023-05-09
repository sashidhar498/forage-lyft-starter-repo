from abc import ABC, abstractmethod
from datetime import datetime


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

    def check(self,service_threshold_date):
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
