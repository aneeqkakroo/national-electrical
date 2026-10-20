# National Electrical Ltd website

Static website for [nationalelectrical.uk](https://nationalelectrical.uk), electrical installation, design and testing across Cambridgeshire, the East of England and Greater London.

## Structure

- `src/content.py`: all page content (business details, services, customer types, areas, FAQs)
- `src/build.py`: page templates; generates the site
- `src/assets/`: stylesheet, script and favicon
- `site/`: the built website that Netlify publishes
- `brand.html`: logo, colours and typography guidelines

## Making changes

1. Edit `src/content.py` (or the templates in `src/build.py`).
2. Rebuild: `python src/build.py`
3. Commit and push. Netlify redeploys automatically.

## Before you launch

Fill in `company_no` and `registered_office` in `src/content.py`. A UK limited company's website must show both.
