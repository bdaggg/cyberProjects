from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <body>
                <form>
                    <label for="text_input">Enter some text:</label><br>
                    <input type="text" id="text_input" name="text_input"><br>
                    <input type="submit" value="Submit">
                </form>
                <br>
                <p>You entered: {}</p>
            </body>
        </html>
    '''.format(request.args.get('text_input'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
