import qrcode

# Cria o objeto QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constant.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicione o texto ao QR Code
qr.add_data('Coloque aqui para que deseja criar um qr code seja link, frases, canais de pagamento, outros...')

# Gera o QR Code
qr.make(fit=True)

# Cria um objeto de imagem a partir de QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem em um arquivo
img.save('qr_code.png')