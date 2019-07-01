import flask
import qrcode
# from datetime import timedelta

app = flask.Flask(__name__)

# app.config["SEND_FILE_MAX_AGE_DEFAULT"] = timedelta(seconds=1)

@app.route("/")
def home():
    # # 第一步： 获取要生成二维码的数据
    # data = flask.request.args.get("data")
    # print(data)

    # # 第二步： 生成二维码图片
    # img = qrcode.make(data)
    # img.save(r"D:\day5\qrcode_tool_online\static\qr.jpg")

    # # 第三步： 在页面上显示二维码图片
    # return '<img src="%s" />' % flask.url_for('static',filename='qr.jpg')

    return flask.render_template('qr_tool.html')

@app.route("/qr", methods=["POST"])
def qr():
    # # 第一步： 获取要生成二维码的数据
    data = flask.request.form.get("data")
    # print(data)

    # # 第二步： 生成二维码图片
    img = qrcode.make(data)
    img.save(r"D:\day5\qrcode_tool_online\static\qr.jpg")

    # # 第三步： 在页面上显示二维码图片
    return '<img src="%s" />' % flask.url_for('static',filename='qr.jpg')

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)