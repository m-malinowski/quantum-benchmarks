import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
mpl.rcParams['savefig.dpi'] = 200
plt.close("all")
ion_data = pd.read_csv("entanglement_size/data/trapped_ions.csv")
supercond_data = pd.read_csv("entanglement_size/data/superconducting.csv")
neutrals_data = pd.read_csv("entanglement_size/data/neutrals.csv")
photon_data = pd.read_csv("entanglement_size/data/photons.csv")
multi_dof_photon_data = pd.read_csv("entanglement_size/data/multi_dof_photons.csv")
color_list = plt.rcParams['axes.prop_cycle'].by_key()['color']
y_max = 30
y_min= 1
x_max = 2023 #adjust to get labels to fit
x_min = 1998
offset = 2

# Flag controversial data
#flag_list = ['Mooney2021']
flag_list = []
flagged_marker = r'$?$'


ion_style = {"color":color_list[0]}
supercond_style = {"color":color_list[1]}
rydberg_style = {"color":color_list[2]}
diamond_style = {"color":color_list[3]}
silicon_style = {"color":color_list[4]}
photon_style = {"color":color_list[5]}
multi_dof_photon_style = {"color":color_list[6]}


def plot_single(data,style,title,filename,annotate=True):
    data_good = data[~data['Citation'].isin(flag_list)]
    data_flagged = data[data['Citation'].isin(flag_list)]
    ax = data_good.plot(x="Year", y="Number",
                        kind="scatter", logy=False, s=50,
                         **style);
    if len(data_flagged)>0:
           ax = data_flagged.plot(ax = ax, x="Year", y="Number",
                        kind="scatter", logy=False, s=50, marker=flagged_marker,
                        **style); 
    ax.set_ylim(y_min,y_max)
    ax.set_xlim(data["Year"].min()-offset,x_max)
    ax.set_title(title)
    ax.grid(which='major', axis='y')
    if annotate:
        for index, row in data.iterrows():
            ax.annotate(row["Place"], (row["Year"],row["Number"]),xytext=(5,5), textcoords='offset points', **style)
    plot = ax.get_figure()
    plot.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close("all")

def plot_combined(data_list,style_list,label_list,filename,annotate=False):
    fig, ax = plt.subplots()
    for data, style, label in zip(data_list, style_list, label_list):
        data_good = data[~data['Citation'].isin(flag_list)]
        data_flagged = data[data['Citation'].isin(flag_list)]
        ax = data_good.plot(ax=ax, x="Year", y="Number", label = label,
                kind="scatter", logy=False, s=50, **style);
        if len(data_flagged)>0:
           ax = data_flagged.plot(ax = ax, x="Year", y="Number",
                    kind="scatter", logy=False, s=50, marker=flagged_marker,
                    **style); 
        if annotate:
            for index, row in data.iterrows():
                ax.annotate(row["Place"], (row["Year"],row["Number"]),xytext=(5,5), textcoords='offset points', **style)
    ax.set_ylim(y_min,y_max)
    ax.set_xlim(x_min,x_max)
    ax.grid(which='major', axis='y')
    ax.set_title('Number of entangled qubits')
    ax.legend()

    plot = ax.get_figure()
    plot.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close("all")



data_list =[ion_data, supercond_data, neutrals_data, photon_data, multi_dof_photon_data]
style_list = [ion_style, supercond_style, rydberg_style, photon_style, multi_dof_photon_style]
label_list = ["Trapped ions", "Superconducting", "Neutral atoms", "Photons", "Multi-DOF photons"]


plot_combined(data_list, style_list,label_list,"entanglement_size/plots/combined.png")
#plot_combined(data_list[0:2], style_list[0:2],label_list[0:2],"plots/ions_vs_supercond.png",annotate=True)

plot_single(ion_data,ion_style,"Trapped ions, number of entangled qubits","entanglement_size/plots/ions.png")
plot_single(supercond_data,supercond_style,"Superconducting, number of entangled qubits","entanglement_size/plots/superconducting.png")
plot_single(neutrals_data,rydberg_style,"Neutrals, number of entangled qubits","entanglement_size/plots/neutrals.png")
plot_single(photon_data,photon_style,"Photons, number of entangled qubits","entanglement_size/plots/photons.png")
plot_single(multi_dof_photon_data,multi_dof_photon_style,"Multi-DOF photons, number of entangled qubits","entanglement_size/plots/multi_dof_photons.png")



