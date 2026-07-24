---
category: topic
created: 2026-07-24
updated: 2026-07-24
tags:
  - SRAM
  - memory-compiler
  - memory-IP
  - DFT
summary: SRAM Memory Compiler 的容量配置、阵列组织、低功耗、测试冗余、交付视图及选型签核说明。
zotero:
  item_key:
  citation_key:
source_uri: /Users/chengping/workspace/obsync/2-Subject/OpenXRAM/pub/SRAM存储器编译器常见功能和配置项说明_补全修订版.md
---

# SRAM Memory Compiler 功能与配置

> 本文以同步嵌入式 SRAM Memory Compiler 为主要对象，介绍常见配置项、内部结构、低功耗模式、DFT/冗余功能及交付文件。
>
> 不同 Foundry、IP 厂商和 Compiler 产品对选项名称、控制引脚、有效电平、进入/退出时序及功能边界的定义可能不同。本文给出的是行业通用含义；项目签核必须以对应版本的 Compiler User Guide、Macro Databook、Liberty 模型和 Verilog 模型为准。
>
> 原文引用的若干相对路径图片未随 Markdown 文件一同提供，本版使用公式、表格和文本示意图补足其表达。

---

## 1. 基本术语和容量关系

### 1.1 常用符号

| 符号或名称 | 含义 | 说明 |
| --- | --- | --- |
| `WD`、`NW`、`Depth`、`D` | Word Depth / Number of Words | 逻辑字深，即可寻址的 Word 数量 |
| `WW`、`NB`、`BPW`、`Width`、`W` | Word Width / Number of Bits per Word | 逻辑字宽，即一次访问的数据位数 |
| `CM`、`MUX`、`M` | Column Mux Ratio | 每个逻辑 I/O 复用的物理列数 |
| `B` | Number of Banks | 内部 Bank 数量 |
| `R` | Physical Rows per Bank | 每个 Bank 的物理字线数量 |
| `C` | Physical Bit-cell Columns per Bank | 每个 Bank 的物理 Bit-cell 列数量 |
| `WL` | Word Line | 字线，激活一行 BitCell 的访问管 |
| `BL/BLB` | Bit Line / Complementary Bit Line | 差分位线对，用于传递读写信号 |
| `SA` | Sense Amplifier | 感应放大器，将微小位线差分放大为全摆幅逻辑值 |
| `WDV` | Write Driver | 写驱动器，将写入数据转换为位线驱动 |

SRAM 的逻辑容量为：

\[
\text{Capacity}_{bit}=D\times W
\]

若字宽是 8 的整数倍，则字节容量为：

\[
\text{Capacity}_{byte}=D\times W/8
\]

在常见的“按深度划分 Bank、按列复用折叠阵列”的结构中，且 `D` 可被 `B×M` 整除时：

\[
R=\frac{D}{B\times M}
\]

\[
C=W\times M
\]

因此全部 Bank 的有效 BitCell 数量满足：

\[
B\times R\times C=D\times W
\]

实际物理阵列还可能加入冗余行、冗余列、ECC/Parity 位、Dummy Cell、Replica Cell 和边界单元，因此物理 BitCell 数量通常大于逻辑容量。

> **重要说明**：上述 Bank 公式适用于常见的按地址深度切分方式；部分 Compiler 会按宽度切分、采用不对称 Bank、共享或复制外围电路，因此最终结构应以 Compiler 报告和版图为准。

### 1.2 地址位宽

外部逻辑地址位宽为：

\[
A=\lceil\log_2 D\rceil
\]

当 `D`、`B`、`M` 都是 2 的幂并采用常见内部划分时：

\[
A=\log_2 B+\log_2 R+\log_2 M
\]

其中三部分分别用于 Bank 选择、物理行选择和 Column Mux 选择。增大 Column Mux 只会把一部分内部行地址转换为列选择地址，**不会减少 SRAM 的外部逻辑地址位宽**。

字深不一定必须是 2 的幂。若 Compiler 支持非 2 的幂深度，则地址总线仍取 `ceil(log2(D))` 位，多出的地址编码可能被定义为非法地址、输出未知值，或者映射到物理填充行，具体行为必须查看模型说明。

### 1.3 物理字线和位线

- **Word Line（WL）**：行译码器激活一条物理字线，使该行所有 BitCell 的访问晶体管导通。
- **Bit Line（BL/BLB）**：每个物理 BitCell 列通常对应一对差分位线，读操作通过微小差分传递数据，写操作由写驱动器强制位线状态以翻转存储节点。
- **Column Mux**：在若干物理列之间选择一列或一组列并连接到 Sense Amplifier/Write Driver。位线本身不承担地址译码功能。

### 1.4 示例

假设一个 SRAM 为 `128 × 2`，Column Mux 为 8，单 Bank：

- 逻辑字深 `D = 128`
- 逻辑字宽 `W = 2`
- Column Mux `M = 8`
- 物理行数 `R = 128 / 8 = 16`
- 物理列数 `C = 2 × 8 = 16`
- 外部地址位宽为 7 位，其中内部行地址 4 位、Column Select 3 位

假设一个 SRAM 为 `4096 × 32`，Column Mux 为 16，单 Bank：

- 物理行数 `4096 / 16 = 256`
- 物理列数 `32 × 16 = 512`
- 外部地址位宽为 12 位，其中内部行地址 8 位、Column Select 4 位

若相同逻辑 SRAM 进一步划分为 4 个按深度切分的 Bank，则常见结构为：

- 每个 Bank 的物理行数 `4096 / (4 × 16) = 64`
- 每个 Bank 的物理列数仍为 `512`
- 内部地址可分为 Bank Select 2 位、Row Address 6 位、Column Select 4 位

---

## 2. Instance Name

该配置用于指定生成 SRAM Macro 的实例或 Cell 名称。命名应尽量反映端口类型、字深、字宽和关键选项，以便 RTL、STA、PnR、LVS、仿真及版本管理使用同一个标识。

推荐命名形式：

```text
<type>_<port>_<depth>x<width>_m<mux>_b<bank>_<flavor>_<options>
```

示例：

```text
sram_1rw_4096x32_m16_b2_hd_pg_bw
```

可表达：单读写端口、4096 Word、32 bit、CM16、2 Banks、High Density、Power Gating、Byte Write Mask。

命名建议：

- 使用字母、数字和下划线，避免空格、连字符及 EDA 工具不接受的特殊字符。
- 以字母或下划线开头，以兼容 Verilog 标识符规则。
- 不建议把 PVT Corner 写入逻辑 Cell 名，因为同一 Macro 的不同 `.lib` Corner 应保持相同 Cell 名和引脚名；Corner 可写入文件名或目录名。
- 对 Power Gating、Retention、Pipeline、Write Through、Write Mask、Redundancy 等会改变接口或功能模型的选项，应体现在命名或版本元数据中。
- Cell 名、LEF Macro 名、Liberty Cell 名、Verilog Module 名、GDS Top Cell 名和 LVS Netlist Subckt 名必须一致，除非交付说明明确给出映射关系。

---

## 3. BitCell

BitCell 是 SRAM 阵列中存储 1 bit 数据的最小核心单元。Compiler 的不同产品系列通常使用不同 BitCell，以优化密度、速度、低压稳定性、漏电或多端口能力。用户通常是在不同 Compiler Flavor 之间选择，而不是在同一个 Compiler 内任意更换晶体管级 BitCell。

### 3.1 常见 BitCell 类型

| 类型 | 典型特点 | 主要优势 | 主要代价 |
| --- | --- | --- | --- |
| 6T Single-Port Cell | 两个交叉耦合反相器和两个访问管 | 面积小、密度高、应用最广 | 读稳定性和写能力存在固有权衡，低压设计难度较高 |
| 8T Read-Decoupled Cell | 增加独立读通路，读节点与存储节点隔离 | 读稳定性高、适合低压或多读端口 | 面积和读位线外围开销增加 |
| 10T/12T Low-Voltage Cell | 采用差分隔离、Schmitt Trigger 或额外控制管 | 更低 Vmin、更好的读写裕量 | 面积、漏电或控制复杂度增加 |
| Dual-Port / Multi-Port Cell | 为多个端口增加独立访问通路 | 支持并发访问 | 面积显著增加，并需定义端口冲突行为 |

晶体管数量与端口定义没有唯一对应关系；不同厂商的 8T、10T 或 12T 拓扑可能实现不同功能。

