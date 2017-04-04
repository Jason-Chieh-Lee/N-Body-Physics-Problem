"""
Basic object class.
"""

import physics as phys

class Object:
    """ Generic object in orbit. """
    def __init__(self, mass, state):
        """ Initialize mass, radius, position, velocity. """
        self.mass = mass
        self.radius = mass * phys.RADIUS_SCALING
        self.state = state
        phys.G_OBJECTS.append(self)

    def __str__(self):
        """Return string representation of Object"""
        return 'Mass: ' + str(self.mass) + '. Radius: ' + str(self.radius) + \
               '. State: ' + self.state.__str__()

    def update_mass(self, mass):
        """ Update mass by overwriting. """
        self.mass = mass

    def update_state(self, state):
        """ Update state by overwriting. """
        self.state = state

    def get_state(self):
        """Return the object state"""
        return self.state

    def iterate_state(self, dt):
        """ Update state after step of iteration. """
        self.state = phys.iterate(self.state, dt)
