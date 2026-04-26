---
type: page
source: raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - 工艺
  - stacked-transistor
topics:
  - advanced-3d-integration
concepts:
  - flip-fet
  - complementary-fet-cfet
entities:
  - peking-university
---

# [[pages/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology|Process Development and Optimization of Flip FET (FFET) for Stacked Transistors Technology]]

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：Process Development and Optimization of Flip FET (FFET) for Stacked Transistors Technology
- 原始文件路径：[原始 PDF](../../../../raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf)
- 文件类型：PDF
- 来源：IEEE Transactions on Electron Devices
- 作者 / 机构：Wanyue Peng 等，[[entities/peking-university|北京大学]]
- 时间：2025
- DOI：`10.1109/TED.2025.3609731`

## 2. 摘要（Summary）

本文系统讨论 [[concepts/flip-fet|FFET]] 在工艺实现层面的关键问题，
覆盖 fin etch、wafer bonding and flipping、substrate thinning、
active fin profile 优化、热预算与金属污染等。作者把 FFET 进一步扩展到
nanosheet 版本，并提出 Double Flips / Triple Flips 等多次翻转流程，
以同时处理热预算与污染问题。文章最后从高纵横比工艺复杂度与电学表现两侧，
将 FFET 与 [[concepts/complementary-fet-cfet|Mono. CFET]] 做了较系统比较，
论证 FFET 在制造可行性上的优势。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：堆叠晶体管要从概念走向可制造技术，工艺流程稳定性比器件示意更关键。
- 目标问题：验证 FFET 的关键工艺是否真的比 Monolithic CFET 更友好，并找出主要风险点。
- 应用场景：FFET 基线工艺流开发、nanosheet 扩展、多次翻转流程设计。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 给出单次翻转 FFET 的基线工艺流，并逐项验证 bonding、flipping 和 thinning。
- 分析 BS fin 轮廓优化、热预算和金属污染问题。
- 提出 Double Flips / Triple Flips 以重新安排前后两面的制程顺序。

### 4.2 核心原理 / 机制

- FFET 通过把 n/p 器件放在晶圆两面来规避 Mono. CFET 的部分 HAR 垂直加工难题。
- 多次翻转流程的本质是重排高温与金属相关步骤，降低热预算冲突与污染风险。
- FFET 的工艺优势不仅是 fewer HAR steps，还包括流程顺序上的更大自由度。

### 4.3 数据与实验（如适用）

- 文中展示了 bonding、CMP stopping on STI、BS active reveal 等关键步骤的实验图像。
- 对比分析指出 FFET 在高 AR 相关集成挑战上明显轻于 Mono. CFET。
- 作者还讨论了不同翻转流程在复杂度、成本和 PP 之间的平衡。

## 5. 关键结论（Key Findings）

- FFET 的关键制造挑战是可管理的，且能通过流程重排获得更稳健的解决方案。
- Double Flips 在工艺复杂度、成本和性能之间提供了较好的平衡。
- 与 Mono. CFET 相比，FFET 的工艺友好性来自更少 HAR 负担和更灵活的双面流程。

## 6. 关键概念（Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/complementary-fet-cfet|Complementary FET (CFET)]]

## 7. 相关实体（Entities）

- [[entities/peking-university|北京大学]]

## 8. 关联主题（Topics）

- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：从工艺步骤而非只从器件示意解释 FFET 的真正可行性。
- 局限性：流程复杂度虽然更可控，但真实量产窗口、良率与缺陷密度仍需长期数据支撑。
- 潜在风险：双面流程引入的翻转、粘接与精确停止步骤，本身也会成为新的集成门槛。

## 10. 参考与来源（References）

- [原始文件](../../../../raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf)
- [[topics/advanced-3d-integration|先进三维集成]]
