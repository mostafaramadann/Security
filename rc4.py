class RC4():
    S=list(range(0,8))
    @staticmethod
    def encrypt(p,key):

        s = RC4.S.copy()
        t = key.copy()
        if len(key)<8:
            for value in key:
                if len(key)+1<8:
                    t.append(value)

        j=0
        for i in range(8):
            j= (j+s[i]+t[i])%8
            s[i],s[j]=s[j],s[i]

        i = j = 0
        C=list()
        for z in range(len(p)):
            i = (i+1) %8
            j = (j+s[i])%8

            s[i],s[j]=s[j],s[i]
            t=(s[i]+s[j])%8

            C.append(s[t]^p[z])

        return C
