import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the csv file
df = pd.read_csv(
    "D:\\Study meterial\\PLACEMENT\\WINTER TRANNING PROGRAM\\PYTHON & SQL\\DAY 8\\dataset.csv")
# print(df.head(10))

# # find total number of runs kohli has scored
# totalruns = df["Runs"].sum()
# no_of_match = len(df["Runs"])
# print(f"Total no. of runs kohli scored {no_of_match} matches: {totalruns}")

# # avarage of number of runs he has
# avg_runs = df["Runs"].mean()
# print(f"Average runs of kohli in {no_of_match} maches : {int(avg_runs)}")

# # number of matchs he played different position
# position = df["Pos"].unique()
# print(position)

# df["Pos"] = df["Pos"].map({
#     3.0: "Batting at 3",
#     4.0: "Batting at 4",
#     2.0: "Batting at 2",
#     1.0: "Batting at 1",
#     7.0: "Batting at 7",
#     5.0: "Batting at 5",
#     6.0: "Batting at 6"
# })

# print(df[["Runs", "Pos", "Opposition"]].head)


def show_pie_plot(df, key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_labels = counts.index

    fig = plt.figure(figsize=(10, 7))
    plt.pie(count_values, labels=count_labels)
    plt.show()


# show_pie_plot(df, "Pos")
# show_pie_plot(df, "Opposition")
# show_pie_plot(df, "Ground")


# pos_counts = df["Pos"].value_counts()
# print(pos_counts)
# print(type(pos_counts))

# pos_values = pos_counts.values
# pos_labels = pos_counts.index
# print(pos_values)

# fig = plt.figure(figsize=(10, 7))
# plt.pie(pos_values, labels=pos_labels)
# plt.show()

# total runs scored in diffirent position
runs_at_pos = df.groupby("Pos")["Runs"].sum()
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

# fig = plt.figure(figsize=(10, 7))
# plt.pie(runs_at_pos_values, labels=runs_at_pos_labels)
# plt.show()

# Total sixes scored with different opposition
sixes_with_ops = df.groupby("Opposition")["6s"].sum()
sixes_with_ops_values = sixes_with_ops.values
sixes_with_ops_labels = sixes_with_ops.index

# fig = plt.figure(figsize=(10, 7))
# plt.pie(sixes_with_ops_values, labels=sixes_with_ops_labels)
# plt.show()

# number of countries scoered by kohli in first
centuries = df.query("Runs >=100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]

# fig = plt.figure(figsize=(10, 7))
# plt.bar(innings, tons, color="blue", width=0.2)
# plt.show()

# calculate the dismissals of kohli
dismissals = df["Dismissal"].value_counts()
print(dismissals)

dismissals_counts = dismissals.values
dismissals_labels = dismissals.index
# show_pie_plot(df, "Dismissal")

# Against which team he has scored the most runs
# fig = plt.figure(figsize=(10, 7))
# plt.bar(
# runsdf[""]    -------------------------------- code not complete
# )
# plt.show()

# Against which team he has scored the most centuries
fig = plt.figure(figsize=(10, 7))
plt.bar(
    centuries["Opposition"], centuries["Runs"], color="green", width=0.2
)
plt.show()

# Analyze the strike rate
