#!/usr/bin/env python3
"""
Automated SEO Article & Banner Generator for SpendSathi Blog.
Generates comprehensive Jekyll blog articles formatted with full IST timestamps,
'published: true' flags, accompanying 1200x630 vector SVG header banners,
and high-resolution WebP banners using Pillow.

Features:
- Dynamic theme palettes (emerald, amethyst, amber, cyan, crimson, teal, bronze, indigo)
  so every article banner has distinct branding, colors, and visual mood.
- Tailored right-side vector illustrations for each topic (SIP chart, credit card payoff,
  safety vault, credit score gauge, subscription radar, budget donut, gold scales, etc.).
- Robust multi-font support for both Linux (GitHub Actions) and Windows.
- Large curated editorial queue of 16+ evergreen Indian personal finance articles so
  automated bi-weekly publishing runs seamlessly for months even without LLM keys.
- Dynamic generation via Google Gemini or OpenAI when API keys are available.
"""

import os
import sys
import json
import glob
import re
import math
import shutil
import argparse
from datetime import datetime
import zoneinfo
from PIL import Image, ImageDraw, ImageFont

IST = zoneinfo.ZoneInfo("Asia/Kolkata")

# Visual theme palettes for banner generation
THEME_PALETTES = {
    "emerald": {
        "name": "Emerald / Mint",
        "bg_start": (6, 29, 26),
        "bg_end": (11, 47, 41),
        "bg_svg_start": "#061D1A",
        "bg_svg_end": "#0B2F29",
        "glow1_hex": "#10B981",
        "glow2_hex": "#06B6D4",
        "glow1_rgb": (16, 185, 129),
        "glow2_rgb": (6, 182, 212),
        "primary": "#10B981",
        "primary_rgb": (16, 185, 129),
        "accent": "#34D399",
        "accent_rgb": (52, 211, 153),
        "badge_bg": "#064E3B",
        "badge_bg_rgb": (6, 78, 59),
        "badge_border": "#10B981",
        "badge_border_rgb": (16, 185, 129),
        "badge_text": "#BBF7D0",
        "badge_text_rgb": (187, 247, 208),
        "card_bg_rgb": (11, 54, 47),
        "card_border_rgb": (16, 185, 129),
    },
    "amethyst": {
        "name": "Amethyst / Violet",
        "bg_start": (24, 8, 41),
        "bg_end": (36, 16, 59),
        "bg_svg_start": "#180829",
        "bg_svg_end": "#24103B",
        "glow1_hex": "#A855F7",
        "glow2_hex": "#F59E0B",
        "glow1_rgb": (168, 85, 247),
        "glow2_rgb": (245, 158, 11),
        "primary": "#A855F7",
        "primary_rgb": (168, 85, 247),
        "accent": "#C084FC",
        "accent_rgb": (192, 132, 252),
        "badge_bg": "#3B0764",
        "badge_bg_rgb": (59, 7, 100),
        "badge_border": "#A855F7",
        "badge_border_rgb": (168, 85, 247),
        "badge_text": "#E9D5FF",
        "badge_text_rgb": (233, 213, 255),
        "card_bg_rgb": (42, 19, 68),
        "card_border_rgb": (168, 85, 247),
    },
    "amber": {
        "name": "Amber / Gold",
        "bg_start": (28, 18, 6),
        "bg_end": (46, 30, 9),
        "bg_svg_start": "#1C1206",
        "bg_svg_end": "#2E1E09",
        "glow1_hex": "#F59E0B",
        "glow2_hex": "#EF4444",
        "glow1_rgb": (245, 158, 11),
        "glow2_rgb": (239, 68, 68),
        "primary": "#F59E0B",
        "primary_rgb": (245, 158, 11),
        "accent": "#FBBF24",
        "accent_rgb": (251, 191, 36),
        "badge_bg": "#451A03",
        "badge_bg_rgb": (69, 26, 3),
        "badge_border": "#F59E0B",
        "badge_border_rgb": (245, 158, 11),
        "badge_text": "#FEF3C7",
        "badge_text_rgb": (254, 243, 199),
        "card_bg_rgb": (56, 36, 13),
        "card_border_rgb": (245, 158, 11),
    },
    "cyan": {
        "name": "Electric Cyan / Sky",
        "bg_start": (6, 24, 38),
        "bg_end": (10, 37, 58),
        "bg_svg_start": "#061826",
        "bg_svg_end": "#0A253A",
        "glow1_hex": "#06B6D4",
        "glow2_hex": "#10B981",
        "glow1_rgb": (6, 182, 212),
        "glow2_rgb": (16, 185, 129),
        "primary": "#06B6D4",
        "primary_rgb": (6, 182, 212),
        "accent": "#38BDF8",
        "accent_rgb": (56, 189, 248),
        "badge_bg": "#082F49",
        "badge_bg_rgb": (8, 47, 73),
        "badge_border": "#06B6D4",
        "badge_border_rgb": (6, 182, 212),
        "badge_text": "#CFFAFE",
        "badge_text_rgb": (207, 250, 254),
        "card_bg_rgb": (14, 51, 77),
        "card_border_rgb": (6, 182, 212),
    },
    "crimson": {
        "name": "Crimson / Coral",
        "bg_start": (36, 7, 18),
        "bg_end": (59, 15, 32),
        "bg_svg_start": "#240712",
        "bg_svg_end": "#3B0F20",
        "glow1_hex": "#E11D48",
        "glow2_hex": "#F59E0B",
        "glow1_rgb": (225, 29, 72),
        "glow2_rgb": (245, 158, 11),
        "primary": "#E11D48",
        "primary_rgb": (225, 29, 72),
        "accent": "#FB7185",
        "accent_rgb": (251, 113, 133),
        "badge_bg": "#4C0519",
        "badge_bg_rgb": (76, 5, 25),
        "badge_border": "#E11D48",
        "badge_border_rgb": (225, 29, 72),
        "badge_text": "#FFE4E6",
        "badge_text_rgb": (255, 228, 230),
        "card_bg_rgb": (69, 18, 38),
        "card_border_rgb": (225, 29, 72),
    },
    "teal": {
        "name": "Teal / Mint",
        "bg_start": (4, 29, 29),
        "bg_end": (11, 45, 44),
        "bg_svg_start": "#041D1D",
        "bg_svg_end": "#0B2D2C",
        "glow1_hex": "#14B8A6",
        "glow2_hex": "#38BDF8",
        "glow1_rgb": (20, 184, 166),
        "glow2_rgb": (56, 189, 248),
        "primary": "#14B8A6",
        "primary_rgb": (20, 184, 166),
        "accent": "#2DD4BF",
        "accent_rgb": (45, 212, 191),
        "badge_bg": "#134E4A",
        "badge_bg_rgb": (19, 78, 74),
        "badge_border": "#14B8A6",
        "badge_border_rgb": (20, 184, 166),
        "badge_text": "#CCFBF1",
        "badge_text_rgb": (204, 251, 241),
        "card_bg_rgb": (14, 61, 59),
        "card_border_rgb": (20, 184, 166),
    },
    "bronze": {
        "name": "Warm Gold / Bronze",
        "bg_start": (26, 20, 8),
        "bg_end": (41, 31, 14),
        "bg_svg_start": "#1A1408",
        "bg_svg_end": "#291F0E",
        "glow1_hex": "#D97706",
        "glow2_hex": "#10B981",
        "glow1_rgb": (217, 119, 6),
        "glow2_rgb": (16, 185, 129),
        "primary": "#D97706",
        "primary_rgb": (217, 119, 6),
        "accent": "#F59E0B",
        "accent_rgb": (245, 158, 11),
        "badge_bg": "#451A03",
        "badge_bg_rgb": (69, 26, 3),
        "badge_border": "#D97706",
        "badge_border_rgb": (217, 119, 6),
        "badge_text": "#FEF3C7",
        "badge_text_rgb": (254, 243, 199),
        "card_bg_rgb": (51, 38, 18),
        "card_border_rgb": (217, 119, 6),
    },
    "indigo": {
        "name": "Indigo / Cyber Blue",
        "bg_start": (11, 16, 40),
        "bg_end": (22, 27, 61),
        "bg_svg_start": "#0B1028",
        "bg_svg_end": "#161B3D",
        "glow1_hex": "#6366F1",
        "glow2_hex": "#10B981",
        "glow1_rgb": (99, 102, 241),
        "glow2_rgb": (16, 185, 129),
        "primary": "#6366F1",
        "primary_rgb": (99, 102, 241),
        "accent": "#818CF8",
        "accent_rgb": (129, 140, 248),
        "badge_bg": "#1E1B4B",
        "badge_bg_rgb": (30, 27, 75),
        "badge_border": "#6366F1",
        "badge_border_rgb": (99, 102, 241),
        "badge_text": "#E0E7FF",
        "badge_text_rgb": (224, 231, 255),
        "card_bg_rgb": (29, 35, 79),
        "card_border_rgb": (99, 102, 241),
    }
}

