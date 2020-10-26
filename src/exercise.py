def main():
    #write your code below this line
    fileName = input("File?")
    lowerBound = int(input("Lower bound?"))
    upperBound = int(input("Upper bound?"))
    noNumbers = 0
    try:
      with open(fileName,'r') as f:
        lines = f.read().splitlines()
        for number in lines:
          if int(number) >=lowerBound and int(number)<=upperBound:
            noNumbers += 1
        print("Numbers: %s"%noNumbers)

    except:
        print("Reading the file %s failed."%fileName)



if __name__ == '__main__':
    main()
