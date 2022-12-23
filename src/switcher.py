
def switcher(file, text):
    try:
        file = open(file, "w")
        file.write(text)
        file.close()
    except Exception as e:
        print(e)
