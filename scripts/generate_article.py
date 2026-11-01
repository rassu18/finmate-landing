#!/usr/bin/env python3
"""
Automated SEO Article & Banner Generator for SpendSathi Blog.
Generates comprehensive Jekyll blog articles formatted with full IST timestamps,
'published: true' flags, accompanying 1200x630 vector SVG header banners,
and optional WebP banners using Pillow.

Supports dynamic generation via Google Gemini or OpenAI when API keys are present,
with an automated editorial queue fallback to guarantee scheduled publishing.
"""

import os
import sys
import json
import glob
import re
import argparse
from datetime import datetime
import zoneinfo

IST = zoneinfo.ZoneInfo("Asia/Kolkata")

# Editorial queue of curated, evergreen topics for SpendSathi
EDITORIAL_QUEUE = [
    {
        "title": "The Debt Avalanche vs Snowball Method: How to Pay Off Credit Cards in India",
        "slug": "debt-avalanche-vs-snowball-india",
        "category": "DEBT MANAGEMENT",
        "author": "Mohit Varma",
        "excerpt": "Struggling with high-interest credit card revolving balances and personal loans? Here is how to choose between the Debt Avalanche and Debt Snowball methods tailored to Indian interest rates, and how local expense tracking keeps you accountable.",
        "tags": ["debt management", "credit cards", "personal finance", "debt avalanche", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Debt Avalanche vs Snowball",
        "svg_headline_2": "for Indian Earners",
        "svg_subtitle_1": "Mathematically eliminate credit card debt and high-interest personal loans,",
        "svg_subtitle_2": "and why 100% private offline tracking guarantees financial consistency.",
        "body": """High-interest debt is the greatest obstacle to building sustainable wealth. In India's post-UPI lending boom, pre-approved personal loans, 'Buy Now Pay Later' (BNPL) schemes, and revolving credit card balances at 36% to 42% APR trap thousands of ambitious professionals in an endless cycle of minimum dues.

If you are carrying multiple balances across credit cards and personal loans, throwing random surplus money at them rarely works. You need a systematic, mathematically proven debt reduction strategy.

Two dominant methodologies exist: the **Debt Avalanche** and the **Debt Snowball**. Here is how to choose the right strategy for your psychological profile and financial reality.

---

## 1. The Debt Avalanche: Mathematical Optimality

The Debt Avalanche prioritizes debt strictly by **Annual Percentage Rate (APR)**, from highest to lowest:

1. List all your outstanding debts with their exact interest rates and minimum monthly obligations.
2. Pay the absolute minimum due on every debt except the one with the highest interest rate.
3. Direct every single surplus rupee from your monthly budget to attack the highest-interest loan until it is completely eliminated.
4. Once cleared, roll that entire monthly payment into the loan with the next highest rate.

### The Math in Action
Suppose you have:
* **Credit Card A:** ₹60,000 balance at **42% APR** (Min due: ₹3,000)
* **Personal Loan:** ₹2,00,000 balance at **14% APR** (EMI: ₹7,000)
* **Car Loan:** ₹3,50,000 balance at **9.5% APR** (EMI: ₹9,500)

Under the Avalanche method, you channel all surplus funds aggressively toward Credit Card A. Because 42% compounding drains your net worth the fastest, eliminating it first minimizes total interest paid across the life of your debt.

---

## 2. The Debt Snowball: Behavioral Momentum

While the Avalanche is mathematically superior, human psychology does not always operate like a spreadsheet. Financial researcher Dave Ramsey popularized the **Debt Snowball**, which organizes balances strictly by **total balance amount**, from smallest to largest:

1. List debts in order of balance size, regardless of the interest rate.
2. Pay minimum dues on everything.
3. Attack the smallest balance with aggressive intensity until it hits zero.
4. Celebrate the win and roll the released cash flow into the next smallest balance.

### Why the Snowball Works
If you feel overwhelmed by five different monthly dues, the cognitive relief of wiping out an entire balance within two months provides an immense psychological boost. That emotional win creates momentum that keeps you disciplined for larger debts.

---

## 3. Which Method Should You Choose?

* **Choose the Avalanche** if you are analytical, disciplined, and motivated by raw numbers and minimizing interest expense.
* **Choose the Snowball** if you are emotionally exhausted by multiple dues and need quick, tangible psychological victories to stay committed.

Whichever path you choose, the golden rule remains: **never take on new uncollateralized debt while paying off existing loans.**

---

## The Role of Private, Offline Tracking in Debt Freedom

The most common reason debt payoff plans fail is unexpected everyday spending. You budget ₹15,000 for extra debt payments, but fifteen micro-UPI transactions silently drain your checking account before month-end.

Many people try to fix this by installing cloud personal finance apps, only to realize that their private financial records, credit limits, and bank alerts are harvested and monetized for more pre-approved loan advertisements.

**SpendSathi solves this through 100% offline local privacy:**
* **Instant Bank SMS Alerts:** SpendSathi captures every debit alert locally on your Android device without cloud uploads.
* **Zero Credit Card Ads:** Because SpendSathi does not sync your data to remote servers, you are never targeted with predatory personal loan or credit card offers.
* **Real-Time Envelope Visibility:** Know immediately if daily dining or entertainment spends are encroaching on your monthly debt repayment fund.

Install **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to take back control of your financial destiny today.
"""
    },
    {
        "title": "Emergency Funds in 2026: The Liquid Safety Net Every Indian Professional Needs",
        "slug": "emergency-funds-liquid-safety-net-india",
        "category": "FINANCIAL SECURITY",
        "author": "Mohit Varma",
        "excerpt": "How much cash should you hold in reserve during uncertain economic times? Here is how to structure a bulletproof emergency fund across liquid mutual funds and high-yield savings without risking market volatility.",
        "tags": ["emergency fund", "savings", "financial planning", "liquid funds", "SpendSathi"],
        "read_time": "6 min read",
        "svg_headline_1": "Emergency Funds 2026",
        "svg_headline_2": "The Liquid Safety Net",
        "svg_subtitle_1": "How much cash reserve do you actually need in modern India,",
        "svg_subtitle_2": "and why keeping your financial tracking private protects your peace of mind.",
        "body": """In personal finance, an emergency fund is your financial seatbelt. Whether it is sudden medical deductibles, unexpected home repairs, or an unexpected career transition, having accessible cash reserves prevents you from liquidating long-term investments at market bottoms.

Here is a practical guide to calculating, building, and parking your emergency fund in 2026.

---

## How Much Runway Do You Really Need?

Traditional Western guidelines recommend holding 3 to 6 months of living expenses. However, given private healthcare costs and variable employment markets in India, a safer tier system is recommended:

* **Dual-Income Household, No Dependents:** 4 to 6 months of mandatory living expenses.
* **Single Earner with Dependents (Parents / Children):** 6 to 9 months of expenses.
* **Freelancers, Contractors & Startup Founders:** 9 to 12 months of mandatory outflows.

Mandatory expenses include rent, loan EMIs, insurance premiums, basic groceries, utilities, and schooling costs. Discretionary expenses (dining out, OTT subscriptions, weekend trips) are excluded from the runway calculation.

---

## Where to Park Your Emergency Fund

An emergency fund must prioritize **capital preservation and instant liquidity** over aggressive returns:

1. **Tier 1 (Instant Access - 20% to 30%):** Park in a high-interest savings account or auto-sweep fixed deposit linked to your primary bank. This must be accessible via ATM or UPI at 2:00 AM on a Sunday.
2. **Tier 2 (T+1 Liquidity - 70% to 80%):** Invest in high-quality Liquid Mutual Funds or Arbitrage Funds. These provide steady yields while allowing withdrawal within 24 business hours without exit loads after seven days.

Never invest emergency reserves in equity mutual funds, crypto, or locked-in tax-saving instruments like PPF or ELSS.

---

## Protect Your Emergency Fund from Daily Creep

The greatest danger to an emergency reserve is the temptation to borrow from it for non-emergencies. 

Using **SpendSathi's local offline expense tracker**, you can separate your operational spending envelopes from your reserve funds. Because SpendSathi categorizes your UPI transactions on-device without cloud sync, you enjoy full clarity without compromising your privacy.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to track your savings journey today.
"""
    }
]


def generate_svg_banner(data, output_path):
    """Generate crisp, modern 1200x630 SVG hero banner matching SpendSathi editorial style."""
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <radialGradient id="bg" cx="25%" cy="45%" r="75%">
      <stop offset="0%" stop-color="#1E293B"/>
      <stop offset="100%" stop-color="#0F172A"/>
    </radialGradient>
    <pattern id="grid" x="0" y="0" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#334155" opacity="0.45"/>
    </pattern>
    <radialGradient id="glow-green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#16A34A" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="#16A34A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow-gold" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#EAB308" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#EAB308" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#06B6D4" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur24">
      <feGaussianBlur stdDeviation="24"/>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect width="1200" height="630" fill="url(#grid)"/>

  <ellipse cx="280" cy="310" rx="300" ry="250" fill="url(#glow-green)" filter="url(#blur24)"/>
  <ellipse cx="960" cy="280" rx="280" ry="260" fill="url(#glow-gold)" filter="url(#blur24)"/>
  <ellipse cx="850" cy="460" rx="200" ry="180" fill="url(#glow-cyan)" filter="url(#blur24)"/>

  <!-- Left Content: Editorial Typography -->
  <rect x="80" y="115" width="240" height="36" rx="18" fill="#14532D" stroke="#22C55E" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="102" cy="133" r="5" fill="#4ADE80"/>
  <text x="118" y="138" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#BBF7D0" letter-spacing="1.5">{data.get('category', 'PERSONAL FINANCE')}</text>

  <text x="80" y="210" font-family="'Inter', system-ui, sans-serif" font-size="46" font-weight="800" fill="#FFFFFF" letter-spacing="-1">{data.get('svg_headline_1', data['title'][:32])}</text>
  <text x="80" y="275" font-family="'Inter', system-ui, sans-serif" font-size="46" font-weight="800" fill="#FFFFFF" letter-spacing="-1"><tspan fill="#22C55E">{data.get('svg_headline_2', '')}</tspan></text>

  <text x="80" y="340" font-family="'Inter', system-ui, sans-serif" font-size="19" fill="#94A3B8" font-weight="400">{data.get('svg_subtitle_1', '')}</text>
  <text x="80" y="370" font-family="'Inter', system-ui, sans-serif" font-size="19" fill="#94A3B8" font-weight="400">{data.get('svg_subtitle_2', '')}</text>

  <line x1="80" y1="415" x2="600" y2="415" stroke="#334155" stroke-width="1.5"/>

  <g transform="translate(80, 445)">
    <circle cx="16" cy="16" r="16" fill="#1E293B" stroke="#334155"/>
    <text x="16" y="21" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#22C55E" text-anchor="middle">MV</text>
    <text x="44" y="21" font-family="'Inter', system-ui, sans-serif" font-size="15" fill="#CBD5E1" font-weight="500">By {data['author']} • {data.get('read_time', '6 min read')}</text>
  </g>

  <g transform="translate(80, 560)">
    <text x="0" y="0" font-family="'Inter', system-ui, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Spend<tspan fill="#22C55E">Sathi</tspan></text>
    <text x="125" y="-1" font-family="'Inter', system-ui, sans-serif" font-size="14" fill="#64748B">• Private Local-First Expense Tracking</text>
  </g>
</svg>"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG Banner: {output_path}")


