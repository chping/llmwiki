# 3D SRAM Reliability And Performance Tradeoffs

This page summarizes the paper "Reliability and Performance-aware 3D SRAM
Design" by Mohit Pathak and Sung Kyu Lim from Georgia Tech. The paper studies
bank-level 3D SRAM physical design and shows that TSV strategy changes area,
wire length, timing, and yield-related risk at the same time.

## Core Claim

3D SRAM organization should not be chosen on performance alone. Bank placement,
TSV placement style, and TSV fabrication flow all change the tradeoff between
timing efficiency and reliability-aware layout quality.

## What The Paper Evaluates

- Bank-level 3D SRAM layouts built from real GDSII-based physical designs rather
  than only analytical models.
- A 4-die stack using 64 KB SRAM banks to construct 1 MB, 4 MB, and 16 MB
  memories.
- Different bank cut sequences across vertical and planar dimensions.
- Different TSV placement styles: periphery, island, and spread.
- Different TSV technologies: via-first and via-last, with different footprint
  and routing constraints.

## Main Design Insights

### 1. Bank Partitioning Changes The TSV Count

The paper argues that delaying the Z cut in the bank-partition sequence tends to
split lower-level interface logic across dies. That increases the number of 3D
nets and therefore the number of TSVs required.

The same choice has mixed consequences:

- More TSVs and more area cost.
- Shorter wire length because related logic and banks can be stacked more
  directly.
- Better longest-path delay in the reported experiments.

The practical point is that the physically best cut sequence depends on whether
the design target values fewer TSVs or lower delay more highly.

### 2. TSV Placement Style Is A Reliability-Performance Knob

The floorplanning comparison separates three styles:

- `TSV periphery`: TSVs stay at the boundary, minimizing direct interaction with
  banks and interface logic.
- `TSV island`: TSVs and logic both occupy channel space, but in separate
  reserved regions.
- `TSV spread`: TSVs and logic share the channel space as long as DRC rules are
  met.

The reported tradeoff is clear:

- `TSV periphery` is the most conservative from a stress-isolation standpoint.
- `TSV spread` gives the best wire-length, area, and delay trends.
- `TSV island` sits between them.

This makes the placement style a first-order architecture choice, not just a
detail of backend implementation.

### 3. Via-First And Via-Last TSVs Affect Layout Quality Differently

The paper compares small and large TSV options under both via-first and via-last
fabrication assumptions. A key distinction is routing blockage:

- Via-first TSVs use only metal 1 for the landing pad in the paper's model.
- Via-last TSVs consume all metal layers at the drilled location.

That means via-last TSVs are more disruptive to routing resources even when the
nominal electrical role is the same. The layout images and discussion frame
via-first TSVs as easier to integrate densely.

## Why It Matters

The useful takeaway is that 3D SRAM design is not just "stack banks and add
TSVs." The physical design choices determine whether the stack optimizes for:

- lower wire length and better delay,
- lower TSV count and lower area overhead,
- or greater separation between TSVs and logic for reliability reasons.

For memory designers, this paper is a reminder that TSV planning has to be
coupled to bank architecture and floorplanning early, because those decisions
are strongly entangled in the final layout.

## Sources

- [Original source PDF](../raw/2026/0425/06026429.pdf)
