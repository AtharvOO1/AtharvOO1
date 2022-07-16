import logging
logging.basicConfig(filename="string.log",level= logging.DEBUG, format= '%(asctime)s %(levelname)s %(message)s')

class String:
    logging.info("We are accessing String class")


    def slice_data(self):
        "This fun. is used for slicing"
        s= input("Enter the string ")
        logging.info("We are inside function")

        try:
            s1= s[1:300:3]
            logging.info("The slicing of the string is %s", s1)
            return s1
        except Exception as e:
            logging.exception(e)


    def upper_split(self):
        "This fun splits and covert in caps"
        s = "this is my first python programming class and I am learning python string and its function"
        logging.info("We are in 2nd fun")

        try:
            s2= s.upper().split()
            logging.info("The result of 2nd fun is %s", s2)
            return s2
        except Exception as e:
            logging.exception(e)


    def expand_tab(self):
        "This fun expands string"
        s = "atha\trv\t"
        logging.info("We are inside fun 3")

        try:
            s3= s.expandtabs()
            logging.info("The result of 3rd fun is %s ", s3)
            return s3
        except Exception as e:
            logging.exception(e)


    def center(self):
        "This fun bring the string at center"
        s = "Atharv"
        logging.info("We are inside func 4")

        try:
            s4= s.center(10, '*')
            logging.info("The result of 4th fun is %s ", s4)
            return s4
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        "This fun reverse the string"
        s= "Atharv Dixit"
        logging.info("We are inside fun 5")

        try:
            s5= s[::-1]
            logging.info("The result of 5th fun is %s ", s5)
            return s5
        except Exception as e:
            logging.exception(e)




call = String()

call.slice_data()
call.upper_split()
call.expand_tab()
call.center()
call.reverse()
