import enum
# Enum de Stados do Zombi
class StateZumbiEnum(enum.Enum):
   IDLE = 1
   PERSEGUIR = 2
   ATTACK = 3
   DEATH = 4