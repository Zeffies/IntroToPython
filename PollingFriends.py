andy_answer = ''
bob_answer = ''
caleb_answer = ''
friends_polled = {'andy':andy_answer, 'bob':bob_answer, 'caleb':caleb_answer}
for person, answer in friends_polled.items():
    ((%s_answer) % person) = input("%s, please input something: " % person)

for person, answer in friends_polled.items():
    print(person + ": " + answer)
