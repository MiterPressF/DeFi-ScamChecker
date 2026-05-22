import customtkinter as ctk
import requests
from web3 import Web3
import qrcode
from fpdf import FPDF
import os
from PIL import Image

web3 = Web3()

NETWORKS = {
    "Ethereum": "1",
    "BSC (Binance Smart Chain)": "56",
    "Polygon": "137",
    "Arbitrum": "42161"
}


def generate_certificate(address, network, score, verdict, report_text):
    try:
        pdf = FPDF()
        pdf.add_page()


        pdf.set_draw_color(31, 83, 141)  #1F538D
        pdf.set_line_width(1.0)
        pdf.rect(5, 5, 200, 287)
        pdf.rect(7, 7, 196, 283)

        # Заголовок
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 20)
        pdf.set_text_color(31, 83, 141)
        pdf.cell(200, 15, txt="DEFI SMART CONTRACT AUDIT REPORT", ln=True, align='C')

        # Подзаголовок
        pdf.set_font("Arial", 'I', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(200, 5, txt="Automated Cryptographic Verification Certificate", ln=True, align='C')

        pdf.ln(5)
        pdf.set_draw_color(200, 200, 200)
        pdf.line(20, 45, 190, 45)

        # --- БЛОК ОСНОВНЫХ ДАННЫХ ---
        pdf.ln(10)
        pdf.set_text_color(0, 0, 0)

        def add_param(label, value, is_bold_val=False):
            pdf.set_font("Arial", 'B', 11)
            pdf.cell(45, 8, txt=label, ln=False)
            pdf.set_font("Arial", 'B' if is_bold_val else '', 11)
            pdf.cell(145, 8, txt=value, ln=True)

        add_param("Target Contract:", address)
        add_param("Blockchain Network:", network)
        add_param("Audit Timestamp:", "May 2026 (Pre-Defense Simulation)")

        if verdict == "SAFE":
            pdf.set_text_color(46, 204, 113)  # Зеленый
        elif verdict == "WARNING":
            pdf.set_text_color(241, 196, 15)  # Желтый
        else:
            pdf.set_text_color(231, 76, 60)  # Красный

        add_param("Security Score:", f"{score}/100", is_bold_val=True)
        add_param("Final Verdict:", verdict, is_bold_val=True)

        pdf.set_text_color(0, 0, 0)

        #ТЕХНИЧЕСКИЕ ДЕТАЛИ
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, txt="Detailed System Analysis:", ln=True)

        pdf.set_font("Courier", size=10)

        raw_bytes = report_text.encode('latin-1', 'ignore')
        clean_report = raw_bytes.decode('latin-1')
        clean_report = clean_report.replace('%', ' percent')

        pdf.set_fill_color(245, 247, 250)
        pdf.set_draw_color(220, 224, 230)

        x, y = pdf.get_x(), pdf.get_y()
        pdf.rect(x + 10, y, 170, 75, 'DF')

        pdf.set_xy(x + 13, y + 3)
        pdf.multi_cell(164, 6, txt=clean_report)

        #ДИНАМИЧЕСКАЯ МЕМНАЯ ПЕЧАТЬ
        if verdict == "SAFE":
            seal_color = (46, 204, 113)
            text_line1 = "GIGA CHAD"
            text_line2 = "100% NOT A RUG PULL"
            status_text = "APPROVED"
        elif verdict == "WARNING":
            seal_color = (241, 196, 15)
            text_line1 = "NORMIE ASSET"
            text_line2 = "HIGH SLIPPAGE RISK"
            status_text = "SUSPICIOUS"
        else:
            seal_color = (231, 76, 60)
            text_line1 = "RUG PULL DETECTED"
            text_line2 = "REJECTED BY CHAD"
            status_text = "SCAM ALERT"

        pdf.set_draw_color(*seal_color)
        pdf.set_text_color(*seal_color)

        pdf.set_line_width(1.5)
        pdf.ellipse(140, 220, 45, 45, 'D')

        pdf.set_line_width(0.5)
        pdf.ellipse(142.5, 222.5, 40, 40, 'D')

        pdf.set_font("Arial", 'B', 7)
        pdf.set_xy(145, 229)
        pdf.cell(35, 4, txt=f"* {status_text} *", ln=True, align='C')

        pdf.set_font("Arial", 'B', 10)
        pdf.set_xy(142, 235)
        pdf.cell(41, 5, txt=text_line1, ln=True, align='C')

        pdf.set_font("Arial", 'B', 6)
        pdf.set_xy(143, 242)
        pdf.cell(39, 4, txt=text_line2, ln=True, align='C')

        pdf.set_font("Arial", 'I', 6)
        pdf.set_xy(145, 249)
        pdf.cell(35, 3, txt="OFFICIAL DeFi SEAL", ln=True, align='C')

        pdf.set_text_color(0, 0, 0)

        pdf_filename = f"audit_{address[:8]}.pdf"
        pdf.output(pdf_filename)

        # ГЕНЕРАЦИЯ QR-КОДА
        qr_data = f"file:///{os.path.abspath(pdf_filename)}"
        qr = qrcode.make(qr_data)
        qr_filename = f"qr_{address[:8]}.png"
        qr.save(qr_filename)

        return qr_filename, pdf_filename
    except Exception as e:
        print(f"Ошибка генерации документов: {e}")
        return None, None


