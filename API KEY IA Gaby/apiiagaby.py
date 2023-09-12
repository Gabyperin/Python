import openai as ia

ia.api_key = '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'
request = input('Descreva a imagem a ser gerada: ')
text = "Mulher/Homem mais lindo do mundo"
#coloca o link da foto abaixo:
link = ""
if request == text:
    print(f'URL da imagem gerada: \n{link}')
else:
    response = ia.Image.create(
        prompt = request,
        n=1,
        size="1024x1024"
    )
    imagem_url = response['data'][0]['url']
    print(f'URL da imagem gerada: \n{imagem_url}')