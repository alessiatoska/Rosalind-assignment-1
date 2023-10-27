#FIBD rosalind

def fibd(n, m):
    rabbit = [1, 1]

    for months in range(2,n):
        if months < m:
            rabbit.append(rabbit[-2] + rabbit[-1])
        elif months == m:
            rabbit.append(rabbit[-2] + rabbit[-1] - 1)
        else:
            rabbit.append(rabbit[-2] + rabbit[-1] - rabbit[-(m + 1)])

    return rabbit[-1]

print(fibd(91,18))
                                                          
#or
'''
def fibd(n, m):
    rabbit = [1, 1]

    for months in range(2, n):
        r = rabbit[-2] + rabbit[-1] - (rabbit[-(m + 1)] if months >= m + 1 else 0) - (1 if months == m else 0)
        rabbit.append(r)

    return rabbit[-1]

print(fibd(91,18))
'''
