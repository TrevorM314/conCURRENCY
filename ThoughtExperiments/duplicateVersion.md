# The Duplicate Version Problem

## The Problem

Suppose two updates are released simultaneously, both with the same version number (eg 15). This will result in the same forking problems present in current blockchains.

How likely is this to happen, however? An update must generate enough support from the community, which would likely self-resolve any versioning conflicts prior to release.

Incentives: Would I benefit more from duplicate versions or unique versions?

## Possible Solution

If version number is determined by the final block on the chain before the update is adopted, this issue is lessened, but not eliminated.

Extension: The update is signified in a specific field within the block. Only one can be specified at a time. The field contains a hash of the protocol update proposal.

What prevents miner from including their own arbitrary protocol?
