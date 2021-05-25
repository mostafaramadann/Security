class PlayFair():

    ### initializing constants
    ### ie the aplhabet
    ALPHABET =  ["a","b","c","d","e","f",
                 "g","h","i","k","l",
                 "m","n","o","p","q","r",
                 "s","t","u","v","w","x",
                 "y","z"
                ]

    @staticmethod
    def encrypt(text:str,key:str)->str:

        ### avoiding errors that could happen
        ### due to different case letters
        text = text.lower().strip()
        key_clone  = key.lower().strip()
        key=""

        ### removing repeated letters from key
        for letter in key_clone:
            if letter not in key:
                key+=letter
        
        key = list(key)
        letter_pairs = list()
        pair = list()

        ### Parsing text into letter pairs for easier encryption
        for letter in text:

            ### checking if current letter has been repeated
            ### and replacing with x
            if len(pair)==1 and pair[len(pair)-1] == letter:
                pair.append('x')
                letter_pairs.append(pair)
                pair = list(letter)
            
            elif len(pair)==1:
                pair.append(letter)
                letter_pairs.append(pair)
                pair = list()
            
            else:
                pair.append(letter)
        
        ### if there are left over letters from the loop
        if len(pair)!=0:
            letter_pairs.append(pair)

        ### checking if last letter is alone
        ### appending x if it is
        last_pair = len(letter_pairs)-1
        if len(letter_pairs[last_pair])%2!=0:
            letter_pairs[last_pair].append("x")


        ### removing Key letters in Alphabet to avoid repetition
        alphabet = PlayFair.ALPHABET.copy()
        for letter in key: 
            if letter in alphabet:
                alphabet.remove(letter)
                

        matrix = list()
        alpha_index = 0

        j_index_r = 0
        j_index_c = 0

        for r in range(0,5):
            row = list()
            for c in range(0,5):
                if len(key)>0:
                    letter = key.pop(0)

                    if letter == "i":
                        j_index_c = c
                        j_index_r = r

                    row.append(letter)
                else:
                    letter = alphabet[alpha_index]

                    if letter == "i":
                        j_index_c = c
                        j_index_r = r

                    row.append(letter)
                    alpha_index+=1
                    
            matrix.append(row)

        matrix[j_index_r][j_index_c] = [matrix[j_index_r][j_index_c],"j"]
        
        cipher_text = ""
        while len(letter_pairs)!=0:

            l1,l2= letter_pairs.pop(0)
            l1r = l1c = l2r = l2c = None
            for r in range(len(matrix)):
                for c in range(len(matrix[r])):

                    letter = matrix[r][c]\
                    if not isinstance(matrix[r][c],list)\
                    else matrix[r][c][0]

                    if letter == l1:
                        l1r = r
                        l1c = c
                    elif letter == l2:
                        l2r = r
                        l2c = c

            cipher_text += PlayFair.return_match(matrix,l1r,l1c,l2r,l2c)
            cipher_text += PlayFair.return_match(matrix,l2r,l2c,l1r,l1c)
        for row in matrix:
            print(row)
        print("*"*20)
        return cipher_text.upper()
        
    @staticmethod
    def return_match(matrix,l1r,l1c,l2r,l2c):
        match=""
       
        if l1r == l2r and l1c!=l2c:
            ### column less than end
            if l1c<4:
                match+=matrix[l1r][l1c+1]
            ### column is end start from begining of row
            elif l1c == 4:
                match+=matrix[l1r][0]

        elif l1r!=l2r and l1c == l2c:
            ### row less than end
            if l1r<4:
                match+=matrix[l1r+1][l1c]
            ### last row resets to go up
            elif l1r == 4:
                match+=matrix[0][l1c]
                
        ### check for intersection
        else:
            if l1c<l2c:
                match+=matrix[l1r][l1c+(l2c-l1c)]\
                if not isinstance(matrix[l1r][l1c+(l2c-l1c)],list)\
                else matrix[l1r][l1c+(l2c-l1c)][0]
            else:
                match+=matrix[l1r][l2c]\
                if not isinstance(matrix[l1r][l2c],list)\
                else matrix[l1r][l2c][0]

        return match

    @staticmethod
    def decrypt(text,key):
       text = text.lower().strip()
       key  = key.lower().strip()

       ### great observation , Encryption 8 times
       ### gives the decrypted text
       ### gat ma3aya bel kofta
       for i in range(9):
           text = PlayFair.encrypt(text,key)
       return text