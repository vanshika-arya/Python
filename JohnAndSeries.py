a = float(input("Enter the first term: "))

d = float(input("Enter the common difference: "))

n = int(input("Enter the term number: "))
nth_term = a + (n - 1) * d

sum_n_terms = (n / 2) * (2 * a + (n - 1) * d)
print("The nth term ", nth_term)
print("The sum up to the nth term ", sum_n_terms)