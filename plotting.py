import matplotlib.pyplot as plt
import numpy as np
import sqlite3

veggie = []
nonveggie = []
vegan = []
headcount = []
waste = []

def create_query(year, week=''):
    query = "SELECT * FROM consumption WHERE year={}".format(year)

    if week:
        query = "SELECT * FROM consumption WHERE year={} AND week={}".format(year, week)

    return query


def plot_stack_bar(year, week, x, y1, y2, y3, y4):
    x = np.arange(1,x)
    y1 = np.rint(np.array(veggie)).astype(int)
    y2 = np.rint(np.array(vegan)).astype(int)
    y3 = np.rint(np.array(nonveggie)).astype(int)
    y4 = np.rint(np.array(headcount)).astype(int)
    
    # plot bars in stack manner
    plt.bar(x, y1, color='r')
    plt.bar(x, y2, bottom=y1, color='b')
    plt.bar(x, y3, bottom=y1+y2, color='y')
    plt.bar(x, y4-y2-y3-y1, bottom=y3+y2+y1, color='g')
    plt.xlabel("Weeks of {}".format(year))
    plt.ylabel("Food Consumption Details")
    plt.legend(["Veggie", "Vegan", "Non-veggie", "Headcounts"])
    plt.title("")
    plt.savefig('static/temp.png', bbox_inches='tight')

    return 


def data_matplot(dbanme, year,week=''):
    conn = sqlite3.connect(dbanme)
    c = conn.cursor()
    form_query = create_query(year)
    week = {}        
    result = conn.execute(form_query)
    for i in result:
        consu = {}
        consu['veggie'] = i[4]
        veggie.append(int(i[4]))
        consu['nonveggie'] = i[3]
        nonveggie.append(int(i[3]))
        consu['vegan'] = i[5]
        vegan.append(int(i[5]))
        consu['headcount'] = i[6]
        headcount.append(int(i[6]))
        consu['waste'] = i[7]
        waste.append(int(i[7]))
        week[i[2]] = consu
    x_values = len(week.keys())+1
    plot_stack_bar(year, week, x_values, veggie, vegan, nonveggie,headcount)

if __name__ == "__main__":
    year = input("select year:")
    data_matplot("instance/canteen.db", int(year))