def generate_webp_banner(data, output_path):
    """Generate sleek, high-res WebP banner using Pillow if available."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        img = Image.new('RGB', (1200, 630), color='#0F172A')
        draw = ImageDraw.Draw(img)

        # Gradient background
        for i in range(1200):
            ratio = i / 1200
            r = int(15 + ratio * 15)
            g = int(23 + ratio * 40)
            b = int(42 + ratio * 30)
            draw.line([(i, 0), (i, 630)], fill=(r, g, b))

        overlay = Image.new('RGBA', (1200, 630), (0, 0, 0, 0))
        draw_ov = ImageDraw.Draw(overlay)
        draw_ov.ellipse([800, 50, 1150, 400], fill=(22, 163, 74, 45))
        draw_ov.ellipse([850, 300, 1100, 550], fill=(6, 182, 212, 35))
        img.paste(Image.alpha_composite(Image.new('RGBA', (1200, 630), (0, 0, 0, 0)), overlay).convert('RGB'), (0, 0))

        draw = ImageDraw.Draw(img)
        try:
            font_large = ImageFont.truetype('arial.ttf', 44)
            font_sub = ImageFont.truetype('arial.ttf', 22)
            font_badge = ImageFont.truetype('arial.ttf', 16)
        except Exception:
            font_large = font_sub = font_badge = ImageFont.load_default()

        draw.rounded_rectangle([80, 90, 340, 126], radius=18, fill='#14532D', outline='#22C55E')
        draw.text((100, 98), data.get('category', 'SMART MONEY GUIDE'), fill='#BBF7D0', font=font_badge)

        draw.text((80, 170), data.get('svg_headline_1', data['title'][:32]), fill='#FFFFFF', font=font_large)
        draw.text((80, 230), data.get('svg_headline_2', ''), fill='#22C55E', font=font_large)
        draw.text((80, 310), data.get('svg_subtitle_1', ''), fill='#94A3B8', font=font_sub)
        draw.text((80, 345), data.get('svg_subtitle_2', ''), fill='#94A3B8', font=font_sub)

        draw.line([(80, 410), (550, 410)], fill='#334155', width=2)
        draw.text((80, 435), f"By {data['author']} • {data.get('read_time', '6 min read')}", fill='#CBD5E1', font=font_sub)
        draw.text((80, 550), 'SpendSathi • Private Offline Expense Tracking', fill='#22C55E', font=font_sub)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, 'WEBP', quality=90)
        print(f"Generated WebP Banner: {output_path}")
        return True
    except Exception as e:
        print(f"WebP generation skipped: {e}")
        return False


def generate_markdown_post(data, output_path, timestamp_str):
    """Generate Markdown post with fully qualified IST timestamp and published: true."""
    tags_formatted = ", ".join(data.get("tags", ["budgeting", "personal finance", "SpendSathi"]))
    image_rel = f"/assets/images/blog/{data['slug']}.webp"

    front_matter = f"""---
