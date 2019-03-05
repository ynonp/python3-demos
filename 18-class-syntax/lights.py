class LightBulb:
    def __init__(self):
        self.is_lights_on = False

    def light_on(self):
        if not self.is_lights_on:
            print("Lights On")
            self.is_lights_on = True

    def light_off(self):
        if self.is_lights_on:
            print("Lights Off")
            self.is_lights_on = False

l1 = LightBulb()
l2 = LightBulb()

l1.light_on()
l1.light_off()

print(l1.is_lights_on)
print(l2.is_lights_on)
