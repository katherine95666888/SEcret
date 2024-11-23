### README.md

---

# **页面置换算法实验**

本项目是一个基于 PyQt5 实现的页面置换算法实验工具，支持多种算法（OPT、FIFO、LRU），并提供用户友好的图形化界面，可用于学习和演示操作系统中页面置换算法的实现与性能比较。

---

## **功能说明**

1. 支持以下页面置换算法：
   - **OPT (Optimal Replacement Algorithm)**: 最优置换算法。
   - **FIFO (First In First Out)**: 先进先出算法。
   - **LRU (Least Recently Used)**: 最近最少使用算法。

2. 用户可以：
   - 输入自定义的页面序列。
   - 指定页框数。
   - 选择页面置换算法进行演示。

3. 输出以下统计数据：
   - **缺页次数**。
   - **缺页率**。
   - **页面置换过程**（每一步的内存状态）。

4. 图形化界面简单直观，适合教学、演示及实验。

---

## **运行截图**
### 主界面
![主界面示例](https://via.placeholder.com/600x400.png?text=主界面示例)

---

## **安装与运行**

### **环境要求**
- Python 3.8 或更高版本
- 已安装 `pip` 和 `virtualenv`（可选）

### **安装步骤**

1. 克隆项目到本地：
   ```bash
   git clone https://github.com/yourusername/page-replacement.git
   cd page-replacement
   ```

2. 创建虚拟环境（可选但推荐）：
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/MacOS
   venv\Scripts\activate         # Windows
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 运行程序：
   ```bash
   python main.py
   ```

---

## **使用说明**

1. 在主界面输入：
   - **页面序列**：一串整数，用逗号分隔（如 `1,2,3,4,1,2,5`）。
   - **页框数**：一个整数（如 `3`）。
   - **选择算法**：从下拉菜单选择（OPT、FIFO、LRU）。

2. 点击 **运行算法** 按钮。

3. 在下方结果区域查看：
   - 缺页次数。
   - 缺页率。
   - 页面置换过程。

---

## **代码结构**

```plaintext
project_root/
├── main.py          # 主程序，运行入口
├── algorithms/      # 页面置换算法目录
│   ├── opt.py       # OPT 算法
│   ├── fifo.py      # FIFO 算法
│   ├── lru.py       # LRU 算法
├── ui/              # 界面目录
│   └── ui_main.py   # 界面代码
├── data/            # 数据目录
│   └── input.txt    # 示例输入文件
├── requirements.txt # 依赖库清单
└── README.md        # 使用说明文档
```

---

## **示例**

### 示例输入
页面序列：  
```plaintext
1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
```

页框数：  
```plaintext
3
```

选择算法：  
```plaintext
FIFO
```

### 输出示例
```plaintext
缺页次数: 9
缺页率: 75.00%

页面置换过程：
步骤 1: [1]
步骤 2: [1, 2]
步骤 3: [1, 2, 3]
步骤 4: [2, 3, 4]
步骤 5: [3, 4, 1]
步骤 6: [4, 1, 2]
步骤 7: [1, 2, 5]
步骤 8: [2, 5, 1]
步骤 9: [5, 1, 3]
步骤 10: [1, 3, 4]
步骤 11: [3, 4, 5]
```

---

## **常见问题**

### **1. 页面序列或页框数输入格式错误**
检查输入是否符合以下规则：
- 页面序列：用逗号分隔的整数列表（如 `1,2,3,4`）。
- 页框数：正整数（如 `3`）。

### **2. 缺少依赖库**
确保按照 `requirements.txt` 安装了所需的依赖：
```bash
pip install -r requirements.txt
```

---

## **贡献指南**

欢迎提出改进建议或提交代码！如需贡献代码，请：
1. Fork 本项目。
2. 在 Fork 的仓库上创建新分支并提交修改。
3. 提交 Pull Request。

---

## **许可证**

本项目采用 MIT 许可证。您可以自由使用、修改和分发本项目代码。详细内容请参阅 [LICENSE](LICENSE)。

---

## **作者**

- **姓名**: jadew
- **联系方式**:1278633681@qq.com
- **GitHub**: https://github.com/katherine95666888

---

通过此 README，用户可以快速了解项目的功能、使用方法和运行方式，并能够轻松启动实验。
# SEcret
