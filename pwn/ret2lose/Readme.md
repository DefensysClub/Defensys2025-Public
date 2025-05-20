# ret2lose

**Author**: med

**Category**: pwn

**Description**: Are you Losing son ?

**flag**: `defensys{Congratulations_You_Lost_Successfully_98744131}`

---

- This challenge is a classic ret2win challenge with a simple twist.

- Normally you just use the address of the function to overwrite the `RIP` register however, the address of the function is actually the address of the first instruction which is usually `endbr64`.

- `endbr64` is a 4-byte marker at a function’s entry that on CET-enabled CPUs verifies valid indirect-branch targets, otherwise acts as a no-op.

- When compiling i used `-fcf-protection=full` so branch protection is enabled.

- So we need to skip the `endbr64` and use the address after it (sometimes the second address after it) to not trigger the protection.
