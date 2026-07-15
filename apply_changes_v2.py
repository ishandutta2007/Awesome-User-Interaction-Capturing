import os
import re
import subprocess

DIR = r"C:\Users\ishan\Documents\Projects\Awesome-User-Interaction-Capturing"
README = os.path.join(DIR, "README.md")

def run_git(commit_msg):
    subprocess.run(["git", "add", "."], cwd=DIR, check=False)
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=DIR, check=False)
    subprocess.run(["git", "push"], cwd=DIR, check=False)

def update_file(content):
    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

with open(README, "r", encoding="utf-8") as f:
    content = f.read()

# Task 1: SaaS Table update
table_regex = re.compile(r'\| Tool \| Description \| Pricing \| Free Tier Limit \|\n\|---\|---\|---\|---\|\n(.*?)\n\n', re.DOTALL)

new_table = """| Tool | Description | Pricing | Free Tier Limit | Company Size / Valuation |
|---|---|---|---|---|
| **Microsoft Clarity** | Session replay and heatmaps. | Free | Unlimited | ~$3 Trillion (Microsoft) |
| **Hotjar** | User behavior analytics and feedback tool. | Freemium / Usage-based | 35 daily sessions | ~$5.4 Billion (Contentsquare) |
| **[Contentsquare](https://contentsquare.com)**| Enterprise session replay and digital experience analytics. | Custom / Enterprise | None | ~$5.4 Billion |
| **[Pendo](https://pendo.io)** | Mobile/web heatmaps, recordings, and in-app guidance. | Freemium / Usage-based | 500 MAUs | ~$2.6 Billion |
| **[FullStory](https://fullstory.com)** | Enterprise session replay and digital experience analytics. | Freemium / Custom | 30,000 sessions/mo | ~$1.8 Billion |
| **[Amplitude](https://amplitude.com)** | Event-based behavioral analytics with strong visualization. | Freemium / Usage-based | 10,000 MTUs, 2M events/mo | ~$1.5 Billion |
| **[Mixpanel](https://mixpanel.com)** | Event-based behavioral analytics with strong visualization. | Freemium / Usage-based | 20M events/mo | ~$1.05 Billion |
| **[PostHog](https://posthog.com)** | All-in-one with session replay, product analytics, feature flags, and A/B testing. | Freemium / Usage-based | 1M events, 5k replays/mo | ~$1 Billion |
| **[Glassbox](https://glassbox.com)** | Enterprise session replay and digital experience analytics. | Custom / Enterprise | None | ~$400 Million |
| **[LogRocket](https://logrocket.com)** | Session replay with debugging and performance insights. | Freemium / Usage-based | 1,000 sessions/mo | ~$200 Million |
| **[Smartlook](https://smartlook.com)** | Mobile/web heatmaps, recordings, and in-app guidance. | Freemium / Usage-based | 3,000 sessions/mo | ~$50 Million |
| **[Matomo](https://matomo.org)** | Privacy-focused analytics with heatmaps and session recordings. | Paid (Cloud) / Free (Self-hosted) | None (Cloud) | ~$10 Million |
"""

content = re.sub(r'\| Tool \| Description \| Pricing \| Free Tier Limit \|\n\|---\|---\|---\|---\|\n(?:.*?)\n\n', new_table + '\n', content, flags=re.DOTALL)
update_file(content)
run_git("Added company size and sorted the SaaS based on that")


# Task 2: Open Source Stars
os_section = """### Featured Projects

- **[Umami](https://umami.is)** [![Stars](https://img.shields.io/github/stars/umami-software/umami?style=social&color=white)](https://github.com/umami-software/umami/stargazers) — Simple, self-hosted web analytics with clean dashboards.
- **[PostHog](https://posthog.com)** [![Stars](https://img.shields.io/github/stars/PostHog/posthog?style=social&color=white)](https://github.com/PostHog/posthog/stargazers) — Leading open-source platform with session replay, autocapture, heatmaps, product analytics, and feature flags. Self-host or cloud.
- **[Matomo](https://matomo.org)** [![Stars](https://img.shields.io/github/stars/matomo-org/matomo?style=social&color=white)](https://github.com/matomo-org/matomo/stargazers) — Full-featured open-source analytics with heatmaps, session recordings, and privacy controls. Self-hosted option is powerful.
- **[Plausible](https://plausible.io)** [![Stars](https://img.shields.io/github/stars/plausible/analytics?style=social&color=white)](https://github.com/plausible/analytics/stargazers) — Lightweight privacy-focused analytics (web-focused, extensible).
- **[OpenReplay](https://openreplay.com)** [![Stars](https://img.shields.io/github/stars/openreplay/openreplay?style=social&color=white)](https://github.com/openreplay/openreplay/stargazers) — Open-source session replay and analytics suite with dev tools, rage click detection, and performance monitoring.
"""

content = re.sub(r'### Featured Projects\n\n- \*\*(.*?)- \*\*\[Umami\](.*?)dashboards\.', os_section, content, flags=re.DOTALL)
update_file(content)
run_git("Added github stars and sorted the opensource based on that")


# Task 3: Banner
assets_dir = os.path.join(DIR, "assets")
os.makedirs(assets_dir, exist_ok=True)
svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(131,58,180);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(253,29,29);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(252,176,69);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="40" fill="white" font-weight="bold">
    Awesome User Interaction Capturing
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" />
  </text>
</svg>'''
with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_banner)

content = "![Banner](assets/banner.svg)\n\n" + content
update_file(content)
run_git("added banner")


# Task 4: Emojis
content = content.replace("# Awesome-User-Interaction-Capturing", "🚀 # Awesome-User-Interaction-Capturing 🚀")
content = content.replace("## Top User Interaction Capturing", "🌟 ## Top User Interaction Capturing")
content = content.replace("## SaaS / Cloud-Hosted", "☁️ ## SaaS / Cloud-Hosted")
content = content.replace("### Leading Options & Notables", "🏆 ### Leading Options & Notables")
content = content.replace("## Open-Source / Self-Hosted", "🔓 ## Open-Source / Self-Hosted")
content = content.replace("### Featured Projects", "⭐ ### Featured Projects")
content = content.replace("## Comparison", "⚖️ ## Comparison")
content = content.replace("## Getting Started", "🏁 ## Getting Started")
content = content.replace("## Contributing", "🤝 ## Contributing")
update_file(content)
run_git("added emojis")


# Task 5: SEO
seo_tags = "<!-- SEO: awesome list, user interaction, session replay, heatmaps, product analytics, open-source analytics, SaaS analytics, Matomo, PostHog, Hotjar alternatives -->\n"
content = seo_tags + content
update_file(content)
run_git("seo optimised")


# Task 6: Badges left
badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
content = content.replace("🚀 # Awesome-User-Interaction-Capturing 🚀\n", f"🚀 # Awesome-User-Interaction-Capturing 🚀\n\n<div align=\"center\">\n{badges_left}\n</div>\n")
update_file(content)
run_git("badges to left added")


# Task 7: Badges right
badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
content = content.replace("</div>\n", f" {badge_right}\n</div>\n")
update_file(content)
run_git("badges to right added")


# Task 8: Star History
star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-User-Interaction-Capturing&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-User-Interaction-Capturing&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-User-Interaction-Capturing&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-User-Interaction-Capturing&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
content += star_history
update_file(content)
run_git("star history added")


# Task 9: chartrepos -> chart?repos
content = content.replace("chartrepos", "chart?repos")
update_file(content)
run_git("fixed star plot")


# Task 10: awesome link
content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
update_file(content)
run_git("invalid awesome link fixed")

print("All tasks completed.")
