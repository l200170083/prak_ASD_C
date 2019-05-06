class mhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kt = kota
        self.us = us
    def __str__(self):
        s = self.nama + ",NIM" + str(self.nim)+ " tinggal di " + self.kt + \
            "uang saku sebesar" + str(self.us) + "per bulan."
        return s
    def getnim (self):
        return self.nim

m1 = mhsTIF("Caca", 16, "Solo", 125000)
m2 = mhsTIF("Rosa", 34, "Sragen", 300000)
m3 = mhsTIF("Lia", 55, "Palembang", 200000)
m4 = mhsTIF("Dewi", 21, "Boyolali", 250000)
m5 = mhsTIF("Angga", 9, "Padang", 500000)

daftar = [m1,m2,m3,m4,m5]

def mergesort(A):
    if len (A)> 1:
        mid = len (A) // 2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]
    
        mergesort (separuhKiri)
        mergesort (separuhKanan)

        #proses penggabungan
        i=0;j=0;k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i].nim < separuhKanan[j].nim:
                A[k].nim = separuhKiri[i].nim
                i = i+1
            else:
                A[k].nim = separuhKanan[j].nim
                j = j+1
            k = k+1
        while i < len(separuhKiri):
            A[k].nim = separuhKiri[i].nim
            i = i+1
            k = k+1
        while j < len (separuhKanan):
            A[k].nim = separuhKanan[j].nim
            j = j+1
            k = k+1

        return A

mergesort (daftar)
for i in daftar:
    print (i)

def quickSort(A):
    quickSortBantu(A, 0, len(A) - 1)
    return A
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal].getnim()

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and\
              A[penandaKiri].getnim() <= nilaiPivot:
            penandaKiri += 1

        while A[penandaKanan].getnim() >= nilaiPivot and\
              penandaKanan >= penandaKiri:
            penandaKanan -= 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

quickSort(daftar)
for i in daftar:
    print (i)
print

#######################################NOMOR 3##############################

from time import time as detak
from random import shuffle as kocok
import time