### 3.2 常见 Compiler Flavor

| Flavor | 含义 | PPA 倾向 |
| --- | --- | --- |
| HD / HDE | High Density | 面积最小，速度通常较低 |
| HS / HC / HPC | High Speed / High Current / High Performance | 速度较高，面积和动态功耗通常较大 |
| LP | Low Power | 降低动态功耗或漏电，性能可能受限 |
| ULP / ULL | Ultra-Low Power / Ultra-Low Leakage | 强调休眠漏电和低功耗，访问速度通常更慢 |
| Wide-Voltage / Low-Vmin | 宽电压范围或低压优化 | 低电压稳定性较好，面积或高压性能可能受影响 |

这些缩写没有统一行业标准，必须以具体产品手册的定义为准。

### 3.3 BitCell 选择原则

- L1 Cache、高频 Buffer 和关键路径上的 SRAM 通常优先考虑高速 Flavor。
- 大容量 LLC、图像缓存或面积受限存储通常优先考虑高密度 Flavor。
- Always-On、IoT 和电池供电场景应关注低漏电 BitCell、Retention 电压和低功耗模式。
- 低压工作时不能只比较典型速度，还应比较读稳定性、写入能力、Hold Vmin、Read Vmin、Write Vmin 和统计失效率。
- BitCell Flavor 与外围电路 Vt 选项是两个不同维度；“高密度 BitCell + LVT Periphery”或“高速 BitCell + Mixed-Vt Periphery”都可能存在。

---

## 4. Frequency

### 4.1 Compiler 中的 Frequency 配置含义

部分 SRAM Compiler 会要求输入目标工作频率或目标 Cycle Time。该参数通常用于以下一种或多种用途：

- 选择内部 Bank、Segment、Column Mux、Decoder、输出驱动和 Pipeline 结构。
- 评估目标配置能否满足所选 PVT 下的最小时钟周期。
- 根据切换电流估算电源环宽度、Power Mesh、Pin 数量或 EM/IR 需求。
- 生成与目标使用场景匹配的功耗报告或筛选可用配置。
- 对某些 Compiler，目标频率只用于报告和电源规划，不改变 SRAM 的逻辑功能。

因此，SRAM 的工作频率**可以作为 Compiler 的设计约束输入**，但它通常不是 SRAM 内部可编程的运行频率。生成后的 SRAM 由 SoC 外部时钟驱动，允许频率由 `.lib`、Databook 和 PVT 条件共同限定。

若 Compiler 没有 Frequency 输入项，用户应通过以下方式判断能否满足系统频率：

1. 读取目标 PVT Corner 下的 `.lib`。
2. 检查最小 Clock Period、Clock Pulse Width、Address/Data/Control Setup/Hold、Clock-to-Q 和 Recovery/Removal 约束。
3. 在 SoC STA 中加入真实的 Clock Slew、输出负载、OCV 和互连延迟。

### 4.2 Frequency 与功耗

频率不能单独确定 SRAM 功耗。动态功耗的近似关系为：

\[
P_{dynamic}\approx \alpha C_{eff}V^2f
\]

其中：

- `α` 为访问率、读写比例、地址和数据翻转率等形成的活动因子；
- `Ceff` 受容量、Mux、Bank、位线长度、输出负载、写掩码和内部结构影响；
- `V` 为工作电压；
- `f` 为时钟频率。

总功耗还包括漏电功耗、待机功耗、Retention 功耗和 Power Mode 切换能量。相同频率下，连续读写、低活动率访问和 Clock Gating 后的功耗会有明显差异。

---

## 5. Clock Frequency (worst-case)

Worst-Case Clock Frequency 指在指定最差时序 Corner、输入 Slew、输出负载、工作模式和约束条件下，SRAM 能满足全部时序要求的最高时钟频率。可近似表示为：

\[
f_{max,macro}=\frac{1}{t_{CYC,min}(P,V,T,load,slew,mode)}
\]

其中 `tCYC,min` 是 Macro 的最小时钟周期。实际限制可能来自：

- 读访问周期和 BitLine 恢复时间；
- 写入脉宽和写恢复时间；
- 时钟高、低电平最小脉宽；
- 内部 Self-Timing 路径；
- 输出 Pipeline 或 Write-Through 路径；
- Power Mode 唤醒后的 Recovery Time；
- 输入 Slew 和输出负载；
- PVT、局部失配、全局 OCV/AOCV/POCV 及老化裕量。

“最大容量 Instance 在最差 PVT 下的频率”可以作为某个 Compiler 产品族的基准指标，但不能替代具体 Instance 的时序模型。最大容量实例通常更慢，但由于 Bank、Mux 和 Pipeline 架构不同，容量与最高频率不一定单调对应。

系统可用频率还需满足 SRAM 之外的数据路径：

\[
T_{CLK}\ge t_{CQ,SRAM}+t_{logic}+t_{setup,next}+t_{uncertainty}
\]

因此，Macro Fmax 与 SoC 最终 Fmax 是相关但不同的指标。

---

## 6. Capacity Range

Capacity Range 定义 Compiler 支持的字深、字宽、总容量、Mux、Bank 以及步长范围。常见限制包括：

- 最小和最大 Word Depth。
- 最小和最大 Word Width。
- 总 Bit 数上限。
- Depth/Width Granularity，即可选数值的步长。
- Column Mux 的合法集合，例如 1、2、4、8、16，部分产品支持 32。
- Bank 数量的合法集合。
- Write Mask、Redundancy、Pipeline 或 Power Gating 对容量范围的附加限制。

### 6.1 Step / Granularity

`Step` 或 `Granularity` 表示参数只能按指定步长变化。例如：

- Depth Range：64～8192，Step 64，表示可选 64、128、192……
- Width Range：8～256，Step 8，表示字宽必须是 8 的整数倍。
- Bit Write 打开后，Width 可能允许 1-bit 步长；Byte Write 打开后，通常要求 Width 是 8 的整数倍。

Granularity 来自 BitCell 拼接、I/O Slice、Mux Group、Power Grid 和版图规则，不能只由逻辑容量推导。

### 6.2 Bank 与 Segment

- **Bank**：具有独立选择逻辑的内部阵列分块，常用于缩短 WordLine/BitLine、改善速度和峰值电流，也可支持局部 Power Gating 或冗余。内部多 Bank 不等于外部多端口；若只有一个外部端口，通常仍然每周期只能访问一个地址。
- **Segment**：在一个 Bank 内进一步将长 WordLine、BitLine 或全局数据线划分为局部段，并通过层次化驱动和选择连接。Segment 通常对外部地址不可见，也不一定可独立访问或断电。

---

## 7. Word Depth (WD) / Number of Words (NW)

Word Depth 表示逻辑上可寻址的 Word 数量，也称字深或字数。建议不要将其称为“字长”，因为“字长”通常用于描述每个 Word 的位数，容易与 Word Width 混淆。

- 逻辑地址空间为 `0` 到 `D-1`。
- 地址位宽为 `ceil(log2(D))`。
- 当 `M > 1` 或 `B > 1` 时，Word Depth 不等于单个物理阵列的 WordLine 数量；在常见结构中，单 Bank 的物理 WordLine 数量为 `D/(B×M)`。
- 增大 Word Depth 通常增加容量，并可能增加 BitLine 长度、译码级数和漏电，但 Compiler 可通过 Mux、Bank、Segment 重新组织物理阵列。
- 非 2 的幂 Word Depth 是否支持、非法地址如何处理，应查看 Verilog 模型和 Databook。

---

## 8. Word Width (WW) / Number of Bits per Word (NB or BPW)

Word Width 表示一次逻辑读写操作处理的数据位数。

- 字宽决定 `D`、`Q` 和 Write Mask 等数据总线的宽度。
- 字宽越大，通常需要更多 I/O Slice、Sense Amplifier、Write Driver 和输出驱动，并会增加 WordLine 负载和瞬时电流。
- 字宽**不要求是 2 的幂**。许多 Compiler 支持任意整数位宽或指定 Granularity，例如 1、4、8 或 16 bit 步长。
- 若使用 Byte Write Mask，字宽通常要求按 8 bit 分组；若支持最后一个不完整 Byte，则行为需查看手册。
- 若 Macro 内置 ECC，物理阵列还会加入校验位，物理列宽大于用户可见的 Word Width。

例如 `1K × 8` 表示 1024 个 Word，每个 Word 8 bit，总容量为 8192 bit，即 8 Kbit 或 1 KiB。

