#Tylor Phillippe
#CSC 450 HW 2
#14 November, 2022
states ={  'wait':{
                'transit': ['cmdT']},
            'set time':{
                'transit': ['cmdFP', 'cmdHP']},
            'full power':{
                'transit': ['cmdHP', 'cmdDC', 'cmdDP']},
            'half power':{
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

def state_machine(initial_state):
    transition = True
    transitionlist = input('Please input list of transitions: ').split(',')
    i=0
    state = initial_state
    statelist = []
    statelist.append(state)
    while (i < len(transitionlist)):
        transition = transitionlist[i]
        if transition not in transitions[state]:
            print('invalid input')
            break
        state = transitions[state][transition]
        statelist.append(state)
        i+=1
    print(statelist)

if __name__ == "__main__":
    state_machine('wait')