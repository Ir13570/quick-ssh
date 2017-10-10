import sys
from server import Server

def mode_select():
    while True:
        print('[cssh] select\n1.connect server\n2.add server\n3.remove server\n4.exit')
        mode = str(input('>>'))

        if mode == ('1' or '2' or '3' or '4'):
            return int(mode)
        else:
            print('[cssh] モード', mode, 'は存在しません。')


def connect():
    print('[cssh] 接続先を入力してください(登録名)')


def add():
    print('[cssh] 登録名を入力してください。')
    name = input('>>')


def exit():
    print('[cssh] プログラムを終了します。')
    sys.exit()
