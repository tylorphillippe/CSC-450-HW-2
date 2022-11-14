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
                    'cmdDP': 'disable'},
                'cook':{
                    'cmdC': 'wait',
                    'cmdD': 'wait'}}