---

## 9. Column Mux

Column Mux 是 SRAM 阵列组织的核心参数。对于每个逻辑输出 bit，Column Mux 从 `M` 个物理列中选择一个，将其连接到对应的 Sense Amplifier 或 Write Driver。

在单 Bank 的常见结构中：

```text
逻辑组织：D rows × W bits
              |
              | Column Mux = M
              v
物理组织：(D/M) wordlines × (W×M) bitcell columns
```

例如 `64 × 8`：

| Column Mux | 物理行数 | 物理列数 | 形状趋势 |
| ---: | ---: | ---: | --- |
| 1 | 64 | 8 | 高而窄 |
| 2 | 32 | 16 | 高度下降、宽度增加 |
| 4 | 16 | 32 | 更矮、更宽 |
| 8 | 8 | 64 | 很矮、很宽 |

### 9.1 内部地址拆分

若 `M = 2^k`，则低 `k` 位地址常用作 Column Select，其余地址用于 Bank/Row Decode。增大 M 后：

- 内部 Row Address 位数减少；
- 内部 Column Select 位数增加；
- 外部逻辑地址位宽保持不变。

### 9.2 对尺寸和 PPA 的影响

增大 Column Mux 通常会：

- 减少物理行数，缩短 BitLine，降低 BitLine RC；
- 增加物理列数，延长 WordLine，增加 WordLine 负载；
- 增加 Column Select 和 Mux 网络的复杂度；
- 改变 Sense Amplifier、Write Driver 和列外围电路的布局匹配关系；
- 使 Macro 趋向“更矮、更宽”。

其对速度、面积和功耗没有统一的单调关系：

- 较短 BitLine 通常有利于读速度和低压感应；
- 较长 WordLine、更大的 Mux 负载可能抵消甚至超过 BitLine 收益；
- BitCell 总面积近似不变，但外围电路、空白区、Power Grid 和布线效率会改变；
- 预充电的总电容、被激活的物理列数量和 Mux 切换功耗相互作用，因此动态功耗可能升高或降低。

Compiler 通常通过 Characterization 选择若干离散的合法 Mux 值，用户应比较真实生成结果，而不是仅依据“Mux 越大越快”或“Mux 越大面积越大”的简单规则。

### 9.3 选择建议

- 优先使用 Compiler 推荐或 PPA 排名靠前的 Mux。
- 在 Floorplan 受限时，可通过 Mux 调整 Macro 宽高比。
- 对高频目标，应同时比较 `tCYC`、`tCQ`、最小脉宽和功耗，而不是只比较 Row Decoder 延迟。
- 对低功耗目标，应检查读、写能量和 Peak Current，而不是只看平均功耗。
- 若 `D` 不能被 `M` 整除，Compiler 可能拒绝配置、增加填充行或使用非均匀结构。

---

## 10. Banks

随着单一阵列变大，WordLine、BitLine、全局数据线和控制线的 RC 负载都会增加。将逻辑 SRAM 分成多个 Bank 可以缩短局部连线，并在面积、性能和功耗之间进行优化。

### 10.1 Bank 的主要作用

- 缩短 WordLine 和 BitLine，改善访问时间和低压稳定性。
- 降低单次访问时被激活的阵列规模和峰值电流。
- 支持更灵活的 Macro 宽高比。
- 为局部 Power Gating、Retention、冗余和测试提供结构基础。
- 在外部接口明确支持时，可提供并行访问能力。

### 10.2 Bank 的代价

- 需要 Bank Decoder、局部 Precharge、局部 Sense Amplifier、Write Driver 或全局数据 Mux。
- 外围电路重复会增加面积和漏电。
- 跨 Bank 的全局数据线和控制线会引入额外延迟。
- 冗余通常按 Bank 分配，某个 Bank 的 Spare 不能自动修复另一个 Bank 的缺陷。
- 多 Bank 可能使电源网络和 IR Drop 分布更复杂。

### 10.3 内部 Bank 与多端口的区别

内部有多个 Bank 并不自动意味着 SRAM 可以在同一周期访问多个地址。只有当 Macro 对外提供独立端口、独立时钟或明确的 Banked Interface 时，系统才可以并行访问。普通单端口多 Bank SRAM 仍然只有一个逻辑访问端口。

---

## 11. Center Decode

Center Decode 通常指把 Row Decoder 或主地址/控制驱动放置在阵列中部，将阵列分为左右两半或上下两半，并从中心向两个方向驱动 WordLine 或局部控制线。

```text
Edge Decode：
[Decoder]====================[Array]
          较长 WordLine

Center Decode：
[Half Array]==========[Decoder]==========[Half Array]
             两侧 WordLine 约为原长度的一半
```

主要优点：

- 缩短最坏 WordLine 长度和 RC 延迟；
- 减小远端与近端 Cell 的延迟差异；
- 有利于高频、大字宽或低压 SRAM；
- 可改善控制线负载和局部电源分布。

主要代价：

- 中央 Decoder/Control Channel 占用阵列面积；
- 需要对称布线和更多局部驱动；
- 可能使 Macro 宽度或高度增大；
- 版图与冗余结构更复杂。

Center Decode 通常是物理实现选项，对逻辑接口透明。部分厂商也可能用该名称表示更广义的中央控制 Spine，应通过版图预览和 Compiler 手册确认具体含义。

---

## 12. Power Gating

Power Gating 通过关闭阵列或外围电路的电源、施加源极偏置或降低 Retention 电压，减少待机漏电。SRAM 的低功耗状态必须同时考虑数据是否保留、供电域状态、唤醒时间、输出状态和进入/退出时序。

### 12.1 通用功耗状态

| 状态 | BitCell Array | Periphery | 数据保持 | 访问能力 | 唤醒时间趋势 | 漏电趋势 |
| --- | --- | --- | --- | --- | --- | --- |
| Active | On | On | 是 | 可读写 | 无 | 最高 |
| Standby / ME Off | On | On，但无切换 | 是 | 不访问 | 极短 | 较高 |
| LS / Light Sleep | On 或轻度偏置 | 部分关闭或强门控 | 通常是 | 不可访问 | 短 | 中等 |
| DS / Deep Sleep / Retention | Retention 电压或强偏置 | Off | 通常是 | 不可访问 | 较长 | 较低 |
| SD / Shutdown | Off | Off | 否 | 不可访问 | 最长 | 最低 |

名称和具体电路并不统一。有些产品将 `Deep Sleep` 定义为数据保持模式，也有产品使用单独的 `Retention` 引脚；项目必须使用对应 Databook 的状态表。

### 12.2 进入与退出低功耗模式的一般要求

1. 等待当前读写周期完成，并将 Memory Enable/Chip Enable 置为非活动状态。
2. 按手册要求停止或保持时钟，避免在模式切换期间产生访问。
3. 按规定顺序控制 Sleep、Retention、Power Switch 和 Isolation 信号。
4. 在 Retention 模式下维持规定的 Array/Retention 电压，不得低于数据保持电压。
5. 唤醒后等待 `tWAKE`、`tRECOVERY` 或规定的若干时钟周期，再发起访问。
6. 低功耗和恢复期间的 `Q` 可能保持、被 Clamp、输出高阻或变为 `X`，应以 Verilog 模型和 Databook 为准。
7. 多个功耗模式控制信号通常要求互斥；同时激活可能是非法状态。

### 12.3 Break-Even Time

Power Gating 存在进入和唤醒能量。只有休眠时间足够长时，节省的漏电能量才超过模式切换能量：

\[
t_{break-even}\approx\frac{E_{entry}+E_{wake}}{P_{standby}-P_{sleep}}
\]

系统电源管理策略应根据实际空闲时长选择 Standby、Light Sleep、Retention 或 Shutdown。

### 12.4 与 UPF 和物理实现的关系

- 若 Macro 内置 Power Switch，用户主要连接控制引脚和电源网；若无内置 Switch，则 SoC 需要外部 Power Gating Cell 和 UPF 策略。
- Retention 与 Periphery-Off 模式通常需要 Isolation/Clamp 规则。
- 不同供电域应在 UPF 中声明 Supply Set、Power State、Isolation 和 Power Sequence。
- Macro 的 Power Ring、Pin、IR/EM 和 Inrush Current 必须按最大活动和唤醒电流签核。

---

## 13. LS - Light Sleep

Light Sleep 是介于 Standby 和 Deep Sleep 之间的低功耗模式，典型目标是以较小的唤醒延迟换取部分漏电降低。

