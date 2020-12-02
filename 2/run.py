# Solution for day 2 of Advent of Code 2020

import re

## Part 1
# First we load the input and we store it so that for each line we have 4 elements

filepath = 'input.txt'
cnt1 = 0;
cnt2 = 0;
linecnt = 0;
with open(filepath) as fp:
    for line in fp:
        line = line.strip();
        out=filter(None,re.split("[ \-:]+",line))
        outarr=list(out)
        linecnt += 1
        #print(outarr)
        
        ## not a good solution with regex
        # then we go through the output and make sure the regex is valid and count how many are valid
        #regextomatch=outarr[2]+"{"+outarr[0]+","+outarr[1]+"}"
        #matched = re.match(regextomatch,outarr[3])
        #if matched is not None:
        #    print(outarr)
        #    print(regextomatch)
        #    print(matched)
        #    cnt1 += 1
         
        # we try just counting the letters
        lettnum = outarr[3].count(outarr[2])
        if int(outarr[0]) <= lettnum <= int(outarr[1]):
            cnt1 += 1
        
        ## Part 2, check that the letters in positions given match the letter

        lettpos1 = outarr[3][int(outarr[0])-1];
        lettpos2 = outarr[3][int(outarr[1])-1];
        if (lettpos1 == outarr[2]) ^ (lettpos2 == outarr[2]):
            print(",".join(outarr)+" "+lettpos1+" "+lettpos2)
            cnt2 += 1

print("Numbers of lines: "+str(linecnt))

print("Answer part 1: "+str(cnt1))
print("Answer part 2: "+str(cnt2))


