import os
import glob

def convert_chinese_symbols_to_english(text):
    """
    将字符串中的中文符号转换为英文符号
    """
    chinese_symbols = {
        "，": ",", "。": ".", "；": ";", "：": ":", "？": "?", "！": "!",
        "“": '"', "”": '"', "‘": "'", "’": "'", "（": "(", "）": ")",
        "【": "[", "】": "]", "《": "<", "》": ">", "、": ","
        # 添加更多需要转换的中文符号
    }
    
    converted_text = ""
    for char in text:
        if char in chinese_symbols:
            converted_text += chinese_symbols[char]
        else:
            converted_text += char
    return converted_text

# 获取当前文件夹下所有的Markdown文件
md_files = glob.glob("*.md")

for file_path in md_files:
    with open(file_path, "r", encoding="utf-8") as file:
        markdown_text = file.read()

    # 转换中文符号为英文符号
    converted_text = convert_chinese_symbols_to_english(markdown_text)

    # 构造输出文件路径
    output_file_path = os.path.splitext(file_path)[0] + "_cov_end.md"

    # 将转换后的内容写入新文件
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(converted_text)

print("OK!")
