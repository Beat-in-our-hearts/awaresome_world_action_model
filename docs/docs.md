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
│   └── ...
```

# 说明
其中，`docs.md` 是文档的主文件，包含了文档的目录和内容。`papers/` 文件夹按赛道拆分为 `embodied_robotics/` 和 `autonomous_driving/` 两个子目录。每篇论文都放在所属赛道下的独立文件夹中，里面包含论文 PDF 和对应的 `paper_arxiv_code/` 文件夹。`paper_item_name` 使用日期加论文标题的格式命名，例如 `20240601_{paper_title}/`。每个论文的 `paper_arxiv_code/` 文件夹可以包含该论文在 arXiv 上的相关信息，如摘要、作者信息、源码包和元数据等。
