""" File to simulate Quatum Key Distribution 
- Lets user play as alice or bob """

### imports 
import random

### Globals ####
num_bits = None
bits_to_reveal = None
inputs = 0
alice = []
bob = []

def compaire_basis(alice, bob) -> list:
    shared_secret = []
    shared_basis_num = []
    for i in range(len(alice)):
        if bob[i][1] == alice[i][1]:
            shared_secret.append(alice[i][0]) 
            shared_basis_num.append(i+1)
    return shared_secret, shared_basis_num

# Let user to play as alice or bob
print("Would you like to play as alice or bob?")
player1 = input("Enter A for alice B for bob ").lower()
while not (player1 != 'a' or player1 != 'b'):
    print("Selection not recognized")
    player1 = input("Enter A for Alice B for Bob ")

if player1 == 'a':
    # player1 is Alice get bit and basis from her aka user
    while num_bits == None:
        try:
            num_bits = int(input("Ok Alice, how many bits and basis would you like to exchange with Bob? "))
        except ValueError:
            print("You did not enter a interger")
            num_bits = None
        
    print(f"You are going to chose {num_bits} bits and {num_bits} basis to pass that photon through \
before it gets to bob. \
You can choose between the L or V basis and as a 1 or 0 for the bit")
    
    while inputs < num_bits:
        bit = None
        alice_basis = 'f'
        while  bit != '0' and bit != '1':
            bit = input(f"Enter your value for bit {inputs+1} ").upper()
        while alice_basis != 'L' and alice_basis != 'V':
            alice_basis = input(f"Enter you Basis as 'L' or 'V ").upper()
        alice.append((bit, alice_basis))
        inputs += 1

    # decide basis for bob
    for i in range(num_bits):
        alice_basis = random.randint(0,1)
        alice_basis = 'L' if alice_basis == 1 else 'V'
        bob.append((None, alice_basis))
    
    
    # Bob will reveal his basis to alice 
    print("bob is callingy you!")
    print("Hey alice its bob... my basis are")
    bobBasis = [x[1] for x in bob]
    print(bobBasis)

    # get check if both bob and alice used same basis 
    shared_secret, shared_basis = compaire_basis(alice, bob)
    print("you and bob have the same basis for basis numbers" ,shared_basis )

    # reveal a couple of bits bits to check for Eve
    print('You and bob now have a shared secret key!' ,shared_secret, ' But what if Eve was on the line?')
    bad_input = True
    while bad_input == True:
        try: 
            bits_to_reveal = int(input('How many bits would you like to share with bob to check for Eve? ' ))
            bad_input = False
        except ValueError:
            bad_input = True
    if bits_to_reveal >= len(shared_secret): 
        print('you shared all your bits you have no shared secret')
    else:
        bobs_first_two = [shared_secret[i] for i in range(bits_to_reveal)] # they are the same as the shared secret as we have not eve in this sim
        print('bob has sent his first two bits over they are', bobs_first_two) 
        print(f'Your and bobs values for the first two bits match meaning that with {1 - (1/(2**bits_to_reveal))} probability that no one was listening in')
        print('Your shared secret is ', shared_secret[bits_to_reveal:])



else:
    # player1 is Bob

    # prompt bob for number of bits
    good_input = False
    while good_input == False:
        try:
            num_bits = int(input("How many photons would you like to share with eve? "))
            good_input = True
        except ValueError:
            print("You did not enter an interger")

    # prompt bob for his basis
    print(f'Ok bob eve is going to send you {num_bits} photons, you will need to choose {num_bits} basis')
    while len(bob) < num_bits:
        good_input = False
        while good_input == False:
                answer = input(f'Enter either a L or V basis for the {len(bob) + 1} basis ').upper()
                good_input = True if (answer == 'L' or answer == 'V')  else False 
        bob.append((None, answer))
    
    bobBasis = [i[1] for i in bob]
    print('bob your basis are ', bobBasis)

    # Alice sends over some photons and we interprete through bobs basis 
    
    # random bits and basis for alice 
    for i in range(num_bits):
        alice_bit = random.randint(0,1)
        alice_basis = random.randint(0,1)
        alice_basis = 'L' if alice_basis == 1 else 'V'
        alice.append((alice_bit, alice_basis))

    # compare with bob, if same basis give alice bit if bad basis give random bit
    bobs_bits = []
    for i in range(len(alice)):
        if alice[i][1] == bob[i][1]:
            # same basis append alice bit
            bobs_bits.append(alice[i][0])
        else:
            # give random bit
            bobs_bits.append(random.randint(0,1))


    print("Bob you have interpreted through your basis the photons alice sent as ", bobs_bits)

    # alice reveals her basis
    print('alices basis were ', [x[1] for x in alice])

    # get check if both bob and alice used same basis 
    shared_secret, shared_basis = compaire_basis(alice, bob)
    print("you and bob have the same basis for basis numbers" ,shared_basis )
            
    # reveal a couple of bits bits to check for Eve
    print('You and Alice now have a shared secret key!' ,shared_secret, ' But what if Eve was on the line?')
    bad_input = True
    while bad_input == True:
        try: 
            bits_to_reveal = int(input('How many bits would you like to share with Alice to check for Eve? ' ))
            bad_input = False
        except ValueError:
            bad_input = True
    if bits_to_reveal >= len(shared_secret): 
        print('you shared all your bits you have no shared secret')
    else:
        bobs_first_two = [shared_secret[i] for i in range(bits_to_reveal)] # they are the same as the shared secret as we have not eve in this sim
        print('Alice has sent his first two bits over they are', bobs_first_two) 
        print(f'Your and Alice values for the first two bits match meaning that with {1 - (1/(2**bits_to_reveal))} probability that no one was listening in')
        print('Your shared secret is ', shared_secret[bits_to_reveal:])
