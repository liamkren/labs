# app.py
from flask import Flask, render_template_string, request
from model import get_apod_data
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    apod_data = get_apod_data()
    return render_template_string('''
        <h1>Astronomy Picture of the Day</h1>
        <img src="{{ apod_data['url'] }}" alt="APOD Image">
        <p>{{ apod_data['title'] }}</p>
        <p>{{ apod_data['date'] }}</p>
        <p>{{ apod_data['explanation'] }}</p>
        {% if apod_data.get('copyright') %}
            <p>Copyright: {{ apod_data['copyright'] }}</p>
        {% endif %}
        <a href="/history">View History</a>
    ''', apod_data=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    apod_data = None
    if request.method == 'POST':
        selected_date = request.form['date']
        apod_data = get_apod_data(selected_date)
    return render_template_string('''
        <h1>APOD History</h1>
        <form method="post">
            <label for="date">Select a date:</label>
            <input type="date" name="date" id="date" required>
            <button type="submit">Submit</button>
        </form>
        {% if apod_data %}
            <img src="{{ apod_data['url'] }}" alt="APOD Image">
            <p>{{ apod_data['title'] }}</p>
            <p>{{ apod_data['date'] }}</p>
            <p>{{ apod_data['explanation'] }}</p>
            {% if apod_data.get('copyright') %}
                <p>Copyright: {{ apod_data['copyright'] }}</p>
            {% endif %}
        {% endif %}
        <a href="/">Back to Home</a>
    ''', apod_data=apod_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
