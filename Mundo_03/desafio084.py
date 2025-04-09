temp = [] 
princ = [] 
mai = men = 0 

while True: 
    temp.append(str(input('Nome: ')))    
    temp.append(float(input('Peso: ')))  # Convert input to float
    
    if len(princ) == 0: 
        mai = men = temp[1]  # Initialize both mai and men with the first weight
    else: 
        if temp[1] > mai: 
            mai = temp[1]  # Update the heaviest weight
        if temp[1] < men: 
            men = temp[1]  # Update the lightest weight
    
    princ.append(temp[:]) 
    temp.clear()  
    
    resp = str(input('Quer continuar [S/N]: ')) 
    if resp in 'Nn': 
        break 
 
print('--=--' * 30) 
print(f'Os dados foram {princ}') 
print(f'Ao todo foram cadastrados {len(princ)} pessoas.') 
print(f'O maior peso foi de {mai} kg.')

for p in princ:
    if p[1]==mai:
        print(f'{p[0]}')

print(f'O menor peso foi de {men} kg.')
for p in princ:
    if p[1]==men:
        print(f'{p[0]}')
        