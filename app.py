from flask import Flask, render_template, request, redirect, url_for
import time
import random

app = Flask(__name__)


texts = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "All that glitters is not gold.",
    "To be or not to be, that is the question.",
    "Do or do not, there is no try.",
    "Practice makes perfect."
    "This tool rearranges the order of lines in the given textual data."
    " It checks if the current line was already seen."
]

best_score = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global best_score
    start_time = time.time()
    original_text = random.choice(texts)

    if request.method == 'POST':
        typed_text = request.form['typed_text']
        start_time = float(request.form['start_time'])

    
        end_time = time.time()
        total_time = end_time - start_time
        
        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(original_text) and c == original_text[i])
        accuracy = (correct_chars / len(original_text)) * 100 if original_text else 0
        
        word_count = len(typed_text.split())
        time_in_minutes = total_time / 60
        wpm = word_count / time_in_minutes if time_in_minutes > 0 else 0
        
        if wpm > best_score:
            best_score = wpm

        return render_template('index.html', text=original_text, wpm=round(wpm, 2), accuracy=round(accuracy, 2), total_time=round(total_time, 2), best_score=round(best_score, 2), start_time=start_time)

    return render_template('index.html', text=original_text, best_score=round(best_score, 2), start_time=start_time)

@app.route('/restart')
def restart():
    return redirect(url_for('index'))

@app.route('/change-text')
def change_text():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 

