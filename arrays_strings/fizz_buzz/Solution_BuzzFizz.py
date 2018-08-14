class Stringassign:
    def change_number(self,upto_numbers):
        if upto_numbers < 0:
            print ("Exception")
        for no in range(1,upto_numbers):
            if no%3==0 and no%5==0:
                print("FizzBuzz")
                continue
            elif(no%3)==0:
                print("Fizz")
                continue
            elif(no%5)==0:
                print("Buzz")
                continue
            print (no)
if __name__ == '__main__':      
    try:
        upto_numbers=input("upto which number you want to print...?\t")
        change_instance=Stringassign()
        change_instance.change_number(int(upto_numbers))
    except ValueError:
        print("Exception")
