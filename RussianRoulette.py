#will either shut down, restart, log off user, or return a smiley face

import os
import random
from collections import Counter
 
# user define function
def shutdown():
    return os.system("shutdown /s /t 1")
 
def restart():
    return os.system("shutdown /r /t 1")
 
def logout():
    return os.system("shutdown -l")
 


def main():
    numbers = [1, 2, 3, 4]
    weights = [3, 1, 1, 1]

    random_selections = random.choices(numbers, weights=weights, k=5)
    counter = Counter(random_selections)
    most_common_number = counter.most_common(1)[0][0]

    if(most_common_number == 1):
        print(":)")
    elif(most_common_number == 2):
        logout()
    elif(most_common_number == 3):
        restart()
    elif(most_common_number == 4):
        shutdown()
    else:
        print("hey howd this happen :0")

if __name__ == '__main__':
    main()