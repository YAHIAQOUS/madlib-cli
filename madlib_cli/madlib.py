import re 

def read_template(filepath: str)->str:
    # if filepath!="assets/dark_and_stormy_night_template.txt":
    #     raise FileNotFoundError('no path found')
    content_of_file=''
    with open(filepath,'r') as file:
        content_of_file = file.read()
    return content_of_file.strip()


def parse_template(content_of_file):
    parse = re.findall(r'\{(.*?)\}',content_of_file)
    for item in parse:
        content_of_file = content_of_file.replace(item,'',1)
        # print(content_of_file)
    return content_of_file,tuple(parse)


def merge(content_of_file,parse):
    content_of_file = content_of_file.format(*parse)
    # print(content_of_file)
    with open('assets/mergeFunction.txt','w') as file:
        file.write(content_of_file)
    return content_of_file


if __name__ == "__main__":
    
    input_list=[]
    adjective = input('Write an Adjective > ')
    a_first_name = input('Write A First Name > ')
    past_tense_verb = input('Write A Past Tense Verb > ')
    plural_noun = input('Write a Plural Noun > ')
    large_animal = input('Write a name of Large Animal > ')
    small_animal = input('Write a name of Small Animal > ')
    a_girls_name = input('Write A Girl\'s Name > ')
    number_1_50 = input('Write a Number Between 1-50 > ')

    input_list=[adjective,adjective,a_first_name,past_tense_verb,a_first_name,adjective,adjective,plural_noun,large_animal,small_animal,a_girls_name,adjective,plural_noun,adjective,plural_noun,number_1_50,a_first_name,number_1_50,plural_noun,number_1_50,plural_noun]

    content_of_file = read_template("assets/madlib.txt")
    print(content_of_file)

    parse = parse_template(content_of_file)
    print(parse)

    print(merge (parse[0],input_list))
