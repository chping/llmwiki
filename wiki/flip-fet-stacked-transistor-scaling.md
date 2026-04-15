# Flip FET And Stacked Transistor Scaling Notes

This page summarizes a VLSI Symposium presentation from Peking University on the first experimental demonstration of dual-sided N/P FETs in Flip FET (FFET) on 300 mm wafers for stacked-transistor technology aimed at sub-1 nm nodes.

## Core Idea

FFET is presented as a self-aligned stacked-transistor approach that places usable devices on both wafer sides. The pitch is that backside processing is no longer only for power delivery or signal routing; it can also host active devices, enabling a dual-sided CMOS integration path with more scaling headroom than conventional monolithic layouts.

## What The Work Demonstrates

- Dual-sided N/P FETs fabricated in an FFET flow on 300 mm wafers.
- A baseline FFET process, flipped frontside-FET process flow, and backside-FET process flow.
- Key enabling backside steps including wafer bonding, active-wafer thinning, backside fin-profile improvement, and backside overlay correction.
- Structural confirmation by TEM for symmetric devices and interconnects.
- Electrical data showing both sides can operate with nearly symmetric behavior.

## Process Takeaways

The presentation emphasizes that FFET depends on integrating several standard but tightly controlled steps rather than inventing an entirely new frontside transistor module. The critical process challenges highlighted in the deck are:

- High-quality wafer bonding after oxide deposition and surface cleaning.
- Precise active-wafer substrate thinning with final position and flatness control.
- Backside fin trimming to avoid reverse-tapered profiles and improve gate control.
- Backside lithography and overlay correction to tighten alignment residue.

The overall message is that these process modules were developed to a point where backside device fabrication can be executed without losing the frontside device stack.

## Electrical And Device Notes

The deck reports that dual-sided FETs behaved well and achieved nearly symmetric performance. It also calls out:

- Backside PFET optimization through contact and EOT tuning, then junction, work-function, and implant tuning.
- A backside PFET example at 30 nm gate length with decent electrostatics, including reported subthreshold slope, DIBL, on/off ratio, and transconductance trends.
- Minor frontside NFET change from bonding thermals, but clear impact from full backside FET processing, which motivates explicit thermal-budget strategies.

## Architecture Implications

The authors position FFET as more than a one-off process demo. The deck highlights several architectural advantages:

- Multi-Vt support and dual-sided threshold-voltage tunability.
- A natural split-gate option in FFET, contrasted with the extra processing needed to realize split-gate behavior in CFET-style schemes.
- Dual-sided CMOS support, with both NFET and PFET placement possible on frontside and backside.
- More flexible and scalable design options than common-gate stacked approaches.

## Why It Matters

The strongest claim in the concluding slides is that this 300 mm wafer demonstration de-risks FFET as a candidate stacked-transistor platform. The technology is framed as promising because it combines:

- Stacked active devices on both sides of the wafer.
- Simpler Vt tunability.
- Natural split-gate behavior.
- Dual-sided CMOS design flexibility.
- A path toward broader "Flip 3D" integration ideas beyond a single logic tier.

## Sources

- [Original source](../raw/2026/0415/T10_T10-3 First Experimental Demonstration of Dual-sided NP FETs in Flip FET (FFET) on .pdf)
- [Original source](<../raw/2026/0415/T10_T10-3 First Experimental Demonstration of Dual-sided NP FETs in Flip FET (FFET) on.pdf>)
- [Original source](../raw/2026/0415/T10_T10-3%20First%20Experimental%20Demonstration%20of%20Dual-sided%20NP%20FETs%20in%20Flip%20FET%20(FFET)%20on.pdf)