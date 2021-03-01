def count_substring(string, sub_string):
    result = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            is_substring = True
            for sub_i in range(1, len(sub_string)):
                if string[i + sub_i] != sub_string[sub_i]:
                    is_substring = False
        
            if is_substring == True:
                result = result + 1

    return result
    
if __name__ == '__main__':
    string = "ABCDCDC"#input().strip()
    sub_string = "CDC"#input().strip()
    
    count = count_substring(string, sub_string)
    print(count)