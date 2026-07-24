---
type: page
source: raw/2026/04_26/From_Flip_FET_to_Flip_3D_Integration_F3D_Maximizing_the_Scaling_Potential_of_Wafer_Both_Sides_Beyond_Conventional_3D_Integration.pdf
created: 2026-04-26
updated: 2026-04-26
tags:
  - 三维集成
  - Flip-FET
  - F3D
  - DSI
topics:
  - advanced-3d-integration
concepts:
  - flip-fet
  - flip-3d-integration-f3d
  - dual-sided-interconnects
  - multi-flipping-processes
entities:
  - peking-university
  - risc-v
---

<!-- markdownlint-disable-next-line MD013 -->
# From Flip FET to Flip 3D Integration (F3D): Maximizing the Scaling Potential of Wafer Both Sides Beyond Conventional 3D Integration

## 1. 文件信息（Metadata）

<!-- markdownlint-disable-next-line MD013 -->
- 文章标题：From Flip FET to Flip 3D Integration (F3D): Maximizing the Scaling Potential of Wafer Both Sides Beyond Conventional 3D Integration
- 原始文件路径：原始 PDF（仓库中未提供）
- 文件类型：PDF
- 来源：2025 IEEE Electron Devices Technology & Manufacturing Conference (EDTM)
- 作者 / 机构：Heng Wu 等，北京大学集成电路学院
- 时间：2025
- DOI：`10.1109/EDTM61175.2025.11040727`

## 2. 摘要（Summary）

本文提出 Flip 3D Integration（F3D），试图把三维晶体管堆叠、
双面互连、双面混合键合堆叠以及双面 Monolithic 3D 统一到同一条技术
路线中。论文以 32-bit [[topics/RISC-V|RISC-V]] 核为案例，说明在既有
[[topics/flip-fet|Flip FET]] 基础上，引入
[[topics/dual-sided-interconnects|双面互连]] 后，布线自由度提升，
核心面积可下降 6.8%，EDP 可改善 5.9%。作者进一步提出 Double Flips 与
Triple Flips 等多次翻转流程，以缓解热预算约束，并报告在 Triple
Flips 优化后，相比未优化方案可带来最高 3.2% 的 EDP 改善和 2.3%
的频率提升。

## 3. 研究背景与问题定义（Background & Problem）

- 研究背景：传统 Moore 缩放放缓后，先进逻辑继续向三维晶体管与三维互连方向演进。
- 目标问题：现有 3D 集成方案通常只充分利用晶圆单面，或在前后两面信号交换时依赖 STC / nTSV，带来面积和实现复杂度损失。
- 应用场景：高密度逻辑、逻辑与存储协同集成、双面混合键合堆叠，以及未来面向 3D IC 的系统级封装。

## 4. 核心内容（Core Content）

### 4.1 关键方法 / 模型

- 提出 [[topics/flip-3d-integration-f3d|F3D]]，
  把 3D 晶体管、双面互连、3D die stacking 与双面 M3D 组合起来。
- 在 [[topics/flip-fet|Flip FET]] 中采用 DSI 2.0，使输入引脚能够分布在
  frontside 与 backside 两侧。
- 提出 [[topics/multi-flipping-processes|Multi-Flipping 流程]]，
  包括 Single Flip、Double Flips、Triple Flips，用于在制造流程中重新安排
  高温步骤与金属互连形成顺序。

### 4.2 核心原理 / 机制

- DSI 2.0 的关键点是双面输出 pin 设计，使 FS 与 BS 的信号布线可相对独立，减少对 STC 或 nTSV 的依赖。
- Double Flips 通过在前后两面高温外延与金属栅形成之间重新排序，降低热预算冲突。
- Triple Flips 进一步把 FS / BS 的 MOL 与 BEOL 尽量放到 FEOL 完成之后，以支持更优互连材料组合。

### 4.3 数据与实验（如适用）

- 基准对象：基于 FFET 的 32-bit RISC-V 核，不含 cache，仅计算核心。
- 版图结果：相较仅前面布线方案，双面信号布线可实现约 6.8% 面积下降。
- 指标结果：作者报告 EDP 可改善 5.9%；在 Triple Flips 优化方案下，EDP 与频率可分别进一步改善最高 3.2% 与 2.3%。

## 5. 关键结论（Key Findings）

- 双面互连不只是用于 backside power delivery，也可以用于时序敏感信号与一般信号布线。
- F3D 的价值不在单一器件，而在于把器件、互连、键合与单片三维工艺纳入统一架构。
- Multi-Flipping 提供了一条相对制造友好的流程路径，使双面 M3D 与双面 die stacking 更可行。

## 6. 关键概念（Concepts）

- [[topics/flip-fet|Flip FET]]
- [[topics/flip-3d-integration-f3d|Flip 3D Integration (F3D)]]
- [[topics/dual-sided-interconnects|Dual-Sided Interconnects]]
- [[topics/multi-flipping-processes|Multi-Flipping Processes]]

## 7. 相关实体（Entities）

- 北京大学
- [[topics/RISC-V|RISC-V]]

## 8. 关联主题（Topics）

- [[topics/advanced-3d-integration|先进三维集成]]

## 9. 评估与思考（Analysis）

- 方法优点：论文把器件、布线与封装路径联动考虑，避免只优化单一层级。
- 局限性：当前给出的结果主要基于 block-level PPA 与流程设想，系统级制造复杂度和良率问题仍需更多实证。
- 潜在风险：双面工艺与多次翻转会放大流程控制、对准精度、热应力与材料兼容性的要求。

## 10. 参考与来源（References）

- 原始文件（仓库中未提供）
- [[topics/advanced-3d-integration|先进三维集成]]
