
def add(numbers): 
    if not numbers: 
        return 0
    
    delimeter = ',' 

    if numbers.startswith('//'):
        delimeter_line, numbers = numbers.split("\n", 1)
        delimeter = delimeter_line[2:]

    numbers = numbers.replace('\n', delimeter) 
    numbers_list = numbers.split(delimeter) #split the numbers

    negative_list = [str(num) for num in numbers_list if int(num) < 0]
    if negative_list:
        raise ValueError("negative numbers not allowed {}".format(",".join(negative_list)))
    
    return sum(int(num) for num in numbers_list if int(num) < 1000 )