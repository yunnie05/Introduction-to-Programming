import random

def rem(lst,dicti):
    new={}
    for i in lst:
        new[i]= dicti[i]
    return new
                

def find_exit(connections, check_booth, seed):
    rng= random.Random(seed)
    aux=[]
    temp={}
    booth= list(connections.keys())
    for i in range(len(booth)):
        if rng.random() > 0.3:
            aux.append(booth[i])
    booth.clear()
    booth= aux.copy()
    temp= rem(booth,connections)
    del aux
    del booth
    try:
        temp[check_booth]
    except:
        return "Compromised booth! Aborting connection."
    else:
        return temp[check_booth]
    
    
connections = {
    "B1": "Go to the red door in the hallway and turn left.",
    "B2": "Head over to the back alley and find the hidden key.",
    "B3": "Find the elevator and press the secret button.",
    "B4": "Turn left at the second street and look for the green sign.",
    "B5": "Follow the alley until you see a blue dumpster, then turn right.",
    "B6": "Look for a door with a glowing symbol and open it.",
    "B7": "Enter the subway station, go down the stairs, and find the secret passage.",
    "B8": "Turn around and go through the abandoned building entrance.",
    "B9": "Find the underground tunnel entrance near the library.",
    "B1O": "Go straight ahead, take the first right, and find the hidden hatch."
    }
