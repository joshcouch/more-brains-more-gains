# More Brains, More Gains

A lightweight Streamlit app for calculating the nutritional value-to-cost ratio of meals, built to make everyday food choices faster to compare on price and nutrition. It used to be connected to an AWS DynamoDB database to allow users to add their own data, but this has been replaced with a static CSV in this repo.

Originally prototyped with ChatGPT shortly after its initial release and later revisited on Streamlit Community Cloud, this project is a practical example of AI-assisted rapid prototyping, iterative product refinement, and dependency maintenance across Python versions.

**[Try out the app here](https://more-brains-more-gains-e45zt8xe38cfxawtfbq6e3.streamlit.app/)**

## Product Overview

Choosing meals based on both cost and nutrition usually requires juggling labels, unit prices, and rough mental arithmetic. This app turns that comparison into a quick, repeatable calculation.

* **Core problem:** Comparing meal options by cost alone ignores nutritional density, while looking at nutrition alone ignores budget constraints.
* **Solution:** A simple interactive interface built in Streamlit that pairs meal cost with key nutritional inputs to rank or compare value per pound/dollar.
* **Target use:** Quick personal meal comparisons and experimenting with lightweight data apps.

## How It Was Built and Refined

### 1. Initial Prototype (Early ChatGPT Era)

* Used ChatGPT right after its initial launch to scaffold the Streamlit UI layout, input fields, and ratio calculation logic.
* Focused on getting a working end-to-end tool quickly rather than over-engineering architecture or storage.
* Captured the core product loop: enter meal cost and nutritional figures, compute a value-for-money metric, and inspect the result immediately.

### 2. Iteration and Refinement

* Tightened the calculation and display logic as edge cases showed up in real meal inputs.
* Kept the app intentionally scoped as a single-purpose tool rather than bloating it with unnecessary features.
* Revisited deployment on Streamlit Community Cloud to test running the app in a hosted environment.

### 3. Modernisation and Maintenance

* Encountered a build failure on Python 3.10 when `pandas==1.1.5` attempted to compile from source inside an isolated build environment where `setuptools` no longer exposed `pkg_resources` (and where legacy `pandas 1.x` build assumptions clash with newer Python releases).
* Diagnosed the root cause—stale dependency pinning from the original build era—and moved toward upgrading `pandas` to a modern 2.x release with pre-built wheels while checking for `pandas 1.x` to `2.x` API changes (such as replacing `DataFrame.append` with `pd.concat` and `Series.iteritems` with `Series.items`).

## Summary of Inputs Provided for This README

To draft this documentation accurately, the following context was used:

* **App purpose:** A simple Streamlit app for calculating the nutrition-to-cost ratio of meals.
* **Origin:** Built with ChatGPT soon after its initial release.
* **Evolution:** Refined iteratively over time and later hit a Python 3.10 / `pandas==1.1.5` / `setuptools` (`pkg_resources`) build issue on Streamlit Community Cloud.
* **Framing goal:** Written for GitHub to highlight skills as an AI-enabled product manager.

## PM Takeaways Demonstrated

* **Rapid 0-to-1 execution with AI:** Using generative AI early on to compress time-to-prototype and validate a simple user workflow.
* **Scope discipline:** Keeping a lightweight utility focused on its core ratio calculation instead of adding scope for its own sake.
* **Ultimately didn't pursue this any further due to low willingness to pay from a few people I asked to try it out (including myself to be honest). Additionally, a usable MVP required heavy upfront data collection—e.g. maintaining recent prices across SKU variations like different pack sizes of chicken—creating high fixed costs before validating demand.**
  
## Setup and Running Locally

1. Clone the repository:
```bash
git clone <your-repo-url>
cd more-brains-more-gains

```


2. Create and activate a virtual environment, then install dependencies (using a modern `pandas` version compatible with your Python runtime):
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```


3. Run the Streamlit app:
```bash
streamlit run <your_app_file>.py

```



*(Note: If you still have your original ChatGPT prompts, screenshots of v1, or exact nutrition metrics used in the formula, adding those to a `NOTES.md` or `CHANGELOG.md` file will make the PM case study even stronger.)*
