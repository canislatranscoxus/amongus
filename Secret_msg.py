'''
description: this class represent a Secret Message, hidden in a box of letters.
'''

import random

class Secret_msg:
    msg_impostor    = 'IMPOSTOR'
    msg_amongus     = 'AMONG_US'
    msg             = []


    def get_rnd_word(self, size):
        word = ''

        for i in range(size):
            word += chr( random.randrange( start=65, stop= 90+1 ) )

        return word

    def create_msg(self, size):
        for i in range(size):
            w = self.get_rnd_word( size )
            self.msg.append( w )

    def show(self):
        print('\n secret message: \n')
        for i in self.msg:
            print( '\t{}'.format( i ) )

        print( '\n' )

    def set_msg(self, plain_msg):
        self.msg[0] = plain_msg

    def show_impostor(self):
        self.msg[0] = self.msg_impostor
        self.show()

    def show_amongus(self):
        self.msg[0] = self.msg_amongus
        self.show()

    def __init__(self):
        row_size    = len( self.msg_impostor )
        self.create_msg( row_size )

if __name__ == '__main__':
    msg = Secret_msg()

    w = msg.get_rnd_word( 4 )
    msg.show()



