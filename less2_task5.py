# Link to flowcharts:
# https://drive.google.com/file/d/12xTQSyUeeSIWUDkwn3nWW-KHMmj31Rxy/view?usp=sharing

# Display the codes and characters of the ASCII table, starting with the character at number 32 and ending with the 127th inclusive.
# Execute the output in tabular form: ten pairs of "code-symbol" in each line.

for i in  range ( 32 , 128 ):
    print("{} - {}".format(i, chr(i)), end=' ')
    if i % 10 == 0:
        print()
