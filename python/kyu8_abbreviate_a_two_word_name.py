# Write a function to convert a name into initials. This kata strictly takes two words with one space
# in between them
#
#The output should be two capital letters wit a dot separating them
#
#It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrevName(name):
    words = name.split(' ')
    return words[0][0].title() + '.' + words[1][0].title()
