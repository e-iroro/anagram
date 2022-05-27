# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from hashlib import shake_128


def find_anagram(word, anagram):
    # [assignment] Add your code here
    print(sorted(word), sorted(anagram))
    if(sorted(word) == sorted(anagram)):
        print(sorted(word), sorted(anagram))
        return True 
    return False
print(find_anagram("liar","rale"))
print(find_anagram("liar","rail"))


    
    
    
