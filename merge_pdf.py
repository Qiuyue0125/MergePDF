from PyPDF2 import PdfMerger
import os
import sys
from tkinter import messagebox
import tkinter as tk

# 初始化GUI
root = tk.Tk()
root.withdraw()

# 当前 exe 所在的真实目录
if getattr(sys, 'frozen', False):
    # 打包成exe后
    current_dir = os.path.dirname(sys.executable)
else:
    # 正常运行.py时
    current_dir = os.path.dirname(os.path.abspath(__file__))

try:
    pdf_files = []

    # 遍历当前目录找PDF
    for file in os.listdir(current_dir):
        if file.lower().endswith(".pdf") and file != "merged_result.pdf":
            pdf_files.append(os.path.join(current_dir, file))

    if not pdf_files:
        messagebox.showwarning("提示", "当前目录未找到PDF文件！")
        sys.exit()

    # 排序
    pdf_files.sort()

    # 合并
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)

    output_path = os.path.join(current_dir, "merged_result.pdf")
    merger.write(output_path)
    merger.close()

    messagebox.showinfo("成功", f"合并完成！\n文件保存在：\n{output_path}")

except Exception as e:
    messagebox.showerror("错误", f"失败原因：\n{str(e)}")