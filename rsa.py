from random import Random
import math

class RSA():
    Rand = Random()

    @staticmethod
    def encrypt(C=None,M=None,p=None,q=None,e=None):
        ### over loaded function where p,q and e are not calculated
            ### creating a list of large prime numbers to be able to select randomly
            ### from it
            if p==None and q==None:
                Rand_list = [i for i in range(1_000,10_000) if RSA.isPrime(i)]

                p_index = RSA.Rand.randint(0,len(Rand_list)-1)

                p = Rand_list[p_index]
                q = p 

                ### checking for different p and q
                while q == p: 
                    q_index = RSA.Rand.randint(0,len(Rand_list)-1)
                    q = Rand_list[q_index]

            n = p*q
            Φn = (p-1)*(q-1)

            ### checking if gcd(e,Φ(n)) = 1 and selecting e randomly
            ### where e >1 and e<Φn
            if e == None:
                e = RSA.Rand.randint(2,Φn-1) 
                while math.gcd(e,Φn)!=1:
                    e = RSA.Rand.randint(2,Φn-1)

            ### euclids inverse
            d=1
            e = e % Φn
            for d in range(1,Φn):
                if(e*d)%Φn == 1:
                    break

            ### encryption
            if C==None and M!=None:
                return  (M ** e) % n 

            ### decryption
            elif C!=None and M == None:
                return (C**d) % n
      
    @staticmethod
    def isPrime(number):
        for i in range(2,number):
            if number%i == 0:
                return False
        return True
        
        
if __name__ == "__main__":
    print(RSA.encrypt(p=3,q=11,C=14,e=7))