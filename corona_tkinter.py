import tkinter as tk
import random
import requests
import pandas as pd
import time
import matplotlib.pyplot as plt


#_____________________________________________________Matplotlib__________________________________________________________
def new_cases(df):

    df['NewCases'] = df['NewCases'].apply(lambda x: ''.join(x.split(',')) if type(x) == str else x).values.astype(float)
    df = df[~df['NewCases'].isna()][['Country', 'NewCases']]
    df.sort_values('NewCases', ascending=False, inplace=True)
    #world = df[0:1]
    #df = df[2:]
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 30:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    #df.iloc[0, 1] = 468895
    fig, ax = plt.subplots()
    ax.bar(df['Country'][:30], df['NewCases'][:30], color=colors)
    ax.set_xticklabels(df['Country'][:30],rotation=90)
    ax.set_ylim([0, 6000])
    #ax.set_yticklabels(range(0,25000, 1000))
    ax.set_yticks(range(0, 6000, 1000))
    ax.set_title("New Corona Cases", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('Countries')
    ax.set_ylabel("New Cases")
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y = h + 500
        if y >= 6000:
            y = 6500
        text = h
        ax.text(x, y, text, fontsize=20, color=color, rotation=90)
        lb.set_color(color)

    c = "#000000"
    i = 9
    for ylb in ax.get_yticklabels():
        c = list(c)
        if i <= 9:
            c[1] = str(i)
            c[2] = str(i)
        else:
            c[1] = chr(i+97-10)
            c[2] = chr(i+97-10)
        c = "".join(c)
        i += 1
        ylb.set_color(c)
    plt.tight_layout()
    plt.text(18, 4000, f"World - {world['NewCases']}", fontsize=20, color='blue')
    plt.text(18, 5000, f"{time.strftime('%d %b, %Y %I:%M %p')}", fontsize=20, color="#333333")
    plt.text(18, 3000, f"India - {india['NewCases'].values[0]}", fontsize=20, color='green')
    plt.show()


def new_deaths(df):
    df['NewDeaths'] = df['NewDeaths'].apply(lambda s:"".join(s.split(',')) if type(s) == str else s).astype(float)
    df = df[~df['NewDeaths'].isna()]

    df.sort_values('NewDeaths', ascending=False, inplace=True)
    df = df[['Country', 'NewDeaths']]
    df.sort_values('NewDeaths', ascending=False, inplace=True)
    #world = df[0:1]
    #df = df[2:]
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 30:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    #df.iloc[0, 1] = 468895
    fig, ax = plt.subplots()
    ax.bar(df['Country'][:30], df['NewDeaths'][:30], color=colors)
    ax.set_xticklabels(df['Country'][:30],rotation=90)
    ax.set_ylim([0, 1400])
    ax.set_yticks(range(0,1400, 100))
    ax.set_title("New Deaths Due To Corona", fontsize=25, color='red', pad=80)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('Countries')
    ax.set_ylabel("Total Cases")

    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y = h + 100
        text = h

        ax.text(x, y, text, fontsize=20, color=color, rotation=90)
        lb.set_color(color)

    c = "#000000"
    i = 1
    for ylb in ax.get_yticklabels():
        c = list(c)
        if i <= 9:
            c[1] = str(i)
            c[2] = str(i)
        else:
            c[1] = chr(i+97-10)
            c[2] = chr(i+97-10)
        c = "".join(c)
        i += 1
        ylb.set_color(c)
    plt.tight_layout()
    plt.text(18, 800, f"World - {world['NewDeaths']}", fontsize=20, color='blue')
    plt.text(18, 1000, f"{time.strftime('%d %b, %Y %I:%M %p')}", fontsize=20, color="#333333")
    plt.text(18, 600, f"India - {india['NewDeaths'].values[0]}", fontsize=20, color='green')
    plt.show()

def total_cases(df):
    #world = df[0:1]
    #india = df[df['Country'] == 'India']
    #df = df[1:-1]
    df = df.sort_values('TotalCases', ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 30:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    #df.iloc[0, 1] = 468895
    fig, ax = plt.subplots()
    ax.bar(df['Country'][:30], df['TotalCases'][:30], color=colors)
    ax.set_xticklabels(df['Country'][:30],rotation=90)
    ax.set_ylim([0, 175000])
    ax.set_yticklabels(range(0,1800000, 200000))
    ax.set_title("Infected Corona Patients Till Now", fontsize=25, color='red', pad=80)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('Countries')
    ax.set_ylabel("Total Cases")
    c = 1
    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y = h + 10000 if c != 1 else 180000
        if c == 1:
            text = df.iloc[0, 1]
        else:
            text = h
        c += 1
        ax.text(x, y, text, fontsize=20, color=color, rotation=90)
        lb.set_color(color)

    c = "#000000"
    i = 6
    for ylb in ax.get_yticklabels():
        c = list(c)
        if i <= 9:
            c[1] = str(i)
            c[2] = str(i)
        else:
            c[1] = chr(i+97-10)
            c[2] = chr(i+97-10)
        c = "".join(c)
        i += 1
        ylb.set_color(c)
    plt.tight_layout()
    plt.text(18, 150000, f"World - {world['TotalCases']}", fontsize=20, color='blue')
    plt.text(18, 180000, f"{time.strftime('%d %b, %Y %I:%M %p')}", fontsize=20, color="#333333")
    plt.text(18, 130000, f"India - {india['TotalCases'].values[0]}", fontsize=20, color='green')
    plt.show()

def total_deaths(df):
    #world = df[0:1]
    #total = df[-1:]
    #df = df[1:-1]
    df = df.sort_values('TotalCases', ascending=False)
    df = df[['Country','TotalDeaths']]
    df = df.sort_values('TotalDeaths', ascending=False)
    choices = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b', 'c', 'd', 'e']
    def make_color():
        ch = [ random.choice(choices) for i in range(6)]
        return "#"+"".join(ch)
    colors = []
    while len(colors) != 30:
        color = make_color()
        if color in colors:
            continue
        colors.append(color)
    #df.iloc[0, 1] = 468895
    fig, ax = plt.subplots()
    ax.bar(df['Country'][:30], df['TotalDeaths'][:30], color=colors)
    ax.set_xticklabels(df['Country'][:30],rotation=90)
    ax.set_ylim([0, 25000])
    #ax.set_yticklabels(range(0,25000, 1000))
    ax.set_yticks(range(0, 25000, 2000))
    ax.set_title("Corona Deaths Till Now", fontsize=25, color='red', pad=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('Countries')
    ax.set_ylabel("Total Deaths")

    for patch,color,lb in zip(ax.patches, colors, ax.get_xticklabels()):
        x  = patch.get_x() + 0.2
        h = patch.get_height()
        y = h + 1000
        text = h
        ax.text(x, y, text, fontsize=20, color=color, rotation=90)
        lb.set_color(color)

    c = "#000000"
    i = 3
    for ylb in ax.get_yticklabels():
        c = list(c)
        if i <= 9:
            c[1] = str(i)
            c[2] = str(i)
        else:
            c[1] = chr(i+97-10)
            c[2] = chr(i+97-10)
        c = "".join(c)
        i += 1
        ylb.set_color(c)
    plt.tight_layout()
    plt.text(18, 15000, f"World - {world['TotalDeaths']}", fontsize=20, color='blue')
    plt.text(18, 19000, f"{time.strftime('%d %b, %Y %I:%M %p')}", fontsize=20, color="#333333")
    plt.text(18, 13000, f"India - {india['TotalDeaths'].values[0]}", fontsize=20, color='green')
    plt.show()

def main(df):
    while True:
        os.system('clear')
        print("\n\n\n\n")
        menu = """
        Press Control+c to close
            1. Total Cases
            2. Total Deaths
            3. New Cases
            4. New Deaths
            5. Update Data
        """
        print(menu)
        ch = int(input("Choice: "))
        if ch == 1:
            total_cases(df.copy())
        elif ch == 2:
            total_deaths(df.copy())
        elif ch == 3:
            new_cases(df.copy())
        elif ch == 4:
            new_deaths(df.copy())
        elif ch == 5:
            df,world, india = get_data()
            print("updated data sucessfully")
        else:
            print("\nInvalid Choice Try Again")
def get_data():
    url = "https://www.worldometers.info/coronavirus/"
    page = requests.get(url)
    data = pd.read_html(page.content)
    df = data[0]
    df.columns = ['Country', 'TotalCases', 'NewCases', 'TotalDeaths', 'NewDeaths',
           'TotalRecovered', 'ActiveCases', 'Serious,Critical', 'Tot Cases/1M pop',
           'Deaths/1M pop', 'TotalTests', 'Tests/ 1M pop']
    india = df[df['Country'] == 'India']
    world = df.iloc[0, :]
    df = df.iloc[1:-1, :]
    return df, world, india



plt.rcParams['figure.figsize']  = 12, 6
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['xtick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['ytick.major.pad'] = 5
plt.rcParams['axes.labelcolor'] = 'red'
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['legend.fontsize'] = 20

df,world, india = get_data()
def update_data():
    global df, world, india
    df, world, india = get_data()












#_________________________________________________________________TKINTER__________________________________________________

root = tk.Tk()
root.wm_minsize(400, 600)
root.wm_maxsize(400, 600)
root.title("Corona Virus Update")




total_cases_button = tk.Button(root, text="TOTAL CASES", fg='white', bg='blue', font=('monospace', 15, 'bold'),
 command=lambda : total_cases(df),height=2, width=20 )
total_deaths_button = tk.Button(root, text="TOTAL DEATHS", fg='white', bg='blue', font=('monospace', 15, 'bold'),
 command=lambda : total_deaths(df) ,height=2, width=20)
new_cases_button = tk.Button(root, text="NEW CASES", fg='white', bg='blue', font=('monospace', 15, 'bold'),
command=lambda : new_cases(df), height=2, width=20 )
new_deaths_button = tk.Button(root, text="NEW DEATHS", fg='white', bg='blue', font=('monospace', 15, 'bold'),
command=lambda : new_deaths(df), height=2, width=20)

refresh_button = tk.Button(root, text="REFRESHDATA", fg='white', bg='blue', font=('monospace', 15, 'bold'),
command=update_data, height=2, width=20 )
exit_button = tk.Button(root, text="EXIT", fg='white', bg='red', font=('monospace', 15, 'bold'), command=root.destroy ,
height=2, width=20)

total_cases_button.pack(pady=20)
total_deaths_button.pack(pady=5)
new_cases_button.pack(pady=5)
new_deaths_button.pack(pady=5)
refresh_button.pack(pady=5)
exit_button.pack(pady=5)
root.mainloop()
