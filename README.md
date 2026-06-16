# From Zero to Python with AI

An interactive, beginner-friendly course site: four animated Python concepts,
a micro:bit step counter, and a step-data analyser. Static site — free to host
on GitHub Pages.

```
python-ai-course/
├── index.html          ← the interactive page (four concept animations)
├── data/
│   └── step_data.csv    ← 28 days of sample step data (Step 3)
├── starter.py           ← starter analysis script (Step 3, runs in Trinket)
├── step3_analysis.ipynb ← Colab notebook (Step 3 deep-dive: charts + real CSV)
└── quiz-bank.md         ← question bank for all checkpoints
```

## Deploy to GitHub Pages

1. Create a new repository on GitHub (e.g. `python-ai-course`), public.
2. Upload the contents of this folder (keep `index.html` at the top level,
   `data/` inside it). You can drag-and-drop in the GitHub web UI, or use git.
3. In the repo, go to **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**.
5. Pick branch **main** and folder **/ (root)**, then **Save**.
6. Wait ~1 minute. Your site is live at
   `https://<your-username>.github.io/python-ai-course/`

To update the site later, just edit/replace files in the repo — Pages redeploys
automatically.

## Notes

- GitHub Pages serves files only; it does not run Python. The `.py` and `.csv`
  are downloads. Live coding happens in the embedded Trinket editor (Python in
  the browser).
- The four animations are plain JavaScript and run natively on the page.
- **Colab badge:** after deploying, edit two `USERNAME` placeholders — one in
  `index.html` (the "Open Step 3 in Colab" link) and one in `step3_analysis.ipynb`
  (the `raw.githubusercontent.com` URL) — to your GitHub username. The badge then
  opens the notebook from your repo. Note: Colab can't be embedded in an iframe
  (Google blocks it), so it opens in a new tab — this is expected.
