from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.brevo.com/v3/account'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = request.form.get('api_key')
        if api_key:
            # Use the provided API key
            headers = {'api-key': api_key}
        else:
            # Use the default API key
            headers = {'api-key': API_KEY}
        
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return render_template('response.html', data=data)
        else:
            return f"Error: {response.status_code}"
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
