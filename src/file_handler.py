def reader(file):
    with open(file, 'r') as f:
        text = f.read()

    text = text.replace('hello world', 'hola mundo')

    with open(file, 'w') as f:
        f.write(text)

    f.close()


def switcher(file, text):
    try:
        file = open(file, "w")
        file.write(text)
        file.close()
    except Exception as e:
        print(e)
