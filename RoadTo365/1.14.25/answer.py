def findThePrefixCommonArray(A, B):
        n=len(A)
        counter=0
        temp_list=[0]*(n+1)
        c=[0]*n
        for i in range(n):
            temp_list[A[i]]+=1
            if temp_list[A[i]] ==2:
                counter+=1
            temp_list[B[i]]+=1
            if temp_list[B[i]]==2:
                counter+=1
            c[i]=counter
        return c

print(findThePrefixCommonArray([1,3,2,4],[3,1,2,4])) # [0,2,3,4]