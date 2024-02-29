
class Command:
    def execute(self):
        pass
    
    

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
        
    def execute(self):
        self.light.off()
        self.light.on()
        

class Light:
    
    def on(self):
        print ("light is turned on")
        
    def off(self):
        print ("light is turned off")



class RemoteControl:
    
    def __init__(self):
        self.Command = None
        
    def set_command(self, command):
        self.command = command
        
    def press_button(self):
        self.command.execute()
        
        
        
        
light = Light()
light_on_command = LightOnCommand(light)

remote = RemoteControl()
remote.set_command(light_on_command)
remote.press_button()
