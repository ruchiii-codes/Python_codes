Languages = ['Java', 'Python', 'Php', 'c', 'JavaScript']
L = [Language for Language in Languages if Language.startswith('P')]  # Check if each language starts with 'P'
print(L)  # Output: ['Python', 'Php']