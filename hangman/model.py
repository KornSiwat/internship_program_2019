
class ReadFile():

    def __init__(self,file_name=''):
        self.__file_name = file_name

# class WordList():

#     def

class Hangman():

    def __init__(self):
        self.detail = [] 
        for i in range(10):
            self.detail.append([])
            for j in range(30):
                self.detail[i].append(' ')
        self.status = { 'rope': False,
                        'head': False,
                        'left_arm': False,
                        'right_arm': False,
                        'body': False,
                        'left_leg': False,
                        'right_leg': False
        }

    def __str__(self):
        for i in self.detail:
            for j in i:
                print(j,end='')
            print('')
        return ''

    def draw_top_edge(self):
        for i in range(len(self.detail[0])):
            self.detail[0][i] = '#'
    
    def draw_rope(self):
        self.detail[1][14] = '|'

    def draw_head(self):
        for i in range(2,4):
            for j in range(13,16):
                self.detail[i][j] = '#'

    def draw_left_arm(self):
        for i in range(10,14):
            self.detail[4][i] = '#' 

    def draw_right_arm(self):
        for i in range(15,19):
            self.detail[4][i] = '#' 
    
    def draw_body(self):
        for i in range(4,7):
            self.detail[i][14] = '#' 

    def draw_left_leg(self):
        for i,j in zip(range(6,8),range(13,11,-1)):
            self.detail[i][j] = '#'
    
    def draw_right_leg(self):
        for i,j in zip(range(6,8),range(15,17)):
            self.detail[i][j] = '#'

if __name__ == "__main__":
    hangman = Hangman()
    hangman.draw_top_edge()
    print(hangman)
    hangman.draw_rope()
    print(hangman)
    hangman.draw_head()
    print(hangman)
    hangman.draw_left_arm()
    print(hangman)
    hangman.draw_right_arm()
    print(hangman)
    hangman.draw_body()
    print(hangman)
    hangman.draw_left_leg()
    print(hangman)
    hangman.draw_right_leg()
    print(hangman)
