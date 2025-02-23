# flag is in /flag.txt

banned_words = ['open', 'read']

def check_if_bad(expression):
    for word in banned_words:
        if word in expression:
            return True
    return False

print("Give me a nice math expression (ex: 5 * 1000) and I'll evaluate it with my calc!")
while True:
    try:
        expression = input("Expression: ")
        if check_if_bad(expression):
            print("Hey! We're serious mathematicians here!")
            continue

        result = eval(expression)
        print(result)

        print()
    except Exception as e:
        print("Hey! Your math error'ed and almost broke my calc!", e)
        print()
