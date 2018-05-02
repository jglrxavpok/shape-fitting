#! /usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from os import path

#plt.rc('text', usetex=True)
import numpy as np

import math

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if plt.rcParams['text.usetex'] is True:
        return s #+ r'$\%$'
    else:
        return s #+ '%'

ground_truth_size=1200;
alpha_=0.4
fontsize_=20;

#ORIENTATION
hough_orientation_results_0=[]
hough_orientation_results_1=[]
hough_orientation_results_2=[]

hough_orientation_file_0 = open("/home/rui/shape-fitting/dataset/results/orientation_noise_0.txt", "r") 
hough_orientation_file_1 = open("/home/rui/shape-fitting/dataset/results/orientation_noise_1.txt", "r") 
hough_orientation_file_2 = open("/home/rui/shape-fitting/dataset/results/orientation_noise_2.txt", "r") 

for line in hough_orientation_file_0:
  hough_orientation_results_0.append(180*float(line)/math.pi)
hough_orientation_results_0 = np.array(hough_orientation_results_0).reshape(ground_truth_size,len(hough_orientation_results_0)/ground_truth_size)

for line in hough_orientation_file_1:
  hough_orientation_results_1.append(float(line))
hough_orientation_results_1 = np.array(hough_orientation_results_1).reshape(ground_truth_size,len(hough_orientation_results_1)/ground_truth_size)

for line in hough_orientation_file_2:
  hough_orientation_results_2.append(float(line))
hough_orientation_results_2 = np.array(hough_orientation_results_2).reshape(ground_truth_size,len(hough_orientation_results_2)/ground_truth_size)

#POSITION
hough_position_results_0=[]
hough_position_results_1=[]
hough_position_results_2=[]

hough_position_file_0 = open("/home/rui/shape-fitting/dataset/results/position_noise_0.txt", "r") 
hough_position_file_1 = open("/home/rui/shape-fitting/dataset/results/position_noise_1.txt", "r") 
hough_position_file_2 = open("/home/rui/shape-fitting/dataset/results/position_noise_2.txt", "r") 

for line in hough_position_file_0:
  hough_position_results_0.append(float(line))
hough_position_results_0 = np.array(hough_position_results_0).reshape(ground_truth_size,len(hough_position_results_0)/ground_truth_size)

for line in hough_position_file_1:
  hough_position_results_1.append(float(line))
hough_position_results_1 = np.array(hough_position_results_1).reshape(ground_truth_size,len(hough_position_results_1)/ground_truth_size)

for line in hough_position_file_2:
  hough_position_results_2.append(float(line))
hough_position_results_2 = np.array(hough_position_results_2).reshape(ground_truth_size,len(hough_position_results_2)/ground_truth_size)

#RADIUS
hough_radius_results_0=[]
hough_radius_results_1=[]
hough_radius_results_2=[]

hough_radius_file_0 = open("/home/rui/shape-fitting/dataset/results/radius_noise_0.txt", "r") 
hough_radius_file_1 = open("/home/rui/shape-fitting/dataset/results/radius_noise_1.txt", "r") 
hough_radius_file_2 = open("/home/rui/shape-fitting/dataset/results/radius_noise_2.txt", "r") 

for line in hough_radius_file_0:
  hough_radius_results_0.append(float(line))
hough_radius_results_0 = np.array(hough_radius_results_0).reshape(ground_truth_size,len(hough_radius_results_0)/ground_truth_size)

for line in hough_radius_file_1:
  hough_radius_results_1.append(float(line))
hough_radius_results_1 = np.array(hough_radius_results_1).reshape(ground_truth_size,len(hough_radius_results_1)/ground_truth_size)

for line in hough_radius_file_2:
  hough_radius_results_2.append(float(line))
hough_radius_results_2 = np.array(hough_radius_results_2).reshape(ground_truth_size,len(hough_radius_results_2)/ground_truth_size)


colors=['red','blue','black','gray']
labels=['Ours (M=20, F=1%)','Ours (M=10, F=1%)','Round-robin','Kriegel et al. (M=10, F=1%)']


# compute orientation average and standard deviation
hough_orientation_results_mean_0 = np.mean(hough_orientation_results_0, axis=0)
hough_orientation_results_std_0  = np.std(hough_orientation_results_0, axis=0)

hough_orientation_results_mean_1 = np.mean(hough_orientation_results_1, axis=0)
hough_orientation_results_std_1  = np.std(hough_orientation_results_1, axis=0)

hough_orientation_results_mean_2 = np.mean(hough_orientation_results_2, axis=0)
hough_orientation_results_std_2  = np.std(hough_orientation_results_2, axis=0)

# compute position average and standard deviation
hough_position_results_mean_0 = np.mean(hough_position_results_0, axis=0)
hough_position_results_std_0  = np.std(hough_position_results_0, axis=0)

