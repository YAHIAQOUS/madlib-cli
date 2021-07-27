import re 
input_list = []


def read_template(filepath: str)->str:
    if filepath!="assets/dark_and_stormy_night_template.txt":
        raise FileNotFoundError('no path found')
    content_of_file=''
    with open(filepath,'r') as file:
        content_of_file = file.read()
    return content_of_file.strip()

content_of_file = read_template("assets/dark_and_stormy_night_template.txt")
print(content_of_file)


def parse_template(content_of_file):
    parse = re.findall(r'\{(.*?)\}',content_of_file)
    for item in parse:
        content_of_file = content_of_file.replace(item,'',1)
        # print(content_of_file)
    return content_of_file,tuple(parse)

parse = parse_template(" It was a {Adjective} and {Adjective} {Noun}.")


def merge(content_of_file,parse):
    content_of_file = content_of_file.format(*parse)
    print(content_of_file)
    with open('assets/mergeFunction.txt','w') as file:
        file.write(content_of_file)
    return content_of_file
