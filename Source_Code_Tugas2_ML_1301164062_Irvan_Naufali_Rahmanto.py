import csv
import math
import random
# import numpy

# deklarasi array untuk menyimpan object data
obj_arr = []

# memanggil file csv
# with open("dataset.csv") as dataset:
with open('Tugas_2_ML_Genap_2018-2019_Dataset_Tanpa_Label.csv') as dataset:
    reader = csv.reader(dataset)

# memasukkan row ditiap csv ke dalam array berdasarkan index
    for row in reader:
        obj_arr.append([float(row[0]), float(row[1])])
    #     print(row)

# Random angka untuk menentukan weight neuron
n = []
temp2 = []
sn = []
tn_arr = []

n.append([random.uniform(0, 15), random.uniform(0, 15)])
n.append([random.uniform(0, 15), random.uniform(0, 15)])
n.append([random.uniform(0, 15), random.uniform(0, 15)])

# melakukan penelusuran Self Organizing Method untuk tiap iterasi nya

# fungsi rumus euclidian


def euclidian(o1, o2):
    formula = 0
    formula = math.sqrt(((o1[0] - o2[0])**2) + ((o1[1] - o2[1])**2))
    return formula

# fungsi jarak neuron j indeks neuron terdekat i(x) dan seterus nya


def rangeS(s1, s2):
    formula = math.sqrt(((s1[0] - s2[0])**2) + ((s1[1] - s2[1])**2))
    return formula

# fungsi rumus Tn menggunakan exponen


def exspTn(t):
    teta = 2
    tn_arr = []
    for tn in range(3):
        tn_arr.append(math.exp(-(t[tn]**2)/(2*(teta**2))))
    return tn_arr

# fungsi rumus Wn1o1 untuk mencari


def wn(x, y):
    learningRate = 0.1  # eta
    wn_arr = []
    wn_arr2 = []
    for i in range(3):
        # wn_arr2=[]
        for j in range(2):
            wn_arr2.append(str(learningRate*y[j]*(x[j] - n[neuron[i]][j])))
        wn_arr.append((wn_arr2[0], wn_arr2[1]))
    return wn_arr


# fungsi rumus Wn untuk mengupdate nilai iterasi nya

def updateWn(x):
    for i in range(len(x)):
        arr = []
        for j in range(2):
            n[neuron[i]][j] = n[neuron[i]][j] + float(x[i][j][:3])
    return arr

# mengurutkan data yang diiterasi


def sorting(x):
    return x[0]


print(n)

teta = 0
teta_before = 2
learningRate = 0.1
learningRate_before = 0.1
tn = 2
t_before = 2

# main
neuron = []
neuron_arr = []

for i in range(5):
    teta = teta_before * math.exp(-(i+1)/teta_before)
    learningRate = learningRate_before*math.exp(-(i+1)/tn)
    for j in range(len(obj_arr)):
        neuron_arr, neuron = [], []
        for x in range(len(n)):
            neuron_arr.append([euclidian(obj_arr[j], n[x]), x])
        neuron_arr.sort(key=sorting)

        for x in range(len(n)):
            neuron_arr.append(neuron_arr[x][1])

        for x in range(3):
            sn.append(rangeS(n[neuron[0]], n[neuron[x]]))

        tn_arr = exspTn(sn)

        temp2 = wn(obj_arr[j], tn_arr)

        z = updateWn(temp2)

print('n paling terakhir')
print(n)
