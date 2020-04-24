
def get_file_len(scores):
    with open(scores) as f:
        for file_len, l in enumerate(f):
            pass
    file_len = file_len + 1
    return file_len


def create_array(scores, file_len, lines, f, scores_array):
    with open('~scores.txt', 'r') as f:
        for x in range(0, file_len):
            line = lines[x].split(",")
            scores_array.append(int(line[1]))
        

def get_average(scores_array):
    total = 0
    for x in range(0, len(scores_array)):
        score = scores_array[x]
        total = total + int(score)
    average = total / len(scores_array)
    return average
    

def get_low(scores_array):
    scores_array.sort()
    low = str(min(scores_array))
    return low


def get_high(scores_array):
    scores_array.sort(reverse = True)
    high = str(scores_array[0])
    return high


def display_results(average, low, high):
    print("The lowest score is " + low + ".")
    print("The highest score is " + high + ".")
    print("The average of the scores is " + "{:12.2f}".format(average) + ".")


def main():
    scores_array = []
    f = open('~scores.txt')
    lines = f.readlines()
    scores = "~scores.txt"
    file_len = get_file_len(scores)
    create_array(scores, file_len, lines, f, scores_array)
    average = get_average(scores_array)
    low = get_low(scores_array)
    high = get_high(scores_array)
    display_results(average, low, high)
    
    
main()
