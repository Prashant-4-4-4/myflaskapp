from flask import Flask , render_template , request # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/manager",methods=["GET","POST"])
def manage():
    if request.method == "POST" :
        income = int(request.form.get("income"))
        mode = request.form.get("mode")

        result = {} 
        if mode == "super" :
            if income <= 15000 :

                result["Rent"] = 0.15 * income
                result["Travel"] = 0.10 * income
                result["Bills"] = 0.10 * income
                result["Grocery"] = 0.15 * income
                result["Hobby"] = 0.05 * income
                result["Saving"] = 0.45 * income

            else :
                result["Rent"] = 2000
                result["Travel"] = 1000
                result["Bills"] = 1500
                result["Grocery"] = 1500
                result["Hobby"] = 900
                result["Saving"] = income - sum(result.values())

        elif mode == "saving" :
            if income >= 80000 :
                result["Rent"] = 15000
                result["Travel"] = 10000
                result["Bills"] = 15000
                result["Grocery"] = 10000
                result["Hobby"] = 5000
                result["Saving"] = income - sum(result.values())

            else :
                result["Rent"] = 0.25 * income
                result["Travel"] = 0.15 * income
                result["Bills"] = 0.20 * income
                result["Grocery"] = 0.20 * income
                result["Hobby"] = 0.05 * income
                result["Saving"] = 0.15 * income

        return render_template("result.html", income = income, result=result, mode=mode)

    
    return render_template("manager.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__" :
    app.run(debug=True)