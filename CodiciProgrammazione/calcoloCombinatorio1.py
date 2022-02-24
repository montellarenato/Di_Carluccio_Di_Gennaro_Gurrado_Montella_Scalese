from itertools import permutations
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self,str):

        self.__stringa = str

        return self.__stringa

    def anagrammi(self):
        lettere = list(parola)

        permutazioni = list(permutations(lettere))

        temp = ''

        anagrammi = []

        for i in permutazioni:

            for carattere in i:
                temp += carattere

            anagrammi.append(temp)

            temp = ''


    def charRipetuti(self):

        word = list(parola) 
        caratteriripetuti={}
        nCaratteri = 0
        count = 0

        for i in word:
            if (i in caratteriripetuti): 
                caratteriripetuti[str(i)] += 1
        else:
            caratteriripetuti[str(i)] = 1 
        for i in caratteriripetuti:
            if caratteriripetuti[i]>1:
                count+=1
                nCaratteri += caratteriripetuti[i] 
                
    def combUtil(self):
        words = 'words.italian.txt'
        f = open(words, 'r')
        for riga in f:

           p=f.readline()

           if self.__stringa in p:
               return("è una parola italiana")
           if parola == p[:-1]:
               return("vero")

    def fattoriale(n):
        if n==0:
            return 1
        else:
            return n*fattoriale(n-1)


    def coeffBinom(n, k):
        x = len(parola)
        y = int(input("Enter a value for y: "))
        if y == 1 or y == x:
           return(1)
        if y > x:
            return(0)
        else:
            a = fattoriale(x)
            b = fattoriale(y)
            div = a // (b*(x-y))
        return(div)  

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(n-k)
        

    def nDispSemplConRip(self):
        P = n**k
        return P

    def dispSemplSenzaRip(self):
        
        return 0


    def dispSemplConRip(self):
      
        return 0

        pass

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n)
     

    def nPermutConRip(self):
        calcComb.fattoriale(self.n)

        numeroripetizioni=fattoriale(n) / fattoriale(h) * fattoriale(k) * fattoriale(s)

        return numeroripetizioni

    def permutSenzaRip(self):
        
        return 0

    def permutConRip(self):
        
        return 0

        pass

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n) / fattoriale(k) * fattoriale(n-k)
       

    def nCombSemplConRip(self):
        calcComb.fattoriale(self.n)
        return fattoriale(n + k - 1) / fattoriale(k) * fattoriale(n-1)
       
    def combSenzaRip(self):

        return 

    def combConRip(self):
        
        pass
