from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []  # List to store tasks

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

#creating task
@app.route('/create_task', methods=['POST'])
def create_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

#Editing task
@app.route('/update_task/<int:index>', methods=['POST'])
def update_task(index):
    updated_task = request.form.get('updated_task')
    if updated_task:
        tasks[index] = updated_task
    return redirect(url_for('index'))

#Deleting task
@app.route('/delete_task/<int:index>', methods=['GET'])
def delete_task(index):
    del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
