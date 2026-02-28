# Python Website Prototype

A multi-page professional website built with a fully Python-based stack using the [Pelican](https://getpelican.com/) static site generator and [uv](https://github.com/astral-sh/uv) for fast, reproducible dependency management.

![MSU-branded theme screenshot](https://github.com/user-attachments/assets/448e20f8-5c5d-4b3b-a72f-c8f4e5328c43)

## Features

- **Pure Python**: Pelican-based static site generation
- **Easy Setup**: Managed with `uv` (Python 3.12+)
- **Multi-Page Structure**: About, Research, Teaching, Outreach, CV (plus optional blog posts)
- **Custom Theme**: Academic MSU-branded responsive theme
- **Markdown Content**: Simple authoring workflow
- **Live Reload**: Development server auto rebuilds on changes
- **MSU Branding**: Spartan Green palette via CSS variables
- **Hero Profile Image**: Circular image on homepage (300px desktop / 225px mobile)
- **CV Page Support**: Dual-mode `cv.md` (PDF embed or Markdown sections)
- **Explicit `Summary:` Metadata**: Prevents duplicate rendered excerpts
- **Alternate Themes**: Neutral `minimal` theme and accessible `dark` theme alongside academic branding

## Quick Start

### Prerequisites

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

### Setup

```bash
git clone https://github.com/yourusername/python-website-prototype.git
cd python-website-prototype
uv sync
```

### Build

```bash
uv run python main.py build
```

Output is generated in `output/` (not committed).

### Development Server

```bash
uv run python main.py serve
```

Visit <http://localhost:8000> — changes rebuild automatically.

### Production Build

```bash
uv run python main.py publish
```

For a fully clean rebuild:

```bash
rm -rf output && uv run python main.py build
```

## Project Structure

```text
python-website-prototype/
├── content/
│   ├── pages/           # Static pages (About, Research, Teaching, Outreach, CV)
│   ├── articles/        # Blog posts (optional)
│   ├── images/          # Image assets (hero/profile placeholders)
│   └── files/           # Downloadable assets (e.g., cv.pdf)
├── themes/
│   └── academic/        # Custom academic theme
│       ├── templates/   # Jinja2 templates
│       └── static/      # CSS / JS (style.css, main.js)
├── main.py              # Build/serve/publish entry point
├── pelicanconf.py       # Development configuration
├── publishconf.py       # Production configuration
├── pyproject.toml       # Dependencies & project metadata
└── README.md            # Documentation
```

## Customization

### Site Configuration

Edit `pelicanconf.py` to set:

- `AUTHOR`
- `SITENAME`
- `SITESUBTITLE`
- `SOCIAL`
- `MENUITEMS` (navigation menu)

### Adding Pages

Create `content/pages/<slug>.md`:

```markdown
Title: Page Title
Slug: page-slug
Summary: Optional short summary (blank allowed)

Page body content here...
```

Notes:

- Omit a leading `# Page Title` heading — Pelican renders the title automatically.
- Always include the `Summary:` line (blank is fine) to prevent auto-generated duplication.
- The `Summary:` field for the About, Research, Teaching, and Outreach pages is displayed on the homepage. The About summary appears below the "About Me" heading, and the Research/Teaching/Outreach summaries appear in their respective tiles.

### Blog Posts

Create `content/articles/<slug>.md`:

```markdown
Title: Post Title
Date: 2025-01-01
Category: Category Name
Tags: tag1, tag2
Summary: Optional summary

Post body content...
```

### CV Page

`content/pages/cv.md` supports two modes:

1. **PDF Embed**: Place `cv.pdf` in `content/files/` and uncomment the embed block.
2. **Markdown Sections**: Fill the provided Education / Experience / Publications / Teaching / Awards / Service / Skills placeholders.

Already included in navigation.

### Hero / Profile Image

- Located in homepage template: `themes/academic/templates/index.html`.
- Replace placeholder (`hero-profile.svg`) with your image (JPG/PNG/SVG) placed in `content/images/` and adjust the filename if needed.
- Sizing & circular styling controlled by `.hero-profile-image` in `themes/academic/static/css/style.css` (300px desktop / 225px mobile).
- Vertical spacing tunable via `.hero` and `.intro` CSS rules.

### Theme Customization

- Styles: `themes/academic/static/css/style.css`
- Templates: `themes/academic/templates/`
- JavaScript: `themes/academic/static/js/main.js`
- Branding variables: defined in `:root` (e.g., `--color-primary`, `--color-accent`)
- Linkable headings: Wrap text in `<a>` (example: homepage “About Me”).

### Switching Themes

The config sets the active theme in `pelicanconf.py`:

```python
# pelicanconf.py
THEME = "themes/academic"  # switch to "themes/minimal" (neutral) or "themes/dark" (accessible dark variant)
```

Themes:

- `themes/academic`: MSU-branded, hero profile image, richer components.
- `themes/minimal`: Neutral palette, lean typography, simplified layout.
- `themes/dark`: Accessible dark palette, gradient hero, no profile hero image by default.

After changing `THEME`, rebuild:

```bash
rm -rf output && uv run python main.py build
```

## Troubleshooting

- Duplicate page content: Ensure a `Summary:` field exists (blank allowed).
- Changes not appearing: Clean build (`rm -rf output && uv run python main.py build`).
- CV PDF not showing: File must be at `content/files/cv.pdf` and `STATIC_PATHS` must include `"files"`.
- Hero image not circular/styled: Confirm filename in template matches file in `content/images/` and CSS class `.hero-profile-image` is present.
- Navigation missing: Add entry to `MENUITEMS` in `pelicanconf.py`.

## Publishing and Deployment

Once you've built and tested your site locally, you're ready to publish and deploy it to the web.

### 1. Build for Production

Generate optimized production files:

```bash
uv run python main.py publish
```

This command:

- Uses production settings from `publishconf.py` (absolute URLs, optimized paths)
- Generates the site in the `output/` directory
- Applies any production-specific configurations (feeds, analytics, etc.)

For a completely clean production build:

```bash
rm -rf output && uv run python main.py publish
```

### 2. Choose a Hosting Provider

The `output/` directory contains a complete static website that can be deployed to any static hosting service:

#### GitHub Pages (Free)

1. **Create a repository**: `<username>.github.io` or use a project repo with GitHub Pages enabled
2. **Configure `publishconf.py`**:

   ```python
   SITEURL = "https://<username>.github.io"  # or https://<username>.github.io/<repo>
   ```

3. **Deploy**:

   ```bash
   # Option A: Push output/ to gh-pages branch
   uv run python main.py publish
   cd output
   git init
   git add -A
   git commit -m "Deploy website"
   git branch -M gh-pages
   git remote add origin https://github.com/<username>/<repo>.git
   git push -f origin gh-pages
   
   # Option B: Use GitHub Actions (recommended)
   # Add .github/workflows/deploy.yml to automate builds on push
   ```

4. **Enable GitHub Pages**: Repository Settings → Pages → Source: `gh-pages` branch

#### Netlify (Free tier available)

1. **Sign up** at [netlify.com](https://www.netlify.com/)
2. **Connect repository** or drag-and-drop `output/` folder
3. **Configure build settings** (if using continuous deployment):
   - Build command: `uv run python main.py publish`
   - Publish directory: `output`
4. **Deploy**: Netlify automatically deploys and provides HTTPS + CDN

#### Vercel (Free tier available)

1. **Sign up** at [vercel.com](https://vercel.com/)
2. **Import repository**
3. **Configure**:
   - Framework Preset: Other
   - Build Command: `uv run python main.py publish`
   - Output Directory: `output`
4. **Deploy**: Automatic deployments on git push

#### AWS S3 + CloudFront (Pay-as-you-go)

1. **Create S3 bucket** with static website hosting enabled
2. **Upload `output/` contents**:

   ```bash
   aws s3 sync output/ s3://your-bucket-name/ --delete
   ```

3. **Optional**: Configure CloudFront CDN for HTTPS and caching
4. **Automate**: Use GitHub Actions or CI/CD to sync on changes

#### Traditional Web Hosting

Upload `output/` contents via FTP/SFTP to your web host's `public_html` or `www` directory.

### 3. Update URLs for Production

Before deploying, ensure `publishconf.py` has the correct `SITEURL`:

```python
# publishconf.py
SITEURL = "https://yourdomain.com"  # Update with your actual domain
RELATIVE_URLS = False
```

After updating, rebuild:

```bash
uv run python main.py publish
```

### 4. Continuous Deployment (Recommended)

Automate builds and deployments with GitHub Actions:

**Example `.github/workflows/deploy.yml`:**

```yaml
name: Deploy Website

on:
  push:
    branches: [main]

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        run: curl -LsSf https://astral.sh/uv/install.sh | sh
      
      - name: Build site
        run: |
          uv sync
          uv run python main.py publish
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./output
```

This workflow automatically builds and deploys your site whenever you push to the `main` branch.

### 5. Custom Domain (Optional)

Most hosting providers support custom domains:

- **GitHub Pages**: Add `CNAME` file to `output/` with your domain, configure DNS
- **Netlify/Vercel**: Add domain in dashboard, follow DNS instructions
- **CloudFront**: Configure alternate domain names (CNAMEs) and SSL certificate

### Deployment Checklist

- [ ] Run `uv run python main.py publish` to generate production build
- [ ] Verify `SITEURL` in `publishconf.py` matches your domain
- [ ] Test `output/index.html` locally (open in browser or use `python -m http.server -d output`)
- [ ] Upload/deploy `output/` directory to hosting provider
- [ ] Configure HTTPS (most hosts provide free SSL certificates)
- [ ] Test all pages and links in production
- [ ] Optional: Set up continuous deployment for automatic updates

## License

Open source; feel free to adapt for your own professional website.
