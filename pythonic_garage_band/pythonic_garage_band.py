from abc import ABC

class Musician:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):   
        pass

    def play_solo(self):
        pass

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):

    def __init__(self,name):
        super().__init__(name)

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band():

    count = 0
    instances = []

    def __init__(self,name,list):
        self.name = name
        self.members = list
        self.__class__.count += 1
        Band.instances.append(self.__class__)

    def play_solos(self):
        solo_list = []
        for musician_obj in self.members:
            solo_list.append(musician_obj.play_solo())
        return solo_list
    
    @classmethod
    def to_list(cls):
        return cls.instances

