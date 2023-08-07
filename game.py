#Global variables declaration
ISLAND_ASCII_ART = '''                                          ..:::::..
                                              ^~^^^^~!!7?J?7!^.
                                              .:^^^:..:^..^!?YY?~.
                                                  .:~?JJJ~   .^7YY!
                                                       :!7!:    :75J      ......
                                              .:~!77777777JYYYY:  !5Y.:::::^^~~~~!~~:.
                                           :~777!~^^:~!:^^::^~!!!: 77:.::^^^^^^~~~^~~!!~.
                                        .~7~^.     .!P^   7J    .....:^^~~~~~~^^^^?!!^~7?7:
                                      .7?~::^^^^^^~~J7^^^!JY!!!?YYY~ .:~JJ?~^^^^^~77~:^~!?Y^
                                      ^!:::::..             .~J75~7P   .:^^7?:            ..
                                                          :7?!7J!?7B?   :^: ^JJ.
                                                        ^?YP!?J^ .^~G^.J7 ~   !P^
                                                      ^YJ: 7P!      ^J??~7.    ~P.
                                                    :?J?77PJ.        :^5YY      ??
                                                   75!  ^P?            !!P      :5
                                                 .Y?^?^?P^               !Y7:    Y.
                                                ^P7  .75.                 .!JY!: J^
                                               ~5:?~YJY                      :!J75~
                                              ^G: ^:YP                          .^.
                                             :G!Y.!YP.
                                             Y^ JJ~P!             ..::^^:.
                                            ?Y^ .^!Y    .:^~!77?????7!~~~!77.
                                           ^7.Y:?~G^ ^J5YJ?!!!~~~~~~~~~~~^^!5.
                                           Y! ~J~~Y .G~. .~7...:^^~~!!!7777!Y!
                                          ~!Y^ ?7?7 ~P!~~^:?7:^~!7?JYY5J?7!~77
                                        . ! .YJ? !?~JJ^7777!Y????7!?YJJ7.::.!?
                                 .^~!!!!~77::!Y^^5J^~5 .:^^~!?:^^::~?777~~^ !?
                           .:~!!!!~:.    .~?J7!!~:. .P^^^^:..J.:^^~~~~~^^^^.7Y!7!~:.
            :^^~~~~~!!7?YY?!~^:.                     J7 :^^^.?~^^^^^~~!7??7!!^  .^~!!~^:.
               .:^^~777!^.                           ^5^^^^::~?.:~!7JJJ?!~:.         .^^~!??7!~^^:.
           :^~?YJ7~:.                      .          .~!?JJ?~7~7?7!^.               ..    .^~~!^::.
         :~^!J~.                          .!               .^~!~:                      .~^^^~~~J7.^.
            ^!~!!~~~~~^^^::...                                                         ^???^:^..
           .:^^^~~~~~~!!!!77777!!!~^.                                         ::^^~~~~~~!!7:.:
                   .......:::::.^~7YJ                                       ^7~^::^:..
                    :^^^^~!777!~^:.                                         .::.::^~~~:.
                   .:.  757~^::........                                             :?!
                     :^::^~~~~~^^^^^^^^~~~~~~!!!!!!!!!!!!~~~~~~^^^::..........:^^~!!!~::^:
                        .                    ..:::::^^^^^^^^^^^^~~~~!!!!!!!!777!!~~^^::.
                                                                            ...
'''
# Define the ASCII art as a global variable
WINNING_ASCII_ART = '''
                          ..                                                                        
            :Y?!~^:~777!!~?J77~^:                                                                   
       .7J?J?YY?!~^::::~77:. .!??^                                                                  
       .:^!JJ?!~~^::^~~^:^!~.   !! :^!!^^::::^~!~!:                                                 
     7?!~~~^.   ....  .::  .~!..Y~::.:^~~^^^^~!7?Y7:::.                                             
     7!!~!P!..^^.  ..        ^J?^    .:....::^~!!J5JJ?~                                             
         7~^7P~.:!77??J?~:    .  ~~^.            .:~~^                                              
        :Y!:!7:77: ^J7~^.   !P~   .~JY7??7^ :~:  !Y7!7J!                                            
        !~ .GY?^:!77?:    ^~Y~J.     77:.:77 :5Y^ J^^~??            .:^^^^:                         
           .??J5Y??7     ^B5  ?.     .??.  !? ?~7?7.             .~~^~^^:~!!~                       
            .:::^77^ .: ^7J^ 7J.      .7.   !?5: ?5 ::^::.      :?^.^!^~^   ~J.                     
              :7!!^ ^Y7~B!7  :!7 ::  .7~^    ~J.  ^ ^!!!J~^^    7. :~!?~~    ~J  ....               
             ^7^:7:!!Y~:P!!  .~!:^J.  7:.            .^~^~!P!: ~!  .^~^!^     ?!~:...^~.            
                ^J7^.G! ??~  ^:^~^^!  !^               ~~..^YJ ^Y~~JJ?~^!!!^:^!?:~^!?7~^            
                75:  P~ .?~ ^?: !.^~  !.             .~^!.  ^~ ^~.!!^!?^~~~~^?^^^?!.  .!J!.         
                !7   !^  7^.!Y:   .:^~:      ..:     ..  ^^J^: .~^~~~ ^:.:~.^~  ~!^^:::::~:         
                      .  ~:.^5:     ~:      ::.:^:    ^:.^..^!^::7~!7..~77. Y7:^J7                  
                         ~^.^5^            .:    ^!^.  ^::^.::.^:P7~!^:~^7!!^7.:..                  
                        ^Y^!!!Y            :^      :~^:!::^..    Y:~~^^^:^ .~?                      
                         ~!::!J             ~           .:?::~7^^Y~:. .^!?7!.^!?Y?!                
                         ?77^:P             ^.       ..   Y^  :~::~?7??!!?^^  :77~ ^?.              
                         ^?. .P.             ~.    ::!?!^7!     :~~~  ..^ :~:..     ^?.             
                         .57~::?             .7~~^~~!!7!?^  ::   .!?!~:^ ^?~.   .    ^?             
                          ?:.  J:              ~777?~!?!  ^~P~     ~!!!:^!:    ~J     7!            
                          7.   ^J.               :^:~7.  ~YYJ:    ^~^ ~7~7.      ?!::.. ^^:          
                          7!:..^7^                .~^  !~^. !.    ?7^ 7~7.      ~^.~Y!   .^:        
                          :^:::::                .Y:   ~~. .?     ~J! !7~       ^7::^.     !        
                               ::..^:.:           ~~    :^.:J:.  :777 ~~7.      :5:      .~^        
                               :^:.~~~!.           ^!:     ~7!~~^^^77 !7!:^7:  :P7.    .7~.         
                                                    ^7~.. .J^.  ^!7GJ:?P:~~?^ :!^^~~~^~5^           
                        .....:::..              :::^^7.:^.::.:~?!!~J!^:. ~~~! ^^:^^..^5^            
         .:.::^^^^^^^^^~~^^^^^~~5B.           .7^    :7.      7?!!7~~7!!^^:^Y:^  .!:^!.             
       ..!^7!!!~~^^^^^~~~~~~~~~JJG5           :?      .J:    ^! :..   ..^J7!!7    ^J~!~^:..         
       5^ ~7^ .^^~~~~~^^^::...^J :#7         :.^^  ....~!   .!.::^77^    !  ^~^ :.^!~:.::^^^^:..    
       7J.^!J~~~^:::...       7:  ~B:        7^.:::^:^^:^   ^: .....~!~  ? ^777:!~!!?J^:....:^~!.   
       !^7 ^7Y!!~^^::..      .Y    75         :.        ^...7:        7^^!  :~:!?^:^ .^^~~~~^:.     
      ^! !^.~Y7!~^::.        ^Y     J7         !. .     :!..:          77      .:~                  
     :!^: 7.^!7    ....      .7      Y:       :7~ ?.    .Y~            7?        ^:                 
     7:~  :! ~77~^:...        :.     :?       ^~:.7   .^7^              ^Y~~~^^^!!~                 
     !!:   ~^.!7....:...       .:.    ^^       .!!^^^^J:                 ?^     J^                  
     .77:   !.^!?^^::.... .:^^:. .:..  :.7^:.   ~7    ^?                 !?^:   7!^                 
     ~7!^.:! !!!^^^:.   !!:?!~:  .^~^ !B7 '''

