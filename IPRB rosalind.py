#IPRB rosalind


#k--> homozygous dominant, m-->heterozygous, n-->homozygous recessive

def p_dominant(k,m,n):
    total = k+m+n 

    n_n = (n / total) * ((n - 1) / (total - 1))
    m_m = (m / total) * ((m - 1) / (total - 1))
    m_n = (m / total) * (n/ (total - 1)) +(n / total) * (m/ (total - 1))

    tot_recessive = n_n + m_m * 1/4 + m_n * 1/2
    dominant=1-tot_recessive
    return dominant
print(p_dominant(22,15,19))