def cari(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiTerkecil(A, dari, sampai):
    posisiTerkecil = dari
    for i in range (dari+1, sampai):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

def bubbleSort(A):
    n = len (A)
    for i in range(n-1):
        for j in range (n-i-1):
            if A[j] > A[j+1]:
                swap (A,j,j+1)

def selectionSort(A):
    n = len (A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos -= 1
        A[pos] = nilai

def mergeSort (A):
    if len (A) > 1 :
        mid = len(A) // 2
        separuhKiri = A [:mid]
        separuhKanan = A [mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0
        j=0
        k=0
        while i < len (separuhKiri) and j < len(separuhKanan):
            if separhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1

        while i < len (separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1
        while j < len (separuhKanan):
            A[k] = separuhKanan [j]
            j = j + 1
            k = k + 1

            return A
        
def quickSort(A):
    quickSortBantu(A, 0, len(A)-1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah -1)
        quickSortBantu(A, titikbeah + 1, akhir)

def partisi (A, awal, akhir):
    nilaiPivot= A(awal)

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and\
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and\
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanana]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan
k = range (6000)
shuffle(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]
u_mrg = k[:]
u_quick = k[:]

print ("No.3")
aw = timeD(); bubbeSort(u_bub); ak=timeD(); print ("BubbleSort: %g detik" %(ak-aw))
aw = timeD(); selectionSort (u_sel); ak=timeD(); print ("SelectionSort: %g detik" %(ak-aw))
aw = timeD(); insertionSort (u_ins); ak=timeD(); print ("InsertionSort: %g detik" %(ak-aw))
aw = timeD(); mergeSort (u_mrg); ak=timeD(); print ("MergeSort: %g detik" %(ak-aw))
aw = timeD(); quickSort(u_quick); ak=timeD(); print ("QuickSort: %g detik" %(ak-aw))
print 

#########################Nomor 5############################################################
class mhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kt = kota
        self.us = us
    def __str__(self):
        s = self.nama + ",NIM" + str(self.nim)+ " tinggal di " + self.kt + \
            "uang saku sebesar" + str(self.us) + "per bulan."
        return s
    def getnim (self):
        return self.nim

m1 = mhsTIF("Caca", 16, "Solo", 125000)
m2 = mhsTIF("Rosa", 34, "Sragen", 300000)
m3 = mhsTIF("Lia", 55, "Palembang", 200000)
m4 = mhsTIF("Dewi", 21, "Boyolali", 250000)
m5 = mhsTIF("Angga", 9, "Padang", 500000)

daftar = [m1,m2,m3,m4,m5]

A=[]
for i in daftar:
    A.append(i.nama)

def cetak ():
    for i in A:
        print (i)
        
def mergeSort(A):
    _mergeSort(A, 0, len(A)-1)

def _mergeSort(A, awal, akhir):
    mid = (awal+akhir) / 2
    if awal < akhir:
        _mergeSort(A, awal, mid)
        _mergeSort(A, mid+1, akhir)

    (a, f, 1 <= 0, awal, mid + 1)
    tmp = [None] * (akhir-awal+1)
    while f <= mid and 1 <= akhir:
        if A[f] < A[1]:
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[1]
            (1 <= 1)
        a+=1

    if f <= mid:
        tmp[a:] = a[f:mid + 1]


    if 1 <= akhir:
        tmp[a:] = A[1:akhir + 1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp [a]
        awal += 1
        a += 1

    print ("Nomor 5")
    print ("Nama sebelum diurutkan:")
    cetak()
    mergeSort(A)
    print
    print ("Nama telah urut:")
    cetak()
    print
    
#####################Nomor 6#################################

class mhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kt = kota
        self.us = us
    def __str__(self):
        s = self.nama + ",NIM" + str(self.nim)+ " tinggal di " + self.kt + \
            "uang saku sebesar" + str(self.us) + "per bulan."
        return s
    def getnim (self):
        return self.nim

m1 = mhsTIF("Caca", 16, "Solo", 125000)
m2 = mhsTIF("Rosa", 34, "Sragen", 300000)
m3 = mhsTIF("Lia", 55, "Palembang", 200000)
m4 = mhsTIF("Dewi", 21, "Boyolali", 250000)
m5 = mhsTIF("Angga", 9, "Padang", 500000)

daftar = [m1,m2,m3,m4,m5]

A=[]
for i in daftar:
    A.append(i.nama)

def cetak ():
    for i in A:
        print (i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len (arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print ("Nomor 6")
print ("Nama sebelum diurutkan:")
cetak()
print
print ("Nama telah urut:")
A=quickSort (A)
cetak()
print

################################Nomor 7##################################

from time import time as detak
from random import shuffle as kocok

def mergesort(A):
    if len (A)> 1:
        mid = len (A) // 2
        kiri = A[:mid]
        kanan = A[mid:]
    
        mergesort (kiri)
        mergesort (kanan)

        #proses penggabungan
        i=0;j=0;k=0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                A[k] = kiri[i]
                i = i+1
            else:
                A[k] = kanan[j]
                j = j+1
            k = k+1
        while i < len(kiri):
            A[k] = kiri[i]
            i = i+1
            k = k+1
        while j < len (kanan):
            A[k] = kanan[j]
            j = j+1
            k = k+1

def partisi (A, awal, akhir):
    nilaiPivot= A(awal)

    penandaKiri = awal + 1
    penandaKanan = akhir

    selesai = False
    while not selesai:

        while penandaKiri <= penandaKanan and\
              A[penandaKiri] <= nilaiPivot:
            penandaKiri = penandaKiri + 1

        while A[penandaKanan] >= nilaiPivot and\
              penandaKanan >= penandaKiri:
            penandaKanan = penandaKanan - 1

        if penandaKanan < penandaKiri:
            selesai = True
        else:
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanana]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

def quickBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah - 1)
        quickSortBantu(A, titikBelah + 1, akhir)

def quickSort(A):
    quickBantu(A, 0, len (A)-1)

def mergeSortBaru(A):
    _mergeSort(A, 0, len (A)-1)

def _mergeSort (A, awal, akhir):
    mid = (awal+akhir) / 2
    if awal < akhir:
        _mergeSort(A, awal, mid)
        _mergeSort(A, mid+1, akhir)

    (a, f, 1 <= 0, awal, mid + 1)
    tmp = [None] * (akhir-awal+1)
    while f <= mid and 1 <= akhir:
        if A[f] < A[1]:
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[1]
            (1 <= 1)
        a+=1

    if f <= mid:
        tmp[a:] = a[f:mid + 1]


    if 1 <= akhir:
        tmp[a:] = A[1:akhir + 1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp [a]
        awal += 1
        a += 1

def quickSortNew(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len (arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih
k = [i fori in (range(1,6001))]
kocok(k)
u_mrg = k[:]
u_mrgnew = k [:]
u_quick = k [:]
u_quicknew = k[:]

print ("Nomor 7")
aw=detak(); mergeSort(u_mrg); ak=detak(); print ("Merge Sort: %g detik" %(ak-aw));
aw=detak(); mergeSortBaru(u_mrgnew); ak=detak(); print ("Merge Sort New: %g detik" %(ak-aw));
aw=detak(); quickSort(u_quick); ak=detak(); print ("Quick: %g detik" %(ak-aw));
aw=detak(); quickSortNew(u_quicknew); ak=detak(); print ("Quick Sort New: %g detik" %(ak-aw));
