
class ReadWordList():

    def __init__(self,file_name):
        self.file_name = file_name
        self.category_name = ''
        self.word_list = []

    # def read(self):


class Hangman():

    def __init__(self):
        self.detail = [] 
        for i in range(10):
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
            return True
        else:
            return False

if __name__ == "__main__":
    hangman = Hangman()
    hangman.print_remaining_life()
    hangman.draw_top_edge()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_rope()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_head()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_left_arm()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_right_arm()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_body()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_left_leg()
    print(hangman)
    hangman.print_remaining_life()
    hangman.draw_right_leg()
    print(hangman)
    hangman.print_remaining_life()
