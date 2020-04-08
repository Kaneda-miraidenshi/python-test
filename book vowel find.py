vowels='aiueoアイウエオあいうえお'
vol = list(vowels)
title =input('please enter the title name of book written in english　or hiragana:')
til = list(title)
find = []
for letter in til:
    if letter in vol:
        if letter not in find:
            find.append(letter)
print ('この本に含まれている母音はこれらです',find)
print ('コンマを消すとこうなります：',''.join(find))
print ('逆にするとこうなります：',''.join(find[::-1]))
print ('何かの単語になりましたか？')
