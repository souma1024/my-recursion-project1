import sys, os, markdown

command = sys.argv

def commands(command):

    if not os.path.isfile(command[2]):
        print(command[2] + ": ファイルが見つかりません")
        sys.exit()

    if command[1] == "markdown":
        get_markdown(command[2], command[3])
        print("マークダウンを HTML に変換しました")
        sys.exit()
    
    else:
        print("command not found")

def get_markdown(inputfile, outputfile):
    input_contents = ""
    with open(inputfile, 'r', encoding = "utf-8") as f:
        input_contents = f.read()

    html = markdown.markdown(input_contents)

    with open(outputfile, 'w', encoding = "utf-8", errors="xmlcharrefreplace") as f:
        f.write(html)

commands(command)