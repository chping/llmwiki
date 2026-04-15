%%  %%# Flip FET And Stacked Transistor Scaling Notes

This page summarizes a 2025 VLSI Symposium presentation from Peking University on the first experimental demonstration of dual-sided N/P FETs in Flip FET (FFET) on 300 mm wafers, positioned as a stacked-transistor option for sub-1 nm logic nodes.

## Core Claim

FFET extends backside processing from interconnect-only functions into active-device integration. The architecture stacks usable transistors across both sides of the wafer and aims to keep the devices and interconnects largely symmetric, which the authors present as an advantage over more asymmetric stacked-transistor approaches.

## What This Work Demonstrates

- First 300 mm wafer demonstration of dual-sided N/P FETs in FFET.
- A self-aligned FFET integration flow with frontside processing, wafer bonding, wafer flipping, substrate thinning, active reveal, and backside device processing.
- Dual-sided CMOS capability, with NFET and PFET placement possible on both frontside and backside.
- Experimental device data rather than only a concept or process sketch.

## Process Development Highlights

The deck identifies four enabling process modules for making backside devices practical in FFET:

- Wafer bonding with edge trimming, low particle counts, no bubbles, and reported bonding strength of 2.2 to 3.2 J/m2.
- Substrate thinning with a SiGe etch-stop layer and final CMP to improve total-thickness variation control.
- Backside fin trimming using ion-beam etching to improve fin profile, gate control, and channel strain.
- Backside overlay correction that reduced mean overlay residue to below 3 nm with much tighter distributions.

These steps are presented as the main process enablers that let the backside device module use industry-standard flows instead of requiring exotic vertical patterning.

## Device Results

- TEM images show frontside and backside FFET devices with 30 nm gate length and broadly symmetric structures.
- The dual-sided PFET/NFET measurements are described as well behaved, with nearly symmetric on-state performance.
- The optimized backside PFET at 30 nm gate length is reported with 73.1 mV/dec subthreshold slope, 24 mV DIBL, about 10^7 on/off ratio, and improved transconductance.
- Frontside NFETs see minor impact from bonding thermals but clearer impact from the full backside process sequence, which motivates explicit thermal-budget management.

## FFET Versus CFET Framing

The authors position FFET as a more manufacturing-friendly stacked-transistor option than CFET in several areas:

- Multi-Vt tuning on both sides, with about 500 mV of dual-sided threshold-voltage tunability shown in the deck.
- Natural split-gate support because frontside and backside gate processes are already separated.
- Dual-sided CMOS rather than a more constrained mono-CFET arrangement.
- Lower aspect-ratio processing and self-aligned active formation, while leaving room for symmetric device and interconnect scaling.

The main tradeoff the deck acknowledges is thermal interaction between backside processing and already-built frontside devices. The proposed mitigation is a multi-flipping flow that defers some frontside gate and BEOL steps until after backside device formation.

## Why It Matters

The significance of the presentation is not just that backside devices can be built, but that they can be built on 300 mm wafers with process modules the authors argue are compatible with industrial practice. The closing slides frame FFET as a candidate path beyond current GAA and CFET scaling, and as a stepping stone toward broader "Flip 3D" integration concepts.

## Sources
  
- [Original source](../raw/2026/0415/T10_T10-3%20First%20Experimental%20Demonstration%20of%20Dual-sided%20NP%20FETs%20in%20Flip%20FET%20%28FFET%29%20on%20.pdf)
