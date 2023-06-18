import telebot
import torch 
from transformers import T5ForConditionalGeneration, T5Tokenizer

def generate_t5(text):
    """Функция суммаризации исходного текста"""
    inputs = tokenizer(text, return_tensors='pt').to(device)
    with torch.no_grad():
        hypotheses = model.generate(inputs["input_ids"], num_beams=3, max_length=len(text)*0.5)
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)

tokenizer = T5Tokenizer.from_pretrained("nikitakhozin/t5_summarization")
model = T5ForConditionalGeneration.from_pretrained("nikitakhozin/t5_summarization")
device = 'cpu'

bot = telebot.TeleBot(<YOUR_TG_BOT_TOKEN>)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я умею упрощать текст. Отправь мне предложение и я его упрощу.")

@bot.message_handler(commands=['simplify'])
def simplify_text(message):
    input_text = message.text[10:]  #удаляем "/simplify " из сообщения
    output_text = generate_t5(f'simplify | {input_text}')
    bot.reply_to(message, output_text)

bot.polling()