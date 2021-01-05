class myClass(object):
    def __init__(self):
        self.num = 100

    def read_number(self):
        print(self.num)

def main():
    myClass.read_number()

if __name__ == '__main__':
    main()