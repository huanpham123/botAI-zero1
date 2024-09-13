# import requests
# from googletrans import Translator

# # Khởi tạo đối tượng Translator
# translator = Translator()

# def translate_text(text, src='vi', dest='en'):
#     """Dịch văn bản từ ngôn ngữ src sang ngôn ngữ dest."""
#     translation = translator.translate(text, src=src, dest=dest)
#     return translation.text

# def get_api_response(query, api_key):
#     """Gửi yêu cầu đến API và nhận phản hồi."""
#     url = 'https://liaspark.chatbotcommunity.ltd/@LianeAPI_Reworks/api/axis'
#     params = {
#         'key': api_key,
#         'query': query,
#     }
#     response = requests.get(url, params=params)
#     return response.json()

# def process_request(query, api_key):
#     """Xử lý yêu cầu từ người dùng và dịch phản hồi."""
#     # Dịch câu hỏi từ tiếng Việt sang tiếng Anh
#     query_in_english = translate_text(query, src='vi', dest='en')
    
#     # Gửi yêu cầu đến API
#     api_response = get_api_response(query_in_english, api_key)
    
#     # Dịch phản hồi từ tiếng Anh về tiếng Việt
#     message_in_vietnamese = translate_text(api_response.get('message', ''), src='en', dest='vi')
    
#     return message_in_vietnamese

# def main():
#     api_key = 'j86bwkwo-8hako-12C'  # Thay bằng API key của bạn

#     # print("Nhập 'exit' để thoát khỏi chương trình.")
#     while True:
#         query = input("Câu hỏi của bạn: ")

#         if query.lower() == 'exit':
#             break

#         # Xử lý yêu cầu và nhận phản hồi
#         response_message = process_request(query, api_key)

#         # In phản hồi ra màn hình
#         print(response_message)

# if __name__ == '__main__':
#     main()































from flask import Flask, request, render_template
import requests
from googletrans import Translator

app = Flask(__name__)

# Khởi tạo đối tượng Translator
translator = Translator()

def translate_text(text, src='vi', dest='en'):
    """Dịch văn bản từ ngôn ngữ src sang ngôn ngữ dest."""
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text

def get_api_response(query, api_key):
    """Gửi yêu cầu đến API và nhận phản hồi."""
    url = 'https://liaspark.chatbotcommunity.ltd/@LianeAPI_Reworks/api/axis'
    params = {
        'key': api_key,
        'query': query,
    }
    response = requests.get(url, params=params)
    return response.json()

def process_request(query, api_key):
    """Xử lý yêu cầu từ người dùng và dịch phản hồi."""
    query_in_english = translate_text(query, src='vi', dest='en')
    api_response = get_api_response(query_in_english, api_key)
    message_in_vietnamese = translate_text(api_response.get('message', ''), src='en', dest='vi')
    return message_in_vietnamese

@app.route('/', methods=['GET', 'POST'])
def home():
    response_message = ""
    if request.method == 'POST':
        query = request.form.get('query')
        api_key = 'j86bwkwo-8hako-12C'  # Thay bằng API key của bạn
        response_message = process_request(query, api_key)
    
    return render_template('index.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)