常见实现包括：

- 关闭 Precharge、Sense Amplifier、Decoder 和内部时钟等外围活动；
- 对部分外围供电进行 Power Gating；
- 对 BitCell 或外围施加轻度 Source Bias；
- 保持 Array 在标称电压或接近标称电压，因此数据通常保留。

典型特点：

- 不允许读写；
- 数据通常保持；
- 唤醒时间通常为零到少数时钟周期；
- 漏电低于 Standby，但通常高于 Deep Sleep/Retention；
- 进入和退出时序必须满足专用 Timing Arc。

---

## 14. DS - Deep Sleep

Deep Sleep 通常是数据保持型的深度低功耗模式。常见实现为：

- 关闭大部分或全部 Periphery；
- 将 BitCell Array 保持在 Retention Voltage；
- 启用更强的 Source Bias 或内部 Header Switch；
- 仅保留维持存储状态所需的电源路径。

典型特点：

- 数据通常保留，但必须满足 Retention Voltage、PVT 和模式持续条件；
- 无法读写；
- 漏电明显低于 Light Sleep；
- 唤醒时间更长，并可能有较大的 Inrush Current；
- 唤醒后必须等待内部电源和 Self-Timing 电路稳定。

若具体 Compiler 将 Deep Sleep 定义为非保持状态，应以其状态表为准，不能仅凭名称判断。

---

## 15. SD - Shut Down

Shutdown 通常关闭 BitCell Array 和 Periphery 的电源，以获得最低漏电。

典型特点：

- 存储数据丢失；
- 输出在关闭或恢复期间通常无效；
- 唤醒时间最长；
- 唤醒后软件或硬件必须重新初始化内容；
- 需要严格的 Power-Up、Isolation、Reset 和 Clock Sequence；
- 适用于长时间不用且内容可重建的 SRAM。

SRAM 在正常上电后通常没有确定的初始内容，除非产品明确支持初始化、ROM 化或上电清零功能；RTL 仿真中应把未初始化内容视为未知值。

---

## 16. Dual Rail

Dual Rail SRAM 将 BitCell Array/Core 与 Periphery 连接到不同的电源域。常见命名包括：

- Array/Core Supply：`VDDM`、`VDDC`、`VDD_ARRAY`；
- Periphery Supply：`VDDP`、`VDDPE`、`VDD_PERI`；
- Ground 可能共用，也可能有独立地网。

### 16.1 主要用途

- 在低功耗状态关闭 Periphery，同时保持 Array 数据。
- 对 Array 和 Periphery 使用不同电压，以优化 Vmin、速度或功耗。
- 支持 DVFS、Retention 和 Always-On 架构。
- 隔离高切换外围电流与敏感 BitCell 供电。

### 16.2 设计约束

- 两个 Rail 的合法电压范围和相对大小由 Compiler 定义，不能任意组合。
- 若两个 Rail 电压不同，Macro 内部必须存在适当的电平转换、Clamp 或电源选择电路；用户不能假设任意压差都被支持。
- 必须遵守 Power-Up、Power-Down 和 Retention Sequence。
- PnR 和 UPF 中应建立独立的电源网络，并分别进行 IR Drop、EM 和 Inrush 分析。
- Liberty 文件中的 `pg_pin`、Operating Condition 和 Power State 必须与连接方式一致。
- 测试模式、Assist 和 Margin Control 可能对两个 Rail 有额外限制。

---

## 17. Periphery Off

Periphery Off 指关闭 Decoder、Precharge、Sense Amplifier、Write Driver、Clock/Control Logic 和 Output Driver 等外围电路，而 BitCell Array 仍保持供电。

典型行为：

- 数据保留；
- 不可读写；
- 输出需要隔离或由系统忽略；
- 唤醒时先恢复 Periphery 电源，等待内部偏置、时钟和 Self-Timing 稳定，再允许访问；
- 漏电低于普通 Standby，具体节省比例取决于 Array 和 Periphery 的漏电占比。

Periphery Off 常与 Dual Rail 配合，也可以由 Macro 内部 Power Switch 实现。

---

## 18. ME-Gating

ME-Gating 通常表示 Memory Enable Gating，即在 Memory Enable/Chip Enable 非活动时，门控 SRAM 内部时钟和动态控制路径，避免不必要的 Precharge、Decoder、WordLine、Sense Amplifier 和输出翻转。

其本质通常是**活动门控或时钟门控**，与切断电源的 Power Gating 不同：

| 特性 | ME-Gating | Power Gating |
| --- | --- | --- |
| 主要降低 | 动态功耗 | 漏电功耗，部分情况下也降低动态功耗 |
| 是否切断电源 | 通常否 | 是或降低电压/施加偏置 |
| 数据保持 | 是 | 取决于模式 |
| 唤醒延迟 | 通常极短 | 从短到很长 |
| 是否需要电源时序 | 通常不需要 | 需要 |

设计要点：

- `ME/CE` 必须满足相对时钟的 Setup/Hold 要求。
- 测试和 MBIST 模式通常需要绕过或强制打开 Gating。
- ME-Gating 不会显著消除 BitCell 和 Periphery 的静态漏电。
- 某些厂商可能对 “ME-Gating” 使用不同定义，应核对其端口和状态表。

---

## 19. BIST Interface

BIST Interface 用于把 SRAM 连接到 SoC 级 Memory BIST（MBIST）控制器、Scan/DFT 网络或外部测试逻辑。它不一定意味着 Macro 内部集成了完整 BIST 算法控制器。

### 19.1 常见架构

```text
Functional Logic ----\
                      >-- Test Mux --> SRAM Port
MBIST Controller ----/
```

Compiler 可提供：

- Functional/Test 输入 Mux；
- Test Enable、Test Mode、BIST Clock；
- 测试地址、测试数据、读写使能、Write Mask；
- 测试数据输出或 Compare 输出；
- Scan Capture/Scan Shift 接口；
- Redundancy Repair 数据装载接口；
- Retention、Read Disturb、Margin 或 Assist 测试控制。

### 19.2 MBIST 的作用

SoC 级 MBIST 控制器可执行 March C-、March SS、Checkerboard、Walking 1/0、Retention、Read Disturb 等算法，用于检测：

- Stuck-at Fault；
- Transition Fault；
- Address Decoder Fault；
- Coupling Fault；
- Read/Write Disturb；
- Retention Fault；
- 部分动态和时序相关故障。

具体故障覆盖率取决于算法、端口能力和测试时钟，不能仅由“有 BIST Interface”推断。

### 19.3 与 BISR/Redundancy 的关系

若 Macro 有 Row/Column/IO Redundancy，MBIST 可与 Built-In Self-Repair（BISR）配合：

1. MBIST 定位故障地址或 I/O；
2. Repair Analysis 选择 Spare Row/Column/IO；
3. Repair Signature 写入 eFuse、OTP、NVM 或可加载寄存器；
4. 上电时 Macro 或 SoC 装载 Repair 信息并重映射地址。

BIST 用于检测，Redundancy/BISR 用于修复，两者是不同功能。

### 19.4 集成注意事项

- 测试控制信号必须满足专用时序和静态约束。
- 测试时通常关闭普通 Power Gating 或按测试规范进入指定状态。
- At-Speed MBIST 时钟不得超过 Macro 的测试模式频率限制。
- Functional 和 Test 模式切换期间不得发生有效访问。
- ATPG/MBIST 使用的接口模型必须与实际 Macro 选项一致。

---

## 20. Self Time Bypass

同步 SRAM 常采用 Self-Timing 电路，根据 Replica/Dummy WordLine、Replica BitLine 或匹配延迟路径生成内部 WordLine 关闭、Sense Amplifier Enable、Write Completion 和 Precharge Restore 时序，以跟踪 PVT 变化。

Self Time Bypass 不是统一标准名称，常见含义是：

- 绕过正常的 Replica/Dummy Self-Timing 路径；
- 由外部 Test Pin、测试时钟或替代的固定延迟路径控制内部读写脉冲；
- 增强 ATE、MBIST、失效分析、Vmin Characterization 或 Debug 的可控性；
- 在特定测试模式下直接观察或扫描内部时序边界。

使用限制：

- 通常属于测试功能，不用于正常 Functional Mode。
- Bypass 后的读写时序可能不再自动跟踪 PVT，过短会造成读写失败，过长可能增加功耗、Read Disturb 或可靠性风险。
- 普通 Functional `.lib` 的时序保证通常不适用于 Bypass Mode，应使用专用 Test Specification。
- 控制引脚的电平、脉冲宽度和切换顺序必须完全按厂商手册执行。

