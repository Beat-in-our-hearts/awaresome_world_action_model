# 文档结构
```
docs/
├── docs.md
├── papers/
│   ├── embodied_robotics/
│   │   ├── paper_item_name1/
│   │   │   ├── paper1.pdf
│   │   │   └── paper_arxiv_code/
│   │   └── ...
│   ├── autonomous_driving/
│   │   ├── paper_item_name2/
│   │   │   ├── paper2.pdf
│   │   │   └── paper_arxiv_code/
│   │   └── ...
│   ├── foundational_works/
│   │   ├── paper_item_name3/
│   │   │   ├── paper3.pdf
│   │   │   └── paper_arxiv_code/
│   │   └── ...
│   └── ...
```

# 说明
其中，`docs.md` 是文档的主文件，包含了文档的目录和内容。`papers/` 文件夹目前包含 `embodied_robotics/`、`autonomous_driving/` 和 `foundational_works/` 三个子目录。每篇论文都放在所属分类下的独立文件夹中，里面包含论文 PDF 和对应的 `paper_arxiv_code/` 文件夹。`paper_item_name` 使用日期加论文标题的格式命名，例如 `20240601_{paper_title}/`。每个论文的 `paper_arxiv_code/` 文件夹可以包含该论文在 arXiv 上的相关信息，如摘要、作者信息、源码包和元数据等。

`foundational_works/` 用于存放最知名、具有铺垫性的论文。这些论文可以不是 world-action model，但应当对理解 WAM 方法脉络有重要帮助。这个分类禁止自动添加，必须经过人工审阅和确认后，才能正式收录到仓库中。
