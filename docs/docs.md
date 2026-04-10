# Document Structure
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

# Notes
`docs.md` is the main documentation file and contains the document index and content. The `papers/` directory currently includes three subdirectories: `embodied_robotics/`, `autonomous_driving/`, and `foundational_works/`. Each paper is stored in its own folder under the appropriate category, containing the paper PDF and a corresponding `paper_arxiv_code/` directory. `paper_item_name` follows the format of `date + paper title`, for example `20240601_{paper_title}/`. The `paper_arxiv_code/` directory for each paper can include related arXiv information such as the abstract, author information, source package, and metadata.

`foundational_works/` is also a formally tracked category used for the most well-known and foundational papers. These papers do not have to be world-action model papers themselves, but they should be important for understanding the development and context of WAM methods. Like the other categories, it uses separate directories, separate entries, and local metadata for tracking. The difference is that it collects foundational work rather than mainline WAM/VAM papers.
