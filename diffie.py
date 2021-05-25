class DiffieHellman():


    @staticmethod
    def calculate(a,q,private_a,private_b):
        ## computing public keys for a & b ##
        public_a = a**private_a % q
        public_b = a**private_b % q

        ## computing shared session key ##
        shared_key_a = public_b ** private_a % q
        shared_key_b = public_a ** private_b % q

        if shared_key_a == shared_key_b:
            return [public_a,public_b,shared_key_a,shared_key_b]
        return None
        
    @staticmethod
    def squareMultiply(power,number,mod):
        pass
