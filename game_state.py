from enum import Enum

class GameState(Enum):
    NotStarted = 1
    InProcess = 2
    FinishSuccessfully = 3
    FinishUnsuccessfully = 4