import logging
logging.basicConfig(filename = "list.log", level = logging.DEBUG , format= '%(asctime)s %(levelname)s %(message)s')

class List:
    logging.info("We are into list class")

    def reverse(self):
        "The fun is used to reverse list"
        l= [3,4,5,6,7,[23,456,67,8,78,78],[345,56,87,8,98,9], (234,6657,6), {"key1": "atha", 234:[23,45,656]}]
        logging.info("We are into 1st function")

        try:
            l.reverse()
            logging.info("The reverse of this list is %s", l)
            return l

        except Exception as e:
            logging.exception(e)



    def Even(self):
        "The fun is used to find even in list"
        l= [1,2,3,4,5,6,7,8]
        logging.info("We are into 2nd function")

        try:

            for i in l:
                if i%2==0:
                    logging.info("The number %s is even", i)

        except Exception as e:
            logging.exception(e)


    def Odd(self):
        "The fun is used to find off in list"
        l= [1,2,3,4,7,9,11,13,15]
        logging.info("We are into 3rd function")

        try:

            for i in l:
                if i%2!=0:
                    logging.info("The number %s is odd", i)

        except Exception as e:
            logging.exception(e)

    def Print_ineuron(self):
        "The fun prints ineuron"
        l= [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"sudh","k2":"ineuron", "k3": "kumar", 3:6,7:8},["ineuron","data science"]]

        logging.info("We are into 4th function")

        try:
            for i in l:
                if type(i)== dict:
                    for j in i.items():
                        for g in j:
                            if g== "ineuron":
                                logging.info("The result is %s", g)


                if type(i)== list:
                    for k in i:
                        if k== "ineuron":
                            logging.info("The result is %s and %s", k, g)

        except Exception as e:
            logging.exception(e)

    def product(self):
        "The fun gives the product"
        l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
             {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

        logging.info("We are into 5th function")

        try:
            j=1
            for i in l:
                if type(i)== list or type(i)== tuple:
                    for k in i:
                        if type(k)== int:
                            j= j*k
                            logging.info("The product is %s", j)

        except Exception as e:
            logging.exception(e)



call= List()
call.reverse()
call.Even()
call.Odd()
call.Print_ineuron()
call.product()
