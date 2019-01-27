import random

class ReadWordFile():

    def __init__(self,file_name):
        self.file_name = file_name

    def read(self):
        with open( self.file_name , 'r') as fin:
            category_name = fin.readline()
            fin = fin.readlines()
        list_of_word = [x.strip().split(',') for x in fin if x != '']
        return WordList(category_name,list_of_word)

class WordList():

    def __init__(self, name, list_of_word):
        self.name = name
        self.word_list = list_of_word

    def generate_word(self):
        result = random.choice(self.word_list)
        self.word_list.remove(result)
        return WordGuess(result[0],result[1])

    def won(self):
        if self.word_list == []:
            return True
        else:
            return False

class WordGuess():

    def __init__(self, word, hint):
        self.word = list(word)
        self.hint = hint
        self.guess_box = []
        for i in range(len(self.word)):
            if self.word[i] == ' ':
                self.guess_box.append(' ')
            else:
                self.guess_box.append('_')
        self.status = False

    def guess(self,char):
        for i in range(len(self.word)):
            if self.word[i].lower() != char.lower():
                continue
            if self.guess_box[i] == '_':
                self.guess_box[i] = self.word[i]
                return True
        else:
            return False

    def print_info(self):
        print(f'Hint: {self.hint}')
        print(f'Word: ', end='')
        for char in self.guess_box:
            print(f'{char} ', end='')
        print('')

    def __str__(self):
        return f'## {"".join(self.guess_box)}  ##'

    def complete(self):
        if self.guess_box == self.word:
            return True
        else:
            return False

class Hangman():

    def __init__(self):
        self.detail = [] 
        for i in range(9):
            self.detail.append([])
            for j in range(30):
                self.detail[i].append(' ')
        self.status = { 
            'rope': False,
            'head': False,
            'left_arm': False,
            'right_arm': False,
            'body': False,
            'left_leg': False,
            'right_leg': False
        }
        self.draw_top_edge()

    def print_hangman(self):
        for i in self.detail:
            for j in i:
                print(j,end='')
            print('')

    def draw_top_edge(self):
        for i in range(len(self.detail[0])):
            self.detail[0][i] = '#'
    
    def draw_rope(self):
        self.detail[1][14] = '|'
        self.status['rope'] = True

    def draw_head(self):
        for i in range(2,4):
            for j in range(13,16):
                self.detail[i][j] = '#'
        self.status['head'] = True

    def draw_left_arm(self):
        for i in range(10,14):
            self.detail[4][i] = '#' 
        self.status['left_arm'] = True

    def draw_right_arm(self):
        for i in range(15,19):
            self.detail[4][i] = '#' 
        self.status['right_arm'] = True
    
    def draw_body(self):
        for i in range(4,7):
            self.detail[i][14] = '#' 
        self.status['body'] = True

    def draw_left_leg(self):
        for i,j in zip(range(6,8),range(13,11,-1)):
            self.detail[i][j] = '#'
        self.status['left_leg'] = True
    
    def draw_right_leg(self):
        for i,j in zip(range(6,8),range(15,17)):
            self.detail[i][j] = '#'
        self.status['right_leg'] = True

    def draw_dead(self):
        message = "You're Dead"
        for i,char in zip(range(9,20),message):
            self.detail[8][i] = char

    def draw_next(self):
        for key in self.status:
            if self.status[key] == False:
                if key == 'rope':
                    self.draw_rope()
                elif key == 'head':
                    self.draw_head()
                elif key == 'left_arm':
                    self.draw_left_arm()
                elif key == 'right_arm':
                    self.draw_right_arm()
                elif key == 'body':
                    self.draw_body()
                elif key == 'left_leg':
                    self.draw_left_leg()
                elif key == 'right_leg':
                    self.draw_right_leg()
                return None

    def remaining_life(self):
        total = len(self.status)
        remain = 0
        for key in self.status:
            if self.status[key] == False:
                remain += 1
        return [remain, total]

    def print_remaining_life(self):
        data = self.remaining_life()
        print(f"Remaining lives {data[0]}/{data[1]}" )

    def is_dead(self):
        if self.remaining_life()[0] == 0:
            self.draw_dead()
            return True
        else:
            return False

class ScoreFileRW():

    def __init__(self,name):
        self.file_name = name

    def read(self):
        with open( self.file_name , 'r') as file:
            file = file.readlines()
            score_list = [x.strip().split(',') for x in file if x != '']
        for elem in score_list:
            elem[1] = int(elem[1])
        return score_list

    def write(self, score_obj):
        with open( self.file_name, 'a') as file:
            file.write(f'\n{score_obj.name},{score_obj.score}')

class ScoreBoard():

    def __init__(self):
        self.name = ''
        self.score = 0

    def set_name(self, name):
        self.name = name

    def correct_guess(self):
        self.score += 1

    def complete_word(self):
        self.score += 10

    def __str__(self):
        return f'Current Score: {self.score}'