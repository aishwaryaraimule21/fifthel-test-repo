
# Code review demo – attendee instructions

Fork this repo, check out the **`first-branch`** branch, and open a PR **into your fork’s `main`** so we can practice code review.

---

## 1. Fork the repository

- Go to the repo on GitHub (or your Git host).
- Click **Fork** and create the fork under your account.

---

## 2. Clone your fork and go into the repo

```bash
git clone https://github.com/YOUR_USERNAME/fifthel-test-repo.git
cd fifthel-test-repo
```

Replace `YOUR_USERNAME` with your GitHub username (or use the SSH URL if you prefer).

---

## 3. Check out the remote branch `first-branch`

**Option A – branch already exists on your fork (e.g. after a full fork):**

```bash
git fetch origin
git checkout first-branch
```

**Option B – branch exists only on the original repo (add upstream and fetch):**

```bash
git remote add upstream https://github.com/aishwaryaraimule21/fifthel-test-repo.git
git fetch upstream
git checkout -b first-branch upstream/first-branch
```

Replace `ORIGINAL_OWNER` with the owner of the repo you forked from.

---

## 4. Push `first-branch` to your fork (if needed)

If you used Option B, or your fork doesn’t have `first-branch` yet:

```bash
git push -u origin first-branch
```

If you used Option A and the branch already exists on your fork, ensure it’s up to date:

```bash
git push -u origin first-branch
```

---

## 5. Open a PR on your fork (first-branch → main)

- Go to **your fork** on GitHub (e.g. `https://github.com/YOUR_USERNAME/fifthel-test-repo`).
- Use **Pull requests** → **New pull request**.
- Set:
  - **base:** `main` (your fork’s `main`)
  - **compare:** `first-branch`
- Add a short title and description (e.g. “Code review demo – first-branch into main”).
- Create the pull request.

We’ll use this PR for the code review demo.

---

## Quick reference – commands in order

```bash
git clone https://github.com/YOUR_USERNAME/fifthel-test-repo.git
cd fifthel-test-repo
git fetch origin
# If first-branch isn’t on your fork, use upstream instead:
git remote add upstream https://github.com/ORIGINAL_OWNER/fifthel-test-repo.git
git fetch upstream
git checkout -b first-branch upstream/first-branch
git push -u origin first-branch
# Then open a PR on your fork: base = main, compare = first-branch
```

---

**Need help?** Ask the facilitator before or during the session.
