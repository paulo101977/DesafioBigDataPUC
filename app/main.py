from File import FileLoader as FL



def main():
    #call_script()
    instance = FL.FileLoader('data\circuits.csv')

    data = instance.load_data()

if __name__ == '__main__':
    main()