---

## 21. Synchronous Write Through

Synchronous Write Through 定义同步写周期中 `Q` 的输出行为。启用后，在有效时钟沿写入数据的同时，Macro 通过内部 Bypass/Mux 将新写入的数据送到输出，通常在该时钟沿后的 Clock-to-Q 时间内有效。

它与异步“透明写”不同：Synchronous Write Through 仍然以有效时钟沿采样地址、数据和写使能，不形成任意时刻的组合 `D→Q` 透明路径。

单端口 SRAM 在写周期可能有以下行为：

| 模式 | 写周期的 Q 行为 |
| --- | --- |
| No Change | 保持上一次输出 |
| Read Before Write / Read First | 输出被覆盖前的旧数据 |
| Write Through / Write First | 输出本次写入的新数据 |
| Undefined | 输出不保证，仿真模型可能给出 `X` |

启用 Write Through 的影响：

- 可简化 Register File、FIFO 或 Load-Store Bypass 逻辑；
- 会改变 RTL/验证可见行为；
- 增加输出 Mux、控制和数据路径负载，可能影响面积、功耗和 Clock-to-Q；
- 与 Bit/Byte Write Mask 组合时，Q 可能需要由新数据与旧数据拼接，具体行为必须查看模型；
- 双端口同地址读写冲突仍需单独查看 Collision Matrix，不能由 Write Through 选项推断。

---

## 22. Read Pipeline

Read Pipeline 在读数据路径中增加一个或多个寄存器级，以提高最高工作频率和隔离外部负载。

典型行为：

- **Pipeline Off**：地址和读使能在时钟沿被采样，数据在同一周期内经过 Clock-to-Q 延迟输出，通常被系统称为 1-cycle read latency。
- **Pipeline On**：内部读结果先进入 Pipeline Register，再在后续时钟沿输出，相对于基础配置增加一个或多个完整时钟周期。

优点：

- 将长的 Array/Sense/Data Path 分割成较短时序段；
- 改善 Fmax、输出 Slew 和大负载驱动能力；
- 便于高频 NoC、Cache 和 Accelerator 接口。

代价：

- 增加读延迟；
- 增加寄存器面积、Clock Power 和测试复杂度；
- 改变控制器、FIFO 指针和 Hazard 处理逻辑；
- 上电或 Reset 后 Pipeline 内容可能为未知值，直到完成有效读操作；部分 Macro 没有 Pipeline Reset。

“Pipeline On”具体增加几级、Read Enable 为 0 时 Q 是保持还是清零，应以 Verilog 模型和 Databook 为准。

---

## 23. Bit Write

Bit Write 允许只更新一个 Word 中被选中的 bit，其余 bit 保持原值。硬件上通常为每个 I/O Slice 提供独立 Write Driver Enable。

常见粒度：

| 类型 | Mask 数量 | 典型用途 |
| --- | ---: | --- |
| Word Write | 1 个 | 整个 Word 同时写入 |
| Byte Write | `ceil(W/8)` 个 | CPU、DMA 和总线 Byte Enable |
| Half-Word / Group Write | 每 16 bit 或指定组 1 个 | DSP、宽数据缓存 |
| Bit Write | W 个 | Tag、状态位、寄存器文件和精细更新 |

常见引脚名包括 `WEM`、`BWE`、`BWEN`、`WEB`、`BEN`，有效电平可能为高或低。

设计注意事项：

- Mask 与地址、数据和写使能一样需要满足 Setup/Hold。
- 被 Mask 的 bit 必须保持原值；仿真模型应验证该行为。
- Bit Write 增加 Mask Decoder、局部 Write Driver 控制和布线，可能增加面积和动态功耗。
- 即使全部 bit 被 Mask，内部时钟或行译码是否仍然切换由具体设计决定，不能假设功耗为零。
- 内置 ECC 的 SRAM 在部分写时可能需要 Read-Modify-Write，以重新计算 ECC；若 Macro 不支持自动 RMW，系统必须在外部完成。

---

## 24. Read/Write Margin Control

Read/Write Margin Control 是一组可编程或静态配置的内部裕量调节功能，常见名称包括 `EMA`、`EMAW`、`RM`、`WM`、`SVOP`、`Margin Adjust` 等。其编码和方向没有统一标准。

### 24.1 可能调节的内部参数

Read Margin Control 可能调节：

- Sense Amplifier Enable 的延迟；
- WordLine 脉冲宽度或 Underdrive；
- BitLine 放电时间；
- Replica/Dummy 路径延迟；
- Read Assist 的强度或时序。

Write Margin Control 可能调节：

- Write WordLine 脉冲宽度；
- Write Driver 强度或启动时间；
- Negative BitLine、WordLine Boost、Cell-VDD Collapse 等 Assist 幅度；
- Write Self-Timing/Replica 延迟。

### 24.2 使用目的

- 补偿工艺、低压、温度和老化造成的读写裕量变化；
- 在速度、功耗和 Vmin 之间进行硅后调节；
- 进行量产测试、Shmoo、失效分析和弱 Cell 筛选；
- 提供一个保守模式以扩大统计裕量。

### 24.3 使用限制

- “更大编码”不一定表示“更大裕量”，必须使用厂商给出的真值表。
- 更保守的裕量设置通常会降低速度或增加能量，但并非所有实现都呈相同趋势。
- 只有 Databook 和 `.lib` 明确覆盖的编码才能用于 Functional Signoff。
- 若 Margin Pin 仅用于测试，应在正常模式固定到推荐默认值，不能由软件任意切换。
- Margin Control 调节的是实现级时序或 Assist，不等同于 BitCell 的静态噪声裕量 SNM 本身。

---

## 25. Read Assist

6T SRAM 读操作时，存储“0”的内部节点会通过访问管与预充高的 BitLine 形成分压，内部节点电压上升过多可能导致 Read Disturb。Read Assist 用于提高读稳定性、降低 Read Vmin 或改善低压良率。

常见 Read Assist 技术：

- WordLine Underdrive：降低读 WordLine 电压，减小对存储节点的扰动；
- Shortened WordLine Pulse：缩短读脉冲，限制扰动时间；
- Cell Supply Boost：读期间提高 BitCell 供电以增强保持能力；
- Regulated/Reduced BitLine Swing：限制位线条件以改善稳定性和能量；
- Read-Decoupled 8T/10T BitCell：使用独立读通路隔离存储节点；
- 适当调整 Sense Timing，使较小的 BitLine 差分能够可靠感应。

主要代价：

- WordLine Underdrive 和短脉冲可能减小读电流、增加访问时间；
- Boost/Regulation 需要额外电路、功耗和可靠性验证；
- Assist 可能影响未选 Cell、Half-Select Cell 或邻近电源噪声；
- 最佳设置依赖 PVT、容量、Mux 和 BitCell 失配。

Compiler 中的 Read Assist 可能是固定电路、可选生成项或由外部控制 Pin 调节，不能假设其接口形式相同。

---

## 26. Write Assist

低电压下，访问管和 Write Driver 可能无法快速压倒 BitCell 内部交叉耦合反相器，造成写失败。Write Assist 用于提高 Writability、降低 Write Vmin 或缩短写入时间。

常见 Write Assist 技术：

- Negative BitLine：把写“0”侧 BitLine 拉到低于地电位；
- WordLine Boost：把写 WordLine 提升到高于标称 VDD；
- Cell-VDD Collapse：写期间暂时降低选中列或选中行的 BitCell 供电；
- Source-Line Raise / Virtual Ground Control：抬高 Cell Ground 或改变局部供电；
- 强化 Write Driver 或延长 Write Pulse；
- 采用更易写入的 BitCell 尺寸或拓扑。

主要代价和风险：

- Charge Pump、Boost 和负压电路增加面积、功耗和启动时间；
- 过度 Assist 可能影响 Half-Select Cell、数据保持和器件可靠性；
- 电压过冲、负压和 Gate Oxide Stress 必须满足工艺可靠性限制；
- 更长写脉冲会降低最高频率并增加能量；
- Assist 控制通常只能使用厂商给定的合法模式和时序。

---

## 27. Column Redundancy

Column Redundancy 在每个 Bank 或 Subarray 中加入 Spare BitLine Pair、Spare Physical Column 或 Spare Column Group，用于替换存在缺陷的物理列。

