import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from statistics import mean, median, mode
from collections import Counter
import math
import statistics 
from math import comb
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

HEIGHT = 700
WIDTH = 800 
window = tk.Tk()
window.geometry("900x700")
window.title("Statistics Calculator")

canvas = tk.Canvas(window, height = HEIGHT, width =WIDTH)
canvas.pack()

upperframe = tk.Frame(window, bg ='#072e51', bd=5)
upperframe.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.03)

frame = tk.Frame(window, bg ='#cfe2f3', bd=5)
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.3)

label = tk.Label(frame, text="CMPSC 136 CALCULATOR", bg="#072e51", font=("Helvetica", 30, "bold"), fg = "#f7f5ef")
label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.3)

lower_frame = tk.Frame(window, bg ='#cfe2f3', bd=10)
lower_frame.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.8)

# Create a list of options for the first dropdown
topic = ["Descriptive Statistics", 
            "Probability and Methods of Counting", 
            "Discrete Random Variables",
            "Sampling Distribution",
            "Confidence Intervals",
            "Hypothesis Testing"]

# Create a StringVar to store the selected option of the first dropdown
topic_var = tk.StringVar(window)
topic_var.set("Choose One")

# Create the first dropdown
dropdown = tk.OptionMenu(lower_frame, topic_var, *topic)
dropdown.config(relief="ridge", borderwidth=3)
dropdown.place(relx = 0.30, rely = 0, relwidth = 0.25, relheight = 0.1)
# Create a list of options for the second dropdown
operations = [""]

# Create a StringVar to store the selected option of the second dropdown
operations_var = tk.StringVar(window)
operations_var.set(" ")

# Create the second dropdown
dropdown2 = tk.OptionMenu(lower_frame, operations_var, *operations)
dropdown2.config(relief="ridge", borderwidth=3)
dropdown2.place(relx = 0.55, rely = 0, relwidth = 0.25, relheight = 0.1)

# Create result frame
def result_frame(result, lower_frame, rel_y):
    result_label = tk.Label(lower_frame, bg="#f0f0f5", font=('Arial', 12))
    result_label.place(relx=0.2, rely=rel_y, relwidth=0.6, relheight=0.5)
    result_label.config(text=result)

def error():
    messagebox.showerror("Error", "Please enter valid integer numbers with appropriate spaces")

# Create lower frame
def create_lower_frame(window, relx, rely, relwidth, relheight):
    lower_frame = tk.Frame(window, bg='#cfe2f3', bd=10)
    lower_frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    return lower_frame

# Function to update the options of the second dropdown based on the selected option of the first dropdown
def update_options(*args):
    global operations
    if topic_var.get() == topic[0]:
        operations = ["Mean, Median, Mode, Max, Min, Range",
                    "Interquartile Range, Upper Outlier Limit, Lower Outlier Limit",
                    "Frequency Distribution Table",
                    "Grouped Frequency Distribution"]
    elif topic_var.get() == topic[1]:
        operations = ["Permutation",
                    "Combination"]
    elif topic_var.get() == topic[2]:
        operations = ["Discrete Probability Distribution",
                    "Binomial Probability Distribution",
                    "Poisson Probability Distribution",
                    "Hypogeometric Probability Distribution"]
    elif topic_var.get() == topic[3]:
        operations = ["Population Standard Deviation",
                      "Sample Standard Deviation",
                      "Sampling Distribution of a Sample Mean",
                      "Sampling Distribution of the Sample Proportion"]
    elif topic_var.get() == topic[4]:
        operations = ["None"]
    elif topic_var.get() == topic[5]:
        operations = ["Z Test Statistic",
                      "T Test Statistic"]

    operations_var.set(operations[0])
    menu2 = dropdown2["menu"]
    menu2.delete(0, "end")
    for option in operations:
        menu2.add_command(label=option, command=tk._setit(operations_var, option))

# Bind the update_options function to the first dropdown
topic_var.trace("w", update_options)