layout: post
title: "{data['title']}"
date: {timestamp_str}
author: "{data['author']}"
image: {image_rel}
categories: [budgeting, personal-finance]
tags: [{tags_formatted}]
published: true
excerpt: "{data['excerpt']}"
---

{data['body'].strip()}
"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
    print(f"Generated Markdown Post: {output_path}")


def get_existing_slugs(posts_dir):
    """Scan existing posts to prevent duplicating slugs."""
    slugs = set()
    for p in glob.glob(os.path.join(posts_dir, "*.md")):
        name = os.path.basename(p)
        m = re.match(r'^\d{4}-\d{2}-\d{2}-(.*)\.md$', name)
        if m:
            slugs.add(m.group(1))
    return slugs


def try_llm_generation(existing_slugs):
    """Attempt dynamic article generation if GEMINI_API_KEY or OPENAI_API_KEY is available."""
    gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
    openai_key = os.environ.get("OPENAI_API_KEY", "").strip()

    prompt = (
        "You are an expert personal finance author for SpendSathi (https://spendsathi.com), an offline "
        "Android expense tracker with on-device SMS parsing for Indian UPI users. Write an engaging, practical, "
        "800+ word article on personal finance tailored for Indian salaried professionals and digital payment users. "
        "Return STRICT JSON with keys: title, slug, category, author, excerpt, tags (array), read_time, "
        "svg_headline_1, svg_headline_2, svg_subtitle_1, svg_subtitle_2, body (markdown text)."
    )

    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(
                prompt + " Ensure the output is valid JSON only without markdown code fence."
            )
            raw = response.text.strip()
            if raw.startswith("```"):
                raw = re.sub(r"^```[a-z]*\n?", "", raw)
                raw = re.sub(r"\n?```$", "", raw)
            data = json.loads(raw)
            if data.get("slug") and data["slug"] not in existing_slugs:
                print(f"Successfully generated article via Google Gemini API: {data['title']}")
                return data
        except Exception as e:
            print(f"Gemini generation fallback: {e}")

    if openai_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=openai_key)
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "You are a professional personal finance writer for SpendSathi. Output valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            data = json.loads(completion.choices[0].message.content)
            if data.get("slug") and data["slug"] not in existing_slugs:
                print(f"Successfully generated article via OpenAI API: {data['title']}")
                return data
        except Exception as e:
            print(f"OpenAI generation fallback: {e}")

    return None


