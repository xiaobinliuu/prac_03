import random


def main():
    random_number = int(input("How many random number?: "))
    get_random(random_number)


def get_random(random_number):
    OUTPUT_FILE = "results.txt"
    out_file = open(OUTPUT_FILE, 'w')
    for i in range(random_number):
        score = random.randint(0, 100)
        if score >= 90:
            print(format(score), "is Excellent", file=out_file)
        elif score >= 50:
            print(format(score), "is Passable", file=out_file)
        else:
            print(format(score), "is Bad", file=out_file)
    out_file.close()


main()
