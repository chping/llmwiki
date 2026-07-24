---
category: topic
created: 2026-07-24
updated: 2026-07-24
tags:
  - SRAM
  - source-bias
  - low-power
  - leakage
summary: SRAM Source Bias 通过待机时调整 Cell 源极电位降低亚阈值漏电，并在功耗、数据保持裕量和唤醒开销之间进行权衡。
zotero:
  item_key:
  citation_key:
source_uri: https://doi.org/10.1109/DAC.2006.229421
---

# SRAM Source Bias

## 定义

Source Bias（源极偏置）是 SRAM 的一种待机降漏电技术。以常见 NMOS Source Bias 为例，SRAM 正常读写时 Cell Pull-Down NMOS 的公共源线接 `GND`；进入待机或数据保持模式后，偏置电路将这条 Source Line 抬高到一个小的正电压 \(V_{\mathrm{SBias}}\)，使其成为 Virtual Ground。

```text
Active：NMOS Source = 0 V
Standby：NMOS Source = VSBias > 0 V
```

部分设计也会降低 Pull-Up PMOS 的 Source 电位，或者联合控制 Source Line、Body Line 和 Array Supply。具体极性和作用对象必须以 BitCell 拓扑为准。

## 降低功耗的原因

SRAM 待机功耗可近似表示为：

\[
P_{\mathrm{standby}}\approx V_{DD}I_{\mathrm{leak}}
\]

Source Bias 的主要作用是降低 \(I_{\mathrm{leak}}\)，而不是减少正常访问产生的动态功耗。

### 降低关断 NMOS 的栅源电压

当关断 NMOS 的 Gate 保持在 0 V、Source 被抬高到 \(V_{\mathrm{SBias}}\) 时：

\[
V_{GS}=V_G-V_S=-V_{\mathrm{SBias}}<0
\]

晶体管关断程度增强。由于亚阈值电流对 \(V_{GS}-V_{TH}\) 近似呈指数关系，较小的 Source Bias 就可能显著降低亚阈值漏电。

### 通过 Body Effect 提高有效阈值电压

如果 NMOS Body 仍接 `GND`，抬高 Source 会增大 \(V_{SB}\)，形成反向体偏效应：

\[
V_{TH}=V_{TH0}+\gamma\left(\sqrt{2\phi_F+V_{SB}}-\sqrt{2\phi_F}\right)
\]

\(V_{TH}\) 增大后，亚阈值漏电进一步下降。Source Bias 与 Body Bias 不是同一种技术：Source Bias 直接调整源极电位，Body Bias 直接调整衬底或 Well 电位；但在 Body 电位固定时，Source Bias 会间接产生 Body Effect。

### 降低漏源电压和 DIBL

Source 电位升高还会减小关断 NMOS 的 \(V_{DS}\)，削弱 Drain-Induced Barrier Lowering（DIBL），进一步抑制亚阈值漏电。部分工作条件下，较小的端电压也有助于降低栅漏电或结漏电。

## SRAM 中的工作方式

Source Bias 通常只在 Standby、Light Sleep 或 Deep Sleep 等不可访问状态启用：

1. 等待当前读写操作完成并关闭新的访问。
2. 将 Source Line 从 `GND` 抬高到规定的 \(V_{\mathrm{SBias}}\)。
3. 在偏置状态下保持数据并降低待机漏电。
4. 唤醒时将 Source Line 恢复到 `GND`。
5. 等待 Virtual Ground、内部供电和 Self-Timing 电路稳定后再允许读写。

偏置电压可由 Sleep Transistor、二极管连接器件、Charge Pump、Replica Cell Feedback 或其他偏置控制电路产生。Compiler 用户通常只能控制 Sleep Mode 引脚，不能直接设定内部 Source Bias 电压。

## 与其他低功耗技术的区别

| 技术 | 主要操作 | 数据保持 | 主要收益 |
| --- | --- | --- | --- |
| Source Bias | 调整 Cell 或外围晶体管的 Source 电位 | 通常保持 | 降低待机漏电 |
| Body Bias | 调整 Body/Well 电位以改变 \(V_{TH}\) | 通常保持 | 调节漏电与速度 |
| Retention Voltage | 降低 BitCell Array 的供电电压 | 保持至 DRV 以上 | 降低漏电和静态功耗 |
| Power Gating | 切断 Array 或 Periphery 电源 | 取决于关闭范围 | 获得更低漏电 |
| ME/Clock Gating | 停止内部时钟和动态切换 | 保持 | 降低动态功耗 |

## 设计权衡

Source Bias 并非越强越好。偏置升高会压缩 Cell 的有效供电差，可能降低 Hold SNM 和数据保持裕量；在 PVT 变化和器件失配下，弱 Cell 可能发生 Hold Failure。偏置电路本身还会带来面积、控制功耗、模式切换能量和唤醒延迟。

- 功耗：偏置越强，待机漏电通常越低，但偏置发生器自身也消耗能量。
- 保持可靠性：必须验证 Hold Vmin、Retention Vmin、Hold SNM 和统计失效率。
- 性能：Active 模式若仍残留 Source Bias，会降低读电流并增加访问延迟。
- 唤醒：Virtual Ground 放电会产生延迟和 Inrush Current，需要满足 Recovery Time。
- 工艺适用性：Body Effect、DIBL 和漏电组成随 Bulk CMOS、FinFET、FD-SOI 或 GAA 工艺变化，不能直接复用偏置电压。

## Compiler 与签核检查

使用带 Source Bias 的 SRAM Macro 时，应在对应 Databook、Verilog 模型和 Liberty/UPF 资料中确认：

- 哪些功耗模式会启用 Source Bias；
- 模式是否保持数据以及允许的最长持续时间；
- Sleep 控制信号的有效电平和进入、退出顺序；
- \(V_{\mathrm{SBias}}\) 是否由 Macro 内部生成；
- Retention Vmin、适用 PVT 和失效率保证；
- 唤醒时间、首个合法访问周期和输出状态；
- Source Line 或 Virtual Ground 是否作为外部电源 Pin 暴露；
- 唤醒 Inrush、IR Drop 和 EM 签核要求。

## 相关主题

- [[sram|SRAM]]
- [[sram-memory-compiler|SRAM Memory Compiler 功能与配置]]

## 参考资料

- [Self-calibration technique for reduction of hold failures in low-power nano-scaled SRAM](https://doi.org/10.1109/DAC.2006.229421)
- [On-chip SRAM macro with ultra-low-leakage data retention using simultaneous source-line and body-line biasing](https://doi.org/10.1016/j.vlsi.2026.102698)
