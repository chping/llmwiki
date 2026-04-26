---
title: FFET
type: concept
created: 2026-04-26
updated: 2026-04-26
tags: [device, 3d-integration, dtco]
---

## 定义

`FFET` 可概括为一类前后双面器件与互连协同设计的工艺路线，核心特征
包括双面有源区、双面布线资源、跨面耦合与更强的 3D 集成兼容性。

## 本次资料补充

### 首次实验验证

2024 年 VLSI 论文将 FFET 描述为一种具备 self-aligned 双面有源区与
互连的堆叠晶体管技术。资料强调其工艺流在纵向集成上比单片
[[concepts/cfet|CFET]] 更具制造友好性，并建立了最小 `2.5T` 标准单元
库，验证了更进一步的标准单元压缩和布线可达性。
[First Experimental Demonstration of Self-Aligned Flip FET
\(FFET\): A Breakthrough Stacked Transistor Technology with 2.5T
Design, Dual-Side Active and
Interconnects](../../raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf)

### 设计收益

现有摘要显示，FFET 由于双面工艺带来的极性放置自由度，可支持 bipolar
SRAM，面积比 CFET SRAM 再缩小约 `12%`，比 FinFET SRAM 缩小至少
`35.9%`。在逻辑评估中，基于 fin 的 FFET 在等功耗下频率高约 `21.5%`，
在等频率下降功耗约 `45.0%`；RISC-V321 核心 P&R 结果相对 CFET
面积缩小超过 `31.3%`。这些指标来自论文摘要转述，后续若需要引用原图表，
应再回查正文。`#needs-verification`
[First Experimental Demonstration of Self-Aligned Flip FET
\(FFET\): A Breakthrough Stacked Transistor Technology with 2.5T
Design, Dual-Side Active and
Interconnects](../../raw/2026/04_26/First_Experimental_Demonstration_of_Self-Aligned_Flip_FET_FFET_A_Breakthrough_Stacked_Transistor_Technology_with_2.5T_Design_Dual-Side_Active_and_Interconnects.pdf)

### 工艺优化路径

2025 年 TED 论文将 FFET 的工程重点落在 fin etch、wafer bonding 与
flipping、substrate thinning、active fin profile、thermal budget 与
metal contamination，并将架构扩展到 nanosheet。同时提出
`Double Flips` 和 `Triple Flips` 以缓解热预算与污染顾虑，其中
`Double Flips` 被描述为在复杂度、成本和功率性能之间更均衡的选择。
[Process Development and Optimization of Flip FET \(FFET\) for Stacked
Transistors
Technology](../../raw/2026/04_26/Process_Development_and_Optimization_of_Flip_FET_FFET_for_Stacked_Transistors_Technology.pdf)

### 继续缩放到 A2

2025 年 VLSI 资料继续把 FFET 路线细分为 `F3ET`、`F4ET` 与 `CFFET`
等变体：`F3ET` 强调前后栅自对准，`F4ET` 在 forksheet 结构上引入
embedded power rail 以把单元高度压到 `2T`，`CFFET` 则尝试
ultra-stacked 4-tier 晶体管进一步压缩面积。摘要还指出，
`A3 HP F4ET` 在 `Vdd = 0.7 V` 下相对 `A14` fin-based FFET
等功耗性能提升约 `38.9%`，而 32-bit RISC-V 核心从 `A14` 到 `A5`
呈现 `44.9% / 49.8%` 的面积缩放和 `20.0% / 27.9%` 的频率提升。
`#needs-verification`
[PPA Scaling of Flip FET Technology Down to A2 Node Enabled by
Architecture Innovations: Self-Aligned Gate, 2T Design with Embedded
Power Rail and Ultra-Stacked 4-Tier
Transistors](../../raw/2026/04_26/PPA_Scaling_of_Flip_FET_Technology_Down_to_A2_Node_Enabled_by_Architecture_Innovations_Self-Aligned_Gate_2T_Design_with_Embedded_Power_Rail_and_Ultra-Stacked_4-Tier_Transistors.pdf)

### 变异与鲁棒性

overlay-aware 变异研究指出，FFET 在 backside lithography
misalignment 为 `4 nm` 时，等漏电频率下降约 `2.20%`，其中
`Drain Merge` 电阻是主要波动源。资料同时认为，只要设计规则优化到位，
FFET 的功率性能仍优于 CFET；只有 misalignment 达到 `8 nm`
这一近乎超规格场景时，优势才会被显著削弱。`#needs-verification`
[Overlay-aware variation study of flip FET and benchmark with
CFET](../../raw/2026/04_26/Overlay-aware%20variation%20study%20of%20flip%20FET%20and%20benchmark%20with%20CFET.pdf)

## 对 SRAM 的直接含义

- 更高的器件与布线密度，为更紧凑的 SRAM bitcell 与外围布局提供空间。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)
- 更复杂的制造对准、寄生与热问题，会直接映射到 SRAM 的稳定性、读路径速度和统计良率。[FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)
- 更适合按 `DTCO` 思路联合优化 bitcell、periphery、测试结构与 3D
  互连，而不是孤立地看单个器件收益。
  [FFET 工艺特点及对 SRAM 设计影响表格汇总](../../raw/2026/04_26/FFET工艺特点及对SRAM设计影响表格汇总.md)

## 关联页面

- [[concepts/cfet|CFET]]
- [[concepts/vfet|VFET]]
- [[topics/ffet-sram-design|FFET 对 SRAM 设计的影响]]
- [[topics/flip-3d-integration|Flip 3D Integration（F3D）]]
- [[topics/vfet-logic-scaling|VFET 逻辑缩放]]
- [[concepts/sram|SRAM]]
