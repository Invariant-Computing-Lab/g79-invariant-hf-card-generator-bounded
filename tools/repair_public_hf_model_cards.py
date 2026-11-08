#!/usr/bin/env python3
"""Invariant Computing Lab: no-cost, explicit-auth Hugging Face model-card repair.

Uses only huggingface_hub and the operator's local HF login.
Dry-run by default; --apply requests one explicit typed confirmation.
Never changes privacy, model weights, licences, datasets or clinical claims.
"""
import argparse
import difflib
import sys

REPOS = (
    "invariant-computing-lab/mri-feature-distance-cp08",
    "invariant-computing-lab/ncl-fitted-research-cp08",
    "invariant-computing-lab/rhythm-source-predictor-cp08",
)
OLD = (
    "Private staging package, not yet uploaded to Hugging Face. "
    "This package does not grant a public license. Read LICENSE_STATUS.md. "
    "No training was performed by this packaging continuation."
)
NEW = (
    "Publicly listed Invariant Computing Lab / Humanization Tech research artefact. "
    "Public visibility does not grant a blanket licence to code, data or model weights. "
    "Consult LICENSE_STATUS.md and underlying source rights. "
    "No new model training was performed in this packaging continuation."
)
OLD_ROUTE = (
    "Upload the repository only after owner approval of rights, model/data "
    "disclosure and public metadata."
)
NEW_ROUTE = (
    "The repository is already publicly listed. Rights to models and data, "
    "release approvals and any licence decision remain separate from "
    "successful packaging or software tests."
)

def patch(repo, content):
    if content.count(OLD) != 1 or content.count(OLD_ROUTE) != 1:
        raise RuntimeError(f"{repo}: expected text not found exactly once; no write")
    return content.replace(OLD, NEW).replace(OLD_ROUTE, NEW_ROUTE)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    try:
        from huggingface_hub import HfApi, hf_hub_download, CommitOperationAdd
    except ImportError as err:
        raise SystemExit("Install free dependency: python -m pip install huggingface_hub") from err
    api = HfApi()
    try:
        user = api.whoami()
    except Exception as err:
        raise SystemExit("Run hf auth login on your own machine; never paste a token into chat") from err
    print("Authenticated Hugging Face account:", user.get("name", "(unknown)"))
    operations = []
    for repo in REPOS:
        info = api.model_info(repo)
        if info.private:
            raise SystemExit(f"{repo}: unexpectedly private; refusing")
        source = hf_hub_download(repo_id=repo, filename="README.md",
                                 repo_type="model", force_download=True)
        with open(source, encoding="utf-8") as f:
            before = f.read()
        after = patch(repo, before)
        print("\n", repo)
        print("".join(difflib.unified_diff(before.splitlines(True),
                                           after.splitlines(True),
                                           fromfile="current/README.md",
                                           tofile="proposed/README.md")))
        operations.append((repo, info.sha, after))
    if not a.apply:
        print("\nDRY RUN ONLY. No remote changes. Run with --apply after review.")
        return 0
    if input("Type APPLY-THREE to commit EXACTLY the three README edits: ").strip() != "APPLY-THREE":
        print("Cancelled; no writes.")
        return 2
    for repo, base_sha, content in operations:
        latest = api.model_info(repo)
        if latest.sha != base_sha:
            raise SystemExit(f"{repo}: head changed since review; stop and rerun dry-run")
        result = api.create_commit(
            repo_id=repo, repo_type="model", revision="main",
            operations=[CommitOperationAdd(path_in_repo="README.md",
                                           path_or_fileobj=content.encode("utf-8"))],
            commit_message="Correct public model status and rights boundaries",
            parent_commit=base_sha,
        )
        print("Committed:", repo, result.commit_url)
        current = hf_hub_download(repo_id=repo, filename="README.md",
                                  repo_type="model", force_download=True)
        with open(current, encoding="utf-8") as f:
            confirmed = f.read()
        if confirmed != content:
            raise RuntimeError(f"{repo}: post-commit readback differs; inspect immediately")
    print("All three README contents verified. No model or licensing changes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
