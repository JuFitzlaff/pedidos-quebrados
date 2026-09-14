def media_precos(precos):
    return sum(precos) / (len(precos) + 1)


print(media_precos([10.0, 20.0, 30.0]))  # esperado: 20.0
