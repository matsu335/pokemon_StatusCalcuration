
import tkinter as tk
import tkinter.ttk as ttk
import math

#システム


def Calucuration_h(s, k, d, l):
    try:
        s = int(s)
        k = int(k)
        d = int(d)
        l = int(l)
        value = math.floor((s * 2 + k + d / 4) * l / 100 + l + 10)
        return value
    except ValueError:
        return None

def Calucuration_abcds(s, k, d, l, personality):
    if personality == "-":
        p = 1
    elif personality == "x1.1":
        p = 1.1
    elif personality == "x0.9":
        p = 0.9
    else:
        p = 0
    try:
        s = int(s)
        k = int(k)
        d = int(d)
        l = int(l)
        value = math.floor(((s*2 + k + d/4)*l/100 + 5)*p)
        return value
    except ValueError:
        return None

def Run():
    #実数値計算
    h = Calucuration_h(input_hs.get(), input_hk.get(), input_hd.get(), combobox_l.get())
    a = Calucuration_abcds(input_as.get(), input_ak.get(), input_ad.get(), combobox_l.get(), combobox_ap.get())
    b = Calucuration_abcds(input_bs.get(), input_bk.get(), input_bd.get(), combobox_l.get(), combobox_bp.get())
    c = Calucuration_abcds(input_cs.get(), input_ck.get(), input_cd.get(), combobox_l.get(), combobox_cp.get())
    d = Calucuration_abcds(input_ds.get(), input_dk.get(), input_dd.get(), combobox_l.get(), combobox_dp.get())
    s = Calucuration_abcds(input_ss.get(), input_sk.get(), input_sd.get(), combobox_l.get(), combobox_sp.get())
    labeloh["text"] = "{}".format(h)
    labeloa["text"] = "{}".format(a)
    labelob["text"] = "{}".format(b)
    labeloc["text"] = "{}".format(c)
    labelod["text"] = "{}".format(d)
    labelos["text"] = "{}".format(s)

def Reset():
    input_hs.delete(0, tk.END)
    input_hk.delete(0, tk.END)
    input_hd.delete(0, tk.END)
    input_as.delete(0,tk.END)
    input_ak.delete(0,tk.END)
    input_ad.delete(0,tk.END)
    input_bs.delete(0, tk.END)
    input_bk.delete(0, tk.END)
    input_bd.delete(0, tk.END)
    input_cs.delete(0, tk.END)
    input_ck.delete(0, tk.END)
    input_cd.delete(0, tk.END)
    input_ds.delete(0, tk.END)
    input_dk.delete(0, tk.END)
    input_dd.delete(0, tk.END)
    input_ss.delete(0, tk.END)
    input_sk.delete(0, tk.END)
    input_sd.delete(0, tk.END)
    combobox_ap.current(0)
    combobox_bp.current(0)
    combobox_cp.current(0)
    combobox_dp.current(0)
    combobox_sp.current(0)



#GUI
root = tk.Tk()
root.title("Pokemon Status Calucuration")
root.geometry("500x300")

#入力用のGUI
frameIN = tk.Frame(root, width=400, relief=tk.SUNKEN, bd=2)
frameIN.pack(side=tk.LEFT, fill=tk.Y)

frameP = tk.Frame(frameIN, height=30)
frameP.pack(side=tk.TOP, fill=tk.X)
labelP = tk.Label(frameP, text="", width=4)
labelP.pack(side=tk.LEFT, fill=tk.Y)
ps = tk.Label(frameP, text="種族値", width=10)
ps.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
pk = tk.Label(frameP, text="個体値", width=10)
pk.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
pd = tk.Label(frameP, text="努力値", width=10)
pd.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)
pp = tk.Label(frameP, text="性格補正", width=10)
pp.pack(side=tk.LEFT, anchor=tk.W, fill=tk.Y)

