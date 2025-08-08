import serial.tools.list_ports
import time
import tkinter as tk
from tkinter import messagebox

def detectar_esp32(portas_antes, portas_depois):
    novas_portas = [p for p in portas_depois if p.device not in [x.device for x in portas_antes]]
    for porta in novas_portas:
        desc = porta.description.lower()
        if "cp210" in desc or "ch340" in desc or "silicon labs" in desc or "usb serial" in desc:
            return porta
    return None

def mostrar_popup(porta):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("ESP32 Detectado", f"Dispositivo ESP32 conectado na porta {porta.device}")
    root.destroy()

def main():
    print("Monitorando conexão de ESP32... (CTRL+C para sair)")
    portas_anteriores = list(serial.tools.list_ports.comports())

    while True:
        time.sleep(2)
        portas_atuais = list(serial.tools.list_ports.comports())
        esp32_porta = detectar_esp32(portas_anteriores, portas_atuais)
        if esp32_porta:
            print(f"ESP32 detectado: {esp32_porta.device}")
            mostrar_popup(esp32_porta)
        portas_anteriores = portas_atuais

if __name__ == "__main__":
    main()
