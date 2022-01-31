question = "Please input your gender:"
valid_answers = ['m', 'man', 'M', 'w','W','Woman']

while (answer := input(question)) not in valid_answers:
    print("Please input one of valid answer: ", ",".join(valid_answers)) 

print("Your answer is ", answer)