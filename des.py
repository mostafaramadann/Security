class SDES():
    ### initializing constants like S-box
    ### and permutation choices
    S = [
        [[1,0,3,2],####S0
         [3,2,1,0],
         [0,2,1,3],
         [3,1,3,2]],

        [[0,1,2,3],####S1
         [2,0,1,3],
         [3,0,1,0],
         [2,1,0,3]]
        ]
    P10 = [3,5,2,7,4,10,1,9,8,6]

    P8  = [6,3,7,4,8,5,10,9] 

    P4  = [2,4,3,1]

    IP  = [2,6,3,1,4,8,5,7]

    EP  = [4,1,2,3,2,3,4,1]

    @staticmethod
    def encrypt(text:str,key:str,rounds=2) -> str:
        ### checking if text is 8 bits and key is 10 bits
        if len(text) == len(key)-2:
            text = text.strip()
            key  = key.strip()
            ### Initial Permutation
            text_IP = SDES.permutate(SDES.IP,text)
            keys = list()
            next_key= None
            shift=1

            ### Key generation Stage
            p10 = None
            shifts = list()
            p8s = list()
            for i in range(rounds):
                if i<1:
                    key = SDES.permutate(SDES.P10,key) ### P10
                    p10=key
                key = SDES.shift(key,shift=shift) ## Shift
                shifts.append(key)
                next_key = key
                key = SDES.permutate(SDES.P8,key) ## P8
                p8s.append(key)
                keys.append(key)
                key = next_key
                shift+=1
            ### end of key Gen
            print("\n")
            print("*"*20)
            print("p10 of first and second key are ",p10)
            print("first left shift is ",shifts[0])
            print("second left shift is ",shifts[1])
            print("p8 of the first key is ",p8s[0])
            print("p8 of the second key is ",p8s[1])
            print("first key is ",keys[0])
            print("second key is ",keys[1])
            print(" initial permutaition ",text_IP)
            print("*"*20)
            ### encryption Stage
            text_half = int(len(text_IP)/2)
            for i in range(rounds):
                right_text = text_IP[text_half:]
                left_text  = text_IP[:text_half]
                right_text = SDES.permutate(SDES.EP,right_text)

                ### xor right of text with key
                xored_text =""
                for bit1,bit2 in zip(right_text,keys[i]):
                    xored_text+= str(int(bit1) ^ int(bit2))


                right_text = SDES.sbox_value(xored_text)
                right_text = SDES.permutate(SDES.P4,right_text)
                
                ### changing left of text and xor with the
                ### temporary changed right side of text
                xored_text = ""
                for bit1,bit2 in zip(left_text, right_text):
                    xored_text += str(int(bit1) ^ int(bit2))
                

                left_text = xored_text
                right_text = text_IP[text_half:]

                ### checking if its last round to not swap
                if i<rounds-1:
                    left_text ,right_text = right_text,left_text
                
                ### new text for the next encryption round
                text_IP = left_text + right_text

            cipher_text = ""
            z=1
            for k in range(9):
                for i in range(len(SDES.IP)):
                    if SDES.IP[i] == z:
                        cipher_text+=text_IP[i]
                        z+=1 
                        break
 
            return cipher_text

    @staticmethod
    def permutate(permutation,key):
        key_P = ""

        for number in permutation:
            key_P += key[number-1]

        return key_P

    @staticmethod
    def shift(key_P,shift=1):

        half_len = int(len(key_P)/2) 
        halfs = list() ### to put two halfs of the string in form of list

        halfs.append( list( key_P[:half_len] )  ) #slicing string
        halfs.append( list( key_P[half_len:] )  )
        
        ### LS each half of key
        for half in halfs:
            for i in range(shift):
                first_bit = half[0]   
                del half[0]
                half.append(first_bit)

        ### changing halfs list into string
        key_P = ""
        for half in halfs:
            for bit in half:
                key_P+=bit

        return key_P

    @staticmethod
    def sbox_value(xored_text):
        halfs = list()
        half_len = int(len(xored_text)/2)

        halfs.append(xored_text[:half_len])
        halfs.append(xored_text[half_len:])
        
        i=0
        s_boxed=""
        for half,s_box in zip(halfs,SDES.S):
            
            ### casting from binary to decimal
            row = int(half[0]+half[-1],2) 
            column =int(half[1]+half[2],2)
            value = s_box[row][column]

            ### avoiding errors during casting from decimal to binary
            if value == 0 or value ==1:
                s_boxed+= "0{0:b}".format(value) 
            else:
                s_boxed+= "{0:b}".format(value)
            i+=1
            
        return s_boxed
