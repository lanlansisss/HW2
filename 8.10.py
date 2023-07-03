#ERIC WANG
inputs=str(input())
inputs_nospace=inputs.replace(' ', '')
inputs_reversed=inputs_nospace
inputs_reversed=inputs_reversed[::-1]
if inputs_reversed==inputs_nospace:
    print (inputs, 'is a palindrome')
else:
    print(inputs, 'is not a palindrome')