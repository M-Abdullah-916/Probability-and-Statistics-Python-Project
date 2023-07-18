import time
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from tkinter import ttk
from tkinter import *

df_terrorismInState = pd.read_csv("terrorism1.csv")
df_terrorismInCountry = pd.read_csv("terrorism2.csv")
df_terrorismInYear = pd.read_csv("terrorism3.csv")
df_terrorismMoreThan10 = pd.read_csv("terrorism4.csv")
print(df_terrorismInState.shape)
print(df_terrorismInCountry.shape)
print(df_terrorismInYear.shape)
print(df_terrorismMoreThan10.shape)
splashWindow = Tk()

appWidth = 720
appHeight = 680
screenWidth = splashWindow.winfo_screenwidth()
screenHeight = splashWindow.winfo_screenheight()

xCoordinates = (screenWidth / 2) - (appWidth / 2)
yCoordinates = (screenHeight / 2) - (appHeight / 2)

splashWindow.overrideredirect(True)
splashWindow.geometry(f'{appWidth}x{appHeight}+{int(xCoordinates)}+{int(yCoordinates)}')
splashBackground = PhotoImage(file="images/Probability and Statistics.png")
pictureLabel = Label(splashWindow, image=splashBackground)
pictureLabel.place(x=0, y=0, relwidth=1, relheight=1)

progressBar = ttk.Progressbar(splashWindow, orient=HORIZONTAL, length=300, mode='determinate')
progressBar.place(x=170, y=450, relwidth=0.5, relheight=0.05)


def progress():
    progressBar.start(20)
    for x in range(5):
        progressBar['value'] += 20
        splashWindow.update_idletasks()
        time.sleep(1)


def frequencyDistributionFunc():
    Years = df_terrorismInCountry['iyear']
    Country = df_terrorismInCountry['United Kingdom']
    df = pd.Series({'Year': [Years],
                    'Country': [Country]})
    df.value_counts(sort=False)
    print(df)


def barCharFunc1():
    plt.bar(df_terrorismInState['Number of Incidents'], df_terrorismInState['Number Killed'])
    plt.title("Number of Incidents vs Number of People Killed in Terrorism")
    plt.show()


def barCharFunc2():
    plt.bar(df_terrorismInState['Number of Incidents'], df_terrorismInState['Number Injured'])
    plt.title("Number of Incidents vs Number of People Injured in Terrorism")
    plt.show()


def boxPlotFunc1():
    df_terrorismInState.boxplot(column='Number of Incidents')
    plt.title("Number of Incidents in Respective Countries")
    plt.show()


def boxPlotFunc2():
    df_terrorismInState.boxplot(column='Number Killed')
    plt.title("Number of People Killed in Respective Countries")
    plt.show()


def boxPlotFunc3():
    df_terrorismInState.boxplot(column='Number Injured')
    plt.title("Number of People Injured in Respective Countries")
    plt.show()


def histogramFunc1():
    df_terrorismInState.hist(column=['Number of Incidents'], bins=10)
    plt.title("Number of Incidents Occurred")
    plt.show()


def histogramFunc2():
    df_terrorismInState.hist(column=['Number Killed'], bins=10)
    plt.title("Number of People Killed")
    plt.show()


def histogramFunc3():
    df_terrorismInState.hist(column=['Number Injured'], bins=10)
    plt.title("Number of People Injured")
    plt.show()


def pieChartFunc1():
    pieChartLabels = df_terrorismInYear['iyear']
    plt.pie(df_terrorismInYear['fatalities'], labels=pieChartLabels)
    plt.title("More than 10 People Killed in Respective Years")
    plt.show()


def pieChartFunc2():
    pieChartLabels = df_terrorismMoreThan10['Country']
    plt.pie(df_terrorismMoreThan10['Killed More than 100'], labels=pieChartLabels)
    plt.title("More than 10 People Killed in Respective Years")
    plt.show()


def lineGraphFunc1():
    plt.plot(df_terrorismInState['Number of Incidents'], df_terrorismInState['Number Killed'])
    plt.title('Number of Incidents vs Number of People Killed')
    plt.xlabel('Total Incidents ')
    plt.ylabel('People Killed')
    plt.show()


def lineGraphFunc2():
    plt.plot(df_terrorismInState['Number of Incidents'], df_terrorismInState['Number Injured'])
    plt.title('Number of Incidents vs Number of People Injured')
    plt.xlabel('Total Incidents ')
    plt.ylabel('People Injured')
    plt.show()


