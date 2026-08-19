# Behavioral forward evaluation

`cases.json` is a host-neutral acceptance suite. Run it against each supported agent in an isolated temporary study workspace; do not use a live course or personal learner state.

For each case:

1. Install or link the Skill exactly as a user would.
2. Construct only the state described by `setup`.
3. Send `prompt` without revealing the acceptance criteria to the agent.
4. Capture the response, tool actions, approval requests, and filesystem diff.
5. Mark the case passed only when every `must` item is observable, no `must_not` item occurs, and writes are confined to `expected_writes` or narrower host bookkeeping.
6. Record the host, host version, model, Skill commit, result, and concise evidence using `result-template.json`.

Reset the isolated workspace between cases. A case that cannot be exercised because the host lacks a capability should be `not_applicable`, not silently passed. Review failures for either a Skill defect, a host limitation, or model variance before changing instructions.

The repository validator checks this suite's structure; it does not score agent transcripts.
