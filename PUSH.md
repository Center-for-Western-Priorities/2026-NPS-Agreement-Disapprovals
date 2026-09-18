# Pushing this to GitHub

Target repository:
<https://github.com/Center-for-Western-Priorities/2026-NPS-Agreement-Disapprovals>

These steps run on Windows, from this project folder, and assume you have write
access to the Center-for-Western-Priorities organization. Nine steps, about ten
minutes the first time.

---

## Step 1. Install Git, if it is not already there

Open PowerShell and run:

```powershell
git --version
```

If you get a version number, skip to step 2. If you get "not recognized," install
Git for Windows from <https://git-scm.com/download/win> and accept the defaults. The
installer includes Git Credential Manager, which handles the GitHub sign-in in step 7.
Close and reopen PowerShell afterward.

## Step 2. Open a terminal in this folder

In File Explorer, navigate to this folder, right-click an empty area, and choose
**Open in Terminal** (Windows 11) or **Git Bash Here** (Windows 10, after installing
Git). Either shell works.

Or type it, quoting the path because it contains spaces and an apostrophe:

```powershell
cd "G:\My Drive\Lilly's Files\Products\NPS disapproved agreements 09.2026"
```

Confirm you are in the right place:

```powershell
dir
```

You should see `index.html`, `README.md`, and the `build`, `data`, `docs`, and
`embed` folders.

## Step 3. Tell Git who you are

Once per machine, not once per project:

```powershell
git config --global user.name "Lilly Bock-Brownstein"
git config --global user.email "lilly@westernpriorities.org"
```

## Step 4. Start the repository

```powershell
git init -b main
git add .
```

## Step 5. Confirm the local-only files are excluded

This is the step worth slowing down for.

```powershell
git status --short
```

Read the list. You should see `index.html`, `README.md`, `PUSH.md`, `.gitignore`,
and files under `build/`, `data/`, `docs/`, and `embed/`.

Then check the three exclusions directly:

```powershell
git ls-files data/source
git ls-files _internal
git ls-files docs
```

The first two must print nothing. The third must print exactly three files:
`docs/DATA-DICTIONARY.md`, `docs/METHODOLOGY.md`, and `docs/PLACEMENTS.md`.

If any of those is wrong, stop and run `git rm --cached -r <the path>` before
continuing. Files stay on your disk either way; `git rm --cached` only removes them
from what gets published.

## Step 6. Make the first commit

```powershell
git commit -m "2026 NPS agreement disapprovals map"
```

## Step 7. Connect the remote and push

```powershell
git remote add origin https://github.com/Center-for-Western-Priorities/2026-NPS-Agreement-Disapprovals.git
git push -u origin main
```

A browser window opens for GitHub sign-in on the first push. Sign in and authorize;
Git remembers it after that.

**If the push is rejected** with "updates were rejected" or "fetch first," GitHub
created the repository with a README or license file, so the two histories differ.
Pull those in and push again:

```powershell
git pull --rebase origin main
git push -u origin main
```

If the rebase reports a conflict in `README.md`, keep this project's version.

Note that during a rebase `--ours` and `--theirs` are swapped from what you would
expect: `--ours` is the version already on GitHub, `--theirs` is yours. Rather than
rely on remembering that, pull the file from your own commit by its hash. The hash is
printed by the `git commit` in step 6, and `git log --oneline` shows it again.

```powershell
git checkout <your-commit-hash> -- README.md
git add README.md
git -c core.editor=true rebase --continue
git push -u origin main
```

`-c core.editor=true` stops Git from opening Vim to confirm the commit message, which
is awkward to escape from PowerShell.

Then confirm you kept the right file before moving on:

```powershell
git show HEAD:README.md | Select-Object -First 5
```

That should print `# 2026 NPS Agreement Disapprovals` and the paragraph starting "An
interactive map of the National Park Service financial assistance agreements." If it
prints a one-line stub instead, GitHub's version won. Recover with:

```powershell
git checkout <your-commit-hash> -- README.md
git commit --amend --no-edit
git push -u origin main
```

## A note on the line-ending warnings

`git add` prints a wall of "LF will be replaced by CRLF" warnings on Windows. That is
Git's normal behavior, not a problem: files are stored with Unix line endings in the
repository and checked out with Windows ones. The published site and the CSV are
unaffected. Nothing to do.

## Step 8. Verify

Open the repository page. You should see 15 files and folders, and the README
rendering below them. Click into `data/` and confirm there is **no** `source`
folder. Click `data/nps-disapprovals-2026.csv` and confirm GitHub previews 133 rows.

## Step 9. Publish the site

The repository is a static site; `index.html` at the root is the whole thing.

**Netlify**, the same path as the BLM data center tracker. Sign in at netlify.com,
"Add new site" → "Import an existing project" → GitHub → pick this repository. Leave
the build command empty and set the publish directory to `/`. You get a
`*.netlify.app` URL, and every later push redeploys automatically.

**GitHub Pages**, if you would rather not add Netlify. In the repository: Settings →
Pages → Source "Deploy from a branch" → branch `main`, folder `/ (root)` → Save. The
URL is
`https://center-for-western-priorities.github.io/2026-NPS-Agreement-Disapprovals/`
after a minute or two.

Then open `embed/wordpress-snippet.html`, replace `HOSTED_URL` with that URL, and
paste the snippet into a Custom HTML block on the WordPress page.

---

## Pushing later changes

```powershell
git add .
git commit -m "what changed"
git push
```

## A note about Google Drive

This folder syncs through Google Drive, and Drive's sync client sometimes locks or
partially syncs files inside Git's hidden `.git` directory while Git is writing them,
which surfaces later as a corrupt object. It usually works. But once the repository is
on GitHub, the cleaner long-term setup is a clone outside Drive:

```powershell
cd $HOME\Documents
git clone https://github.com/Center-for-Western-Priorities/2026-NPS-Agreement-Disapprovals.git
```

Work there, push from there, and leave the Drive copy as the shared reference. If you
do, copy `data/source/` and `_internal/` across by hand; `build/prep.py` falls back to
the published CSV when the source workbook is absent.

## If you get stuck

- **"fatal: not a git repository"** — you are in the wrong folder. Redo step 2.
- **"Permission denied" or "403" on push** — your GitHub account is not a member of
  the organization, or lacks write access to the repository.
- **"remote origin already exists"** — you ran step 7 twice. Use
  `git remote set-url origin https://github.com/Center-for-Western-Priorities/2026-NPS-Agreement-Disapprovals.git`
  instead of `git remote add`.
- **Wrong account cached** — Windows Credential Manager → Windows Credentials →
  delete the `git:https://github.com` entry, then push again to sign in fresh.