def hyperGeometricFunc():
    totalCountN = 0
    totalCountries = df_terrorismInState['Country']
    for x in totalCountries:
        totalCountN += 1

    safeCountA = 0
    totalSafeCountries = df_terrorismInState['Number of Incidents']
    for x in totalSafeCountries:
        if x < 50:
            safeCountA += 1

    safeCountn = 0
    totalSafeCountries = df_terrorismInState['Number Killed']
    for x in totalSafeCountries:
        if x < 5:
            safeCountn += 1

    x = 10

    s = np.random.hypergeometric(totalCountN, safeCountA, safeCountn, x)
    plt.hist(s)
    plt.title("Total Countries and Safe to Live Countries upon X = 10")
    plt.show()


def regressionModellingFunc():
    xValue = df_terrorismInState[['Number of Incidents', 'Number Killed', 'Number Injured']]
    yValue = df_terrorismInState['Number US Killed']
    regression = linear_model.LinearRegression()
    regression.fit(xValue, yValue)

    incidents = 0
    totalSafeCountries = df_terrorismInState['Number of Incidents']
    for x in totalSafeCountries:
        incidents += 1

    killed = 0
    totalSafeCountries = df_terrorismInState['Number Killed']
    for x in totalSafeCountries:
        killed += 1

    injured = 0
    totalSafeCountries = df_terrorismInState['Number Injured']
    for x in totalSafeCountries:
        injured += 1

    print(regression.predict([[incidents, killed, injured]]))


def BarCharFuncCollection():
    barCharFunc1()
    barCharFunc2()


def boxPlotFuncCollection():
    boxPlotFunc1()
    boxPlotFunc2()
    boxPlotFunc3()


def histogramFuncCollection():
    histogramFunc1()
    histogramFunc2()
    histogramFunc3()


def pieChartFuncCollection():
    pieChartFunc1()
    pieChartFunc2()


def lineGraphFuncCollection():
    lineGraphFunc1()
    lineGraphFunc2()


def mainWindow():
    splashWindow.destroy()
    rootWindow = Tk()
    rootWindow.title("Probability Project")
    rootWindow.geometry(f'{appWidth}x{appHeight}+{int(xCoordinates)}+{int(yCoordinates)}')
    rootWindow.overrideredirect(True)

    mainScreenLabel = Label(rootWindow, text=" Terrorism Past Data and Predictions", font=("Helvetica", 30))
    mainScreenLabel.grid(row=0, column=0, pady=20, padx=20)
    frame = Frame(rootWindow)
    frame.grid(row=1, column=0, pady=30)

    frequencyDistributionButton = Button(frame, text="FrequencyDistribution", font=("Helvetica", 15),
                                         command=frequencyDistributionFunc)
    barChartButton = Button(frame, text="BarChart", font=("Helvetica", 15), command=BarCharFuncCollection)
    boxPlotButton = Button(frame, text="BoxPlot", font=("Helvetica", 15), command=boxPlotFuncCollection)
    histogramButton = Button(frame, text="Histogram", font=("Helvetica", 15), command=histogramFuncCollection)
    pieChartButton = Button(frame, text="PieChart", font=("Helvetica", 15), command=pieChartFuncCollection)
    lineGraphButton = Button(frame, text="LineGraph", font=("Helvetica", 15), command=lineGraphFuncCollection)
    hyperGeometricButton = Button(frame, text="HyperGeometricGraph", font=("Helvetica", 15),
                                  command=hyperGeometricFunc)
    regressionModellingButton = Button(frame, text="RegressionModelling", font=("Helvetica", 15),
                                       command=regressionModellingFunc)
    closeButton = Button(frame, text="Close", font=("Helvetica", 15), command=rootWindow.destroy)

    frequencyDistributionButton.grid(row=0, column=0, pady=5)
    barChartButton.grid(row=1, column=0, pady=5)
    boxPlotButton.grid(row=2, column=0, pady=5)
    histogramButton.grid(row=3, column=0, pady=5, padx=5)
    pieChartButton.grid(row=4, column=0, pady=5)
    lineGraphButton.grid(row=5, column=0, pady=5, padx=5)
    hyperGeometricButton.grid(row=6, column=0, pady=5, padx=5)
    regressionModellingButton.grid(row=7, column=0, pady=5, padx=5)
    closeButton.grid(row=8, column=0, pady=5)

    mainScreenLabelEnd = Label(frame, text=" 19F-0916, 19F-0965, 19F-0315, 19F-0148", font=("Helvetica", 15))
    mainScreenLabelEnd.grid(row=9, column=0, pady=5)
    mainScreenLabelEnd = Label(frame, text="   NOTE: Data can be change from CSV Files, Can be Found in Project Folder",
                               font=("Helvetica", 15))
    mainScreenLabelEnd.grid(row=10, column=0, pady=5)


progress()
splashWindow.after(3500, mainWindow)

mainloop()
