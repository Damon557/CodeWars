#Complete the function/method so that it returns the url with anything after the anchor (#) removed.

#Examples
#"www.codewars.com#about" --> "www.codewars.com"
#"www.codewars.com?page=1" -->"www.codewars.com?page=1"#

def remove_url_anchor(url):
    return url.split('#')[0]





#rolls are attacking your comment section!

#A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#Note: for this kata y isn't considered a vowel.#

def disemvowel(string_):
    return "".join([x if x.lower() not in "aeiou" else "" for x in string_])



#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

#Examples input/output:

#XO("ooxx") => true
#XO("xooxx") => false
#XO("ooxXm") => true
#XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#XO("zzoo") => false


def xo(letters):
    letters = letters.lower()
    x = letters.count('x')
    o = letters.count('o')
    if x == o:
        return True
    else:
        return False
print(xo("zzoo"))