def start_analysis():
    address = entry.get().strip()
    selected_network = network_var.get()
    chain_id = NETWORKS[selected_network]

    if not web3.is_address(address):
        result_text.set("❌ Ошибка: Неверный адрес")
        qr_label.configure(image="")  # Сбрасываем старый QR при ошибке
        return

    progress_bar.set(0)
    progress_bar.configure(progress_color="gray")
    result_text.set(f"🧪 Запуск ML-аудита...\nСеть: {selected_network}")
    qr_label.configure(image="")
    root.update_idletasks()

    try:
        api_url = f"https://api.gopluslabs.io/api/v1/token_security/{chain_id}?contract_addresses={address}"
        response = requests.get(api_url, timeout=15).json()

        if response.get("code") != 1 or not response.get("result"):
            result_text.set(f"❌ Данные по адресу не найдены в сети {selected_network}.")
            return

        res_key = address.lower()
        if res_key not in response["result"]:
            result_text.set("❌ Ошибка: API не вернуло отчет для данного контракта.")
            return

        data = response["result"][res_key]

        #МАТЕМАТИЧЕСКИЙ СКОРИНГ
        score = 100
        reasons = []

        if data.get("is_honeypot") == "1":
            score -= 90
            reasons.append("Honeypot Detected")

        s_tax = float(data.get("sell_tax", 0)) * 100
        b_tax = float(data.get("buy_tax", 0)) * 100
        if s_tax > 10 or b_tax > 10:
            score -= 30
            reasons.append(f"High Tax ({max(s_tax, b_tax):.1f}%)")

        if data.get("slippage_modifiable") == "1":
            score -= 25
            reasons.append("Slippage Modifiable")

        if data.get("lp_locked") == "0" or data.get("lp_holder_count", "0") == "0":
            score -= 40
            reasons.append("Liquidity NOT Locked")

        if data.get("can_mint") == "1":
            score -= 20
            reasons.append("Mint Function Active")

        if data.get("is_open_source") == "0":
            score -= 40
            reasons.append("Closed Source Code")

        score = max(0, min(100, score))

        #ВИЗУАЛИЗАЦИЯ И ВЕРДИКТ
        progress_val = score / 100
        progress_bar.set(progress_val)

        if score >= 85:
            color = "#2ecc71"
            verdict = "SAFE"
        elif score >= 50:
            color = "#f1c40f"
            verdict = "WARNING"
        else:
            color = "#e74c3c"
            verdict = "SCAM"

        progress_bar.configure(progress_color=color)

        report = f"📊 TRUST SCORE: {score}/100\n"
        report += f"VERDICT: {verdict}\n"
        report += "--------------------------------------\n"
        report += f"Token: {data.get('token_name')} ({data.get('token_symbol')})\n"

        if reasons:
            report += "Issues: " + ", ".join(reasons) + "\n"
        else:
            report += "No critical issues found\n"

        report += f"Taxes: Buy {b_tax:.1f}% / Sell {s_tax:.1f}%"

        #ИНТЕГРАЦИЯ СЕРТИФИКАТА И QR-КОДА
        qr_file, pdf_file = generate_certificate(address, selected_network, score, verdict, report)

        if qr_file and pdf_file:
            report += f"\n--------------------------------------\n"
            report += f"📄 Certificate generated: {pdf_file}"
            print(f"Файлы успешно созданы в: {os.path.abspath(pdf_file)}")

            #ВЫВОД QR КОДА В ОКНО ПРИЛОЖЕНИЯ
            try:
                # Открываем сохраненную картинку через Pillow
                img = Image.open(qr_file)
                # Конвертируем в формат, понятный CustomTkinter
                ctk_image = ctk.CTkImage(light_image=img, dark_image=img, size=(140, 140))
                # Передаем картинку в виджет
                qr_label.configure(image=ctk_image)
                qr_label.image = ctk_image  # Защита от удаления картинки сборщиком мусора
            except Exception as img_err:
                print(f"Не удалось отобразить QR-код в окне: {img_err}")
        else:
            report += f"\n--------------------------------------\n"
            report += f"⚠️ Ошибка генерации PDF/QR."

        result_text.set(report)

    except Exception as e:
        result_text.set(f"❌ Системная ошибка: {str(e)}")


#ИНТЕРФЕЙС (GUI)
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("D-Security DeFi Auditor v3.5")
root.geometry("600x780")  # Немного увеличили высоту окна для QR-кода

ctk.CTkLabel(root, text="DeFi Blockchain Security Expert System", font=("Arial", 20, "bold")).pack(pady=20)

network_var = ctk.StringVar(value="Ethereum")
ctk.CTkOptionMenu(root, values=list(NETWORKS.keys()), variable=network_var).pack(pady=5)

frame_in = ctk.CTkFrame(root)
frame_in.pack(pady=15)
entry = ctk.CTkEntry(frame_in, placeholder_text="Enter contract address 0x...", width=380)
entry.grid(row=0, column=0, padx=5)
ctk.CTkButton(frame_in, text="📋", width=40,
              command=lambda: [entry.delete(0, 'end'), entry.insert(0, root.clipboard_get())]).grid(row=0, column=1,
                                                                                                    padx=5)

ctk.CTkButton(root, text="AUDIT ASSET", command=start_analysis, fg_color="#1f538d", height=40,
              font=("Arial", 14, "bold")).pack(pady=10)

ctk.CTkLabel(root, text="Security Scale (Trust Score):", font=("Arial", 12)).pack(pady=(10, 0))
progress_bar = ctk.CTkProgressBar(root, width=450, height=15)
progress_bar.set(0)
progress_bar.pack(pady=10)

result_text = ctk.StringVar(value="Awaiting contract address...")
res_label = ctk.CTkLabel(root, textvariable=result_text, font=("Courier New", 13), justify="left", wraplength=550)
res_label.pack(pady=15, padx=25)

#ВИДЖЕТ ДЛЯ ОТОБРАЖЕНИЯ QR-КОДА
qr_label = ctk.CTkLabel(root, text="")  # Изначально пустой, без текста
qr_label.pack(pady=10)

root.mainloop()
