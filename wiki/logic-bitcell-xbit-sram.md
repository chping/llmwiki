# Logic-Bitcell xBIT SRAM Notes

Logic-bitcell, described here as `xBIT`, is a cache-oriented SRAM approach that
tries to recover logic-style scaling at advanced nodes by rebuilding the bitcell
around logic design rules instead of classic SRAM-specific rules.

## Why It Matters

At advanced nodes, logic cell area keeps shrinking while SRAM scaling has
slowed. The source frames SRAM as a system bottleneck because it still occupies
a large share of chip area and power, and because SRAM read stability can force
a higher supply voltage than the surrounding logic. That creates practical
limits for DVFS, floorplanning, and overall SoC energy efficiency.

## Main Idea

The key claim is not that conventional 6T or 8T SRAM has become unusable, but
that those cells no longer match the constraints of highly scaled logic-centric
designs. Traditional SRAM macros rely on dedicated memory rules, transistor
sizing for read and write stability, and separation structures that make
physical integration with logic more awkward.

`xBIT` instead combines two asymmetric logic-style subcells:

- `NBIT`: `6N/4P`, NMOS-heavy
- `PBIT`: `4N/6P`, PMOS-heavy

Placed together as a `2-row x 1-column` structure, they restore overall N/P
balance while matching standard-cell height and rectangular placement rules. The
result is positioned as a logic-rule-compatible SRAM cell rather than a slightly
modified conventional SRAM macro.

## Read and Write Design

The source emphasizes low-voltage operation:

- Write uses a controlled latch-style structure intended to avoid write
  contention.
- Read uses separate read stacks and two read bitlines with opposite polarities.
- Each read bitline only serves half the rows, reducing loading and helping
  low-voltage read certainty.

The design goal is to stop both read stability and write assist from dominating
minimum operating voltage.

## Claimed Operating Envelope

The article positions `xBIT` for small, latency-sensitive memories rather than
for large bulk SRAM arrays:

- Capacity range: roughly `16KB` to `128KB`
- Access style: `2-port`, `1R1W`
- Use cases: `L1 cache`, `scratchpad`, near-pipeline local memory

That scope matters because the density and frequency claims depend on short
wires, bounded row depth, and carefully managed banking.

## Reported Results

The source summarizes an ISSCC 2026 result implemented in a `2nm` nanosheet
process:

- Macro example: `64KB`
- Aggregate demo: `0.5Mb` across eight macros
- `Vmin`: `0.35V` at `100MHz`, reported at `100% yield`
- `Fmax`: `4GHz` at `0.95V`
- Access latency: `102ps` at `0.95V`
- Compared with same-node `8T` SRAM: higher density for sub-`128KB`
  configurations and about `30%` lower dynamic power

The article presents the most important system-level point as single-rail
operation, which would reduce one of the standard integration penalties of
high-performance SRAM.

## Position Relative to Other SRAM Types

The source places `xBIT` in a gap between dense conventional SRAM and small
logic-rule memories:

- `6T SRAM`: best for large-capacity macros
- `8T SRAM`: common for high-performance small caches
- Logic/compiler SRAM: logic-rule-compatible but usually much less dense
- `xBIT`: aims to keep logic-rule compatibility without giving up cache-class
  density

This makes `xBIT` a targeted architectural answer, not a universal SRAM
replacement.

## Open Questions

The source is optimistic but leaves several practical questions unresolved:

- Yield and manufacturability outside the reported configuration
- Compiler and macro-generation support
- Scaling beyond the stated capacity range
- How broadly single-rail integration holds across full products rather than
  isolated test vehicles

## Sources

- [Original
  source](../raw/2026/0421/SRAM%20%E7%9A%84%E4%B8%8B%E4%B8%80%E6%AD%A5%EF%BC%9F%20SRAM%20%E9%80%BB%E8%BE%91%E5%8C%96%E7%9A%84%E6%9C%80%E6%96%B0%E6%BC%94%E8%BF%9B%EF%BC%9ALogic%E2%80%91Bitcell%EF%BC%88xBIT%EF%BC%89%20%E9%99%84%E5%90%84%E7%B1%BB%20SRAM%20%E6%9E%B6%E6%9E%84%E5%AF%B9%E6%AF%94%E8%A1%A8.md)
