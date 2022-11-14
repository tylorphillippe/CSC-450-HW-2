#Tylor Phillippe
#CSC 450 HW 2
#14 November, 2022
states ={  'wait':{
                'prompt': 'Machine ready',
                'transit': ['cmdT']},
            'set time':{
                'prompt': 'time set',
                'transit': ['cmdFP', 'cmdHP']},
            'full power':{
                'prompt': 'full power',
                'transit': ['cmdHP', 'cmdDC', 'cmdDP']},
            'half power':{
                'prompt': 'half power',
                'transit': ['cmdFP', 'cmdDC', 'cmdDP']},
            'disable':{
                'prompt': 'disable',
                'transit': ['cmdDC']},
            'enable':{
                'prompt': 'enable',
                'transit': ['cmdS']},
            'cook': {
                'prompt': 'cook',
                'transit': ['cmdC', 'cmdD']}}

transitions ={  'wait':{
                    'cmdT': 'set time'},
                'set time':{
                    'cmdFP': 'full power',
                    'cmdHP': 'half power'},
                'full power':{
                    'cmdHP': 'half power',
                    'cmdDC': 'enable',
                    'cmdDP': 'disable'},
                'half power':{
                    'cmdFP': 'full power',
                    'cmdDC': 'enable',
                    'cmdDP': 'disable'},
                'disable':{
                    'cmdDC': 'enable'},
                'enable':{
                    'cmdDP': 'disable',
                    'cmdS': 'cook'},
                'cook':{
                    'cmdC': 'wait',
                    'cmdD': 'wait'}}

def Acceptor(prompt, valids):
    ''' Acceptor style finite state machine to prompt for user input'''
    if not valids: 
        print(prompt)
        return ''
    else:
        while True:
            resp = input(prompt)
            if resp in valids:
                return resp

def finite_state_machine(initial_state):
    response = True
    next_state = initial_state
    current_state = states[next_state]
    while response:
        response = Acceptor(current_state['prompt'], current_state['transit'])
        next_state = transitions[next_state][response]
        current_state = states[next_state]

if __name__ == "__main__":
    finite_state_machine('wait')