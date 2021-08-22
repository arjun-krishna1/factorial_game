from colorama import Fore

import os

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def wait_till_right_answer(ans: int, question: str) -> None:
    print(Fore.GREEN + "\n🚀 Go!\n" + Fore.WHITE)
    print(question)
    this_ans = input()
    while not representsInt(this_ans) or int(this_ans) != ans:
        os.system('clear')
        print(Fore.RED + "\n😞 Wrong. try again"+ Fore.WHITE)
        print(question)
        this_ans = input()


if __name__ == "__main__":
    os.system('clear')
    n = 1000
    curr_res = 1
    for i in range(1, n + 1):
        ans = curr_res * i
        min_len = len(str(curr_res)) + 3
        question = str(f"🤓 Calculate {i}!").rjust(min_len) + "\n" + str(curr_res).rjust(min_len) + "\n"\
                   + ("× " + str(i)).rjust(min_len, " ")\
                   + "\n" + "="*(min_len * 2) + "\n"

        wait_till_right_answer(ans, question)
        os.system('clear')
        print(Fore.GREEN + "\n🥳 🎉 Correct!" + Fore.WHITE)
        print("\nNext question:\n")
        curr_res *= i

