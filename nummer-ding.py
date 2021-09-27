
geraden = 0
punten = 0

import random
nummer = random.randint(1,1000)

print(nummer)

for i in range (1,21):
    ronde = 0 + i
    print("Ronde " + str(ronde))
    print("Als u wilt stoppen typ: Quit")
    stop = input(" ")

    if (stop.lower() == "quit"):
        exit()
    
    else:
        
        for a in range (1,11):

            print("Gok" + str(a) + "/10")

            print("Rara welk nummer heb ik in mijn hoofd?")
            geraden = input(" ")

    
            if int(geraden) == nummer:
                punten += 1
                print("Correct!")

                ronde += 1
            
                nummer = random.randint(1,1000)

                print(nummer)
                print ("punten" + str(punten))

                break
                
            else:
                print("FOUT!")
                if int(geraden) >= nummer:
                    print("Lager")
            
                else:
                    print("Hoger")

        nummer = random.randint(1,1000)

        print(nummer)

        ronde = i + 1
        print("ronde " + str(ronde))

print("eindscore " + str(punten))