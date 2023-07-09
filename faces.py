def main():
    text = input("the text: ")
    print(convert(text))
    
def convert(text):
    text = text.replace(':(','🙁').replace(':)','🙂')
    return text
main()