frameH = tk.Frame(frameIN, height=30)
frameH.pack(fill=tk.X, pady=5)
labelH = tk.Label(frameH, text="H", width=4)
labelH.pack(side=tk.LEFT, fill=tk.Y)
input_hs = tk.Entry(frameH, width=4)
input_hs.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_hk = tk.Entry(frameH, width=4)
input_hk.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_hd = tk.Entry(frameH, width=4)
input_hd.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameA = tk.Frame(frameIN, height=30)
frameA.pack(fill=tk.X, pady=5)
labelA = tk.Label(frameA, text="A", width=4)
labelA.pack(side=tk.LEFT, fill=tk.Y)
input_as = tk.Entry(frameA, width=4)
input_as.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_ak = tk.Entry(frameA, width=4)
input_ak.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_ad = tk.Entry(frameA, width=4)
input_ad.pack(side=tk.LEFT, fill=tk.Y, padx=24)
module_a = ('-', 'x1.1', 'x0.9')
combobox_ap = ttk.Combobox(frameA, height=3, width=4, values=module_a)
combobox_ap.set("-")
combobox_ap.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameB = tk.Frame(frameIN, height=30)
frameB.pack(fill=tk.X, pady=5)
labelB = tk.Label(frameB, text="B", width=4)
labelB.pack(side=tk.LEFT, fill=tk.Y)
input_bs = tk.Entry(frameB, width=4)
input_bs.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_bk = tk.Entry(frameB, width=4)
input_bk.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_bd = tk.Entry(frameB, width=4)
input_bd.pack(side=tk.LEFT, fill=tk.Y, padx=24)
module_b = ('-', 'x1.1', 'x0.9')
combobox_bp = ttk.Combobox(frameB, height=3, width=4, values=module_b)
combobox_bp.set("-")
combobox_bp.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameC = tk.Frame(frameIN, height=30)
frameC.pack(fill=tk.X, pady=5)
labelC = tk.Label(frameC, text="C", width=4)
labelC.pack(side=tk.LEFT, fill=tk.Y)
input_cs = tk.Entry(frameC, width=4)
input_cs.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_ck = tk.Entry(frameC, width=4)
input_ck.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_cd = tk.Entry(frameC, width=4)
input_cd.pack(side=tk.LEFT, fill=tk.Y, padx=24)
module_c = ('-', 'x1.1', 'x0.9')
combobox_cp = ttk.Combobox(frameC, height=3, width=4, values=module_c)
combobox_cp.set("-")
combobox_cp.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameD = tk.Frame(frameIN, height=30)
frameD.pack(fill=tk.X, pady=5)
labelD = tk.Label(frameD, text="D", width=4)
labelD.pack(side=tk.LEFT, fill=tk.Y)
input_ds = tk.Entry(frameD, width=4)
input_ds.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_dk = tk.Entry(frameD, width=4)
input_dk.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_dd = tk.Entry(frameD, width=4)
input_dd.pack(side=tk.LEFT, fill=tk.Y, padx=24)
module_d = ('-', 'x1.1', 'x0.9')
combobox_dp = ttk.Combobox(frameD, height=3, width=4, values=module_d)
combobox_dp.set("-")
combobox_dp.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameS = tk.Frame(frameIN, height=30)
frameS.pack(fill=tk.X, pady=5)
labelS = tk.Label(frameS, text="S", width=4)
labelS.pack(side=tk.LEFT, fill=tk.Y)
input_ss = tk.Entry(frameS, width=4)
input_ss.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_sk = tk.Entry(frameS, width=4)
input_sk.pack(side=tk.LEFT, fill=tk.Y, padx=24)
input_sd = tk.Entry(frameS, width=4)
input_sd.pack(side=tk.LEFT, fill=tk.Y, padx=24)
module_s = ('-', 'x1.1', 'x0.9')
combobox_sp = ttk.Combobox(frameS, height=3, width=4, values=module_s)
combobox_sp.set("-")
combobox_sp.pack(side=tk.LEFT, fill=tk.Y, padx=24)

frameL = tk.Frame(frameIN, pady=10, relief=tk.RAISED, bd=1)
frameL.pack(fill=tk.X, pady=5)
labelL = tk.Label(frameL, text="レベル", width=4, padx=32)
labelL.pack(side=tk.LEFT, fill=tk.Y)
module_l = ('', '50', '100')
combobox_l = ttk.Combobox(frameL, height=3, width=4, values=module_l)
combobox_l.set("50")
combobox_l.pack(side=tk.LEFT, fill=tk.Y, pady=10)
labelLper = tk.Label(frameL, text="Lv.", width=4)
labelLper.pack(side=tk.LEFT, fill=tk.Y)

ButtonReset = tk.Button(frameL, text='リセット', relief=tk.RAISED, bg='firebrick3', bd=1, padx=5, pady=3, command=lambda:Reset())
ButtonReset.pack(side=tk.RIGHT, fill=tk.Y, padx=30, pady=5)


#出力用のGUI
frameOUT = tk.Frame(root, relief=tk.SUNKEN, bd=2, padx=20)
frameOUT.pack(side=tk.LEFT, fill=tk.Y)

frameop = tk.Frame(frameOUT, height=30)
frameop.pack(side=tk.TOP, fill=tk.X)
outp = tk.Label(frameop, text="実数値")
outp.pack(side=tk.LEFT, fill=tk.Y)
frameoh = tk.Frame(frameOUT, height=30)
frameoh.pack(fill=tk.X, pady=6)
if 'h' in locals() or 'h' in globals():
    labeloh = tk.Label(frameoh, text="{}".format(h), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labeloh = tk.Label(frameoh, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labeloh.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameoa = tk.Frame(frameOUT, height=30)
frameoa.pack(fill=tk.X, pady=6)
if 'a' in locals() or 'a' in globals():
    labeloa = tk.Label(frameoa, text="{}".format(a), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labeloa = tk.Label(frameoa, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labeloa.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameob = tk.Frame(frameOUT, height=30)
frameob.pack(fill=tk.X, pady=6)
if 'b' in locals() or 'b' in globals():
    labelob = tk.Label(frameob, text="{}".format(b), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labelob = tk.Label(frameob, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labelob.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameoc = tk.Frame(frameOUT, height=30)
frameoc.pack(fill=tk.X, pady=6)
if 'c' in locals() or 'c' in globals():
    labeloc = tk.Label(frameoc, text="{}".format(c), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labeloc = tk.Label(frameoc, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labeloc.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameod = tk.Frame(frameOUT, height=30)
frameod.pack(fill=tk.X, pady=6)
if 'd' in locals() or 'd' in globals():
    labelod = tk.Label(frameod, text="{}".format(d), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labelod = tk.Label(frameod, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labelod.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameos = tk.Frame(frameOUT, height=30)
frameos.pack(fill=tk.X, pady=6)
if 's' in locals() or 's' in globals():
    labelos = tk.Label(frameos, text="{}".format(s), width=4, relief=tk.SUNKEN, bg='white', bd=1)
else:
    labelos = tk.Label(frameos, text=" ", width=4, relief=tk.SUNKEN, bg='white', bd=1)
labelos.pack(side=tk.LEFT, fill=tk.Y, padx=10)
frameRUN = tk.Frame(frameOUT, relief=tk.SOLID, bd=1)
frameRUN.pack(fill=tk.X, pady=20)
ButtonRun = tk.Button(frameRUN, text='実行', relief=tk.RAISED, bg='aquamarine3', bd=1, padx=15, pady=15, command=lambda:Run())
ButtonRun.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()