def select_editorial_article(existing_slugs):
    """Select the first unposted article from the curated editorial queue."""
    for article in EDITORIAL_QUEUE:
        if article["slug"] not in existing_slugs:
            return article
    return None


def main():
    parser = argparse.ArgumentParser(description="SpendSathi Blog Article Generator")
    parser.add_argument("--date", help="Custom timestamp in 'YYYY-MM-DD HH:MM:SS +0530' format")
    parser.add_argument("--force", action="store_true", help="Force generate even if already posted today")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(repo_root, "_posts")
    svg_dir = os.path.join(repo_root, "assets", "blog-images")
    webp_dir = os.path.join(repo_root, "assets", "images", "blog")

    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(webp_dir, exist_ok=True)

    if args.date:
        timestamp_str = args.date
        date_part = timestamp_str.split(" ")[0]
    else:
        now = datetime.now(IST)
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S +0530")
        date_part = now.strftime("%Y-%m-%d")

    existing_slugs = get_existing_slugs(posts_dir)
    print(f"Found {len(existing_slugs)} existing articles in _posts/")

    # 1. Try dynamic LLM generation first
    data = try_llm_generation(existing_slugs)

    # 2. Fall back to editorial queue if LLM unavailable
    if not data:
        data = select_editorial_article(existing_slugs)

    if not data:
        print("No new unique articles to generate at this time. All queue articles are published.")
        return

    # Check if this slug already exists for today
    md_filename = f"{date_part}-{data['slug']}.md"
    md_path = os.path.join(posts_dir, md_filename)
    if os.path.exists(md_path) and not args.force:
        print(f"Article {md_filename} already exists. Skipping duplicate generation.")
        return

    svg_filename = f"{data['slug']}.svg"
    webp_filename = f"{data['slug']}.webp"

    svg_path = os.path.join(svg_dir, svg_filename)
    webp_path1 = os.path.join(webp_dir, webp_filename)
    webp_path2 = os.path.join(svg_dir, webp_filename)

    generate_svg_banner(data, svg_path)
    generate_webp_banner(data, webp_path1)
    generate_webp_banner(data, webp_path2)
    generate_markdown_post(data, md_path, timestamp_str)

    print("\nGeneration summary:")
    print(f"  Post file:   {md_filename}")
    print(f"  Timestamp:   {timestamp_str}")
    print(f"  Published:   true")
    print(f"  Banner WebP: {webp_path1}")


if __name__ == "__main__":
    main()
