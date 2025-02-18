import emoji
a = input("Digite 'sim' se você gosta de pizza, ou digite 'não' se você desgosta:  ").strip().lower()
if a == "sim": 
    print(emoji.emojize("que bom! Eu tambem curto! :thumbs_up: "))
elif a == "não":
    print(emoji.emojize("Você não gosta de pizza? Estou decepcionado! :thumbs_down:"))
elif a.isdigit:
    print("Hum.. porque você digitou numeros?")