# Create calculate button
def create_calculate_button(frame, command, text, relx, rely):
    calculate_button = tk.Button(frame, text=text, command=command, bg="#16537e", fg="white", font=("Helvetica", 10), relief="ridge")
    calculate_button.place(relx=relx, rely=rely, relwidth=0.2, relheight=0.05)
    return calculate_button

def calculate():
    # Mean, Median, Mode, Max, Min, Range
    if topic_var.get() == topic[0]:
        if operations_var.get() == operations[0]:
            lower_frame1 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame1, text="Enter numbers separated by spaces:", font=("Helvetica", 10))
            label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
            entry = tk.Entry(lower_frame1, font = 5)
            entry.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.1)

            def mean_med_mode():
                try:
                    numbers = [float(num.strip()) for num in entry.get().split(" ")]
                    result = f"Mean: {mean(numbers): }\nMedian: {median(numbers): }\nMode: {mode(numbers): }\nMax: {max(numbers): }\nMin: {min(numbers): }\nRange: {max(numbers) - min(numbers): }"
                    result_frame(result, lower_frame1, 0.4)
                except ValueError:
                    error()
            calculate_button = create_calculate_button(lower_frame1, mean_med_mode, "Calculate", 0.4, 0.3)
        elif operations_var.get() == operations[1]:
        # Interquartile Range, Upper Outlier Limit, Lower Outlier Limit
            lower_frame2 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame2, text="Enter numbers separated by spaces:", font=("Helvetica", 10))
            label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
            entry = tk.Entry(lower_frame2, font = 5)
            entry.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.1)

            def quartile():
                try:
                    numbers = [float(num.strip()) for num in entry.get().split(" ")]
                    sorted_numbers = sorted(numbers)
                    n = len(sorted_numbers)
                    q1 = sorted_numbers[int(n * 0.25)]
                    q3 = sorted_numbers[int(n * 0.75)]
                    iqr = q3 - q1
                    lower_outlier_limit = q1 - (1.5 * iqr)
                    upper_outlier_limit = q3 + (1.5 * iqr)
                    result = f"IQR: {iqr:.2f}\nLower Outlier Limit: {lower_outlier_limit:.2f}\nUpper Outlier Limit: {upper_outlier_limit:.2f}"
                    result_frame(result, lower_frame2, 0.4)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers with appropriate spaces")
            calculate_button = create_calculate_button(lower_frame2, quartile, "Calculate", 0.4, 0.3)
        # Frequency Distribution Table
        elif operations_var.get() == operations[2]:
            lower_frame3 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame3, text="Enter numbers separated by spaces:", font=("Helvetica", 10))
            label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
            entry = tk.Entry(lower_frame3, font = 5)
            entry.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.1)

            def frequency():
                try:
                    numbers = [float(num.strip()) for num in entry.get().split(" ")]
                    counter = Counter(numbers)
                    n = len(numbers)
                    table = "Value\tF\tCF\tRF\tCRF\n"
                    cumulative_freq = 0
                    for value, frequency in sorted(counter.items()):
                        cumulative_freq += frequency
                        relative_freq = frequency / n
                        #percent_freq = relative_freq*100
                        cumulative_relative_freq = cumulative_freq / n
                        #cumulative_percent_freq = cumulative_relative_freq*100
                        table += f"{value:.2f}\t{frequency}\t{cumulative_freq}\t{round(relative_freq, 2)}\t{cumulative_relative_freq:.2f}\n"
                        result = table
                        result_frame(result, lower_frame3, 0.4)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers with appropriate spaces")
            calculate_button = create_calculate_button(lower_frame3, frequency, "Calculate", 0.4, 0.3)
    # Grouped Frequency Distribution
        elif operations_var.get() == operations[3]:
            lower_frame4 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame4, text="Enter numbers separated by spaces:", font=("Helvetica", 10))
            label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
            entry = tk.Entry(lower_frame4, font = 5)
            entry.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.1)

            def grouped_freq():
                try:           
                    numbers = [float(num.strip()) for num in entry.get().split(" ")]
                    n = len(numbers)
                    num_classes = math.ceil(1 + 3.3 * math.log10(n))
                    # Calculate class width
                    data_range = max(numbers) - min(numbers)
                    class_width = data_range / num_classes
    
                    # Create class intervals
                    intervals = []
                    lower_bound = min(numbers)
                    upper_bound = lower_bound + class_width
                    while upper_bound <= max(numbers):
                        intervals.append((lower_bound, upper_bound))
                        lower_bound = upper_bound
                        upper_bound += class_width
                    intervals.append((lower_bound, max(numbers)))
    
                # Calculate frequency distribution
                    freq_dist = Counter()
                    for num in numbers:
                        for interval in intervals:
                            if interval[0] <= num <= interval[1]:
                                freq_dist[interval] += 1
                                break
    
            # Calculate midpoint and frequency density
                    class_stats = []
                    for interval, freq in freq_dist.items():
                        midpoint = (interval[0] + interval[1]) / 2
                        class_stats.append((interval, freq, midpoint))
    
            # Format results as a string
                    result = "Grouped Frequency Distribution:\n"
                    result += f"{'Interval':<20} {'Frequency':<20} {'Midpoint':<20}\n"
                    for interval, freq, midpoint in class_stats:
                        result += f"{interval[0]:<10.2f} - {interval[1]:<10.2f} {freq:<20} {midpoint:<20.2f}\n"
                    result += f"\nRange: {max(numbers) - min(numbers):.2f}"
                    result_frame(result, lower_frame4, 0.4)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers with appropriate spaces")
            calculate_button = create_calculate_button(lower_frame4, grouped_freq, "Calculate", 0.4, 0.3)

    #Permutation
    elif topic_var.get() == topic[1]:
        if operations_var.get() == operations[0]:
            lower_frame5 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label5 = tk.Label(lower_frame5, text="n = number of objects \n r = number of positions", bg="#cfe2f3", font = ('Arial', 10), fg = "#000000")
            label5.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

            label_n = tk.Label(lower_frame5, text="n:")
            label_n.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_n = tk.Entry(lower_frame5, font=5)
            entry_n.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.1)
            label_r = tk.Label(lower_frame5, text="r:")
            label_r.place(relx=0.50, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_r = tk.Entry(lower_frame5, font=5)
            entry_r.place(relx=0.60, rely=0.15, relwidth=0.12, relheight=0.1)

            def permutation():
                try:
                    n = int(entry_n.get())
                    r = int(entry_r.get())
                    if n >= r:
                        permutation = math.perm(n, r)
                        result = f"Permutation: {permutation}"
                        result_frame(result, lower_frame5, 0.4)
                    else:
                        messagebox.showerror("Error", "n should be greater than or equal to r")
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers for n and r")
            calculate_button = create_calculate_button(lower_frame5, permutation, "Calculate", 0.4, 0.3)

    #Combination
        elif operations_var.get() == operations[1]:
            lower_frame6 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label6 = tk.Label(lower_frame6, text="n = number of objects \n r = number of positions", bg="#cfe2f3", font = ('Arial', 10), fg = "#000000")
            label6.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

            label_n = tk.Label(lower_frame6, text="n:")
            label_n.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_n = tk.Entry(lower_frame6, font=5)
            entry_n.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.1)
            label_r = tk.Label(lower_frame6, text="r:")
            label_r.place(relx=0.50, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_r = tk.Entry(lower_frame6, font=5)
            entry_r.place(relx=0.60, rely=0.15, relwidth=0.12, relheight=0.1)

            def combination():
                try:
                    n = int(entry_n.get())
                    r = int(entry_r.get())
                    if n >= r:
                        combination = math.comb(n, r)
                        result = f"Combination: {combination}"
                        result_frame(result, lower_frame6, 0.4)
                    else:
                        messagebox.showerror("Error", "n should be greater than or equal to r")
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers for n and r")
            calculate_button = create_calculate_button(lower_frame6, combination, "Calculate", 0.4, 0.3)

    elif topic_var.get() == topic[2]:
        if operations_var.get() == operations[0]:
            lower_frame7 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label1 = tk.Label(lower_frame7, text="Enter the values separated by spaces:", font=("Helvetica", 10))
            label1.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=0.1)

            entry1 = tk.Entry(lower_frame7, font=5)
            entry1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)

            label2 = tk.Label(lower_frame7, text="Enter the probabilities separated by spaces:", font=("Helvetica", 10))
            label2.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)

            entry2 = tk.Entry(lower_frame7, font=5)
            entry2.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)

            def discrete_probability():
                try:
                    values = [float(num.strip()) for num in entry1.get().split()]
                    probabilities = [float(num.strip()) for num in entry2.get().split()]
                    n = len(values)
                    table = "Value\tProbability\n"
                    mean = 0
                    variance = 0
                    for i in range(n):
                        value = values[i]
                        probability = probabilities[i]
                        mean += value * probability
                        variance += (value - mean)**2 * probability
                        table += f"{value:.2f}\t{round(probability,2)}\n"
                    mean = mean
                    variance = variance
                    std_deviation = variance ** 0.5
                    table += f"\nMean: {mean}\nVariance: {variance}\nStandard Deviation: {std_deviation}"
                    result = table
                    result_frame(result, lower_frame7, 0.6)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer numbers with appropriate spaces")
            calculate_button = create_calculate_button(lower_frame7, discrete_probability, "Calculate", 0.4, 0.45)

    #Binomial Probability Distribution
        elif operations_var.get() == operations[1]:
            lower_frame8 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label8 = tk.Label(lower_frame8, text="p = probability of success     x = number of items\nq = probability of failure         n = total number of items", bg="#cfe2f3", font = ('Arial', 10), fg = "#000000", justify = "left")
            label8.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

            label_p = tk.Label(lower_frame8, text="p:")
            label_p.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_p = tk.Entry(lower_frame8, font=5)
            entry_p.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.1)
            label_q = tk.Label(lower_frame8, text="q:")
            label_q.place(relx=0.50, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_q = tk.Entry(lower_frame8, font=5)
            entry_q.place(relx=0.60, rely=0.15, relwidth=0.12, relheight=0.1)
            label_x = tk.Label(lower_frame8, text="x:")
            label_x.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.1)
            entry_x = tk.Entry(lower_frame8, font=5)
            entry_x.place(relx=0.35, rely=0.25, relwidth=0.12, relheight=0.1)
            label_n = tk.Label(lower_frame8, text="n:")
            label_n.place(relx=0.50, rely=0.25, relwidth=0.1, relheight=0.1)
            entry_n = tk.Entry(lower_frame8, font=5)
            entry_n.place(relx=0.60, rely=0.25, relwidth=0.12, relheight=0.1)

            def binomial_prob():
                try:
                    p = float(entry_p.get())
                    q = float(entry_q.get())
                    x = int(entry_x.get())
                    n = int(entry_n.get())
                    if n >= x:
                        binom_coeff = math.comb(n, x)
                        prob = binom_coeff * p**x * q**(n-x)
                        result = f"Binomial Probability: {prob}"
                        result_frame(result, lower_frame8, 0.5)
                    else:
                        messagebox.showerror("Error", "n should be greater than or equal to x")
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numers")
            calculate_button = create_calculate_button(lower_frame8, binomial_prob, "Calculate", 0.4, 0.4)

    #Poisson Probability Distribution
        elif operations_var.get() == operations[2]:
            lower_frame9 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label9 = tk.Label(lower_frame9, text="x = 0, 1, 2, 3, …         λ = mean number of occurrences in the interval", bg="#cfe2f3", font = ('Arial', 10), fg = "#000000", justify = "left")
            label9.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

            label_x = tk.Label(lower_frame9, text="x:")
            label_x.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_x = tk.Entry(lower_frame9, font=5)
            entry_x.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.1)
            label_λ = tk.Label(lower_frame9, text="λ:")
            label_λ.place(relx=0.50, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_λ = tk.Entry(lower_frame9, font=5)
            entry_λ.place(relx=0.60, rely=0.15, relwidth=0.12, relheight=0.1)

            def poisson_prob():
                try:
                    x = int(entry_x.get())
                    λ = float(entry_λ.get())

                    probability = (math.e ** -λ) * (λ  ** x) / math.factorial(x)
                    result = f"The probability of getting {x} occurrences with mean {λ} is {probability:.4f}"
                    result_frame(result, lower_frame9, 0.5)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")
            calculate_button = create_calculate_button(lower_frame9, poisson_prob, "Calculate", 0.4, 0.4)

    #Hypogeometric Probability Distribution
        elif operations_var.get() == operations[3]:
            lower_frame10 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label10 = tk.Label(lower_frame10, text="N = items in the population    k = population item successes\nn= items in the sample         x = sample items successes", bg="#cfe2f3", font = ('Arial', 10), fg = "#000000", justify = "left")
            label10.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)

            label_N = tk.Label(lower_frame10, text="N:")
            label_N.place(relx=0.25, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_N = tk.Entry(lower_frame10, font=5)
            entry_N.place(relx=0.35, rely=0.15, relwidth=0.12, relheight=0.1)
            label_k = tk.Label(lower_frame10, text="k:")
            label_k.place(relx=0.50, rely=0.15, relwidth=0.1, relheight=0.1)
            entry_k = tk.Entry(lower_frame10, font=5)
            entry_k.place(relx=0.60, rely=0.15, relwidth=0.12, relheight=0.1)
            label_n = tk.Label(lower_frame10, text="n:")
            label_n.place(relx=0.25, rely=0.25, relwidth=0.1, relheight=0.1)
            entry_n = tk.Entry(lower_frame10, font=5)
            entry_n.place(relx=0.35, rely=0.25, relwidth=0.12, relheight=0.1)
            label_x = tk.Label(lower_frame10, text="x:")
            label_x.place(relx=0.50, rely=0.25, relwidth=0.1, relheight=0.1)
            entry_x = tk.Entry(lower_frame10, font=5)
            entry_x.place(relx=0.60, rely=0.25, relwidth=0.12, relheight=0.1)

            def hypergeometric_prob():
                try:
                    N = int(entry_N.get())
                    k = int(entry_k.get())
                    n = int(entry_n.get())
                    x = int(entry_x.get())

                    numerator = comb(k, x) * comb(N - k, n - x)
                    denominator = comb(N, n)
                    result = numerator / denominator
                    result = f"Hypergeometric Probability: {result} or {round(result*100, 2)}%"
                    result_frame(result, lower_frame10, 0.5)
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid integer number")
            calculate_button = create_calculate_button(lower_frame10, hypergeometric_prob, "Calculate", 0.4, 0.44)

    #population standard deviation 
    elif topic_var.get() == topic[3]:
        if operations_var.get() == operations[0]:
            lower_frame11 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label11 = tk.Label(lower_frame11, text="Population Standard Deviation", bg="#cfe2f3", font=('Arial', 10), fg="#000000", justify="left")
            label11.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_avg = tk.Label(lower_frame11, text="Population Average:")
            label_avg.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
            entry_avg = tk.Entry(lower_frame11, font=5)
            entry_avg.place(relx=0.45, rely=0.2, relwidth=0.25, relheight=0.1)

            label_values = tk.Label(lower_frame11, text="Individual Values \n(space-separated):")
            label_values.place(relx=0.2, rely=0.35, relwidth=0.2, relheight=0.1)
            entry_values = tk.Entry(lower_frame11, font=5)
            entry_values.place(relx=0.45, rely=0.35, relwidth=0.25, relheight=0.1)

            label_count = tk.Label(lower_frame11, text="Count of Values:")
            label_count.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)
            entry_count = tk.Entry(lower_frame11, font=5)
            entry_count.place(relx=0.45, rely=0.5, relwidth=0.25, relheight=0.1)


            def calculate_population_stdev():
                try:
                    avg = float(entry_avg.get())
                    values = [float(x.strip()) for x in entry_values.get().split()]
                    count = int(entry_count.get())

                    deviations = [(x - avg) ** 2 for x in values]
                    population_stdev = np.sqrt(sum(deviations) / count)

                    result_text = f"Population Standard Deviation: {population_stdev:.2f}"
                    result_label = tk.Label(lower_frame11, text=result_text)
                    result_label.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame11, calculate_population_stdev, "Calculate", 0.4, 0.65)

        #Sample standard deviation
        elif operations_var.get() == operations[1]:
            lower_frame11 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label11 = tk.Label(lower_frame11, text="Sample Standard Deviation", bg="#cfe2f3", font=('Arial', 10), fg="#000000", justify="left")
            label11.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_avg = tk.Label(lower_frame11, text="Sample Average:")
            label_avg.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
            entry_avg = tk.Entry(lower_frame11, font=5)
            entry_avg.place(relx=0.45, rely=0.2, relwidth=0.25, relheight=0.1)

            label_values = tk.Label(lower_frame11, text="Individual Values \n(space-separated):")
            label_values.place(relx=0.2, rely=0.35, relwidth=0.2, relheight=0.1)
            entry_values = tk.Entry(lower_frame11, font=5)
            entry_values.place(relx=0.45, rely=0.35, relwidth=0.25, relheight=0.1)

            label_count = tk.Label(lower_frame11, text="Count of Values:")
            label_count.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.1)
            entry_count = tk.Entry(lower_frame11, font=5)
            entry_count.place(relx=0.45, rely=0.5, relwidth=0.25, relheight=0.1)

            def calculate_sample_stdev():
                try:
                    avg = float(entry_avg.get())
                    values = [float(x.strip()) for x in entry_values.get().split()]
                    count = int(entry_count.get())

                    deviations = [(x - avg) ** 2 for x in values]
                    sample_stdev = np.sqrt(sum(deviations) / (count - 1))

                    result_text = f"Sample Standard Deviation: {sample_stdev:.2f}"
                    result_label = tk.Label(lower_frame11, text=result_text)
                    result_label.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame11, calculate_sample_stdev, "Calculate", 0.4, 0.65)
        
        #sampling distribution of sample mean
        elif operations_var.get() == operations[2]:
            lower_frame11 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label11 = tk.Label(lower_frame11, text="Sampling Distribution of Sample Mean", bg="#cfe2f3", font=('Arial', 10), fg="#000000", justify="left")
            label11.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_n = tk.Label(lower_frame11, text="Sample Size:")
            label_n.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
            entry_n = tk.Entry(lower_frame11, font=5)
            entry_n.place(relx=0.45, rely=0.2, relwidth=0.25, relheight=0.1)

            label_mu = tk.Label(lower_frame11, text="Population Mean:")
            label_mu.place(relx=0.2, rely=0.35, relwidth=0.2, relheight=0.1)
            entry_mu = tk.Entry(lower_frame11, font=5)
            entry_mu.place(relx=0.45, rely=0.35, relwidth=0.25, relheight=0.1)

            label_sigma = tk.Label(lower_frame11, text="Population Standard Deviation:")
            label_sigma.place(relx=0.2, rely=0.5, relwidth=0.4, relheight=0.1)
            entry_sigma = tk.Entry(lower_frame11, font=5)
            entry_sigma.place(relx=0.65, rely=0.5, relwidth=0.25, relheight=0.1)

            def calculate_sampling_distribution():
                try:

                    n = int(entry_n.get())
                    mu = float(entry_mu.get())
                    sigma = float(entry_sigma.get())

                    sampling_distribution = sigma / np.sqrt(n)

                    result_text = f"Sampling Distribution of Sample Mean: {sampling_distribution:.2f}"
                    result_label = tk.Label(lower_frame11, text=result_text)
                    result_label.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame11, calculate_sampling_distribution, "Calculate", 0.4, 0.65)

        elif operations_var.get() == operations[3]:
            lower_frame11 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label11 = tk.Label(lower_frame11, text="Sample Distribution of Sample Proportion", bg="#cfe2f3", font=('Arial', 10), fg="#000000", justify="left")
            label11.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_n = tk.Label(lower_frame11, text="Sample Size:")
            label_n.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.1)
            entry_n = tk.Entry(lower_frame11, font=5)
            entry_n.place(relx=0.45, rely=0.2, relwidth=0.25, relheight=0.1)

            label_p = tk.Label(lower_frame11, text="Sample Proportion:")
            label_p.place(relx=0.2, rely=0.35, relwidth=0.2, relheight=0.1)
            entry_p = tk.Entry(lower_frame11, font=5)
            entry_p.place(relx=0.45, rely=0.35, relwidth=0.25, relheight=0.1)

            def calculate_sample_distribution():
                try:
                    n = int(entry_n.get())
                    p = float(entry_p.get())

                    sample_distribution = np.sqrt((p * (1 - p)) / n)

                    result_text = f"Sample Distribution of Sample Proportion: {sample_distribution:.2f}"
                    result_label = tk.Label(lower_frame11, text=result_text)
                    result_label.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)

                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame11, calculate_sample_distribution, "Calculate", 0.4, 0.65)



    # Confidence Interval
    elif topic_var.get() == topic[4]:
        lower_frame11 = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

        label11 = tk.Label(lower_frame11, text="Enter the values separated by spaces:", font=("Helvetica", 10))
        label11.place(relx=0.25, rely=0.0, relwidth=0.5, relheight=0.1)

        entry11 = tk.Entry(lower_frame11, font=5)
        entry11.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)

        label12 = tk.Label(lower_frame11, text="Confidence Level (%):", font=("Helvetica", 10))
        label12.place(relx=0.25, rely=0.2, relwidth=0.5, relheight=0.1)

        entry12 = tk.Entry(lower_frame11, font=5)
        entry12.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.1)

        def confidence_interval():
        
            try:
                data = [float(num.strip()) for num in entry11.get().split()]
                confidence_level = float(entry12.get())

                n = len(data)
                mean = sum(data) / n
                stdev = statistics.stdev(data)  # Calculate the standard deviation

                # Calculate the margin of error
                margin_of_error = stdev * (1.96 / math.sqrt(n))

                # Calculate the lower and upper bounds of the confidence interval
                lower_bound = round(mean - margin_of_error, 2)  # Round to 2 decimal places
                upper_bound = round(mean + margin_of_error, 2)  # Round to 2 decimal places

                result = f"Confidence Interval: [{lower_bound:.2f}, {upper_bound:.2f}]"  # Format the result with 2 decimal places
                result_frame(result, lower_frame11, 0.5)

            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers")

        calculate_button = create_calculate_button(lower_frame11, confidence_interval, "Calculate", 0.4, 0.45)
    


    #hypothesis testing
    elif topic_var.get() == topic[5]:
        #z test
        if operations_var.get() == operations[0]:
            lower_frame = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame, text="Z-Test Statistics\n\nEnter the following values:", bg="#cfe2f3", font=('Arial', 10),
                            fg="#000000", justify="left")
            label.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_x = tk.Label(lower_frame, text="Sample Mean (x̄):")
            label_x.place(relx=0.1, rely=0.15, relwidth=0.35, relheight=0.1)
            entry_x = tk.Entry(lower_frame, font=5)
            entry_x.place(relx=0.5, rely=0.15, relwidth=0.35, relheight=0.1)

            label_mu = tk.Label(lower_frame, text="Population Mean (μ):")
            label_mu.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.1)
            entry_mu = tk.Entry(lower_frame, font=5)
            entry_mu.place(relx=0.5, rely=0.25, relwidth=0.35, relheight=0.1)

            label_sigma = tk.Label(lower_frame, text="Population Standard Deviation (σ):")
            label_sigma.place(relx=0.1, rely=0.35, relwidth=0.35, relheight=0.1)
            entry_sigma = tk.Entry(lower_frame, font=5)
            entry_sigma.place(relx=0.5, rely=0.35, relwidth=0.35, relheight=0.1)

            label_n = tk.Label(lower_frame, text="Sample Size (n):")
            label_n.place(relx=0.1, rely=0.55, relwidth=0.35, relheight=0.1)
            entry_n = tk.Entry(lower_frame, font=5)
            entry_n.place(relx=0.5, rely=0.55, relwidth=0.35, relheight=0.1)

            def z_test():
                try:
                    x = float(entry_x.get())
                    mu = float(entry_mu.get())
                    sigma = float(entry_sigma.get())
                    n = int(entry_n.get())

                    # Compute z-test statistic
                    z = (x - mu) / (sigma / math.sqrt(n))

                    # Display the result
                    result_label = tk.Label(lower_frame, text=f"Z-Test Statistic: {z:.2f}")
                    result_label.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame, z_test, "Calculate", 0.4, 0.65)

        #t test
        elif operations_var.get() == operations[1]:
            lower_frame = create_lower_frame(window, 0.1, 0.3, 0.8, 0.7)

            label = tk.Label(lower_frame, text="T-Test Statistics\n\nEnter the following values:", bg="#cfe2f3", font=('Arial', 10),
                            fg="#000000", justify="left")
            label.place(relx=0, rely=0, relwidth=1, relheight=0.1)

            label_x = tk.Label(lower_frame, text="Sample Mean (x̄):")
            label_x.place(relx=0.1, rely=0.15, relwidth=0.35, relheight=0.1)
            entry_x = tk.Entry(lower_frame, font=5)
            entry_x.place(relx=0.5, rely=0.15, relwidth=0.35, relheight=0.1)

            label_mu = tk.Label(lower_frame, text="Population Mean (μ):")
            label_mu.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.1)
            entry_mu = tk.Entry(lower_frame, font=5)
            entry_mu.place(relx=0.5, rely=0.25, relwidth=0.35, relheight=0.1)

            label_sigma = tk.Label(lower_frame, text="Sample Standard Deviation (s):")
            label_sigma.place(relx=0.1, rely=0.35, relwidth=0.35, relheight=0.1)
            entry_sigma = tk.Entry(lower_frame, font=5)
            entry_sigma.place(relx=0.5, rely=0.35, relwidth=0.35, relheight=0.1)

            label_n = tk.Label(lower_frame, text="Sample Size (n):")
            label_n.place(relx=0.1, rely=0.45, relwidth=0.35, relheight=0.1)
            entry_n = tk.Entry(lower_frame, font=5)
            entry_n.place(relx=0.5, rely=0.45, relwidth=0.35, relheight=0.1)

            def t_test():
                try:
                    x = float(entry_x.get())
                    mu = float(entry_mu.get())
                    s = float(entry_sigma.get())
                    n = int(entry_n.get())

                    # Compute t-test statistic
                    t = (x - mu) / (s / math.sqrt(n))

                    # Display the result
                    result_label = tk.Label(lower_frame, text=f"T-Test Statistic: {t:.2f}")
                    result_label.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numbers")

            calculate_button = create_calculate_button(lower_frame, t_test, "Calculate", 0.4, 0.65)

 
calculate_button = tk.Button(lower_frame, text="Enter", command=calculate, bg="#ffdf66", relief = "ridge", bd = 3)
calculate_button.place(relx = 0.20, rely = 0.005, relwidth = 0.1, relheight = 0.091)

window.mainloop()
