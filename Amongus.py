import random

from os import system, name

from Secret_msg  import Secret_msg
#import amongus.Secret_msg

class Amongus:

    msg = None

    def clean_screen(self):
        if name == 'nt':
            # windows
            _ = system( 'cls' )
        else:
            _ = system( 'clear' )

    def run(self):
        self.clean_screen()
        players = [ 'axel', 'itza', 'mama', 'papa' ]
        num_players = len( players )
        player = ''
        impostor = random.randint(0, num_players - 1)
        #print( 'impostor: {}'.format( impostor ) )

        while True:
            player = input( 'Escriba el nombre del jugador o q para salir: ' )
            if player == 'q':
                break

            try:
                i = players.index( player )
                #print( 'i: {}'.format( i ) )
                if i == impostor:
                    self.msg.show_impostor()
                else:
                    self.msg.show_amongus()

                input( 'pulsa enter para limpiar pantalla' )
                self.clean_screen()
            except:
                print( 'El jugador {} no esta registrado en el juego'.format( player ) )



    def __init__(self):
        self.msg = Secret_msg()


if __name__ == '__main__':
    amongus = Amongus()
    amongus.run()