EXECUTING_GAME = True

#Function used in main program 
def choice1():
    # This function presents the player with the first choice upon entering the island.
    # The player can choose to go left or right.

    answer = None

    print("You just arrived on the island, and you enter a cave.")
    print("Upon entering you see two paths, one to the left and the other to the right.")

    while True:
        choice = input("Which do you choose? Type \"left\" or \"right\":").lower()

        if choice == "left":
            #correct answer
            answer = True
            break
        elif choice == "right":
            print("You fell into a hole. Game Over")
            answer = False
            break
        else:
            print("Invalid type. Pleas try again")
            continue

    return answer

def choice2():
    # This function presents the player with the second choice after entering the cave.
    # The player can choose to search for a small boat or swim in the lake.

    answer = None

    print("Upon entering you perceive a strange smell, and when you walk a little more you find a lake.")
    print("A lake in the middle of a castle? you ask yourself.")
    print("You try to look into the lake and you can't see what's how deep it is.")
    while True:
        choice = input("You have two options: look for a small boat or swim. Which do you choose? Type \"search\" or \"swim\":").lower()

        if choice == "search":
            #correct answer
            answer = True
            break
        elif choice == "swim":
            print("You jumped into the water but as soon as you entered a group of crocodiles ate you")
            print("Game Over")
            answer = False
            break
        else:
            print("Invalid type. Pleas try again")
            continue

    return answer

