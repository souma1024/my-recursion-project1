import sys
import os

command = sys.argv

def commands(command):

    if command[1] == "help":
        help_explain()
        sys.exit()

    if not os.path.isfile(command[2]):
        print(command[2] + ": ファイルが見つかりません")
        sys.exit()

    if command[1] == "reverse":
        reverse(command[2], command[3])
        print("ファイルの内容を逆順にしました。\n")
        sys.exit()
    
    if command[1] == "copy":
        copy(command[2], command[3])
        print(command[2] + "を" + command[3] + "としてコピーしました\n")
        sys.exit()
    
    if command[1] == "duplicate_contents":
        duplicate_contents(command[2], command[3])
        print(command[2] + "に" + command[3] + "回複製しました。\n")
        sys.exit()
    
    if command[1] == "replace_string":
        replace_string(command[2], command[3], command[4])
        print(command[2] + "の" + command[3] + "を" + command[4] + "に置換しました。\n")
        sys.exit()
    
    else:
        print(command[1])
        print(f"command not found!\n")
        sys.exit()

def help_explain():
    print("python3 file_manipulator.py command args1 args2 ・・・")
    print("command: reverse  args1: file1  args2: file2      file1 にあるファイルを受け取り、file2 に file1 の内容を逆にした新しいファイルを作成します。\n")
    print("command: copy  args1: file1  args2: file2     file1 にあるファイルのコピーを作成し、file2 として保存します。\n")
    print("command: duplicate_contents  args1: file args2: n      file にあるファイルの内容を読み込み、その内容を複製し、複製された内容を file1 に n 回複製します。\n")
    print("command: replace_string  args1: file  args2: needle  args3: newstring     file にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。\n")



def reverse(inputpath, outputpath):
    input_contents = ""
    with open(inputpath, 'r') as f:
        input_contents = f.read()

    output = ''.join(list(reversed(input_contents)))

    with open(outputpath, 'x') as f:
        f.write(output)
    

def copy(inputpath, outputpath):
    input_contents = ""
    with open(inputpath, 'r') as f:
        input_contents = f.read()
    
    with open(outputpath, 'x') as f:
        f.write(input_contents)

def duplicate_contents(inputpath, count):
    count = int(count)
    input_contents = ""
    with open(inputpath, 'r') as f:
        input_contents = f.read()

    output = ""
    for i in range(count):
        output += input_contents 
    
    with open(inputpath, 'w') as f:
        f.write(output)
    

def replace_string(inputpath, needle, newstring):
    input_contents = ""
    with open(inputpath, 'r') as f:
        input_contents = f.read()
    
    output = ""
    output = input_contents.replace(needle, newstring)

    with open(inputpath, 'w') as f:
        f.write(output)
    
commands(command)