可修复的典型缺陷包括：

- BitCell 列中的单点或多点缺陷；
- BitLine Open/Short；
- Column Mux 路径缺陷；
- 某些局部 Sense/Write 路径缺陷。

常见实现流程：

1. MBIST/ATE 识别故障列或地址；
2. Repair Analysis 将故障列映射到 Spare Column；
3. Fuse/OTP/eFuse 或 Repair Register 保存映射；
4. 地址访问时 Column Select 网络自动重映射。

Column Spare 的修复粒度可能是单个物理列、一对差分列、一个 Mux Group 或多个相邻列。Spare 数量越多，面积和路由开销越大；Repair Mux 也可能增加访问延迟。

---

## 28. Row Redundancy

Row Redundancy 在每个 Bank 或 Subarray 中加入 Spare WordLine/Spare Row，用于替换有缺陷的物理行。

常见实现：

- Repair Comparator 检测输入地址是否命中故障行；
- 命中时关闭原始 WordLine，激活 Spare WordLine；
- 映射信息由 Laser Fuse、eFuse、OTP、NVM 或可加载 Repair Register 保存。

可修复的典型缺陷：

- 某一行的 BitCell 缺陷；
- WordLine Open/Short；
- Row Decoder 或局部 WordLine Driver 缺陷；
- 在 Repair 粒度覆盖范围内的耦合缺陷。

Row Redundancy 的代价包括 Spare Row 面积、Repair Compare 延迟、Fuse 资源和 BISR 复杂度。Spare Row 通常按 Bank 分配，不能跨 Bank 任意共享。

---

## 29. IO Redundancy

IO Redundancy 使用 Spare I/O Slice 替换故障的逻辑数据位通路。一个 I/O Slice 通常包含与某个逻辑 bit 相关的 Column Mux、Global BitLine、Sense Amplifier、Write Driver、Output Driver 和 Mask Logic。

IO Redundancy 可用于修复：

- Sense Amplifier 或 Write Driver 缺陷；
- Global Data Line 缺陷；
- 某个逻辑 I/O 对应的多个物理列组缺陷；
- 列外围电路中难以用单列 Spare 修复的问题。

不同厂商对 Column Redundancy 和 IO Redundancy 的边界定义并不一致：有些产品把替换完整 I/O Slice 也称为 Column Redundancy。必须依据 Repair Granularity、Fuse Map 和版图说明判断。

### 29.1 Redundancy 与 ECC 的区别

- Redundancy 修复制造缺陷并形成永久或可加载映射，主要提高生产良率。
- ECC 在运行时检测或纠正瞬态 Soft Error 和部分永久错误，主要提高现场可靠性。
- 两者可以同时使用，但不能相互替代。

---

## 30. Optional Periphery Transistor Threshold Voltage

该选项用于选择 SRAM Periphery 中晶体管或逻辑 Cell 的阈值电压类型。BitCell 的 Vt 通常由 Compiler Flavor 固定，外围 Vt 选项不一定会改变 BitCell。

### 30.1 VT Type

| Vt 类型 | 速度 | 漏电 | 典型用途 |
| --- | --- | --- | --- |
| HVT | 最慢 | 最低 | 非关键外围、低漏电产品 |
| SVT / RVT | 中等 | 中等 | 通用平衡配置 |
| MVT / Mixed-Vt | 关键路径用低 Vt，非关键路径用高 Vt | 折中 | 在时序和漏电间优化 |
| LVT | 快 | 高 | 高频 Decoder、Sense、Output Path |
| ULVT | 最快 | 最高 | 极高性能且漏电预算充足的关键路径 |

实际工艺可能使用 `RVT`、`SVT`、`LVTLL`、`SLVT` 等不同名称。

### 30.2 选择影响

- 较低 Vt 可改善 Decoder、Self-Timing、Sense Amplifier 和输出路径速度。
- 较低 Vt 会显著增加 Standby/Retention 漏电，并提高热失控和 IR Drop 风险。
- 较高 Vt 可降低漏电，但可能使低电压下的 Delay 和 Slew 快速恶化。
- Mixed-Vt 通常是较好的综合选择，但具体关键路径分配由 Compiler 固化。
- 不同 Vt 版本必须使用各自对应的 `.lib`、GDS、LEF 和 LVS Netlist，不能混用。
- 选择 Vt 时应同时检查全部 PVT、Vmin、温度、老化、功耗状态和唤醒时序。

---

## 31. Outputs

一个可用于 SoC 全流程的 SRAM Macro 通常需要逻辑、时序、功耗、物理、版图和验证等多种 View。各 View 必须来自同一 Compiler 版本、同一配置和同一 Cell 名。

### 31.1 `.lib` — Liberty Timing/Power Model

`.lib` 是 ASCII 格式的 Liberty 模型，通常包含：

- Cell/Pin 功能和方向；
- Clock-to-Q、Setup、Hold、Recovery、Removal；
- 最小时钟周期和最小高/低脉宽；
- 输入 Capacitance、输出 Transition 和负载表；
- Internal Power、Switching Power、Leakage Power；
- PVT、Operating Condition 和 Power/Ground Pin；
- 功耗模式、Write Mask、Pipeline 或其他模式相关 Timing Arc。

用途：

- 综合时将 SRAM 作为 Hard Macro/Black Box 解析并进行接口时序检查；
- STA、PnR 优化、功耗分析和时序签核；
- SRAM 内部阵列不会由综合工具重新综合。

通常每个 PVT Corner 对应一个 `.lib`，Cell 名和接口保持一致。

### 31.2 `.db` — Compiled Liberty

`.db` 是 Synopsys 工具使用的二进制编译库，通常由对应 `.lib` 通过 Library Compiler 生成。可用于 Design Compiler、Fusion Compiler、PrimeTime 等工具。`.db` 不是通用交换格式，应保留原始 `.lib` 作为可审查源文件。

### 31.3 `.lef` — Macro Physical Abstract

`.lef` 提供 PnR 所需的物理抽象，包括：

- Macro Boundary 和尺寸；
- Pin 位置、层、形状和方向；
- Routing Obstruction、Placement Obstruction 和 Blockage；
- Site、Symmetry、合法 Orientation 等信息。

LEF 不包含完整晶体管和内部连线几何，不能用于最终 DRC/LVS。PnR 需要同时读取 PDK 的 Technology LEF 和 Macro LEF。

旧版 Synopsys ICC 流程可由 Technology File、LEF/GDS 创建 Milkyway；ICC2/Fusion Compiler 常使用 NDM。是否直接交付 Milkyway/NDM 取决于供应商。

### 31.4 `.tf` — Technology File

`.tf` 通常指 Synopsys Milkyway Technology File，描述工艺层、Layer Purpose、Via、设计规则和物理属性，属于 Foundry/PDK 级技术文件。

它通常**不是每个 SRAM Macro 单独生成的标准输出**。SRAM Compiler 可能提供 Layer Map、Tool Setup 或与 PDK `.tf` 匹配的导入脚本，但项目应使用 Foundry 认可的 Technology File，不能把某个 Macro 的 `.tf` 当作完整工艺定义。

### 31.5 `.v` / `.sv` — Verilog/SystemVerilog Model

Verilog 模型用于 RTL、Gate-Level 或 Timing Simulation，常见形式包括：

- Zero-Delay Functional Model；
- 带 Specify Block 和 Timing Check 的模型；
- 支持 SDF Back-Annotation 的模型；
- Power-Aware 或 Test Mode 模型。

模型应准确描述：

- Clock Edge 和 Enable；
- Read/Write Latency；
- Write Through、No-Change 和 Collision 行为；
- Bit/Byte Write Mask；
- Power Mode、Retention 和输出 `X` 传播；
- Setup/Hold 违例后的 Notifier 行为。

### 31.6 `.gds` / `.gdsii` / `.oas` — Full Layout

GDSII 或 OASIS 包含完整掩膜几何，用于：

- Top-Level Stream-In/Stream-Out；
- DRC、LVS、Density、Antenna 和最终 Tapeout；
- 版图查看和物理签核。

OASIS 通常比 GDSII 文件更小，先进工艺中较常见。

### 31.7 `.cdl` / `.sp` / `.spi` — Circuit Netlist

CDL/SPICE Netlist 描述晶体管级或层次化电路连接，用于：

- LVS Source Netlist；
- SPICE/Post-Layout 验证；
- 功耗、时序和可靠性分析；
- 与 GDS Top Cell 进行连通性比对。

