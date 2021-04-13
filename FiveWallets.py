#Imagine five wallets with different amounts of cash in them. Store these five values in a list, and print out the following sentences:
wallets = [540, 37, 1002, 61, 20]
#"The fattest wallet has $ value in it."
print('"The fattest wallet has $' + str(max(wallets)) + ' value in it."')
#"The skinniest wallet has $ value in it."
print('"The skinniest wallet has $' + str(min(wallets)) + ' value in it."')
#"All together, these wallets have $ value in them."
print('"All together, these wallets have $' + str(sum(wallets)) + ' value in them."')
