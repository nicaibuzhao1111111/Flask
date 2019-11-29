from flask import Flask,render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    context={
        "users":["你猜1","你猜3","你猜2"],
        "person":{
            "user":"李磊",
            "age":18,
            "country":"china"
        },
        "books":[
            {
                "name":"三国演义",
                "author":"罗贯中",
                "price":110
            },
            {
                "name": "西游记",
                "author": "罗贯中",
                "price": 110
            },
            {
                "name": "红楼梦",
                "author": "罗贯中",
                "price": 110
            },
            {
                "name": "水浒传",
                "author": "施耐庵",
                "price": 110
            },
        ]
    }

    return render_template("index.html",**context)


if __name__ == '__main__':
    app.run(debug=True)
