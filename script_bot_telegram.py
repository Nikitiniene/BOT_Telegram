import requests
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TOKEN_BOT")

async def iniciar(update, context):
    msg = (
        "Olá, sou o Cotador Monetário!\n"
        "Use:\n"
        "/dolar_americano\n"
        "/dolar_australiano\n"
        "/dolar_canadense\n"
        "/euro\n"
        "/libra_esterlina\n"
        "/iene_japones\n"
        "/peso_argentino\n"
        "/peso_uruguaio\n"
        "/peso_chileno\n"
        "/peso_colombiano\n"
        "/peso_mexicano\n"
        "/rial_saudita\n"
        "/bitcoin\n"
        "/ethereum\n"
        "para ver o preço de cada moeda convertida em R$ em tempo real."
    )
    await update.message.reply_text(msg)

async def mostrar_preco(update, context):
    texto = update.message.text.lower()

    if "/dolar_americano" in texto:
        moeda = "USD"
        nome = "Dólar Americano"
    elif "/dolar_australiano" in texto:
        moeda = "AUD"
        nome = "Dólar Australiano"
    elif "/dolar_canadense" in texto:
        moeda = "CAD"
        nome = "Dólar Canadense"
    elif "/euro" in texto:
        moeda = "EUR"
        nome = "Euro"
    elif "/libra_esterlina" in texto:
        moeda = "GBP"
        nome = "Libra Esterlina"
    elif "/iene_japones" in texto:
        moeda = "JPY"
        nome = "Iene Japonês"
    elif "/peso_argentino" in texto:
        moeda = "ARS"
        nome = "Peso Argentino"
    elif "/peso_uruguaio" in texto:
        moeda = "UYU"
        nome = "Peso Uruguaio"
    elif "/peso_chileno" in texto:
        moeda = "CLP"
        nome = "Peso Chileno"
    elif "/peso_colombiano" in texto:
        moeda = "COP"
        nome = "Peso Colombiano"
    elif "/peso_mexicano" in texto:
        moeda = "MXN"
        nome = "Peso Mexicano"
    elif "/rial_saudita" in texto:
        moeda = "SAR"
        nome = "Rial Saudita"
    elif "/bitcoin" in texto:
        moeda = "BTC"
        nome = "Bitcoin"
    elif "/ethereum" in texto:
        moeda = "ETH"
        nome = "Ethereum"
    else:
        await update.message.reply_text(
            "Comando não reconhecido. Digite /start para ver a lista de moedas disponíveis."
        )
        return

    link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    dados = requests.get(link).json()
    preco = float(dados[f"{moeda}BRL"]["bid"])

    await update.message.reply_text(f"1 {nome} = R$ {preco:.5f}")

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("start", iniciar))
app.add_handler(CommandHandler("dolar_americano", mostrar_preco))
app.add_handler(CommandHandler("dolar_australiano", mostrar_preco))
app.add_handler(CommandHandler("dolar_canadense", mostrar_preco))
app.add_handler(CommandHandler("euro", mostrar_preco))
app.add_handler(CommandHandler("libra_esterlina", mostrar_preco))
app.add_handler(CommandHandler("iene_japones", mostrar_preco))
app.add_handler(CommandHandler("peso_argentino", mostrar_preco))
app.add_handler(CommandHandler("peso_uruguaio", mostrar_preco))
app.add_handler(CommandHandler("peso_chileno", mostrar_preco))
app.add_handler(CommandHandler("peso_colombiano", mostrar_preco))
app.add_handler(CommandHandler("peso_mexicano", mostrar_preco))
app.add_handler(CommandHandler("rial_saudita", mostrar_preco))
app.add_handler(CommandHandler("bitcoin", mostrar_preco))
app.add_handler(CommandHandler("ethereum", mostrar_preco))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mostrar_preco))

print("CONECTADO COM SUCESSO!")
app.run_polling()