用于 LVS 的 Netlist 可能包含 Black-Box、Device Parameter 和 PDK 专用语法，不能随意修改。

### 31.8 `.sdf` — Standard Delay Format

部分 Compiler 提供 SDF，用于门级仿真回标时序。很多 SRAM 流程主要依赖 Verilog `specify` 和 Liberty，因此 SDF 是否交付取决于供应商和仿真流程。

### 31.9 `.upf` / Power Intent 示例

低功耗 Macro 可能提供 UPF 示例、Power State Table、Isolation/Retention 说明或电源连接脚本。最终 SoC UPF 仍需由项目根据实际电源架构编写。

### 31.10 Databook、报告和辅助文件

常见还包括：

- HTML/PDF/TXT Databook；
- Pin List、Truth Table 和 Timing Diagram；
- Area、PPA、Peak Current 和 Power Report；
- DRC/LVS Clean Report；
- Compiler Configuration Log 和版本信息；
- Layer Map、GDS Map、Tool Import Script；
- BIST/Redundancy/Fuse Map 说明；
- EM/IR Current Profile 或 Power Model；
- 校验和及 Release Note。

### 31.11 View 一致性检查

集成前应检查：

- Cell/Module/Subckt/Top Cell 名一致；
- Pin 名、总线范围、方向和有效电平一致；
- Word Depth、Width、Mask、Port、Pipeline 和 Write Through 一致；
- Power/Ground Pin 和 Power Mode 一致；
- LEF 尺寸与 GDS Boundary 一致；
- `.lib` PVT 与项目 Corner 配置一致；
- 所有文件来自同一 Release 和同一 Compiler Run。

---

## 32. Aspect Ratio

Aspect Ratio 表示 Macro 外框宽度与高度的比值。本文定义：

\[
AR=\frac{W_{macro}}{H_{macro}}
\]

有些工具使用相反定义，使用前应确认。

### 32.1 影响 Aspect Ratio 的主要参数

- Column Mux：增大 M 通常使阵列更矮、更宽；
- Bank 数量和 Bank 排布；
- Center Decode 或 Edge Decode；
- Sense Amplifier、Write Driver 和 Output Driver 的位置；
- Power Ring、Power Mesh 和 Pin Placement；
- Redundancy、ECC、Pipeline 和测试外围；
- Metal Option 和 Routing Track 限制。

### 32.2 Floorplan 选择原则

- 根据芯片 Floorplan 的可用通道、数据流方向和相邻模块位置选择，而不是单独追求 Macro 最小面积。
- 评估信号 Pin 可达性、总线拥塞、Macro Halo、Power Strap 穿越和 Clock/Reset 走线。
- 较宽的 Macro 可能缩短横向数据总线但占用更多行；较高的 Macro 可能增加纵向通道压力。
- 检查允许的 Orientation，例如 `R0`、`MX`、`MY`、`R180`，部分 SRAM 不允许任意旋转或镜像。
- Aspect Ratio 通常只能从离散架构中选择，无法连续调节到任意值。
- 最终选择应基于完整 SoC 的 Timing、Congestion、IR Drop、Area 和 Power，而不只看 Macro PPA。

---

## 33. Word-Write Mask

Word-Write Mask 是对写入粒度的总称，可包括 Global Word Enable、Byte Mask、Sub-Word Mask 和 Bit Mask。其功能与“Bit Write”章节一致，但项目接口通常按总线协议进行分组。

以 32-bit SRAM、4 个 Byte Mask 为例：

```text
WM[0] -> D[7:0]
WM[1] -> D[15:8]
WM[2] -> D[23:16]
WM[3] -> D[31:24]
```

若 `WM[1]` 被 Mask，则写周期中 `D[15:8]` 不更新，原内容保持。实际产品可能使用低有效 `WEMN/BWEN`，上述仅为分组示例。

应确认以下行为：

- Mask 的有效电平；
- Mask 与数据位的映射顺序；
- Mask 全关闭时是否仍执行内部访问；
- Write Through 模式下被 Mask bit 的 Q 输出行为；
- 非 8 倍数字宽时最后一组 Mask 的处理；
- ECC SRAM 的部分写是否自动执行 Read-Modify-Write。

---

## 34. 行选择器（Row Decoder）

Row Decoder 根据内部 Row Address 选择一条物理 WordLine。外部地址在进入 Row Decoder 前可能已经经过 Bank Decode 和 Column Select 拆分。

典型结构包括：

- Address Buffer/Latch；
- Predecode；
- Final Decode；
- Local WordLine Driver；
- Center/Edge Distribution；
- Self-Timing 控制。

Row Decoder 的设计目标是：

- 只激活一条合法 WordLine；
- 在规定时间内驱动大电容负载；
- 控制 WordLine 脉宽，避免 Read Disturb 和写不足；
- 在未访问、Sleep 或 Test Mode 下保持安全状态；
- 降低 Glitch、Short-Circuit Current 和地址切换功耗。

当 Column Mux 大于 1 时，同一物理 WordLine 上包含多个逻辑地址对应的数据，低位地址由 Column Mux 再选择其中一组。

---

## 35. 列选择器（Column Decoder / Column Mux Select）

Column Decoder 根据 Column Select 地址控制 Column Mux，将选中的物理 BitLine Pair 连接到 Global BitLine、Sense Amplifier 或 Write Driver。

其作用不是“激活一条位线”，而是：

- 选择 `M` 个候选物理列中的一个；
- 为每个逻辑 I/O bit 建立选中列到读写外围的通路；
- 隔离未选列，减少 Sense/Write 负载；
- 配合 Column/IO Redundancy 完成故障列重映射。

当 `M=1` 时可能不需要显式 Column Select，逻辑列可直接连接到对应 I/O Slice。

---

## 36. 读写电路及读写过程

### 36.1 主要外围电路

- Address/Control Latch；
- Bank/Row/Column Decoder；
- BitLine Precharge 和 Equalization；
- Sense Amplifier；
- Write Driver；
- Input Data Buffer 和 Write Mask Logic；
- Output Latch/Register/Driver；
- Self-Timing、Replica/Dummy Path；
- Power Gating、Assist、Margin 和 Test Logic。

### 36.2 典型同步读过程

1. 在有效时钟沿采样 Address、Memory Enable 和 Read Control。
2. 预充电和均衡电路将 BitLine Pair 初始化到规定电平；具体实现可在前一周期完成。
3. Bank/Row Decoder 激活目标 WordLine。
4. 选中行的 BitCell 在 BL/BLB 上形成小差分电压。
5. Column Mux 选择目标物理列并连接到 Global BitLine/Sense Amplifier。
6. Sense Amplifier 在 Self-Timing 控制下放大差分。
7. 数据经 Output Latch、Pipeline Register 或 Driver 输出到 Q。
8. WordLine 关闭，BitLine 恢复预充电，准备下一周期。

### 36.3 典型同步写过程

1. 在有效时钟沿采样 Address、D、Write Enable 和 Write Mask。
2. Bank/Row/Column Decoder 选择目标 Cell Group。
3. Write Driver 根据 D 驱动选中列的 BL/BLB；被 Mask 的 I/O Slice 不驱动。
4. WordLine 激活，位线驱动压倒 BitCell 内部反馈并完成状态翻转。
5. Self-Timing 关闭 WordLine 和 Write Driver，BitLine 恢复到预充电状态。
6. 若启用 Write Through，Q 按模型定义输出新数据；否则可能保持旧值、输出旧内容或无定义。

具体的“先驱动 BitLine 还是先打开 WordLine”、脉冲重叠和内部时钟相位属于电路实现细节，以上顺序用于说明功能关系。

### 36.4 同地址和多端口冲突

Pseudo-Dual-Port、True-Dual-Port 或 1R1W SRAM 必须定义以下情况：

- 两端口同时读同一地址；
- 一个端口读、另一个端口写同一地址；
- 两端口同时写同一地址；
- 异步时钟端口在相近时间访问同一地址。

结果可能为旧数据、新数据、端口优先、合并写入或未知值。验证环境应直接依据 Compiler Verilog Model 和 Collision Table，不应自行假设。

---

## 37. 其他常见 Compiler 配置项

### 37.1 Port Type

