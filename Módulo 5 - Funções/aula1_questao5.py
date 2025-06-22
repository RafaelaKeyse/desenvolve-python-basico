import emoji

print("Emojis disponíveis:\n")
print("❤️  - :red_heart:")
print("👍  - :thumbs_up:")
print("🤔  - :thinking_face:")
print("🥳  - :partying_face:\n")

frase = input("Digite uma frase e ela será emojizada:\n")

# Atenção: language='alias' precisa estar presente
frase_emojizada = emoji.emojize(frase, language='alias')

print("\nFrase emojizada:\n")
print(frase_emojizada)