hough_position_results_mean_1 = np.mean(hough_position_results_1, axis=0)
hough_position_results_std_1  = np.std(hough_position_results_1, axis=0)

hough_position_results_mean_2 = np.mean(hough_position_results_2, axis=0)
hough_position_results_std_2  = np.std(hough_position_results_2, axis=0)

# compute radius average and standard deviation
hough_radius_results_mean_0 = np.mean(hough_radius_results_0, axis=0)
hough_radius_results_std_0  = np.std(hough_radius_results_0, axis=0)

hough_radius_results_mean_1 = np.mean(hough_radius_results_1, axis=0)
hough_radius_results_std_1  = np.std(hough_radius_results_1, axis=0)

hough_radius_results_mean_2 = np.mean(hough_radius_results_2, axis=0)
hough_radius_results_std_2  = np.std(hough_radius_results_2, axis=0)

### Plots

error_levels=[0.1,5,10,15,20,25,30,35,40,45,50];


f, axarr = plt.subplots(1, 1)

### Orientation
plt.plot(error_levels,hough_orientation_results_mean_0,color=colors[0],label=labels[0])
error_sup=hough_orientation_results_mean_0+hough_orientation_results_std_0;
error_inf=hough_orientation_results_mean_0-hough_orientation_results_std_0;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[0])

plt.plot(error_levels,hough_orientation_results_mean_1,color=colors[1],label=labels[1])
error_sup=hough_orientation_results_mean_1+hough_orientation_results_std_1;
error_inf=hough_orientation_results_mean_1-hough_orientation_results_std_1;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[1])

plt.plot(error_levels,hough_orientation_results_mean_2,color=colors[2],label=labels[2])
error_sup=hough_orientation_results_mean_2+hough_orientation_results_std_2;
error_inf=hough_orientation_results_mean_2-hough_orientation_results_std_2;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[2])

#plt.sca(axarr[0])

plt.xlabel('noise standard deviation (% of cylinder radius)',fontsize=fontsize_)
#plt.xlim(0, max_time)
plt.xticks(color='k', size=fontsize_)
plt.show()


### Position
plt.plot(error_levels,hough_position_results_mean_0,color=colors[0],label=labels[0])
error_sup=hough_position_results_mean_0+hough_position_results_std_0;
error_inf=hough_position_results_mean_0-hough_position_results_std_0;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[0])

plt.plot(error_levels,hough_orientation_results_mean_1,color=colors[1],label=labels[1])
error_sup=hough_position_results_mean_1+hough_position_results_std_1;
error_inf=hough_position_results_mean_1-hough_position_results_std_1;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[1])

plt.plot(error_levels,hough_position_results_mean_2,color=colors[2],label=labels[2])
error_sup=hough_position_results_mean_2+hough_position_results_std_2;
error_inf=hough_position_results_mean_2-hough_position_results_std_2;
plt.fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[2])


f, axarr = plt.subplots(1, 1)

### Radius
axarr[0].plot(error_levels,hough_radius_results_mean_0,color=colors[0],label=labels[0])
error_sup=hough_radius_results_mean_0+hough_radius_results_std_0;
error_inf=hough_radius_results_mean_0-hough_radius_results_std_0;
axarr[0].fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[0])

axarr[0].plot(error_levels,hough_orientation_results_mean_1,color=colors[1],label=labels[1])
error_sup=hough_position_results_mean_1+hough_position_results_std_1;
error_inf=hough_position_results_mean_1-hough_position_results_std_1;
axarr[0].fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[1])

axarr[0].plot(error_levels,hough_position_results_mean_2,color=colors[2],label=labels[2])
error_sup=hough_position_results_mean_2+hough_position_results_std_2;
error_inf=hough_position_results_mean_2-hough_position_results_std_2;
axarr[0].fill_between(error_levels,error_sup,error_inf,where=error_inf<=error_sup,interpolate=True,alpha=alpha_,color=colors[2])

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

#plt.tight_layout()

#plt.tight_layout(pad=0.9, w_pad=0.01, h_pad=0.01)
#plt.subplots_adjust(left=0.05, right=0.99, top=0.95, bottom=0.1,  wspace=0.25, hspace=None)
plt.subplots_adjust(left=0.08, right=0.99, top=0.95, bottom=0.1,  wspace=0.25, hspace=None)
#plt.subplots_adjust(left=0.05, right=0.99, top=0.95, bottom=0.1)
#plt.subplots_adjust(left=0.05, right=0.99, top=0.75, bottom=0.25)
plt.show()



#fig1.savefig(path.join(outpath,"entropy.pdf"))#,      bbox_inches='tight', transparent="True", pad_inches=0)
#fig2.savefig(path.join(outpath,"occupied_cells.pdf"), bbox_inches='tight', transparent="True", pad_inches=0)
#fig3.savefig(path.join(outpath,"histogram.pdf"),      bbox_inches='tight', transparent="True", pad_inches=0)