| 类型 | 常见名称 | 功能 |
| --- | --- | --- |
| Single-Port | 1RW、SP SRAM | 一个端口完成读或写，同周期通常只能进行一种操作 |
| One-Port Register File | 1P RF | 常用于小容量高速存储，接口和读延迟可能不同于 SRAM |
| Simple/Pseudo Dual-Port | 1R1W、P2P | 独立读端口和写端口，可同周期读写，但同地址行为受限 |
| True Dual-Port | 2RW、TDP | 两个端口均可读写，需要完整 Collision 定义 |
| Two-Port Register File | 2P RF | 常见为 1R1W 或多读写变体，BitCell 与外围针对高速优化 |

### 37.2 Clock Edge、Clocking 和 Duty Cycle

可选项可能包括：

- Rising-Edge 或 Falling-Edge Trigger；
- 单时钟或独立 Read/Write Clock；
- Duty-Free Clock，即内部脉冲主要由时钟边沿和 Self-Timing 生成，对占空比依赖较小，但仍需满足最小高/低脉宽；
- Clock Gating/ME Gating；
- Pipeline Clock、Test Clock 和 Scan Clock 选择。

### 37.3 Output Drive Strength

Compiler 可能提供多个 Q Driver Strength，以适应不同负载：

- 更强 Driver 可降低 Output Slew 和外部延迟；
- 会增加面积、动态功耗和 Clock-to-Q 内部负载；
- 最佳做法通常是使用合理驱动并在 SRAM 旁放置 Buffer，而不是让 Macro 直接驱动超大扇出或长距离总线。

### 37.4 ECC / Parity

- Parity 可检测奇数个 bit 错误，但不能纠正。
- SEC 可纠正单 bit 错误；SECDED 可纠正单 bit 并检测双 bit 错误。
- 内置 ECC 会增加校验位、编码/译码延迟、面积和功耗。
- 部分写需要 Read-Modify-Write，以保持数据和 ECC 一致。
- ECC 不能替代制造冗余，也不能覆盖所有 Multi-Bit Upset。

### 37.5 Test Muxes、Scan Capture 和 Scan Shift

- Test Muxes 将 Functional Port 切换到 MBIST/ATPG 控制。
- Scan Capture 可把读出结果捕获到扫描链。
- Scan Shift 用于串行移入控制或移出观测结果。
- 打开这些选项会增加端口、面积和时序路径，必须同步更新 DFT Wrapper 和仿真模型。

### 37.6 Read Disturb Test

Read Disturb Test 模式可延长 WordLine、重复读取或改变 Sense 时序，以暴露弱 Cell。该模式通常只用于测试，正常功能和 `.lib` 时序不适用。

### 37.7 Operating Voltage、PVT 和 Temperature Range

生成 Macro 时应确认：

- 标称电压、最小/最大工作电压；
- Array 与 Periphery 的双 Rail 范围；
- TT、SS、FF、FS、SF 等 Process Corner；
- Temperature Range；
- RC Corner、OCV 和 Aging 条件；
- Functional Vmin、Hold Vmin、Retention Vmin；
- 每个 Corner 是否同时提供 `.lib`、功耗和仿真支持。

### 37.8 Power Ring、Metal Option 和 Pin Placement

部分 Compiler 可选择：

- Power Ring 宽度、层和数量；
- Top Metal/Route-Over 规则；
- Pin 在顶部、底部、左右或多边分布；
- Signal Pin 层、Pitch 和总线顺序；
- Power Mesh、Strap 和多个 VDD/VSS Pin；
- Blockage、Keepout 和 Abutment 方式。

这些选项对逻辑功能透明，但会显著影响 Floorplan、Congestion、IR/EM 和集成脚本。

---

## 38. 常见误区和修正

1. **Word Depth 不等于物理 WordLine 数量**：有 Column Mux 或多 Bank 时，物理行数通常小于逻辑字深。
2. **Word Width 不要求是 2 的幂**：合法值由 Compiler 的 Width Granularity 决定。
3. **Column Mux 不会减少外部地址位宽**：它只改变内部 Row/Column 地址分配。
4. **Column Mux 越大不一定越快**：BitLine 缩短的收益可能被 WordLine、Mux 和外围负载抵消。
5. **Bank 数量多不等于多端口**：外部并发能力由 Port 定义决定。
6. **目标频率不能单独确定功耗**：活动率、电压、容量、读写比例和 PVT 同样重要。
7. **`.lib` 不会让综合工具重新综合 SRAM 内部电路**：SRAM 是 Hard Macro，`.lib` 主要提供接口时序和功耗。
8. **`.lef` 不是完整 Layout**：最终 DRC/LVS 和 Tapeout 需要 GDS/OASIS 与 Circuit Netlist。
9. **`.tf` 通常属于 PDK**：不是每个 SRAM Macro 的独立标准输出。
10. **Power Mode 名称不能跨厂商直接类比**：LS、DS、Retention、Nap 和 Shutdown 的数据保持行为必须查状态表。
11. **Margin Control 不是通用性能旋钮**：只有被 Characterize 的编码才能用于功能模式。
12. **Redundancy 与 ECC 解决不同问题**：前者主要提高制造良率，后者主要处理运行时错误。

---

## 39. SRAM Compiler 选型和签核检查表

### 39.1 功能接口

- Port 类型、Clock 数量和有效边沿；
- Word Depth、Word Width、地址位宽；
- Read Latency、Pipeline、Write Through；
- Write Mask 粒度和有效电平；
- 同地址读写和多端口 Collision 行为；
- Power-Up 初始值和 Q Hold 行为。

### 39.2 PPA 和物理集成

- BitCell/Compiler Flavor；
- Column Mux、Bank、Center Decode 和 Aspect Ratio；
- Macro 面积、尺寸和合法 Orientation；
- Timing、Peak Current、Dynamic/Leakage Power；
- Pin Placement、Routing Blockage、Power Ring 和 IR/EM；
- 输出负载与 Driver Strength。

### 39.3 低功耗

- Standby、LS、DS、Retention、Shutdown 的数据保持行为；
- Dual Rail 和合法电压范围；
- 进入/退出时序、Wake-Up Latency 和 Inrush Current；
- Isolation、UPF Power State 和输出状态；
- Retention Vmin 与 Break-Even Time。

### 39.4 DFT、良率和可靠性

- BIST Interface、Test Mux、Scan；
- Row/Column/IO Redundancy 和 Repair 方式；
- ECC/Parity；
- Read/Write Margin、Read/Write Assist；
- Read Disturb、Retention 和 Vmin 测试；
- Automotive/Safety 项目的诊断覆盖率、ECC 注错和周期性测试要求。

### 39.5 交付和一致性

- `.lib/.db`、`.lef`、`.gds/.oas`、`.v/.sv`、`.cdl/.sp` 是否齐全；
- PVT Corner、Power Mode 和 Test Mode 是否覆盖；
- 所有 View 的 Cell 名、Pin、总线和配置是否一致；
- DRC/LVS、Characterization 和 Silicon Validation 状态；
- Compiler Version、Release Note、Checksum 和 License 是否可追溯。

---

## 40. 参考资料与适用范围

本文的通用定义和选项分类参考了公开的 Memory Compiler 产品资料、开源 SRAM Compiler 文档、SoC SRAM 集成文档以及常见 CMOS SRAM 设计方法，主要包括：

- M31 Technology Memory Compiler 产品功能说明；
- Silvaco Single & Dual Port SRAM Compiler 的功耗模式说明；
- Dolphin Technology Memory Compiler 的 Write Mask、Write Through、Redundancy、Dual Rail 和多种输出选项说明；
- OpenRAM 的 SRAM Layout、Netlist、Timing/Power Model 和 PnR View 生成说明；
- NVIDIA NVDLA Integration Guide 中的 SRAM Port、Retention、Sleep 和 Margin Control 示例；
- IHP Open PDK 中 SRAM 的 Liberty、LEF、GDS、CDL/SPICE 和 Verilog View 组织方式；
- 标准 CMOS SRAM BitCell、Array、Sense Amplifier、Self-Timing、Read/Write Assist 和冗余设计方法。

本文不替代受 NDA 约束的具体 Compiler User Guide。涉及以下内容时，必须回到对应产品手册：

- 低功耗引脚的真值表和进入/退出顺序；
- Margin/Assist 编码及合法工作模式；
- 同地址读写和多端口冲突行为；
- Self Time Bypass 和测试引脚；
- Redundancy Fuse Map；
- 双 Rail 电压关系；
- 各 PVT 下的 Timing、Power、Vmin 和可靠性保证。
