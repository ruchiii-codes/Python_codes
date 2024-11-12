letter = ''' Dear <|Name|>, 
 You are selected! 
 <|Data|> '''
print(letter.replace("<|Name|>", "Harry").replace("<|Data|>", "24 September 2050"))  # Chaning of .replace function