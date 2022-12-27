class Animals():
    def __init__(self, general_features, behaviour):
        self.genera_features = general_features
        self.behaviour = behaviour

class Mammals(Animals):
    def __init__(self, general_features, behaviour, mammals_features, mammals_behaviour):
        super().__init__(general_features, behaviour)
        self.mammals_features = mammals_features
        self.mammals_behaviour = mammals_behaviour

class Human(Mammals):
    def __init__(self, general_features, behaviour, mammals_features, mammals_behaviour,
                human_features, human_behaviour):
        super().__init__(self, general_features, behaviour, mammals_features, mammals_behaviour)
        self.human_features = human_features
        self.human_behaviour = human_behaviour

class Dog(Mammals):
    def __init__(self, general_features, behaviour, mammals_features, mammals_behaviour,
                dog_features, dog_behaviour):
        super().__init__(self, general_features, behaviour, mammals_features, mammals_behaviour)
        self.dog_features = dog_features
        self.dog_behaviour = dog_behaviour

class Cat(Mammals):
    def __init__(self, general_features, behaviour, mammals_features, mammals_behaviour,
                cat_features, cat_behaviour):
        super().__init__(self, general_features, behaviour, mammals_features, mammals_behaviour)
        self.cat_features = cat_features
        self.cat_behaviour = cat_behaviour

class Student(Human):
     def __init__(self, general_features, behaviour, mammals_features, mammals_behaviour,
                human_features, human_behaviour, completed_hw):
        super().__init__(self, general_features, behaviour, mammals_features, mammals_behaviour, human_features, human_behaviour)
        self.human_features = human_features
        self.human_behaviour = human_behaviour
        self.completed_hw = completed_hw
        
     def __gt__(self, other):
        return self.completed_hw > other.completed_hw