def get_font(size, bold=False):
    """Retrieve best available true type font across platforms with graceful fallback."""
    candidates = [
        # Linux standard paths
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        # Windows standard paths
        "arialbd.ttf" if bold else "arial.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        # Generic names
        "DejaVuSans.ttf",
        "arial.ttf"
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    try:
        return ImageFont.load_default(size=size)
    except Exception:
        return ImageFont.load_default()


# Curated editorial queue of 16 comprehensive, evergreen personal finance articles for SpendSathi
EDITORIAL_QUEUE = [
    {
        "title": "The Debt Avalanche vs Snowball Method: How to Pay Off Credit Cards in India",
        "slug": "debt-avalanche-vs-snowball-india",
        "category": "DEBT MANAGEMENT",
        "theme": "amber",
        "graphic_type": "credit_card",
        "author": "Mohit Varma",
        "excerpt": "Struggling with high-interest credit card revolving balances and personal loans? Here is how to choose between the Debt Avalanche and Debt Snowball methods tailored to Indian interest rates, and how local expense tracking keeps you accountable.",
        "tags": ["debt management", "credit cards", "personal finance", "debt avalanche", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Debt Avalanche vs Snowball",
        "svg_headline_2": "for Indian Earners",
        "svg_subtitle_1": "Mathematically eliminate credit card debt and high-interest loans,",
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

While the Avalanche is mathematically superior, human psychology does not always operate like a spreadsheet. The **Debt Snowball** organizes balances strictly by **total balance amount**, from smallest to largest:

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
        "theme": "teal",
        "graphic_type": "vault_shield",
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
    },
    {
        "title": "Step-Up SIP in India: How a 10% Annual Boost Multiplies Your Crorepati Timeline",
        "slug": "step-up-sip-wealth-accelerator-india",
        "category": "WEALTH BUILDING",
        "theme": "amethyst",
        "graphic_type": "sip_chart",
        "author": "Mohit Varma",
        "excerpt": "A fixed ₹10,000 monthly SIP is good, but a Step-Up SIP is game-changing. Here is how increasing your mutual fund contributions by just 10% every year cuts years off your wealth creation goals.",
        "tags": ["SIP", "mutual funds", "step-up SIP", "compounding", "wealth creation", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "Step-Up SIP Accelerator",
        "svg_headline_2": "The 10% Annual Boost",
        "svg_subtitle_1": "How indexing your mutual fund contributions to salary increments",
        "svg_subtitle_2": "cuts years off your financial independence journey in India.",
        "body": """Systematic Investment Plans (SIPs) are celebrated as India's favorite wealth creation vehicle. Every month, millions of salaried professionals invest a fixed sum into equity mutual funds.

However, most investors make a critical mistake: **they keep their SIP amount constant for five, seven, or even ten years**, even while their annual salary increases by 8% to 15%.

This is where the **Step-Up SIP (Top-Up SIP)** changes everything. By committing to increase your monthly investment by a modest percentage once every twelve months, you harness the combined firepower of salary growth and exponential compounding.

---

## The Math: Flat SIP vs Step-Up SIP

Let us look at a real-world scenario over a 15-year investment horizon assuming a conservative **12% annualized return**:

### Scenario A: Flat SIP
* **Monthly Investment:** ₹10,000 fixed for 15 years
* **Total Invested Capital:** ₹18,00,000
* **Estimated Corpus at 15 Years:** **₹50,45,760** (~₹50.4 Lakhs)

### Scenario B: 10% Annual Step-Up SIP
* **Initial Monthly Investment:** ₹10,000
* **Year 2:** ₹11,000 / month
* **Year 3:** ₹12,100 / month
* **Total Invested Capital:** ₹38,12,700
* **Estimated Corpus at 15 Years:** **₹88,75,410** (~₹88.7 Lakhs)

**The Difference:** By simply stepping up your investment by 10% every year, your final wealth increases by **₹38.3 Lakhs (a 76% higher corpus)**, while your savings effortlessly keep pace with your career progression!

---

## Why Step-Up SIP Beats Human Willpower

1. **Automated Lifestyle Inflation Defense:** When you get an appraisal or annual bonus, lifestyle creep naturally expands your discretionary spending. A scheduled annual SIP step-up automatically captures a portion of your raise before you get used to spending it.
2. **Accelerates Financial Independence:** Stepping up your investments can shorten your journey to your first crore by 3 to 5 years.
3. **Painless Increments:** Adding ₹1,000 to a ₹10,000 SIP barely pinches your monthly cash flow, but over a decade, it generates life-altering compound interest.

---

## How to Fund Your Annual Step-Up Without Strain

The easiest way to fund an annual SIP top-up is to plug unnecessary daily leaks. When micro-UPI expenses—daily food deliveries, ride upgrades, and unmonitored subscriptions—go untracked, surplus capital vanishes.

With **SpendSathi's 100% offline Android tracker**:
* **Real-time Monthly Burn Rate:** Keep track of your exact monthly surplus so you know precisely how much you can afford to step up.
* **No Server Snooping:** Your bank balance and investment numbers never touch third-party servers.
* **Instant Category Budgets:** Cap discretionary categories with clean visual envelopes.

Try our free **[Step-Up SIP Calculator](https://spendsathi.com/step-up-sip-calculator/)** on the SpendSathi website to simulate your custom corpus, and download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to protect your monthly savings today.
"""
    },
    {
        "title": "Subscription Creep: How ₹199 Micro-Transactions Silently Steal ₹30,000 a Year",
        "slug": "subscription-creep-ott-quick-commerce-leak",
        "category": "EXPENSE CONTROL",
        "theme": "crimson",
        "graphic_type": "subscription_radar",
        "author": "Mohit Varma",
        "excerpt": "Between OTT streaming apps, quick commerce club memberships, cloud storage, and gym autopays, recurring subscriptions silently bleed Indian bank accounts. Here is how to conduct a ruthless subscription audit.",
        "tags": ["subscriptions", "money leaks", "UPI autopay", "personal finance", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Subscription Creep",
        "svg_headline_2": "The ₹30,000 Silent Leak",
        "svg_subtitle_1": "How ₹199 and ₹499 monthly auto-debits quietly compound,",
        "svg_subtitle_2": "and how to audit recurring UPI mandates 100% privately.",
        "body": """A decade ago, consumers bought products once and owned them. Today, almost every service has transformed into a monthly recurring subscription.

In India's hyper-convenient digital payment landscape, recurring UPI e-mandates and credit card auto-debits make signing up frictionless. Because individual amounts seem trivial—₹149 for music, ₹299 for video streaming, ₹99 for delivery perks, ₹199 for cloud storage—your brain dismisses them as negligible.

This cognitive blind spot is known as **subscription creep**. When left unchecked, these micro-commitments quietly compound into an annual outflow of ₹25,000 to ₹50,000.

---

## The True Cost of 'Just ₹199 a Month'

Consider an average urban professional's active subscription stack:

* Video Streaming App 1: ₹299 / month
* Video Streaming App 2: ₹499 / month
* Music Streaming: ₹119 / month
* Quick Commerce Delivery Pass: ₹99 / month
* Cloud Storage: ₹130 / month
* Productivity / AI Tool: ₹1,650 / month ($20)
* Fitness / Gym App: ₹799 / month

**Monthly Outflow:** ₹3,595  
**Annual Drain:** **₹43,140**

If that same ₹3,595 was invested monthly in an equity index fund at a 12% annualized return over 10 years, it would grow into **₹8.3 Lakhs**. You are not just paying ₹43,000 a year—you are surrendering a substantial chunk of your long-term wealth.

---

## How to Conduct a Ruthless Subscription Audit

### 1. The 30-Day Usage Test
Look at your active services. Have you actively used this service in the last 14 days? If not, cancel the recurring mandate immediately. You can always re-subscribe in 10 seconds if you genuinely need it later.

### 2. Rotate, Don't Hoard
There is zero reason to pay for three video streaming platforms simultaneously. Subscribe to one, binge the shows you want, cancel it, and switch to another the next month.

### 3. Check Recurring UPI Mandates
Open your primary banking app or UPI settings and review active e-mandates. You will often discover auto-debits for trial services you forgot to cancel six months ago.

---

## Take Back Control with Offline Expense Tracking

Most cloud budgeting apps fail at tracking subscriptions because they rely on slow server-side scraping or bombard you with ads for more subscription credit cards.

**SpendSathi takes a radically different approach:**
* **Instant Recurring Detection:** Because SpendSathi parses your incoming debit SMS alerts locally on your device, it immediately detects repeated monthly charges.
* **100% Privacy:** Your banking notifications, mandates, and account balances remain securely inside your phone's encrypted sandbox.
* **Zero Cloud Profiling:** No third-party data broker will ever know what services you subscribe to.

Stop the silent drain. Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and audit your monthly subscriptions today.
"""
    },
    {
        "title": "The 750+ CIBIL Playbook: How Indian Borrowers Can Boost Their Credit Score in 90 Days",
        "slug": "credit-score-repair-750-plus-cibil-india",
        "category": "CREDIT & LOANS",
        "theme": "teal",
        "graphic_type": "credit_gauge",
        "author": "Mohit Varma",
        "excerpt": "A credit score above 750 saves you lakhs in home loan interest. Here is the step-by-step playbook to repair your CIBIL score, optimize credit utilization, and remove reporting errors within 90 days.",
        "tags": ["CIBIL score", "credit score", "home loans", "credit utilization", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "The 750+ CIBIL Playbook",
        "svg_headline_2": "Boost Credit in 90 Days",
        "svg_subtitle_1": "How high credit scores unlock lowest home and car loan interest rates,",
        "svg_subtitle_2": "and why keeping your financial tracking private protects your credit profile.",
        "body": """In India's financial system, your **CIBIL score (ranging from 300 to 900)** is your financial passport. Whether you are applying for a ₹50 Lakh home loan, leasing an apartment, or seeking an emergency credit line, lenders evaluate your creditworthiness through this single three-digit number.

A score above **750** marks you as a prime borrower, unlocking the lowest interest rates, waived processing fees, and instant approvals. Conversely, a score below 700 can increase your home loan rate by 0.5% to 1.5%—costing you **₹6 Lakhs to ₹12 Lakhs in extra interest** over a 20-year tenure!

Here is the exact 90-day playbook to elevate your credit score into the prime 750+ tier.

---

## The 5 Pillars of Your CIBIL Score

Understanding how credit bureaus calculate your score is the first step to mastering it:

1. **Payment History (35% weight):** Paying every credit card bill and loan EMI on or before the due date. Even a single 30-day late payment can drop your score by 40 to 60 points.
2. **Credit Utilization Ratio (30% weight):** The percentage of your available credit card limits you utilize. Spending ₹90,000 of a ₹1,00,000 limit signals credit hunger, even if you pay in full every month!
3. **Credit Age & Vintage (15% weight):** The average length of your active credit history. Older accounts demonstrate seasoned borrowing discipline.
4. **Credit Mix (10% weight):** A balanced combination of secured debt (home/car loan) and unsecured debt (credit card/personal loan).
5. **Hard Inquiries (10% weight):** Applying for multiple loans or credit cards in a short window triggers hard inquiries, dinging your score each time.

---

## The 90-Day Credit Boost Protocol

### Step 1: Cap Credit Utilization Below 30%
If your total credit card limit across all cards is ₹2,00,000, your total reported statement balances should never exceed **₹60,000 (30%)**. For maximum score acceleration, aim for **under 15%**.

*Tactical Hack:* Pay down 70% of your credit card balance 3 days *before* the monthly bill generation date. The bank reports the lower balance to CIBIL, giving you an immediate score boost.

### Step 2: Never Close Your Oldest Credit Card
Closing your first credit card shortens your average credit history and reduces your overall available limit. Keep your oldest card open and use it for one recurring utility bill each month.

### Step 3: Audit Your CIR for Erroneous Dues
Download your official free annual credit report from CIBIL. Check for closed loans still marked as 'Active', misspelled PAN numbers, or fraudulent inquiries. File online disputes for swift rectification.

### Step 4: Avoid BNPL and PayLater Apps
Many quick-checkout PayLater services register a fresh consumer durable loan inquiry on your bureau profile. Having eight separate micro-loan lines damages your credit profile perception.

---

## Keep Your Everyday Spends on Track Without Cloud Scrapers

Many free credit score apps continuously scan your email inbox and financial records to pitch high-interest personal loans that compromise your credit score.

**SpendSathi keeps your finances 100% private and disciplined:**
* **On-Device Card Tracking:** Track your credit card outflows locally to ensure your utilization stays strictly under 30%.
* **Zero Predatory Loan Ads:** SpendSathi does not sell your financial footprint to banks or third-party loan brokers.
* **Biometric Security:** Keep your financial records shielded behind PIN and fingerprint authentication.

Build your credit reputation and protect your financial privacy with **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** today.
"""
    },
    {
        "title": "Digital Gold vs Sovereign Gold Bonds vs Equity SIP: The Modern Indian Dilemma",
        "slug": "gold-vs-equity-mf-indian-investor-dilemma",
        "category": "INVESTMENT STRATEGY",
        "theme": "bronze",
        "graphic_type": "gold_scales",
        "author": "Mohit Varma",
        "excerpt": "Gold is deeply woven into Indian culture, but how should modern investors allocate between digital gold, Sovereign Gold Bonds (SGB), and equity mutual fund SIPs? Here is the balanced asset allocation guide.",
        "tags": ["gold", "SGB", "mutual funds", "asset allocation", "investing", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "Gold vs Equity SIPs",
        "svg_headline_2": "The Modern Allocation",
        "svg_subtitle_1": "Navigating digital gold, Sovereign Gold Bonds, and mutual funds,",
        "svg_subtitle_2": "and why balanced local financial tracking builds true independence.",
        "body": """In Indian households, gold is not just an asset—it represents cultural heritage, security, and an intergenerational hedge against currency depreciation.

However, modern retail investors face a dilemma: with equity mutual funds delivering 12% to 15% long-term returns and digital gold platforms promoting instant micro-purchases, how should a salaried individual structure their precious metals allocation in 2026?

Here is an objective breakdown of physical gold, digital gold, Sovereign Gold Bonds (SGB), and Equity SIPs.

---

## 1. Comparing Gold Investment Avenues

### Digital Gold
* **Pros:** Buy for as low as ₹10 via UPI; 24K pure gold stored in insured vaults.
* **Cons:** High 3% GST on purchase, 2% to 3% spread between buy and sell prices, and holding period caps (must convert to physical or sell within 5 to 10 years).
* **Verdict:** Convenient for gifting, but suboptimal for long-term compounding due to upfront friction costs.

### Sovereign Gold Bonds (SGBs) & Gold ETFs
* **Pros:** Issued by RBI on behalf of the Government of India; pays an additional **2.5% annual interest** on nominal value; zero making charges.
* **Tax Benefit:** Capital gains are **100% tax-free** if held until maturity (8 years).
* **Verdict:** The gold standard for financial gold allocation in India. Secondary market purchases through demat accounts remain an exceptional option.

---

## 2. Gold vs Equity Mutual Funds: Historical Reality

Over a 20-year horizon, equity indices like the Nifty 50 have historically outpaced gold by 3% to 5% annualized. A 14% equity return compounds ₹10,000/month into ₹1.3 Crores over 20 years, whereas a 9% gold return yields ₹67 Lakhs.

However, gold performs its magic when equities crash. During market drawdowns (like 2008 and 2020), gold acts as an uncorrelated anchor, preserving capital and stabilizing portfolio volatility.

---

## The Recommended Golden Ratio: The 80-15-5 Rule

For most Indian professionals under 45:
* **75% to 80%:** Diversified Equity Mutual Funds (Index + Flexi-cap funds) for compounding wealth.
* **10% to 15%:** Sovereign Gold Bonds or Gold ETFs for portfolio hedging and crisis liquidity.
* **5% to 10%:** Liquid reserves and fixed income.

---

## Track Your Asset Allocation Locally with SpendSathi

Whether you are investing ₹5,000 into gold or ₹20,000 into an index fund, maintaining steady monthly investments requires disciplined cash flow control.

**SpendSathi ensures you never miss an investment installment:**
* **Automated Wealth Categorization:** Tag your SIP and investment debits with rich gold badges.
* **Local Data Protection:** Your investment values and bank notifications remain private on your device.
* **Clear Cash Flow Clarity:** Know your operational surplus before making impulsive discretionary purchases.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to track your wealth-building journey today.
"""
    },
    {
        "title": "Old vs New Tax Regime in 2026: The Definitive Math Guide for Salaried Indians",
        "slug": "old-vs-new-tax-regime-salaried-indians",
        "category": "TAX PLANNING",
        "theme": "teal",
        "graphic_type": "tax_calculator",
        "author": "Mohit Varma",
        "excerpt": "Should you stick with Section 80C, HRA, and home loan deductions in the Old Regime, or switch to the simplified slabs of the New Tax Regime? Here is the exact breakeven formula to minimize your tax liability.",
        "tags": ["income tax", "tax planning", "old vs new regime", "section 80C", "HRA", "SpendSathi"],
        "read_time": "9 min read",
        "svg_headline_1": "Old vs New Tax Regime",
        "svg_headline_2": "The Breakeven Math",
        "svg_subtitle_1": "Compare HRA, 80C deductions, and streamlined tax slabs,",
        "svg_subtitle_2": "and discover how local tracking simplifies year-end tax season.",
        "body": """Every financial year, salaried employees across India face the same annual puzzle: **Should I choose the Old Tax Regime or the New Tax Regime?**

With the Indian government progressively sweetening the New Tax Regime with higher basic exemption limits, standard deductions of ₹75,000, and lower tax slabs, the default choice has shifted. However, for employees with significant House Rent Allowance (HRA), home loan interest, and Section 80C/80D investments, the Old Regime can still save tens of thousands in hard cash.

Here is the straightforward mathematical framework to make the right choice.

---

## Key Differences at a Glance

* **New Tax Regime (Default):** Concessional tax slabs, standard deduction of ₹75,000, and full tax rebate on taxable income up to ₹7 Lakhs. However, almost all itemized deductions (80C, 80D, HRA, LTA, 24b home loan interest) are forgone.
* **Old Tax Regime:** Higher tax slab rates, but permits substantial deductions: Section 80C (up to ₹1.5 Lakhs), Section 80D health insurance (up to ₹75,000), HRA exemption, and home loan interest deduction up to ₹2 Lakhs under Section 24(b).

---

## The Breakeven Deduction Benchmark

To know which regime wins, calculate your **Total Eligible Deductions** (80C + 80D + HRA + Home Loan Interest + NPS 80CCD(1B)):

* **Income ₹10 Lakhs:** If total deductions exceed **₹2,50,000**, the Old Regime wins. Otherwise, the New Regime is superior.
* **Income ₹15 Lakhs:** If total deductions exceed **₹3,75,000**, the Old Regime wins.
* **Income ₹20 Lakhs+:** If total deductions exceed **₹4,25,000**, the Old Regime wins.

If you do not pay substantial house rent and do not service a home loan EMI, **the New Tax Regime is mathematically unbeatable** for almost all salaried professionals.

---

## Keep Your Tax Records Clean with SpendSathi

Scrambling for rent receipts, insurance premium receipts, and medical bills in March creates unnecessary stress. 

By categorizing your insurance payments, school fees, and rent debits throughout the year using **SpendSathi's local offline tracker**:
* **Export PDF Reports:** Generate clean categorized transaction reports in one tap to share with your chartered accountant.
* **Zero Cloud Exposure:** Your salary credits and private tax deductions never leave your device.
* **Year-Round Awareness:** Never wonder whether you met your planned tax-saving investment targets.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and simplify your financial life today.
"""
    },
    {
        "title": "The Credit Card Reward Trap: Are You Overspending Just for 1.5% Cashback?",
        "slug": "credit-card-cashback-traps-upi-rupay",
        "category": "SMART SPENDING",
        "theme": "amber",
        "graphic_type": "credit_card",
        "author": "Mohit Varma",
        "excerpt": "Credit card reward points, air miles, and 1.5% cashback offers are engineered to trigger spending friction-loss. Here is the behavioral psychology behind reward traps and how to stay disciplined.",
        "tags": ["credit cards", "cashback", "reward points", "behavioral finance", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Credit Card Reward Trap",
        "svg_headline_2": "The 1.5% Illusion",
        "svg_subtitle_1": "Why spending ₹1,000 to earn ₹15 in points is a losing battle,",
        "svg_subtitle_2": "and how on-device offline tracking preserves real savings.",
        "body": """Credit card reward programs are one of the most brilliant marketing innovations in financial history. Banks promise you 2% cashback, 5X accelerated reward points on dining, or air miles toward your next domestic flight.

Yet credit card companies are not charities. They spend billions on rewards because behavioral economics proves a simple truth: **consumers spend 18% to 30% more when paying with plastic or reward cards than when paying with cold cash or direct bank debits.**

Spending ₹2,000 on an unnecessary dinner just to earn ₹30 in cashback is not a saving—it is a net loss of ₹1,970.

---

## The 3 Psychological Traps of Reward Programs

### 1. The Justification Bias
Reward points create artificial cognitive justification for purchases you would otherwise decline. "It is okay to buy this ₹4,000 jacket because I get 10X reward points on this card."

### 2. Milestone Chasing
"Spend ₹2 Lakhs in a quarter to unlock a free ₹5,000 voucher." Borrowers often spend ₹30,000 on low-priority items just to hit the milestone, effectively spending ₹30,000 to 'win' ₹5,000.

### 3. Devaluation Risk
Airlines and card issuers routinely devalue reward redemption ratios overnight without warning. Hoarding points is like holding depreciating currency.

---

## How to Win the Credit Card Game

1. **Treat Credit Cards as Debit Cards:** Never charge an expense to a credit card unless you already have the full cash amount sitting in your checking account.
2. **Never Roll a Balance:** Paying 42% APR interest erases ten years of cashback points in a single billing cycle.
3. **Automate Pay-in-Full:** Set your card to auto-debit the full statement balance every month.

---

## Keep Your Real Spending Honest with SpendSathi

Credit card apps highlight your available limit and reward balance, hiding the cumulative impact on your monthly budget.

**SpendSathi keeps you anchored in reality:**
* **Instant Debit Tracking:** Track every card swipe locally in real time.
* **No Marketing Push Notifications:** SpendSathi never sends you ads prompting you to spend more for rewards.
* **Envelope Budgeting:** Set a firm ceiling on dining and entertainment that credit card perks cannot bypass.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and master your credit habits today.
"""
    },
    {
        "title": "Base Health Insurance vs Super Top-Up: How to Get ₹50 Lakhs Coverage for Salaried Indians",
        "slug": "health-insurance-super-topup-vs-base-policy-india",
        "category": "HEALTH & INSURANCE",
        "theme": "cyan",
        "graphic_type": "vault_shield",
        "author": "Mohit Varma",
        "excerpt": "Medical inflation in India is running at 14% annually. Relying solely on corporate group cover is dangerous. Here is how pairing a ₹5 Lakh base health plan with a ₹45 Lakh Super Top-up saves you over 60% on premiums.",
        "tags": ["health insurance", "super top-up", "medical inflation", "financial safety", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "Health Insurance Blueprint",
        "svg_headline_2": "₹50L Cover on a Budget",
        "svg_subtitle_1": "Why combining a base health policy with a deductible super top-up",
        "svg_subtitle_2": "slashes annual premiums while securing bulletproof medical cover.",
        "body": """With Indian healthcare inflation exceeding 14% per annum, a single tertiary hospitalization for critical illness or cardiac surgery can easily rack up a ₹15 Lakh to ₹25 Lakh bill.

Yet, a staggering number of salaried professionals rely entirely on their employer's corporate group health insurance (usually capped at ₹3 Lakhs to ₹5 Lakhs). If you switch jobs, face corporate layoffs, or retire, that cover vanishes overnight.

Here is how you can build a massive **₹50 Lakh family health insurance shield** without paying exorbitant premiums.

---

## The Base Policy + Super Top-Up Hack

Buying a standalone ₹50 Lakh base policy directly can cost ₹35,000 to ₹50,000 annually. However, you can dramatically reduce this cost through a two-tier structure:

1. **Base Health Policy (₹5 Lakhs Sum Insured):** This covers routine hospitalizations and fulfills the deductible threshold. (Approx. ₹8,000 – ₹12,000/year).
2. **Super Top-Up Policy (₹45 Lakhs with ₹5 Lakh Deductible):** A super top-up kicks in once total cumulative hospital expenses in a policy year exceed the ₹5 Lakh deductible. Because catastrophic claims are rare, insurers price super top-ups extremely cheaply (Approx. ₹3,500 – ₹5,500/year).

**Total Outlay:** Around ₹12,000 to ₹17,000 per year for a massive ₹50 Lakh safety net—a savings of over 60% compared to a single comprehensive mega-policy!

---

## 4 Critical Clauses to Verify Before Buying

* **Zero Room Rent Capping:** Avoid policies with room rent caps (e.g., 1% of sum insured), as exceeding it triggers proportionate deductions across your entire medical bill.
* **Restore / Refill Benefit:** Ensure the base policy automatically recharges 100% of the sum insured if exhausted during the year.
* **Pre-Existing Disease (PED) Waiting Period:** Look for policies with 2 or 3-year waiting periods rather than 4 years.
* **Consumables Add-On:** Post-2020, non-medical consumables (gloves, PPE kits, syringes) account for 10% to 15% of hospital bills. Ensure you have a consumable cover rider.

---

## Budget for Annual Premiums with SpendSathi

Large annual insurance payments often derail monthly budgets when they hit all at once. 

Using **SpendSathi's local offline tracker**:
* **Sinking Fund Planning:** Break down your ₹15,000 annual premium into a painless ₹1,250 monthly reserve.
* **100% Data Privacy:** Your family medical disclosures and policy costs stay on your phone.
* **Instant Export:** Generate expense breakdowns for Section 80D tax deductions effortlessly.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and fortify your family's financial fortress today.
"""
    },
    {
        "title": "Term Insurance in India: Why Pure Vanilla Term Cover Beats ULIPs and Endowment Plans",
        "slug": "term-insurance-riders-worth-it-or-waste-india",
        "category": "LIFE INSURANCE",
        "theme": "amethyst",
        "graphic_type": "vault_shield",
        "author": "Mohit Varma",
        "excerpt": "Never mix insurance with investment. Discover why traditional endowment plans and ULIPs offer subpar 5% returns and low cover, while a pure term insurance policy gives your family crore-level protection for pocket change.",
        "tags": ["term insurance", "life insurance", "ULIP", "financial protection", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Pure Term Insurance",
        "svg_headline_2": "Protect Your Family",
        "svg_subtitle_1": "Why separating insurance from investment guarantees ₹1 Crore+ protection,",
        "svg_subtitle_2": "and why 100% private offline budgeting ensures premiums are never missed.",
        "body": """One of the most persistent financial traps in India is the **Endowment or ULIP policy** sold by well-meaning relatives or bank relationship managers promising 'guaranteed returns plus life cover'.

The harsh mathematical reality? These hybrid policies give you the worst of both worlds: dismal 4% to 5.5% annualized returns (barely beating inflation) and an inadequate life cover of ₹5 Lakhs to ₹10 Lakhs that would not sustain a family for two years in an emergency.

The golden rule of personal finance is absolute: **Never mix insurance with investment.**

---

## Why Pure Term Insurance Wins Every Time

A Pure Term Insurance policy has no maturity value. If you survive the policy term, you receive ₹0 back. But if you pass away during the policy tenure, your nominee receives the full sum assured (e.g., ₹1 Crore to ₹2 Crores) tax-free.

Because there is no investment component, pure term plans are exceptionally affordable:
* A healthy 28-year-old non-smoker can secure **₹1 Crore life cover up to age 60 for just ₹800 to ₹1,000 per month**.
* If you take the difference between an expensive ULIP premium (₹60,000/yr) and a term plan (₹12,000/yr) and invest the remaining ₹48,000 in an Equity Mutual Fund SIP at 12%, you will accumulate over **₹1.5 Crores** in 25 years while enjoying ₹1 Crore protection from Day 1!

---

## How Much Term Cover Do You Need?

A sound rule of thumb for breadwinners in urban India:
$$\\text{Ideal Term Cover} = (15 \\times \\text{Annual Take-Home Income}) + \\text{Outstanding Debts (Home/Car Loans)} - \\text{Existing Liquid Savings}$$

If you earn ₹12 Lakhs per annum with a ₹30 Lakh outstanding home loan, your family needs at least **₹2 Crores in term insurance cover**.

---

## Keep Track of Financial Commitments Privately

Protecting your family's future requires disciplined monthly cash flow management.

With **SpendSathi's offline expense manager**:
* **No Telemarketing Leaks:** Insurance portals often sell phone numbers to aggressive telecallers. SpendSathi never uploads your financial footprint.
* **Category Budgets:** Tag insurance premiums under fixed obligations so your operational money is always protected.
* **Biometric Security:** Your net worth and asset plans remain strictly protected under your fingerprint lock.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to keep your family budget on track.
"""
    },
    {
        "title": "EPF vs VPF vs PPF: Where Salaried Indians Should Park Their Fixed Income Allocation",
        "slug": "provident-fund-epf-vpf-vs-ppf-retirement-math",
        "category": "RETIREMENT PLANNING",
        "theme": "bronze",
        "graphic_type": "gold_scales",
        "author": "Mohit Varma",
        "excerpt": "Balancing your equity portfolio with sovereign-backed fixed income? Here is the complete comparison of Employees' Provident Fund (EPF), Voluntary PF (VPF), and Public Provident Fund (PPF) regarding returns, taxability, and lock-in periods.",
        "tags": ["EPF", "VPF", "PPF", "retirement", "fixed income", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "EPF vs VPF vs PPF",
        "svg_headline_2": "The Sovereign Fixed Income Trio",
        "svg_subtitle_1": "Maximize risk-free returns, navigate tax thresholds on PF interest,",
        "svg_subtitle_2": "and track your retirement contributions with 100% private expense control.",
        "body": """Every prudent investment portfolio requires a sturdy debt or fixed-income anchor to counterbalance the volatility of equities.

For Indian salaried earners, sovereign-backed provident funds—**EPF, VPF, and PPF**—offer sovereign credit safety, attractive compounding interest rates (typically 7% to 8.25%), and sovereign backing.

However, recent tax reforms have introduced taxation on annual employee PF contributions exceeding ₹2.5 Lakhs. Which instrument should you prioritize in 2026?

---

## Detailed Comparison: EPF vs VPF vs PPF

### 1. Employees' Provident Fund (EPF)
* **Interest Rate:** ~8.25% per annum (set annually by EPFO).
* **Mandatory Contribution:** 12% of basic salary matched by your employer.
* **Tax Status:** EEE (Exempt-Exempt-Exempt) up to ₹2.5 Lakhs employee contribution per financial year. Interest on employee contributions exceeding ₹2.5 Lakhs is taxable at slab rates.

### 2. Voluntary Provident Fund (VPF)
* **Interest Rate:** Same as EPF (8.25%).
* **How It Works:** Salaried employees can voluntarily contribute an extra percentage of basic salary beyond the mandatory 12%.
* **Strategy:** Excellent vehicle for risk-averse investors up to the ₹2.5 Lakh overall EPF+VPF employee threshold.

### 3. Public Provident Fund (PPF)
* **Interest Rate:** 7.1% per annum, compounded annually.
* **Maximum Limit:** ₹1.5 Lakhs per financial year.
* **Tax Status:** Absolute 100% EEE tax-free status on all interest and maturity amounts, completely immune to the ₹2.5 Lakh rule!
* **Lock-in Period:** 15 years, with partial withdrawal facilities after Year 7.

---

## The Strategic Allocation Playbook

1. **Maximize Mandatory EPF:** Let your mandatory 12% EPF contribution run silently—it builds your foundation.
2. **Hit the ₹1.5L PPF Ceiling First:** For non-taxable debt allocation, PPF remains completely tax-free upon withdrawal regardless of total income slabs.
3. **Use VPF up to the ₹2.5L Total Cap:** If your basic salary is modest and your mandatory EPF is ₹1 Lakh/year, consider adding ₹1.5 Lakhs via VPF to earn 8.25% sovereign tax-free interest.

---

## Gain Full Visibility Over Your Net Savings

Retirement planning fails when day-to-day UPI micro-spends devour your investable surplus.

**SpendSathi empowers your wealth accumulation:**
* **Track Net Cash Flow:** Know exactly how much operational cash remains after salary deductions.
* **Zero Cloud Analytics:** Keep your retirement goals, provident fund numbers, and bank transactions 100% local.
* **Custom Category Envelopes:** Restrict eating out and lifestyle creep so your long-term goals remain intact.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and secure your future today.
"""
    },
    {
        "title": "The 50% Rule for Salary Raises: How to Defeat Lifestyle Inflation in Corporate India",
        "slug": "lifestyle-inflation-salary-hike-trap-india",
        "category": "PSYCHOLOGY & WEALTH",
        "theme": "indigo",
        "graphic_type": "budget_donut",
        "author": "Mohit Varma",
        "excerpt": "Got an appraisal, promotion, or job switch? Learn why expanding your lifestyle to match your new pay scale traps you on the corporate hedonic treadmill—and how the 50% Rule turns pay raises into rapid financial independence.",
        "tags": ["lifestyle inflation", "salary hike", "hedonic treadmill", "financial freedom", "SpendSathi"],
        "read_time": "6 min read",
        "svg_headline_1": "Defeat Lifestyle Creep",
        "svg_headline_2": "The 50% Salary Raise Rule",
        "svg_subtitle_1": "How capturing half of every promotion before spending expands",
        "svg_subtitle_2": "accelerates your retirement timeline while letting you enjoy life.",
        "body": """It is a universal corporate phenomenon:
You land a 25% salary hike during appraisals or a 35% jump after switching companies. For the first two months, you feel flush with liquidity. 

Yet within six months, a strange reality sets in: **you are saving the exact same amount of money you were saving two years ago.**

Where did the raise go? It vanished into an upgraded apartment rent, more frequent dining out at premium cafes, daily quick-commerce orders, cab upgrades, and higher credit card limits. This psychological trap is called **Lifestyle Inflation** (the Hedonic Treadmill).

---

## Why More Income Does Not Equal More Wealth

Wealth is not what you earn—it is what you keep and compound. When your living expenses expand proportionally with every increment, your financial runway never actually increases. If you earn ₹2 Lakhs a month but spend ₹1.9 Lakhs, you are just as vulnerable to a job loss as someone earning ₹40,000 and spending ₹38,000.

To build true financial independence, you must consciously decouple your lifestyle standard from your income line.

---

## The 50% Rule for Every Salary Increment

You do not need to live like an ascetic monk to become wealthy. The **50% Rule** provides the perfect psychological balance:

$$\\text{50% of Net Increment} \\longrightarrow \\text{Automated Wealth Compounding (SIPs, Emergency Fund, Debt Prepayment)}$$
$$\\text{50% of Net Increment} \\longrightarrow \\text{Guilt-Free Lifestyle Upgrades (Better Housing, Travel, Hobbies)}$$

### Real-Life Scenario:
Suppose your monthly take-home salary increases by **₹20,000**:
* **₹10,000** goes immediately into an automated Step-Up SIP in an equity index fund.
* **₹10,000** is added to your discretionary spending budget—letting you enjoy the rewards of your hard work without compromising your future.

Over a 10-year career across three job switches, this single habit adds **₹50 Lakhs to ₹1 Crore** to your net worth without making you feel deprived.

---

## Stay Disciplined Without Cloud Surveillance

Budgeting does not have to mean uploading your bank statements to invasive third-party servers.

**SpendSathi keeps your financial discipline private:**
* **Instant SMS Expense Parsing:** Track your daily expenses directly from bank debit SMS alerts locally on your phone.
* **Visual Envelope Limits:** See when your dining or shopping categories are approaching their ceiling in real time.
* **100% Offline Architecture:** No account registration, no passwords, and zero data leaves your handset.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to master your cash flow today.
"""
    },
    {
        "title": "Sinking Funds 101: How Indian Families Can Stop Dipping Into Savings for Annual Outflows",
        "slug": "emergency-car-home-maintenance-sinking-funds-india",
        "category": "BUDGETING STRATEGY",
        "theme": "emerald",
        "graphic_type": "budget_donut",
        "author": "Mohit Varma",
        "excerpt": "Car insurance renewals, Diwali shopping, school admission fees, and annual health checkups are not unpredictable emergencies. Discover how sinking funds smooth out lump-sum yearly expenses without wrecking your monthly budget.",
        "tags": ["sinking funds", "budgeting", "annual expenses", "personal finance", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "Sinking Funds 101",
        "svg_headline_2": "Smooth Lump-Sum Expenses",
        "svg_subtitle_1": "How planning for car insurance, festive gifts, and annual school fees",
        "svg_subtitle_2": "prevents credit card debt and protects your long-term investments.",
        "body": """Every year, millions of Indian households experience what feels like an unexpected financial emergency:
* In August: School annual fees and book kits arrive (₹40,000).
* In October: Diwali gifting, home renovation, and ethnic wear (₹50,000).
* In December: Comprehensive car insurance renewal and service (₹25,000).

When these large expenses strike, families frequently raid their emergency funds, pause mutual fund SIPs, or swipe high-interest credit cards.

Yet, none of these expenses were emergencies! **They occur at the exact same time every single year.** The proven solution is the **Sinking Fund**.

---

## What Is a Sinking Fund?

A Sinking Fund is a strategic savings bucket created by setting aside a small, fixed amount every month for a specific, known future expense.

Unlike an Emergency Fund (which covers true surprises like job loss or medical emergencies), a Sinking Fund handles **predictable lump-sum expenses**.

### The Math:
$$\\text{Monthly Sinking Contribution} = \\frac{\\text{Expected Annual Expense}}{\\text{Months Remaining}}$$

* **Car Insurance & Annual Maintenance:** ₹30,000 / 12 = **₹2,500 / month**
* **Diwali & Festive Shopping:** ₹60,000 / 12 = **₹5,000 / month**
* **Child's Annual School Fees:** ₹48,000 / 12 = **₹4,000 / month**

When the renewal notice arrives, you simply pay cash from your sinking reserve. Zero stress, zero EMI loans, zero guilt!

---

## Where to Keep Sinking Funds

Keep sinking funds segregated from your everyday spending account to prevent accidental spending:
1. **Secondary Zero-Balance Savings Account:** High-yield digital savings accounts or sweep-in FDs.
2. **Liquid / Overnight Mutual Funds:** Stable returns with instant T+1 redemption.

---

## Track Your Monthly Allocations Privately

Maintaining multiple categories can be tedious if your tracking tool bombards you with ads.

**SpendSathi makes category budgeting effortless:**
* **Custom Envelope Allocations:** Create dedicated categories for maintenance, festivals, and insurance.
* **Offline Privacy:** Your financial buffers and account balances remain safely stored on your device.
* **Instant Burn Rate Tracking:** Spot overspending before it impacts your sinking reserves.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and master your annual budgeting today.
"""
    },
    {
        "title": "The Hidden Costs of Investing in India: STT, GST, AMC, and How Discount Brokers Really Charge You",
        "slug": "demat-account-charges-amc-stt-hidden-broker-costs-india",
        "category": "INVESTING BASICS",
        "theme": "amber",
        "graphic_type": "sip_chart",
        "author": "Mohit Varma",
        "excerpt": "Discount brokers advertise '₹0 brokerage on equity delivery', but how much do you actually lose to STT, exchange turnover fees, DP charges, stamp duty, and SEBI turnover fees? Here is the complete breakdown of investor transaction drag.",
        "tags": ["demat charges", "STT", "discount brokers", "investing costs", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "The Hidden Costs of Investing",
        "svg_headline_2": "Taxes, STT & Broker Drag",
        "svg_subtitle_1": "Understand depository fees, turnover charges, and GST leaks,",
        "svg_subtitle_2": "and why keeping your operational accounting private maximizes net worth.",
        "body": """In India's retail investing boom, discount brokerages advertise '₹0 account opening' and 'Zero brokerage for equity delivery investments'.

While retail investors have saved billions in traditional brokerage commissions, trading and holding securities in India is far from free. Between statutory government taxes, exchange transaction levies, and depository fees, hidden friction costs quietly reduce your net portfolio returns.

Here is the transparent breakdown of every charge deducted when you buy and sell Indian stocks and mutual funds.

---

## The 6 Hidden Layers of Transaction Drag

### 1. Securities Transaction Tax (STT)
Levied directly by the Central Government. On equity delivery, STT is **0.1% on both purchase and sale**. On futures and options, recent budget hikes have increased STT rates significantly.

### 2. Depository Participant (DP) Charges
When you sell a stock from your demat account, your depository (CDSL or NSDL) and your broker charge a flat fee—typically **₹13 to ₹20 + 18% GST per company per day**, regardless of transaction volume. If you sell ₹500 worth of shares across three companies, you could lose ₹60 (12%) in DP charges alone!

### 3. Stamp Duty
Imposed under the Indian Stamp Act: **0.015% (₹1,500 per ₹1 Crore)** on buy orders for equity delivery.

### 4. Exchange Turnover Fees & SEBI Turnover Charges
Both the NSE and BSE levy turnover fees (~0.003% to 0.0035%), alongside SEBI's regulatory fee of ₹10 per crore.

### 5. 18% GST on Services
Goods and Services Tax of 18% applies to brokerage, exchange turnover charges, and DP charges.

### 6. Demat Annual Maintenance Charges (AMC)
Many brokers waive AMC for Year 1, then deduct ₹300 to ₹500 + GST every year from your trading ledger.

---

## How to Minimize Transaction Drag

* **Invest for the Long Term:** High-frequency churning multiplies DP charges and STT. Long-term compounding minimizes tax drag.
* **Prefer Direct Mutual Funds over Stocks for Small Amounts:** Direct mutual funds incur zero DP charges on redemption and benefit from economies of scale.
* **Consolidate Sales:** Avoid selling tiny odd lots of shares across multiple trading days to reduce repetitive DP charges.

---

## Keep Your Real Net Worth Transparent with SpendSathi

Managing investments requires keeping your core living expenses lean and organized.

**SpendSathi provides total financial visibility:**
* **Zero Telemarketing & Spam:** Unlike stock trading apps, SpendSathi never pushes speculative F&O tips or margin loans.
* **Local Expense Tracking:** Monitor your investment outflows 100% offline.
* **Instant Monthly Reports:** Generate categorized PDF financial summaries for your tax filings.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to take control of your financial journey.
"""
    },
    {
        "title": "RuPay Credit Cards on UPI: The Convenience, Hidden Traps, and How to Avoid Overspending",
        "slug": "rupay-credit-cards-on-upi-pros-and-pitfalls",
        "category": "UPI & PAYMENTS",
        "theme": "crimson",
        "graphic_type": "credit_card",
        "author": "Mohit Varma",
        "excerpt": "Linking your credit card to UPI makes scanning QR codes dangerously frictionless. Here is the behavioral psychology behind RuPay-UPI debt creep, and how to enjoy 50-day interest-free credit without falling into debt traps.",
        "tags": ["RuPay credit card", "UPI", "frictionless payments", "debt trap", "SpendSathi"],
        "read_time": "7 min read",
        "svg_headline_1": "RuPay Credit Cards on UPI",
        "svg_headline_2": "Convenience vs Debt Creep",
        "svg_subtitle_1": "How scanning QR codes with borrowed money erodes spending discipline,",
        "svg_subtitle_2": "and why local on-device tracking keeps your credit utilization safe.",
        "body": """The integration of **RuPay credit cards with the Unified Payments Interface (UPI)** is one of the most innovative fintech milestones in India.

Suddenly, you can scan a roadside tea stall, pay for groceries at the local kirana store, or settle restaurant bills with your credit card—even when the vendor doesn't own a POS card swipe machine.

However, blending the friction-free ease of UPI with uncollateralized credit card limits creates a behavioral trap that can quietly double your monthly spending.

---

## The Behavioral Hazard: 'Invisible Money'

When you pay via UPI linked to your bank account, you experience immediate **payment friction**: your account balance drops, and an SMS alert confirms money leaving your pocket.

When you link a RuPay credit card:
1. **The Pain of Paying Disappears:** You are spending the bank's money, deferring payment by up to 50 days.
2. **Micro-Spends Accumulate:** Scanning ₹60 for coffee, ₹150 for snacks, and ₹300 for rides three times a day feels trivial. Yet 90 micro-transactions easily total ₹35,000 by month-end.
3. **Credit Utilization Spikes:** Because your card is used for daily groceries and utility bills, your credit utilization can breach the critical 30% ceiling, damaging your CIBIL score.

---

## 3 Rules to Master RuPay Credit Cards on UPI

### 1. Set a Daily Merchant Transaction Limit
Open your banking app and set a strict daily transaction cap (e.g., ₹2,000) on your RuPay UPI card. This prevents impulsive large-ticket purchases.

### 2. Never Use RuPay UPI for Peer-to-Peer Payments
Reserve your card strictly for verified merchant transactions that earn rewards or fuel surcharge waivers.

### 3. Pay Your Card Bill Weekly, Not Monthly
Do not wait for the monthly statement date. Settle your RuPay credit card balance every Sunday from your primary bank account. This eliminates the shock of a huge bill and keeps your CIBIL utilization near zero.

---

## Track Daily Micro-Spends 100% Privately with SpendSathi

Credit card apps highlight your available limit to encourage more swipes, rarely showing your true monthly burn rate.

**SpendSathi keeps your financial reality crystal clear:**
* **Instant Offline Parsing:** Parses debit notifications on-device the moment you scan a QR code.
* **100% Privacy:** No third-party servers ever read your UPI IDs or merchant details.
* **Strict Category Budgets:** Alert yourself before dining and grocery budgets exceed monthly targets.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** and master your digital spending habits today.
"""
    },
    {
        "title": "NPS (National Pension System) in 2026: Is the Extra ₹50,000 Section 80CCD(1B) Deduction Worth It?",
        "slug": "nps-tier-1-tax-benefit-80ccd-worth-it-india",
        "category": "RETIREMENT & TAX",
        "theme": "teal",
        "graphic_type": "tax_calculator",
        "author": "Mohit Varma",
        "excerpt": "Section 80CCD(1B) offers an exclusive ₹50,000 tax deduction for NPS Tier-1 investments over and above the ₹1.5L Section 80C limit. But does the mandatory annuity purchase and age 60 lock-in justify the tax savings? Here is the math.",
        "tags": ["NPS", "Section 80CCD", "tax saving", "retirement", "annuity", "SpendSathi"],
        "read_time": "8 min read",
        "svg_headline_1": "NPS Tier-1 Analysis",
        "svg_headline_2": "The ₹50,000 Tax Deduction Math",
        "svg_subtitle_1": "Evaluate equity allocation, annuity constraints, and lock-in periods,",
        "svg_subtitle_2": "and discover how disciplined local tracking builds long-term wealth.",
        "body": """Every year between January and March, salaried professionals in India search for ways to trim their tax liability.

Among the options, the **National Pension System (NPS) Tier-1 account** stands out because of **Section 80CCD(1B)**—an exclusive deduction of up to **₹50,000** over and above the standard ₹1.5 Lakh limit under Section 80C.

For someone in the 30% tax bracket (under the Old Tax Regime), investing ₹50,000 into NPS saves **₹15,600 in cold tax cash**.

However, NPS comes with strict lock-in rules and mandatory annuity purchases. Is the tax break worth locking your capital away until age 60?

---

## The Pros of NPS Tier-1

1. **Ultra-Low Fund Management Costs:** NPS fund management charges are capped at ~0.09%, making it one of the lowest-cost retirement investment products in the world.
2. **Equity Exposure up to 75%:** Through Active Choice, investors can allocate up to 75% of their contributions into equities (Class E) for long-term compound growth.
3. **Partial Tax-Free Maturity:** At age 60, up to **60% of your accumulated corpus can be withdrawn completely tax-free**.

---

## The Cons & The Annuity Catch

* **Mandatory 40% Annuity:** At least 40% of your corpus must be used to purchase an annuity from an insurance provider. Current annuity yields in India range from 6% to 6.5%, and the monthly pension received is **fully taxable at your income tax slab rate**.
* **Strict Lock-in until Age 60:** Premature withdrawals before age 60 are severely restricted (capped at 20% lump sum, with 80% forced into annuity).
* **New Tax Regime Consideration:** Section 80CCD(1B) is **only deductible under the Old Tax Regime**. Under the New Tax Regime, only employer contributions under Section 80CCD(2) are deductible.

---

## The Verdict: Who Should Invest in NPS?

* **Invest in NPS** if: You are committed to the Old Tax Regime, struggle with the self-discipline to keep your hands off retirement funds, and want ultra-cheap equity+debt exposure.
* **Skip NPS** if: You have opted for the New Tax Regime (where 80CCD(1B) provides zero benefit), or you prefer full liquidity and flexible SWP (Systematic Withdrawal Plans) in mutual funds.

---

## Track Your Retirement Milestones Privately

Whether you invest via NPS, PPF, or mutual funds, consistent saving starts with intentional daily cash flow management.

**SpendSathi gives you full clarity without cloud exposure:**
* **Private Expense Logging:** Your bank SMS alerts and financial numbers never touch third-party servers.
* **Instant Monthly Reports:** Generate categorized statements for your CA or tax advisor in one click.
* **Biometric Lock:** Secure your financial records behind fingerprint authentication.

Download **[SpendSathi on Google Play](https://play.google.com/store/apps/details?id=com.finmate.app)** to take control of your financial destiny today.
"""
    }
]


def generate_svg_banner(data, output_path):
    """Generate crisp, modern 1200x630 SVG hero banner with distinct theme colors and tailored right-side graphics."""
    theme_key = data.get("theme", "emerald")
    t = THEME_PALETTES.get(theme_key, THEME_PALETTES["emerald"])
    graphic_type = data.get("graphic_type", "budget_donut")

    # Generate custom right-side graphic SVG element based on graphic_type
    right_graphic_svg = ""
    if graphic_type == "sip_chart":
        right_graphic_svg = f"""
  <!-- Right Graphic: Step-Up SIP Compounding Growth Staircase -->
  <g transform="translate(740, 110)">
    <!-- Chart Background Glass Plate -->
    <rect x="0" y="0" width="380" height="380" rx="24" fill="{t['card_bg_rgb']}" fill-opacity="0.65" stroke="{t['primary']}" stroke-width="1.5" stroke-opacity="0.4"/>
    
    <!-- Gridlines -->
    <line x1="30" y1="80" x2="350" y2="80" stroke="#334155" stroke-dasharray="4,4" stroke-width="1"/>
    <line x1="30" y1="160" x2="350" y2="160" stroke="#334155" stroke-dasharray="4,4" stroke-width="1"/>
    <line x1="30" y1="240" x2="350" y2="240" stroke="#334155" stroke-dasharray="4,4" stroke-width="1"/>
    <line x1="30" y1="320" x2="350" y2="320" stroke="#475569" stroke-width="1.5"/>

    <!-- Staircase Bars -->
    <rect x="50" y="250" width="45" height="70" rx="8" fill="{t['accent']}" fill-opacity="0.4"/>
    <rect x="115" y="210" width="45" height="110" rx="8" fill="{t['accent']}" fill-opacity="0.6"/>
    <rect x="180" y="150" width="45" height="170" rx="8" fill="{t['accent']}" fill-opacity="0.8"/>
    <rect x="245" y="80" width="45" height="240" rx="8" fill="{t['primary']}"/>

    <!-- Rising Exponential Trendline -->
    <path d="M 72 230 Q 150 180 267 60" fill="none" stroke="#F59E0B" stroke-width="4.5" stroke-linecap="round"/>
    <!-- Arrowhead -->
    <polygon points="267,48 277,65 257,65" fill="#F59E0B"/>

    <!-- Floating Badge: +10% Annual Top-Up -->
    <g transform="translate(180, 20)">
      <rect x="0" y="0" width="160" height="36" rx="18" fill="#1E1B4B" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="80" y="23" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#FDE68A" text-anchor="middle">+10% Step-Up SIP</text>
    </g>

    <!-- Floating Rupee Coin Node -->
    <g transform="translate(60, 200)">
      <circle cx="16" cy="16" r="18" fill="#F59E0B" stroke="#FEF3C7" stroke-width="2"/>
      <text x="16" y="23" font-family="'Inter', system-ui, sans-serif" font-size="18" font-weight="800" fill="#78350F" text-anchor="middle">₹</text>
    </g>
  </g>
"""
    elif graphic_type == "credit_gauge":
        right_graphic_svg = f"""
  <!-- Right Graphic: CIBIL Score 750+ Speedometer Gauge -->
  <g transform="translate(730, 95)">
    <!-- Outer decorative ring -->
    <circle cx="210" cy="220" r="195" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,6" opacity="0.6"/>
    
    <!-- Dial Background Arc (from 180 to 0 deg) -->
    <path d="M 50,220 A 160,160 0 0,1 370,220" fill="none" stroke="#1E293B" stroke-width="32" stroke-linecap="round"/>
    
    <!-- Red Zone (300-600) -->
    <path d="M 50,220 A 160,160 0 0,1 120,105" fill="none" stroke="#EF4444" stroke-width="30" stroke-linecap="round"/>
    <!-- Yellow Zone (600-750) -->
    <path d="M 120,105 A 160,160 0 0,1 270,75" fill="none" stroke="#F59E0B" stroke-width="30"/>
    <!-- Green Zone (750-900) -->
    <path d="M 270,75 A 160,160 0 0,1 370,220" fill="none" stroke="{t['primary']}" stroke-width="32" stroke-linecap="round"/>

    <!-- Center Hub -->
    <circle cx="210" cy="220" r="105" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="2"/>

    <!-- Pointer Needle pointing to ~785 (around 35 deg from horizontal right) -->
    <line x1="210" y1="220" x2="310" y2="135" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>
    <circle cx="210" cy="220" r="14" fill="{t['primary']}" stroke="#FFFFFF" stroke-width="3"/>

    <!-- Digital Score Readout inside Hub -->
    <text x="210" y="275" font-family="'Inter', system-ui, sans-serif" font-size="44" font-weight="900" fill="#FFFFFF" text-anchor="middle">785</text>
    <rect x="145" y="295" width="130" height="26" rx="13" fill="{t['badge_bg']}" stroke="{t['primary']}" stroke-width="1"/>
    <text x="210" y="312" font-family="'Inter', system-ui, sans-serif" font-size="11" font-weight="800" fill="{t['accent']}" text-anchor="middle" letter-spacing="1.5">EXCELLENT</text>
  </g>
"""
    elif graphic_type == "credit_card":
        right_graphic_svg = f"""
  <!-- Right Graphic: Debt Avalanche Credit Cards & Avalanche Payoff -->
  <g transform="translate(740, 110)">
    <!-- Back Card (Revolving Debt) -->
    <g transform="rotate(-8 170 120)">
      <rect x="30" y="50" width="310" height="190" rx="18" fill="#451A03" stroke="#F59E0B" stroke-width="2"/>
      <rect x="60" y="85" width="45" height="34" rx="6" fill="#FBBF24" fill-opacity="0.8"/>
      <text x="60" y="155" font-family="'Courier New', monospace" font-size="15" fill="#FEF3C7" letter-spacing="2">•••• •••• •••• 4281</text>
      <text x="60" y="195" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#F59E0B">APR: 42% REVOLVING</text>
    </g>

    <!-- Front Card (Avalanche Attack Card) -->
    <g transform="rotate(6 190 230)">
      <rect x="50" y="160" width="310" height="190" rx="18" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="2.5"/>
      <rect x="80" y="195" width="45" height="34" rx="6" fill="{t['accent']}" fill-opacity="0.85"/>
      <text x="80" y="265" font-family="'Courier New', monospace" font-size="15" fill="#FFFFFF" letter-spacing="2">•••• •••• •••• 8819</text>
      <rect x="80" y="285" width="150" height="24" rx="12" fill="{t['badge_bg']}" stroke="{t['primary']}" stroke-width="1"/>
      <text x="155" y="301" font-family="'Inter', system-ui, sans-serif" font-size="10" font-weight="800" fill="{t['accent']}" text-anchor="middle">DEBT CLEARED: ₹0</text>
    </g>

    <!-- Downward Payoff Trendline Badge -->
    <g transform="translate(20, 20)">
      <rect x="0" y="0" width="190" height="40" rx="20" fill="#14532D" stroke="#22C55E" stroke-width="1.5"/>
      <text x="95" y="25" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#BBF7D0" text-anchor="middle">⚡ High APR Eliminated</text>
    </g>
  </g>
"""
    elif graphic_type == "subscription_radar":
        right_graphic_svg = f"""
  <!-- Right Graphic: Subscription Radar & Micro-Charge Detector -->
  <g transform="translate(730, 95)">
    <!-- Radar concentric circles -->
    <circle cx="210" cy="210" r="190" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,6" opacity="0.5"/>
    <circle cx="210" cy="210" r="130" fill="none" stroke="{t['primary']}" stroke-width="1.5" stroke-opacity="0.3"/>
    <circle cx="210" cy="210" r="70" fill="none" stroke="{t['accent']}" stroke-width="1.5" stroke-opacity="0.5"/>
    <circle cx="210" cy="210" r="10" fill="{t['primary']}"/>

    <!-- Radar Sweep Cone -->
    <path d="M 210,210 L 390,140 A 190,190 0 0,0 210,20 Z" fill="{t['primary']}" fill-opacity="0.12"/>

    <!-- Floating Subscription Cards -->
    <g transform="translate(30, 70)">
      <rect x="0" y="0" width="130" height="50" rx="14" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="1.5"/>
      <text x="18" y="23" font-family="'Inter', system-ui, sans-serif" font-size="11" font-weight="600" fill="#CBD5E1">Video OTT</text>
      <text x="18" y="40" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="800" fill="{t['accent']}">₹499 / mo</text>
    </g>

    <g transform="translate(230, 260)">
      <rect x="0" y="0" width="140" height="50" rx="14" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="1.5"/>
      <text x="18" y="23" font-family="'Inter', system-ui, sans-serif" font-size="11" font-weight="600" fill="#CBD5E1">Cloud Storage</text>
      <text x="18" y="40" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="800" fill="{t['accent']}">₹199 / mo</text>
    </g>

    <g transform="translate(40, 270)">
      <rect x="0" y="0" width="130" height="50" rx="14" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="1.5"/>
      <text x="18" y="23" font-family="'Inter', system-ui, sans-serif" font-size="11" font-weight="600" fill="#CBD5E1">Delivery Pass</text>
      <text x="18" y="40" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="800" fill="{t['accent']}">₹99 / mo</text>
    </g>

    <!-- Center Cut-Off Badge -->
    <g transform="translate(130, 360)">
      <rect x="0" y="0" width="160" height="34" rx="17" fill="#4C0519" stroke="#E11D48" stroke-width="1.5"/>
      <text x="80" y="22" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFE4E6" text-anchor="middle">✂️ Cancel Mandates</text>
    </g>
  </g>
"""
    elif graphic_type == "vault_shield":
        right_graphic_svg = f"""
  <!-- Right Graphic: Emergency Safety Vault & Runway Ladder -->
  <g transform="translate(740, 100)">
    <!-- Vault Outer Wheel -->
    <circle cx="200" cy="200" r="180" fill="none" stroke="#334155" stroke-width="10"/>
    <circle cx="200" cy="200" r="160" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="3"/>
    
    <!-- Vault Spokes -->
    <line x1="200" y1="40" x2="200" y2="360" stroke="#334155" stroke-width="3"/>
    <line x1="40" y1="200" x2="360" y2="200" stroke="#334155" stroke-width="3"/>
    <line x1="86" y1="86" x2="314" y2="314" stroke="#334155" stroke-width="3"/>
    <line x1="86" y1="314" x2="314" y2="86" stroke="#334155" stroke-width="3"/>

    <!-- Vault Central Hub -->
    <circle cx="200" cy="200" r="85" fill="{t['bg_svg_start']}" stroke="{t['primary']}" stroke-width="3.5"/>

    <!-- Central Security Shield Motif -->
    <path d="M 200 150 L 240 168 L 240 215 C 240 242 200 258 200 258 C 200 258 160 242 160 215 L 160 168 Z" fill="{t['primary']}" fill-opacity="0.25" stroke="{t['primary']}" stroke-width="3"/>
    <!-- Checkmark inside shield -->
    <path d="M 188 205 L 197 214 L 214 195" fill="none" stroke="{t['accent']}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>

    <!-- Floating Runway Pill: 6 Months Covered -->
    <g transform="translate(110, 340)">
      <rect x="0" y="0" width="180" height="36" rx="18" fill="{t['badge_bg']}" stroke="{t['primary']}" stroke-width="1.5"/>
      <text x="90" y="23" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="{t['badge_text']}" text-anchor="middle">🛡️ 6-Month Liquid Runway</text>
    </g>
  </g>
"""
    elif graphic_type == "gold_scales":
        right_graphic_svg = f"""
  <!-- Right Graphic: Gold Bullion vs Equity SIP Balance Scales -->
  <g transform="translate(730, 110)">
    <rect x="0" y="0" width="380" height="370" rx="24" fill="{t['card_bg_rgb']}" fill-opacity="0.6" stroke="{t['primary']}" stroke-width="1.5"/>
    
    <!-- Central Scale Pillar -->
    <line x1="190" y1="60" x2="190" y2="300" stroke="#94A3B8" stroke-width="5" stroke-linecap="round"/>
    <polygon points="170,300 210,300 200,320 180,320" fill="#64748B"/>

    <!-- Scale Beam -->
    <line x1="70" y1="90" x2="310" y2="90" stroke="#F59E0B" stroke-width="4.5" stroke-linecap="round"/>
    <circle cx="190" cy="90" r="10" fill="#F59E0B"/>

    <!-- Left Pan: Gold Bars (SGB) -->
    <line x1="90" y1="90" x2="90" y2="180" stroke="#94A3B8" stroke-width="2"/>
    <path d="M 40,180 Q 90,210 140,180 Z" fill="#78350F" stroke="#F59E0B" stroke-width="2"/>
    <rect x="65" y="150" width="50" height="22" rx="4" fill="#F59E0B" stroke="#FEF3C7" stroke-width="1.5"/>
    <text x="90" y="166" font-family="'Inter', system-ui, sans-serif" font-size="10" font-weight="800" fill="#78350F" text-anchor="middle">SGB 2.5%</text>

    <!-- Right Pan: Equity SIP Growth -->
    <line x1="290" y1="90" x2="290" y2="180" stroke="#94A3B8" stroke-width="2"/>
    <path d="M 240,180 Q 290,210 340,180 Z" fill="#064E3B" stroke="#10B981" stroke-width="2"/>
    <polygon points="275,170 290,145 305,170" fill="#10B981"/>
    <text x="290" y="165" font-family="'Inter', system-ui, sans-serif" font-size="10" font-weight="800" fill="#BBF7D0" text-anchor="middle">12% SIP</text>

    <!-- Bottom Balanced Ratio Pill -->
    <g transform="translate(100, 315)">
      <rect x="0" y="0" width="180" height="34" rx="17" fill="#451A03" stroke="#F59E0B" stroke-width="1.5"/>
      <text x="90" y="22" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#FEF3C7" text-anchor="middle">⚖️ 80/15/5 Balanced Ratio</text>
    </g>
  </g>
"""
    elif graphic_type == "tax_calculator":
        right_graphic_svg = f"""
  <!-- Right Graphic: Old vs New Tax Regime Comparison Card -->
  <g transform="translate(740, 110)">
    <!-- Comparison Card Container -->
    <rect x="0" y="0" width="370" height="370" rx="22" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="2"/>
    
    <!-- Header -->
    <rect x="0" y="0" width="370" height="60" rx="22" fill="{t['badge_bg']}"/>
    <rect x="0" y="30" width="370" height="30" fill="{t['badge_bg']}"/>
    <text x="185" y="38" font-family="'Inter', system-ui, sans-serif" font-size="15" font-weight="800" fill="{t['badge_text']}" text-anchor="middle">TAX SLAB COMPARISON</text>

    <!-- Left Column: Old Regime -->
    <g transform="translate(25, 80)">
      <rect x="0" y="0" width="150" height="180" rx="14" fill="#0F172A" stroke="#334155" stroke-width="1.5"/>
      <text x="75" y="30" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#94A3B8" text-anchor="middle">Old Regime</text>
      <text x="75" y="55" font-family="'Inter', system-ui, sans-serif" font-size="11" fill="#64748B" text-anchor="middle">HRA + 80C + 80D</text>
      <line x1="20" y1="75" x2="130" y2="75" stroke="#1E293B" stroke-width="1"/>
      <text x="75" y="110" font-family="'Inter', system-ui, sans-serif" font-size="11" fill="#94A3B8" text-anchor="middle">High Deductions</text>
      <text x="75" y="145" font-family="'Inter', system-ui, sans-serif" font-size="16" font-weight="800" fill="#F59E0B" text-anchor="middle">> ₹3.75L</text>
    </g>

    <!-- Right Column: New Regime (Winner) -->
    <g transform="translate(195, 80)">
      <rect x="0" y="0" width="150" height="180" rx="14" fill="{t['badge_bg']}" stroke="{t['primary']}" stroke-width="2"/>
      <text x="75" y="30" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="800" fill="{t['badge_text']}" text-anchor="middle">New Regime</text>
      <text x="75" y="55" font-family="'Inter', system-ui, sans-serif" font-size="11" fill="{t['accent']}" text-anchor="middle">₹75k Std Deduction</text>
      <line x1="20" y1="75" x2="130" y2="75" stroke="{t['primary']}" stroke-width="1" stroke-opacity="0.4"/>
      <text x="75" y="110" font-family="'Inter', system-ui, sans-serif" font-size="11" fill="{t['badge_text']}" text-anchor="middle">Zero Friction</text>
      <text x="75" y="145" font-family="'Inter', system-ui, sans-serif" font-size="16" font-weight="800" fill="#FFFFFF" text-anchor="middle">DEFAULT 🏆</text>
    </g>

    <!-- Bottom Breakeven formula banner -->
    <g transform="translate(25, 290)">
      <rect x="0" y="0" width="320" height="50" rx="14" fill="#0F172A" stroke="{t['primary']}" stroke-width="1"/>
      <text x="160" y="31" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="{t['accent']}" text-anchor="middle">Breakeven: Deductions > ₹3.75 Lakhs</text>
    </g>
  </g>
"""
    else:  # default: budget_donut
        right_graphic_svg = f"""
  <!-- Right Graphic: 50/30/20 Budget Allocation Ring -->
  <g transform="translate(730, 95)">
    <circle cx="210" cy="220" r="195" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,6" opacity="0.6"/>
    <!-- 50% Arc -->
    <path d="M 210,35 A 185,185 0 0,1 210,405" fill="none" stroke="{t['primary']}" stroke-width="36" stroke-linecap="round"/>
    <!-- 30% Arc -->
    <path d="M 210,405 A 185,185 0 0,1 55,140" fill="none" stroke="#F59E0B" stroke-width="36" stroke-linecap="round"/>
    <!-- 20% Arc -->
    <path d="M 55,140 A 185,185 0 0,1 210,35" fill="none" stroke="#06B6D4" stroke-width="36" stroke-linecap="round"/>

    <!-- Central Hub -->
    <circle cx="210" cy="220" r="110" fill="{t['card_bg_rgb']}" stroke="{t['primary']}" stroke-width="2"/>
    <text x="210" y="215" font-family="'Inter', system-ui, sans-serif" font-size="34" font-weight="900" fill="#FFFFFF" text-anchor="middle">50/30/20</text>
    <text x="210" y="245" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="{t['accent']}" text-anchor="middle">BUDGET RULE</text>
  </g>
"""

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <radialGradient id="bg" cx="25%" cy="45%" r="75%">
      <stop offset="0%" stop-color="{t['bg_svg_end']}"/>
      <stop offset="100%" stop-color="{t['bg_svg_start']}"/>
    </radialGradient>
    <pattern id="grid" x="0" y="0" width="28" height="28" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" fill="#334155" opacity="0.45"/>
    </pattern>
    <radialGradient id="glow-1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t['glow1_hex']}" stop-opacity="0.32"/>
      <stop offset="100%" stop-color="{t['glow1_hex']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow-2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{t['glow2_hex']}" stop-opacity="0.26"/>
      <stop offset="100%" stop-color="{t['glow2_hex']}" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur24">
      <feGaussianBlur stdDeviation="28"/>
    </filter>
  </defs>

  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect width="1200" height="630" fill="url(#grid)"/>

  <!-- Left Content: Editorial Typography -->
  <rect x="80" y="105" width="250" height="38" rx="19" fill="{t['badge_bg']}" stroke="{t['badge_border']}" stroke-width="1.4"/>
  <circle cx="102" cy="124" r="5" fill="{t['accent']}"/>
  <text x="118" y="129" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="{t['badge_text']}" letter-spacing="1.5">{data.get('category', 'PERSONAL FINANCE')}</text>

  <text x="80" y="205" font-family="'Inter', system-ui, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" letter-spacing="-1">{data.get('svg_headline_1', data['title'][:32])}</text>
  <text x="80" y="268" font-family="'Inter', system-ui, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" letter-spacing="-1"><tspan fill="{t['primary']}">{data.get('svg_headline_2', '')}</tspan></text>

  <text x="80" y="335" font-family="'Inter', system-ui, sans-serif" font-size="19" fill="#94A3B8" font-weight="400">{data.get('svg_subtitle_1', '')}</text>
  <text x="80" y="365" font-family="'Inter', system-ui, sans-serif" font-size="19" fill="#94A3B8" font-weight="400">{data.get('svg_subtitle_2', '')}</text>

  <line x1="80" y1="415" x2="600" y2="415" stroke="#334155" stroke-width="1.5"/>

  <g transform="translate(80, 445)">
    <circle cx="18" cy="18" r="18" fill="{t['bg_svg_end']}" stroke="{t['primary']}" stroke-width="1.5"/>
    <text x="18" y="23" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="{t['accent']}" text-anchor="middle">MV</text>
    <text x="48" y="23" font-family="'Inter', system-ui, sans-serif" font-size="15" fill="#CBD5E1" font-weight="500">By {data['author']} • {data.get('read_time', '7 min read')}</text>
  </g>

  <g transform="translate(80, 560)">
    <text x="0" y="0" font-family="'Inter', system-ui, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Spend<tspan fill="{t['primary']}">Sathi</tspan></text>
    <text x="125" y="-1" font-family="'Inter', system-ui, sans-serif" font-size="14" fill="#64748B">• 100% Offline Expense Tracker</text>
  </g>

{right_graphic_svg}
</svg>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG Banner: {output_path}")


def generate_webp_banner(data, output_path):
    """Generate sleek, high-resolution 1200x630 WebP banner with theme colors and graphic motif using Pillow."""
    try:
        theme_key = data.get("theme", "emerald")
        t = THEME_PALETTES.get(theme_key, THEME_PALETTES["emerald"])
        graphic_type = data.get("graphic_type", "budget_donut")

        img = Image.new('RGB', (1200, 630), color=t['bg_start'])
        draw = ImageDraw.Draw(img)

        # 1. Background gradient
        r1, g1, b1 = t['bg_start']
        r2, g2, b2 = t['bg_end']
        for i in range(1200):
            ratio = i / 1200.0
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            draw.line([(i, 0), (i, 630)], fill=(r, g, b))

        font_large = get_font(42, bold=True)
        font_sub = get_font(20, bold=False)
        font_badge = get_font(13, bold=True)
        font_author = get_font(15, bold=False)
        font_brand = get_font(22, bold=True)
        font_graphic = get_font(16, bold=True)
        font_graphic_large = get_font(38, bold=True)

        # 3. Category Badge
        category_text = data.get('category', 'PERSONAL FINANCE').upper()
        draw.rounded_rectangle([80, 95, 340, 133], radius=19, fill=t['badge_bg_rgb'], outline=t['badge_border_rgb'], width=2)
        draw.ellipse([98, 110, 108, 120], fill=t['accent_rgb'])
        draw.text((118, 106), category_text, fill=t['badge_text_rgb'], font=font_badge)

        # 4. Headlines & Subtitles
        h1 = data.get('svg_headline_1', data['title'][:32])
        h2 = data.get('svg_headline_2', '')
        s1 = data.get('svg_subtitle_1', '')
        s2 = data.get('svg_subtitle_2', '')

        draw.text((80, 160), h1, fill=(255, 255, 255), font=font_large)
        draw.text((80, 220), h2, fill=t['primary_rgb'], font=font_large)
        draw.text((80, 305), s1, fill=(148, 163, 184), font=font_sub)
        draw.text((80, 338), s2, fill=(148, 163, 184), font=font_sub)

        # 5. Divider & Author
        draw.line([(80, 410), (600, 410)], fill=(51, 65, 85), width=2)
        draw.ellipse([80, 435, 116, 471], fill=t['bg_end'], outline=t['primary_rgb'], width=2)
        draw.text((90, 443), "MV", fill=t['accent_rgb'], font=font_badge)
        draw.text((130, 444), f"By {data['author']}  •  {data.get('read_time', '7 min read')}", fill=(203, 213, 225), font=font_author)

        # 6. SpendSathi Wordmark at bottom
        draw.text((80, 545), "SpendSathi", fill=t['primary_rgb'], font=font_brand)
        draw.text((215, 550), "•  100% Offline Expense Tracker", fill=(100, 116, 139), font=font_author)

        # 7. Render distinct stylized right-side illustration
        right_box = [750, 110, 1130, 490]
        # Glass card container on the right
        draw.rounded_rectangle(right_box, radius=24, fill=t['card_bg_rgb'], outline=t['primary_rgb'], width=2)

        if graphic_type == "sip_chart":
            # Staircase compounding chart
            draw.line([(780, 420), (1100, 420)], fill=(71, 85, 105), width=2)
            draw.rounded_rectangle([790, 340, 840, 418], radius=8, fill=(*t['accent_rgb'], 100), outline=t['accent_rgb'])
            draw.rounded_rectangle([860, 290, 910, 418], radius=8, fill=(*t['accent_rgb'], 150), outline=t['accent_rgb'])
            draw.rounded_rectangle([930, 220, 980, 418], radius=8, fill=(*t['accent_rgb'], 200), outline=t['accent_rgb'])
            draw.rounded_rectangle([1000, 150, 1050, 418], radius=8, fill=t['primary_rgb'], outline=(255, 255, 255))
            # Golden growth curve
            draw.line([(815, 320), (885, 270), (955, 200), (1025, 130)], fill=(245, 158, 11), width=4)
            # Coin badge
            draw.ellipse([880, 140, 930, 190], fill=(245, 158, 11), outline=(254, 243, 199), width=2)
            draw.text((898, 150), "₹", fill=(120, 53, 15), font=font_graphic)
            # Label
            draw.text((860, 440), "10% Annual Step-Up", fill=t['accent_rgb'], font=font_graphic)

        elif graphic_type == "credit_gauge":
            # Speedometer Gauge
            draw.arc([800, 160, 1080, 440], start=180, end=0, fill=(71, 85, 105), width=28)
            draw.arc([800, 160, 1080, 440], start=180, end=235, fill=(239, 68, 68), width=28)
            draw.arc([800, 160, 1080, 440], start=235, end=300, fill=(245, 158, 11), width=28)
            draw.arc([800, 160, 1080, 440], start=300, end=360, fill=t['primary_rgb'], width=30)
            # Score Hub
            draw.ellipse([870, 230, 1010, 370], fill=t['bg_start'], outline=t['primary_rgb'], width=3)
            draw.text((905, 265), "785", fill=(255, 255, 255), font=font_graphic_large)
            draw.rounded_rectangle([890, 315, 990, 340], radius=12, fill=t['badge_bg_rgb'], outline=t['primary_rgb'])
            draw.text((905, 320), "EXCELLENT", fill=t['accent_rgb'], font=font_badge)

        elif graphic_type == "credit_card":
            # Staggered credit cards
            draw.rounded_rectangle([790, 160, 1050, 310], radius=16, fill=(69, 26, 3), outline=(245, 158, 11), width=2)
            draw.rounded_rectangle([810, 190, 850, 220], radius=6, fill=(251, 191, 36))
            draw.text((810, 240), "••••  ••••  ••••  42%", fill=(254, 243, 199), font=font_author)

            draw.rounded_rectangle([820, 260, 1090, 420], radius=16, fill=t['bg_end'], outline=t['primary_rgb'], width=3)
            draw.rounded_rectangle([845, 290, 885, 320], radius=6, fill=t['accent_rgb'])
            draw.text((845, 345), "DEBT CLEARED: ₹0", fill=(255, 255, 255), font=font_graphic)
            draw.rounded_rectangle([845, 375, 1010, 405], radius=12, fill=t['badge_bg_rgb'], outline=t['primary_rgb'])
            draw.text((865, 382), "AVALANCHE WIN", fill=t['accent_rgb'], font=font_badge)

        elif graphic_type == "subscription_radar":
            # Radar circles
            draw.ellipse([820, 170, 1060, 410], outline=(71, 85, 105), width=2)
            draw.ellipse([870, 220, 1010, 360], outline=t['primary_rgb'], width=2)
            draw.ellipse([930, 280, 950, 300], fill=t['primary_rgb'])
            # Streaming service pill badges
            draw.rounded_rectangle([780, 140, 920, 185], radius=12, fill=t['bg_start'], outline=t['primary_rgb'], width=2)
            draw.text((795, 152), "OTT: ₹499/mo", fill=t['accent_rgb'], font=font_badge)
            draw.rounded_rectangle([950, 210, 1100, 255], radius=12, fill=t['bg_start'], outline=(245, 158, 11), width=2)
            draw.text((965, 222), "Cloud: ₹199/mo", fill=(254, 243, 199), font=font_badge)
            draw.rounded_rectangle([860, 430, 1020, 470], radius=14, fill=(76, 5, 25), outline=(225, 29, 72), width=2)
            draw.text((880, 440), "Auto-Pay Cut", fill=(255, 228, 230), font=font_badge)

        elif graphic_type == "vault_shield":
            # Vault door
            draw.ellipse([800, 150, 1080, 430], outline=(71, 85, 105), width=8)
            draw.ellipse([830, 180, 1050, 400], fill=t['bg_end'], outline=t['primary_rgb'], width=3)
            draw.ellipse([880, 230, 1000, 350], fill=t['bg_start'], outline=t['accent_rgb'], width=2)
            draw.line([(800, 290), (1080, 290)], fill=(71, 85, 105), width=3)
            draw.line([(940, 150), (940, 430)], fill=(71, 85, 105), width=3)
            draw.rounded_rectangle([850, 435, 1030, 470], radius=14, fill=t['badge_bg_rgb'], outline=t['primary_rgb'])
            draw.text((865, 444), "6-Month Runway", fill=t['badge_text_rgb'], font=font_badge)

        elif graphic_type == "gold_scales":
            # Scales
            draw.line([940, 150, 940, 410], fill=(148, 163, 184), width=4)
            draw.line([830, 200, 1050, 200], fill=(245, 158, 11), width=4)
            draw.ellipse([930, 190, 950, 210], fill=(245, 158, 11))
            # Left gold bar
            draw.rounded_rectangle([805, 270, 875, 310], radius=6, fill=(245, 158, 11), outline=(254, 243, 199), width=2)
            draw.text((818, 282), "SGB 2.5%", fill=(120, 53, 15), font=font_badge)
            # Right SIP icon
            draw.rounded_rectangle([1005, 270, 1075, 310], radius=6, fill=t['primary_rgb'], outline=(255, 255, 255), width=2)
            draw.text((1015, 282), "12% SIP", fill=(255, 255, 255), font=font_badge)
            draw.rounded_rectangle([840, 435, 1040, 470], radius=14, fill=t['badge_bg_rgb'], outline=t['primary_rgb'])
            draw.text((855, 444), "80/15/5 Ratio", fill=t['accent_rgb'], font=font_badge)

        elif graphic_type == "tax_calculator":
            # Tax comparison
            draw.rounded_rectangle([775, 160, 925, 390], radius=16, fill=t['bg_start'], outline=(71, 85, 105), width=2)
            draw.text((800, 180), "Old Regime", fill=(148, 163, 184), font=font_badge)
            draw.text((795, 220), "80C + HRA", fill=(100, 116, 139), font=font_badge)
            draw.text((800, 310), "> ₹3.75L", fill=(245, 158, 11), font=font_graphic)

            draw.rounded_rectangle([950, 160, 1105, 390], radius=16, fill=t['badge_bg_rgb'], outline=t['primary_rgb'], width=3)
            draw.text((975, 180), "New Regime", fill=t['badge_text_rgb'], font=font_badge)
            draw.text((970, 220), "₹75k Std Ded", fill=t['accent_rgb'], font=font_badge)
            draw.text((975, 310), "DEFAULT", fill=(255, 255, 255), font=font_graphic)
            draw.rounded_rectangle([805, 430, 1075, 470], radius=14, fill=t['bg_start'], outline=t['primary_rgb'])
            draw.text((820, 442), "Breakeven: Deductions > ₹3.75L", fill=t['accent_rgb'], font=font_badge)

        else:  # budget_donut
            draw.arc([800, 150, 1080, 430], start=0, end=180, fill=t['primary_rgb'], width=32)
            draw.arc([800, 150, 1080, 430], start=180, end=290, fill=(245, 158, 11), width=32)
            draw.arc([800, 150, 1080, 430], start=290, end=360, fill=(6, 182, 212), width=32)
            draw.ellipse([860, 210, 1020, 370], fill=t['bg_start'], outline=t['primary_rgb'], width=2)
            draw.text((885, 260), "50/30/20", fill=(255, 255, 255), font=font_graphic)
            draw.text((895, 295), "BUDGET", fill=t['accent_rgb'], font=font_badge)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path, 'WEBP', quality=92)
        print(f"Generated WebP Banner: {output_path}")
        return True
    except Exception as e:
        print(f"WebP generation failed: {e}")
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


def select_editorial_article(existing_slugs, requested_slug=None):
    """Select requested article or first unposted article from editorial queue."""
    if requested_slug:
        for article in EDITORIAL_QUEUE:
            if article["slug"] == requested_slug:
                return article
    for article in EDITORIAL_QUEUE:
        if article["slug"] not in existing_slugs:
            return article
    return None


def regenerate_all_banners(repo_root):
    """Regenerate distinct, colorful banners for all queue articles that exist in _posts."""
    posts_dir = os.path.join(repo_root, "_posts")
    svg_dir = os.path.join(repo_root, "assets", "blog-images")
    webp_dir = os.path.join(repo_root, "assets", "images", "blog")

    queue_map = {a["slug"]: a for a in EDITORIAL_QUEUE}

    # Also add metadata for first-of-the-month-budgeting so it gets a distinct banner
    queue_map["first-of-the-month-budgeting"] = {
        "slug": "first-of-the-month-budgeting",
        "title": "First of the Month Budgeting: Plan November Expenses",
        "category": "MONTHLY BUDGETING",
        "theme": "emerald",
        "graphic_type": "budget_donut",
        "author": "Mohit Varma",
        "read_time": "6 min read",
        "svg_headline_1": "First of the Month",
        "svg_headline_2": "Budgeting Blueprint",
        "svg_subtitle_1": "Take control of your salary before UPI scans begin,",
        "svg_subtitle_2": "and why 100% private offline tracking guarantees success."
    }

    queue_map["zero-based-budgeting-upi-india"] = {
        "slug": "zero-based-budgeting-upi-india",
        "title": "The Zero-Based Budgeting Guide for Indians",
        "category": "ZERO-BASED BUDGETING",
        "theme": "indigo",
        "graphic_type": "budget_donut",
        "author": "Mohit Varma",
        "read_time": "7 min read",
        "svg_headline_1": "Zero-Based Budgeting",
        "svg_headline_2": "Give Every Rupee a Job",
        "svg_subtitle_1": "How allocating salary stops high-frequency UPI leaks,",
        "svg_subtitle_2": "and why private offline budgeting guarantees adherence."
    }

    count = 0
    for p in glob.glob(os.path.join(posts_dir, "*.md")):
        name = os.path.basename(p)
        m = re.match(r'^\d{4}-\d{2}-\d{2}-(.*)\.md$', name)
        if not m:
            continue
        slug = m.group(1)
        if slug in queue_map:
            data = queue_map[slug]
            svg_path = os.path.join(svg_dir, f"{slug}.svg")
            webp_path1 = os.path.join(webp_dir, f"{slug}.webp")
            webp_path2 = os.path.join(svg_dir, f"{slug}.webp")
            generate_svg_banner(data, svg_path)
            generate_webp_banner(data, webp_path1)
            generate_webp_banner(data, webp_path2)
            if slug == "first-of-the-month-budgeting":
                shutil.copyfile(webp_path1, os.path.join(webp_dir, "november-budget.webp"))
                shutil.copyfile(webp_path2, os.path.join(svg_dir, "november-budget.webp"))
            count += 1

    print(f"Successfully regenerated {count} distinct banners!")


def main():
    parser = argparse.ArgumentParser(description="SpendSathi Blog Article Generator")
    parser.add_argument("--date", help="Custom timestamp in 'YYYY-MM-DD HH:MM:SS +0530' format")
    parser.add_argument("--slug", help="Generate a specific article slug from the editorial queue")
    parser.add_argument("--force", action="store_true", help="Force generate even if already posted")
    parser.add_argument("--regenerate-banners", action="store_true", help="Regenerate all banners for existing posts")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(repo_root, "_posts")
    svg_dir = os.path.join(repo_root, "assets", "blog-images")
    webp_dir = os.path.join(repo_root, "assets", "images", "blog")

    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(svg_dir, exist_ok=True)
    os.makedirs(webp_dir, exist_ok=True)

    if getattr(args, "regenerate_banners", False):
        regenerate_all_banners(repo_root)
        return

    if args.date:
        timestamp_str = args.date
        date_part = timestamp_str.split(" ")[0]
    else:
        now = datetime.now(IST)
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S +0530")
        date_part = now.strftime("%Y-%m-%d")

    existing_slugs = get_existing_slugs(posts_dir)
    print(f"Found {len(existing_slugs)} existing articles in _posts/")

    data = select_editorial_article(existing_slugs, requested_slug=args.slug)

    if not data:
        print("No new unique articles to generate at this time. All queue articles are published.")
        return

    # Check if this slug already exists
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
    print(f"  Theme:       {data.get('theme')}")
    print(f"  Graphic:     {data.get('graphic_type')}")
    print(f"  Published:   true")
    print(f"  Banner WebP: {webp_path1}")


if __name__ == "__main__":
    main()
