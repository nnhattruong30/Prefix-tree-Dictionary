# Prefix-tree-Dictionary
## 1. Dataset
- Tập tin dataset 63920 từ lưu trong thư mục res
## 2. Cấu trúc tập tin
- mean_word.bin : tập tin nhị phân lưu nghĩa của từ
- trie.pickle: cấu trúc cây tiền tố
- hash_mean.pickle: cấu trúc bảng băm lưu địa chỉ nghĩa của từ trong mean_word.bin
- dictionary.py: lớp từ điển
- prefix_tree.py: cấu trúc cây tiền tố
- ui.py: giao diện
## 3. Cài đặt Module cần thiết
- PyQt5: `pip install PyQt5`
## 4. Chạy chương trình
- Chạy chương trình bằng lệnh: `python main.py`