def choice3():
    # This function presents the player with the third choice after finding the boat with human remains.
    # The player can choose to take the key or leave it.
    answer = None

    print("You found a boat but you got scared when you saw human remains inside it")
    print("However, you realize that one of the bodies has a key in his hand.")
    while True:
        choice = input("Do you want to take the key? type \"yes\" or \"no\" :").lower()

        if choice == "yes":
            #correct answer
            answer = True
            break
        elif choice == "no":
            print("")
            print("You decide to put the boat in the lake, and you start rowing aimlessly")
            print("You start to wonder if it was a good idea to have come to this island")
            print("You see land in front of you so you decide to get off there.")
            print("as soon as you get off the boat, you see how a group of crocodiles eat your boat")
            print("You keep walking and find a locked door and to open it you need a key")
            print("Unfortunately you realize that the key you needed was the one you didn't take. Now you are trapped and your death is a matter of days")
            print("Game Over")
            answer = False
            break
        else:
            print("Invalid type. Pleas try again")
            continue

    return answer

def start_over_question():
    # This function asks the player if they want to start over after making incorrect choices.
    
    answer = None

    while True:
        choice = input("Do you want to start over? Type \"yes\" or \"no\":" ).lower()
        if choice == "yes":
            answer = True
            break
        elif choice == "no":
            print("Thank you for playing!")
            answer = False
            break
        else:
            print("Invalid type. Pleas try again")
            continue
        
    return answer        

# Main program
while EXECUTING_GAME:
    print(ISLAND_ASCII_ART)
    print("Welcome to the Treasure Island")
    print("Your mission is to find the treasure. Good Luck!!")
    print("")

    if not choice1():
        if not start_over_question():
            break
        continue

    print("")
    if not choice2():
        if not start_over_question():
            break
        continue

    print("")
    if choice3():
        print("")
        print("You decide to put the boat in the lake and start rowing aimlessly.")
        print("You start to wonder if it was a good idea to have come to this island.")
        print("You see land in front of you, so you decide to get off there.")
        print("As soon as you get off the boat, you see how a group of crocodiles eat your boat.")
        print("You keep walking and find a locked door, and to open it, you need a key.")
        print("You try the key you picked up and luckily it opens")
        print("In front of you you see a treasure full of gold. Congratulations you found the treasure!!!!")
        print(WINNING_ASCII_ART)
        EXECUTING_GAME = False
    else:
        if not start_over_question():
            break
