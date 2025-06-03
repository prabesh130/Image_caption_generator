from flask import Flask, request,render_template,redirect,url_for
import os
from werkzeug.utils import secure_filename
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file=request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath=(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(filepath)
            caption="This is a placeholder caption"
            return render_template('index.html', image_url=filepath, caption=caption)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
