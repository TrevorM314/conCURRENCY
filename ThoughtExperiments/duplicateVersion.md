# The Duplicate Version Problem

## The Problem

Suppose two updates are released simultaneously, both with the same version number (eg 15). This will result in the same forking problems present in current blockchains.

How likely is this to happen, however? An update must generate enough support from the community, which would likely self-resolve any versioning conflicts prior to release.

Incentives: Would I benefit more from duplicate versions or unique versions?

## Possible Solution

If version number is determined by the final block on the chain before the update is adopted, this issue is lessened, but not eliminated.

Extension: The update is signified in a specific field within the block. Only one can be specified at a time. The field contains a hash of the protocol update proposal.

What prevents miner from including their own arbitrary protocol?

## Game Theory

Does Nash Equilibrium Play a role?

Suppose there are 2 version 6s with conflicting protocols and unequal popularity.

Once version 7 is released, there must exist only one canonical version 6 from which it will accept forward payments.

Therefore, it is in my best interest to mine on the more popular version.

What prevents the same splitting that occurs between Bitcoin and Bitcoin Gold, for example? 2 sects could create 2 separate version 7s, then create 2 entirely different cryptocurrency communities.

What if we voted on updates with votes proportional to our conCURRENCY amount?

## Possible solution Reexplored

If 2 updates with the same version are being proposed, miner holds vote on an update block. Users can vote with conCURRENCY with a special VOTE transaction.

The issue: Miners can decide which transactions to include and can control the vote.

Ammendment: The voting takes place not over 1 block, but over n blocks. Outcome therefore a mixture of those with the largest stake and those with the largest computing power.

Alternatively, an update may occur upon reaching a preset amount of conCURRENCY as opposed to a set amount of blocks to vote during. If update is not popular, it will not be approved before a different update. Is conCURRENCY backing constant or proportional to total conCURRENCY?

VOTE transaction contains conCURRENCY source addresses and the hash of the update proposal.
