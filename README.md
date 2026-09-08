# MergePDF

一个简单的 PDF 合并工具，将程序所在目录中的多个 PDF 合并成一个文件。

## 下载与使用

[下载 Windows 版 merge_pdf.exe](https://github.com/Qiuyue0125/MergePDF/releases/latest/download/merge_pdf.exe)

1. 将 `merge_pdf.exe` 放到需要合并的 PDF 文件夹中。
2. 双击运行，程序会按文件名排序后合并当前目录中的 PDF。
3. 合并结果保存为同目录下的 `merged_result.pdf`，完成后弹窗提示。

建议用 `01.pdf`、`02.pdf` 等文件名控制合并顺序。程序只处理当前目录，不扫描子目录；会跳过已有的 `merged_result.pdf`，并覆盖该结果文件。

## 从源码运行

需要 Python 和 Tkinter（Windows 官方 Python 安装程序自带）。将脚本放到 PDF 所在文件夹中，然后运行：

```powershell
python -m pip install -r requirements.txt
python merge_pdf.py
```
