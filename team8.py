####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'C' or 'B'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'Losing is not a word in my vocabulary'
strategy_description = 'Guess and Check till an answer makes itself evident'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    elif len(my_history) == 1:
        return 'b'
    elif len(my_history) == 2:
        return 'c'
    elif len(my_history) >= 3:    
        if their_history[len(their_history)-3:len(their_history)].upper() == 'CCB':
            return 'b'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'CBC':
            return 'b'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'BCC':
            return 'b'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'CBB':
            return 'c'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'BCB':
            return 'c'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'BBC':
            return 'c'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'CCC':
            return 'c'
        elif their_history[len(their_history)-3:len(their_history)].upper() == 'BBB':
            return 'b'
    elif their_history[-1:].upper() != 'C':
        if their_history[-1].upper() != 'B':
            return 'b'
    elif len(my_history)%6 ==0:
        return ' '

    
def test_move(my_history, their_history, my_score, their_score, result):     # if their_history[len(their_history)-3:len(their_history)].upper() == 'CCC'
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    a = 0
    
    if len(my_history) == 0:
        return 'b'
    elif len(my_history) == 1:
        return 'b'
    elif len(my_history) == 2:
        return 'c'
    elif len(my_history) >= 3:    
        if their_history[-1].upper() == 'C':
            if their_history[-2].upper() == 'C':
                if their_history[-3].upper() == 'B':
                    return 'c'
        elif their_history[-1].upper() == 'C':
            if their_history[-2].upper() == 'B':
                if their_history[-3].upper() == 'C':
                    return 'b'
        elif their_history[-1].upper() == 'B':
            if their_history[-2].upper() == 'C':
                if their_history[-3].upper() == 'C':
                    return 'c'
        elif their_history[-1].upper() == 'C':
           if their_history[-2].upper() == 'B':
                if their_history[-3].upper() == 'B':
                    return 'c'
        elif their_history[-1].upper() == 'B':
            if their_history[-2].upper() == 'C':
                if their_history[-3].upper() == 'B':
                    return 'b'
        elif their_history[-1].upper() == 'B':
            if their_history[-2].upper() == 'B':
                if their_history[-3].upper() == 'C':
                    return 'c'
        elif their_history[-1].upper() == 'C':
            if their_history[-2].upper() == 'C':
                if their_history[-3].upper() == 'C':
                    return 'c'
        elif their_history[-1].upper() == 'B':
            if their_history[-2].upper() == 'B':
                if their_history[-3].upper() == 'B':
                    return 'b'
    elif their_history[-1:].upper() != 'C':
        if their_history[-1].upper() != 'B':
            return 'b'
    elif len(my_history)%6 ==0:
        return ' '