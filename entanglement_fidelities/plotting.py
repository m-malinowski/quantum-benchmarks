import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
mpl.rcParams['savefig.dpi'] = 200
plt.close("all")
ion_data = pd.read_csv("entanglement_fidelities/data/trapped_ions.csv")
supercond_data = pd.read_csv("entanglement_fidelities/data/superconducting.csv")
rydberg_data = pd.read_csv("entanglement_fidelities/data/rydbergs.csv")
diamond_data = pd.read_csv("entanglement_fidelities/data/diamond.csv")
silicon_data = pd.read_csv("entanglement_fidelities/data/silicon.csv")
color_list = plt.rcParams['axes.prop_cycle'].by_key()['color']
y_max = 1
y_min=1e-4
x_max = 2024
x_min = 1998
offset = 2


ion_style = {"color":color_list[0]}
supercond_style = {"color":color_list[1]}
rydberg_style = {"color":color_list[2]}
diamond_style = {"color":color_list[3]}
silicon_style = {"color":color_list[4]}


def plot_single(data,style,title,filename,annotate=True):
    ax = data.plot(x="Year", y="Error", yerr = "Uncertainty",
                        kind="scatter", logy=True, s=50, **style);
    ax.set_ylim(y_min,1)
    ax.set_xlim(data["Year"].min()-offset,x_max)
    ax.set_title(title)
    ax.grid(which='major', axis='y')
    if annotate:
        for index, row in data.iterrows():
            ax.annotate(row["Place"], (row["Year"],row["Error"]),xytext=(5,5), textcoords='offset points', **style)
    plot = ax.get_figure()
    plot.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close("all")

def plot_combined(data_list,style_list,label_list,filename,annotate=False):
    fig, ax = plt.subplots()
    for data, style, label in zip(data_list, style_list, label_list):
        ax = data.plot(ax=ax, x="Year", y="Error", yerr = "Uncertainty", label = label,
                kind="scatter", logy=True, s=50, **style);
        if annotate:
            for index, row in data.iterrows():
                ax.annotate(row["Place"], (row["Year"],row["Error"]),xytext=(5,5), textcoords='offset points', **style)
    ax.set_ylim(y_min,y_max)
    ax.set_xlim(x_min,x_max)
    ax.grid(which='major', axis='y')
    ax.set_title('2-qubit entanglement errors')
    ax.legend()

    plot = ax.get_figure()
    plot.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close("all")



data_list =[ion_data,supercond_data,rydberg_data,diamond_data,silicon_data]
style_list = [ion_style, supercond_style, rydberg_style, diamond_style, silicon_style]
label_list = ["Trapped ions", "Superconducting", "Rydberg atoms", "Spins in diamond", "Qubits in silicon"]


plot_combined(data_list, style_list,label_list,"entanglement_fidelities/plots/combined.png")
plot_combined(data_list[0:2], style_list[0:2],label_list[0:2],"entanglement_fidelities/plots/ions_vs_supercond.png",annotate=True)

plot_single(ion_data,ion_style,"Trapped ions 2-qubit entanglement errors","entanglement_fidelities/plots/ions.png")
plot_single(supercond_data,supercond_style,"Superconducting 2-qubit entanglement errors","entanglement_fidelities/plots/superconducting.png")
plot_single(rydberg_data,rydberg_style,"Rydberg 2-qubit entanglement errors","entanglement_fidelities/plots/rydbergs.png")
plot_single(diamond_data,diamond_style,"Spins in diamond 2-qubit entanglement errors","entanglement_fidelities/plots/diamond.png")
plot_single(silicon_data,silicon_style,"In-silicon 2-qubit entanglement errors","entanglement_fidelities/plots/silicon.png")

