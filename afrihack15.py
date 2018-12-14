def anagrams(word, words):
    ans = []
    for y in words:
        if len(y) == len(word):
            hold1 = hold2 = 0
            counter = 0
            counter2 = 0
            #checking if all the letters that appear in word are in y
            for x in word:
                if x in y:
                    counter +=1
                if counter == len(word):
                    hold1 = 1
            #checking if all the letters in y are in word
            for x in y:
                if x in word:
                    counter2 +=1
                if counter2 == len(word):
                    hold2 = 1
            if (hold1 == 1) and (hold2 == 1):
                ans.append(y)
    return ans
            