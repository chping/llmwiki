---
type: page
source: raw/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - FFET
  - 变异
  - overlay
topics:
  - advanced-3d-integration
concepts:
  - flip-fet
  - complementary-fet-cfet
  - drain-merge
entities:
  - peking-university
---

# [[pages/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET|Overlay-aware Variation Study of Flip FET and Benchmark with CFET]]

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：Overlay-aware Variation Study of Flip FET and Benchmark with CFET
- 原始文件路径：[原始 PDF](../../../../raw/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET.pdf)
- 文件类型：PDF
- 来源：会议论文
- 作者 / 机构：Wanyue Peng 等，[[entities/peking-university|北京大学]]
- 时间：2025

## 2. 摘要（Summary）

本文围绕 [[concepts/flip-fet|FFET]] 的 backside lithography misalignment
开展 overlay-aware 变异研究，并与
[[concepts/complementary-fet-cfet|CFET]] 做功耗性能对比。作者发现，
在 0 到 4 nm 的合理失配范围内，FFET 的 iso-leakage 频率最多下降约 2.20%，
而主要变异来源并不是所有寄生一起恶化，而是
[[concepts/drain-merge|Drain Merge]] 电阻对 misalignment 极度敏感。
通过 DTCO 重新布置电源轨和增大相关几何裕量后，最坏频率下降可压到约 1.30%，
Monte Carlo 结果也显示分布标准差明显改善。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：FFET 虽能避开不少 CFET 的高 AR 工艺，但背面图形对准误差会引入独特变异。
- 目标问题：识别 misalignment 对 FFET 的主要影响路径，并评估其与 CFET 的真实差距。
- 应用场景：FFET 设计规则优化、variation-aware DTCO、库与标准单元稳健性评估。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 以 Misalignment Vector 描述背面对前面的偏移方向与大小。
- 采用 15-stage ring oscillator 在 iso-leakage、`VDD = 0.7 V` 下评估频率变化。
- 构造 DM-only 和 GM-only 模型来分离不同寄生变化来源。

### 4.2 核心原理 / 机制

- misalignment 会使 [[concepts/drain-merge|Drain Merge]] 和 Gate Merge
  与前面结构的落点偏离，造成寄生电阻变化。
- 其中 DM 电阻波动远大于 GM，因此成为主导频率退化的来源。
- 通过重新安排电源轨位置并给 Drain Merge 留出更大工艺裕量，可以明显抑制变异。

### 4.3 数据与实验（如适用）

- 在 4 nm misalignment 下，最坏频率下降约 2.20%。
- 设计规则优化后，最坏频率下降改善到约 1.30%。
- Monte Carlo 10,000 次实验显示频率标准差可进一步下降约 19.7%。

## 5. 关键结论（Key Findings）

- FFET 的 overlay variation 是真实问题，但并未大到抵消其系统级优势。
- Drain Merge 是 FFET variation-aware DTCO 的第一优先级结构。
- 在合理对准范围内，FFET 相比 CFET 仍保持竞争力。

## 6. 关键概念（Concepts）

- [[concepts/flip-fet|Flip FET]]
- [[concepts/complementary-fet-cfet|Complementary FET (CFET)]]
- [[concepts/drain-merge|Drain Merge]]

## 7. 相关实体（Entities）

- [[entities/peking-university|北京大学]]

## 8. 关联主题（Topics）

- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：把变异问题落实到具体寄生结构，而不是停留在抽象“overlay 风险”层面。
- 局限性：本文只考虑部分器件与寄生通路，对 intrinsic device variation 仍有留白。
- 潜在风险：若未来 FFET 导入更复杂标准单元与 SRAM，DM 波动会进一步与统计尾部耦合。

## 10. 参考与来源（References）

- [原始文件](../../../../raw/2026/04_26/Overlay-aware_variation_study_of_flip_FET_and_benchmark_with_CFET.pdf)
- [[topics/advanced-3d-integration|先进三维集成]]
