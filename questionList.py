'''
enter "quit", then quit
enter "insert", then enter question_idx and level
    enter "quit", quit to main
enter "info", show the information of the question database
enter "get_question", show 4 questions of today, and delete the questions
from database
enter "past_questions", print the questions_idx and time of past_question
'''
import random
import datetime
import pytz

data_list = []
easy_list = []
medium_list = []

total_num = 0
easy_num = 0
medium_num = 0

data_file = "data.txt"
easy_file = "easy.txt"
medium_file = "medium.txt"
past_que_file = "past_questions.txt"

def get_time():
    tz = pytz.timezone('Europe/Dublin')
    ireland_time = datetime.datetime.now(tz)
    ireland_date = ireland_time.date()
    return str(ireland_date)

def write_to_file(file_name, data, type):
    with open(file_name, type) as f:
        f.write(str(data) + '\n')

def read_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def get_questions(file_name):
    temp_arr = []
    with open(past_que_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n' and line.split()[0] == get_time():
                print("today's questions has got, please check_today_questions")
                return
    with open(file_name, 'r') as f:
        lines = f.readlines()
        temp_arr += [int(line.strip()) for line in lines]
        select_numbers = random.sample(temp_arr, 4)
        print("today question:", select_numbers)
        for _ in select_numbers:
            write_to_file(past_que_file, get_time() + "  " + str(_), 'a')
        temp_str = ''
        for x in temp_arr:
            if x not in select_numbers:
                temp_str += str(x) + '\n'
        write_to_file(file_name, temp_str, 'w')

while True:
    get_time()
    print("\nquit(q), insert(i), info, get_question(gq), past_questions(pq), check_today_questions(c)")
    ipt = input()
    if ipt == "quit" or ipt == "q":
        print('program stop')
        break
    if ipt == "insert" or ipt == "i":
        while True:
            ipt = input()
            if ipt == "quit" or ipt == "q":
                break
            que_num, level = map(int, ipt.split())
            data_list.append((que_num, level))
            write_to_file(data_file, ipt, 'a')
            if level == 1:
                easy_list.append(que_num)
                write_to_file(easy_file, que_num, 'a')
            elif level == 2:
                medium_list.append(que_num)
                write_to_file(medium_file, que_num, 'a')
    if ipt == "info":
        data = read_file(data_file)
        total_num = len(data)
        for arr in data:
            temp_arr = arr.split()
            if temp_arr[1] == 1:
                easy_num += 1
            else:
                medium_num += 1
        pt = f'''            total question number: {total_num}
            easy question number: {easy_num}
            medium question number: {medium_num}
            done questions number: {len(read_file(past_que_file))}
            rest easy question number: {len(read_file(easy_file))}
            rest medium question number: {len(read_file(medium_file))}'''
        print(pt)
    if ipt == "get_question" or ipt == "gq":
        if len(read_file(easy_file)) == 0:
            get_questions(medium_file)
        else:
            get_questions(easy_file)
    if ipt == "past_questions" or ipt == "pq":
        temp_arr = read_file(past_que_file)
        for arr in temp_arr:
            print(arr)
    if ipt == "check_today_questions" or ipt == 'c':
        temp_arr = read_file(past_que_file)
        for arr in temp_arr:
            if arr != '' and arr.split()[0] == get_time():
                print(arr)
                print('1102, 1137')