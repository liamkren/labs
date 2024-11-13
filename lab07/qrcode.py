from flask import Flask, request, render_template_string
import segno
import io
import base64

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator</title>
</head>
<body>
    <h1>Generate a QR Code</h1>
    <form method="POST">
        <label for="data">Enter your message:</label>
        <input type="text" id="data" name="data" required>
        <button type="submit">Generate QR Code</button>
    </form>
    {% if qr_code %}
        <h2>Your QR Code:</h2>
        <p>Message: {{ message }}</p>
        <img src="{{ qr_code }}" alt="QR Code">
    {% endif %}
</body>
</html>
'''


@app.route("/", methods=["GET", "POST"])
def generate_qr():
    qr_code = None
    message = None

    if request.method == "POST":
        # Get the data from the form
        message = request.form["data"]

        # Generate QR code
        qr = segno.make(message)

        # Save QR code as a binary image in memory
        img_buffer = io.BytesIO()
        qr.save(img_buffer, kind="png", scale=4)

        # Convert the binary image to base64 to embed in HTML
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
        qr_code = f"data:image/png;base64,{img_base64}"

    return render_template_string(html_template, qr_code=qr_code, message=message)


if __name__ == "__main__":
    app.run(debug=True)

