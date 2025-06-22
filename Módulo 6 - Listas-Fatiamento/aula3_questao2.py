# Extração de domínios usando fatiamento

# aula3_questao2.py

urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Remove 'www.' do início e '.com' do fim usando slicing
dominios = [url[4:-4] for url in urls]

print("URLs:", urls)
print("Domínios:", dominios)
