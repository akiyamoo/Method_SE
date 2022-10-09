from abc import ABC, abstractmethod, abstractproperty


class AbstractExercise(ABC):
    x = None

    def __init__(self):
        x = 0
