"""
create by  hanxiao on  2018/5/31
"""

from app import create_app


__author__ = "hanxiao"

app = create_app()

if __name__ == "__main__":
    app.run(host=app.config["HOST"], debug=app.config["DEBUG"], port=app.config["PORT"], threaded=False)
