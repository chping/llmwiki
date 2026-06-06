---
type: page
source: raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf
created: 2026-04-26
updated: 2026-04-26
status: needs-review
tags:
  - SRAM
  - 三维集成
  - memory-compiler
topics:
  - ffet-sram-design
  - advanced-3d-integration
concepts:
  - bipolar-sram
entities:
  - open-source-memory-compiler
---

<!-- markdownlint-disable-next-line MD013 -->
# [[pages/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler|3D SRAM Design & Optimization with Open Source Memory Compiler]]

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：3D SRAM Design & Optimization with Open Source Memory Compiler
- 原始文件路径：[原始 PDF](../../../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)
- 文件类型：PDF
- 来源：2024 International 3D Systems Integration Conference (3DIC)
- 作者 / 机构：Sunan Chen、Chao Wu、Yunlang Cai、Yuan Guan、Yuanqing Cheng
- 时间：2024
- DOI：`10.1109/3DIC63395.2024.10830085`

## 2. 摘要（Summary）

由于该 PDF 的正文文本提取失败，当前只能依据题目、元数据和主题词判断：
论文聚焦使用开源 memory compiler 来完成 3D SRAM 的设计与优化，
重点考察三维集成条件下的功耗、性能、面积（PPA）权衡，并尝试把
SRAM 编译器流程扩展到更适合 3D memory 结构的设计空间。
其中具体 bitcell 架构、阵列组织和实验数字仍需人工复核。 #needs-verification!

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：随着逻辑与存储协同三维集成加速，SRAM 设计需要同时面对布局、互连与热预算新约束。
- 目标问题：如何借助开源 memory compiler，把 3D SRAM 的结构探索与 PPA 优化流程自动化。
- 应用场景：三维存储宏设计、研究原型编译器、3D memory architecture 早期探索。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 使用开源 [[entities/open-source-memory-compiler|memory compiler]]
  作为 3D SRAM 设计与参数探索的基础平台。
- 以 3D integration 为约束，分析 SRAM 的功耗、性能与面积折中。

### 4.2 核心原理 / 机制

- 将二维 SRAM 编译流程扩展到三维结构时，需要同时考虑层间互连、
  阵列组织和外围电路映射。
- 编译器价值在于快速扫描设计空间，而不只是输出单一宏版图。

### 4.3 数据与实验（如适用）

- 元数据表明论文关键词覆盖 SRAM、Memory Compiler、3D Integration、PPA。
- 具体实验设置和定量结论当前无法可靠提取，需要二次复核。 #needs-verification!

## 5. 关键结论（Key Findings）

- 3D SRAM 设计已经开始从手工结构探索转向编译器驱动的自动化搜索。
- 开源 memory compiler 是把 3D SRAM 研究流程标准化的重要基础设施。

## 6. 关键概念（Concepts）

- [[concepts/bipolar-sram|Bipolar SRAM]]

## 7. 相关实体（Entities）

- [[entities/open-source-memory-compiler|Open Source Memory Compiler]]

## 8. 关联主题（Topics）

- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]
- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：编译器方法适合快速比较 3D SRAM 的组织与参数组合。
- 局限性：当前正文抽取失败，尚不能可靠判断论文是否聚焦 FFET、
  M3D 还是更一般的 3D SRAM 实现。 #needs-verification!
- 潜在风险：如果编译器模型未充分覆盖层间寄生与热效应，PPA 结论可能偏乐观。

## 10. 参考与来源（References）

- [原始文件](../../../../raw/2026/04_26/3D_SRAM_Design_amp_Optimization_with_Open_Source_Memory_Compiler.pdf)
- [[topics/ffet-sram-design|FFET 与 SRAM 设计]]
