def is_eq(i1, i2):
    return i1 == i2

def is_correct(i):
    outp = False
    if (i == 's' ) or (i == 'k') or (i == 'g'):
        outp = True
    
    return outp

def winner(i1, i2):
    if (i1 == 's' and i2 == 'k') or (i1 == 'g' and i2 == 's') or (i1 == 'k' and i2 == 'g'):
        return 'u2'
    else:
        return 'u1'
number_of_win = 3
num_win_u1 = 0
num_win_u2 = 0 
itera = 0   
while (num_win_u1 < number_of_win) and (num_win_u2 < number_of_win):
    itera += 1
    while True:
        
        print("round: ", itera)
        i1 = input("user1: input your desicion (s or k or g): ")
        i2 = input("user2: input your desicion (s or k or g): ")
        if is_correct(i2) and is_correct(i1):
            break
        else:
            print('please import correct input')
    
    if is_eq(i1, i2):
        print("equal")
        print("u1: ", num_win_u1)
        print("u2: ", num_win_u2)
        continue
    else:
        win = winner(i1, i2)
        if win == 'u1':
            num_win_u1 += 1
            print("u1 win")
            print("u1: ", num_win_u1)
            print("u2: ", num_win_u2)
        else:
            num_win_u2 +=1
            print("u2 win")
            print("u1: ", num_win_u1)
            print("u2: ", num_win_u2)
    
if num_win_u1 == number_of_win:
    print("user1 is winner")
else:
    print("user2 is winner")
        
    