from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_ticket(self, type):
        pass
    

class ticket(ABC):
    
    @abstractmethod
    def info(self):
        pass

class arianaFactory(AbstractFactory):
    def create_ticket(self, type):
        if type == 'emergency':
            return Emergencyticket()
        if type == 'torrist':
            return torristticket()
        

class Kam_AirFactory(AbstractFactory):
    
    def create_ticket(self, type):
        
        if type == 'emergency':
            return Emergencyticket()
        if type == 'torrist':
            return torristticket()
        if type == 'private':
            return privateticket()

class factoryproducer:
    
    def get_factory(self, type):
        
        if type == 'arianaFactory':
            return arianaFactory()
        if type == 'Kam_AirFactory':
            
            return Kam_AirFactory()
        
        
class Emergencyticket(ticket):
    
    def info(self):
        return self.__class__.__name__
    
class torristticket(ticket):
    
    def info(self):
        return self.__class__.__name__
    
class privateticket(ticket):
    
    def info(self):
        
        return self.__class__.__name__
    


producer = factoryproducer()

jira_factory = producer.get_factory('arianaFactory')
snow_factory = producer.get_factory('Kam_AirFactory')

emergency_ticket = jira_factory.create_ticket('emergency')
torrist_ticket = snow_factory.create_ticket('torrist')
private_ticket = snow_factory.create_ticket('private')

print (emergency_ticket.info())
print (torrist_ticket.info())
print (private_ticket.info()) 
