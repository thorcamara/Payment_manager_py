print('{:=^40}'.format('\tSHOP\t'))
price = float(input('Price Total: $ '))
print('{:=^42}'.format('\tPayment Methods \t'))
print(''' [ 1 ] Cash
 [ 2 ] Debit card
 [ 3 ] 2x Installments
 [ 4 ] 3x Installments or more\n''')
option = int(input('What is your choice? '))
if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    installment = total / 2
    print('\nYour purchase will be financed in \033[1;33m2\033[mx of $\033[1;32m{:.2f} INTEREST-FREE\033[m'.format(installment))
elif option == 4:
    total = price + (price * 20 / 100)
    totalInstallments = int(input('How many installments? '))
    installment = total / totalInstallments
    print('\nYour purchase will be payed in \033[1;33m{}\033[mx installments of $\033[1;32m{:.2f}\033[m \033[1;31mWITH INTEREST\033[m'.format(totalInstallments, installment))
else:
    total = price
    print('\033[1;31mINVALID OPTION \033[mof payment method. Try again!')
print('\nYour purchase of $\033[1;33m{:.2f}\033[m will cost $\033[1;32m{:.2f}\033[m'.format(price, total))
