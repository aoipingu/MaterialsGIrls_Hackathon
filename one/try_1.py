from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"
if __name__ =='__main__':
    app.run()



@app.route("/John")
def John():
    return "Hello, John!"
if __name__=='__main__':
    app.run(debug=True)

class  materials_selection(database):
    def database_creator():
        import csv
        materials = 'materials.csv'
        fields = []
        rows = []
        with open(materials, 'r') as materialscsv:
            csvreader = csv.reader(materialscsv)
            fields = next(csvreader)

            for row in csvreader:
                rows.append(row)
            print ('No. of different materials is : %d"%(csvreader.line_num)')


    def search():
        pass
    pass