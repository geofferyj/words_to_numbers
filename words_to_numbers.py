def to_numbers(num_string):

    # Control set   
    CONTROL = {'and', 'hundred', 'thousand', 'million', 'zero', 'one', 'two','three', 'four', 'five', 'six','seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred'}

    # dictionary for lookup
    numbers_dict = {
        'and':'a',
        'zero':'0',
        'one':'1',   
        'two':'2',
        'three':'3', 
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9',
        'ten':'10',
        'eleven':'11',
        'twelve':'12',
        'thirteen':'13',
        'fourteen':'14',
        'fifteen':'15',
        'sixteen':'16',
        'seventeen':'17',
        'eighteen':'18',
        'nineteen':'19',
        'twenty':'20',
        'thirty':'30',
        'forty':'40',
        'fifty':'50',
        'sixty':'60',
        'seventy':'70',
        'eighty':'80',
        'ninety':'90',
        'hundred':'00',
        'thousand':'000',
        'million':'000000'}

    # ------------- place holder lists start ---------------
    one_to_nineteen= ['one', 'two','three', 'four', 'five', 'six','seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    ten_hundred = ['ten', 'eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    units = ['one', 'two','three', 'four', 'five', 'six','seven', 'eight', 'nine']
    # ------------- place holder lists stop ----------------

    # -------------- Start of string proccessing ------------------
    words = num_string.lower()
    
    # convert input to list
    list_of_words = words.split()
    list_of_numbers = []
    numbers = []
    # check that all words entered are valid
    if set(list_of_words) < CONTROL:

        # Make sure that thousand dosen't come before million 
        if all(item in list_of_words for item in ['thousand', 'million']) and list_of_words.index('thousand') < list_of_words.index('million'):
            return "Invalid Input"
        
        # Make sure the same number isn't enter twice
        # Make sure the words are in the right order
        for i in range(len(list_of_words) - 1):
            
            if list_of_words[i] == list_of_words[i+1]\
            or ((list_of_words[i] in one_to_nineteen) and (list_of_words[i+1] in one_to_nineteen))\
            or ((list_of_words[i] in ten_hundred) and (list_of_words[i+1] in ten_hundred)):
                return "INVALID INPUT"
                
        # --------------- Start of convertion ------------------
        i = 0
        while i <= len(list_of_words) - 1:  
            
            if list_of_words[i] != 'and': # looks for "and" in the list
                
                if i >= len(list_of_words)-1: # if you are at the last item
                    list_of_numbers.append(numbers_dict.get(list_of_words[i]))
                    break
                
                # Joins numbers in place value tens and units
                elif list_of_words[i] in tens and list_of_words[i + 1] in units:
                    list_of_numbers.append(str(int(numbers_dict.get(list_of_words[i])) + int(numbers_dict.get(list_of_words[i+1]))))
                    i += 2
                # if next item in list is hundred, join 00 to current item
                elif list_of_words[i + 1] == 'hundred':
                    list_of_numbers.append(numbers_dict.get(list_of_words[i]) + numbers_dict.get(list_of_words[i + 1]))
                    i += 2
                else:
                    list_of_numbers.append(numbers_dict.get(list_of_words[i]))
                    i += 1
            else:
                list_of_numbers.append(numbers_dict.get('and')) # execute if and is found
                i += 1
        # --------------- End of convertion ------------------    

        # ---------------- Start of results proccessing -------------------
        new_list = []
        before = 0
        after = 0
        i = 0
        
        if 'a' in list_of_numbers:
            while i <= len(list_of_numbers) - 1:
                
                if list_of_numbers[i] != 'a' and list_of_numbers[i+1] != 'a' and int(list_of_numbers[i+1]) == 0:
                    new_list.append(list_of_numbers[i] + list_of_numbers[i+1])
                    
                    i += 2
                    
                    
                elif list_of_numbers[i] == 'a':
                    before = int(list_of_numbers[i-1])
                    after = int(list_of_numbers[i+1])
                    new_list.append(str(before + after))
                    i += 2
                else:
                    if int(list_of_numbers[i]) == 0:
                        new_list.append(list_of_numbers[i])
                        
                    i += 1
                    
        else:
            new_list = list_of_numbers[:]
        

        i = 0
        if len(new_list) - 1 == i:
            numbers = new_list[:]
        else:
            
            while i <= len(new_list) - 1:

                if i == len(new_list)-1:
                    numbers.append(new_list[i])
                    break
                elif int(new_list[i]) == 0:
                    i += 1
                elif int(new_list[i+1]) == 0:
                    numbers.append(new_list[i] + new_list[i+1])
                    i += 1
                else:
                    numbers.append(new_list[i])
                    i += 1
                

        result = 0
        for i in numbers:
            result = result + int(i)
        return result

        # --------------- End of results processing ------------------
    else:
        return "The Input contains words that are not numbers " # if the input is not a subset of the control set
    # ------------------- End of String proccessing ------------------


print(to_numbers('one hundred and fifty five million six hundred and twenty eight thousand three hundred and seventy three'))from sklearn.preprocessing import StandardScaler