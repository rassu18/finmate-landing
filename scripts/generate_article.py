#!/usr/bin/env python3
"""
Automated SEO Article & Banner Generator for SpendSathi Blog.
Generates comprehensive Jekyll blog articles formatted with full IST timestamps,
'published: true' flags, and accompanying 1200x630 vector SVG header banners.
"""

import os
import sys
import argparse
from datetime import datetime
import zoneinfo

IST = zoneinfo.ZoneInfo("Asia/Kolkata")

DEFAULT_ARTICLE = {
    "title": "The Zero-Based Budgeting Guide for Indians: How to Give Every Rupee a Job in the UPI Era",
    "slug": "zero-based-budgeting-upi-india",
    "category": "BUDGETING GUIDE",
    "author": "Mohit Kumar Varma",
    "excerpt": "When money sits unassigned in your savings account, high-frequency UPI scans slowly bleed it dry. Here is how Zero-Based Budgeting gives every single rupee an intentional mission before the month starts — and how automated local tracking makes it effortless.",
    "tags": ["zero-based budgeting", "UPI", "personal finance", "money management", "SpendSathi"],
    "read_time": "8 min read",
    "svg_headline_1": "Zero-Based Budgeting",
    "svg_headline_2": "for UPI Users",
    "svg_subtitle_1": "How giving every rupee a job stops the silent scan-and-pay leak,",
    "svg_subtitle_2": "and why 100% local tracking is the missing link.",
    "body": """Have you ever checked your bank account on salary day, felt a warm surge of financial security, only to find yourself wondering where all that money vanished three weeks later?

You did not make any reckless purchases. You did not buy international flight tickets, luxury watches, or overpriced designer apparel. Yet, transaction by transaction—a ₹120 quick-commerce grocery addon, a ₹250 Swiggy delivery, an automated ₹699 OTT subscription renewal, a ₹40 evening filter coffee—your salary quietly evaporated into thin air.

In personal finance, this phenomenon is known as the **"idle cash trap."** When money sits in a checking or savings account without an explicit assignment, human psychology defaults to viewing it as surplus spending money. In an economy powered by instant UPI QR scans, this ambiguity is fatal to your savings.

The antidote is an aggressive, battle-tested budgeting framework developed over four decades ago, now radically updated for the digital rupee: **Zero-Based Budgeting (ZBB)**.

---

## What Exactly Is Zero-Based Budgeting?

Most people budget backwards:
1. They earn their monthly income.
2. They spend money throughout the month on bills, food, and daily impulses.
3. They promise to save "whatever is left over" at the end of the month.

The fatal flaw? **Nothing is ever left over.** Parkinson’s Law dictates that expenses expand to fill whatever balance is available.

Zero-Based Budgeting flips this equation entirely:

$$\\text{Income} - \\text{Expenses} - \\text{Savings} = \\text{₹0}$$

The name "Zero-Based" causes panic for beginners who mistakenly assume it means having zero money in their bank account. It does not. Rather, it means that **every single rupee of your net income is deliberately assigned a specific purpose before the month begins.**

If your take-home pay is ₹80,000 this month, every single one of those 80,000 rupees receives a job:
* ₹24,000 for Rent & Maintenance
* ₹12,000 for Groceries & Utilities
* ₹8,000 for Discretionary Dining & Entertainment
* ₹15,000 for Mutual Fund SIPs
* ₹5,000 for Emergency Fund Buffer
* ₹6,000 for Term & Health Insurance Reserves
* ₹10,000 for Upcoming Festive Travel

$$\\text{₹80,000} - \\text{₹80,000} = \\text{₹0 unassigned.}$$

When every rupee has an assigned post, you eliminate the mental illusion of "free money."

---

## Why Traditional Zero-Based Budgeting Fails in Modern India

The Zero-Based method is world-famous. Yet, if you ask ten working professionals in Bengaluru, Mumbai, or Delhi who attempted it, nine will tell you they abandoned it within 14 days.

Why? Because the original zero-based system was engineered in America during the era of paper checks and physical cash envelopes. In that world, you withdrew cash on the 1st of the month, divided notes into physical paper envelopes labeled "Rent," "Groceries," and "Fuel," and when an envelope was empty, you stopped spending.

Try doing that in modern India, where:
1. **You make 5 to 15 UPI transactions every single day.** From paying a roadside coconut vendor ₹50 to booking an Uber for ₹240, cash is practically obsolete.
2. **Transactions are frictionless.** Swiping or scanning takes two seconds via phone biometrics.
3. **Manual logging creates cognitive exhaustion.** Nobody has the patience to open a spreadsheet or tap through multiple menus in a bloated budgeting app 10 times a day just to log a ₹20 bottle of water.

By day seven, untracked transactions pile up. Your manual ledger falls behind by ₹4,200. Frustrated and overwhelmed, you abandon the system.

---

## The 4 Steps to Adapt Zero-Based Budgeting for the UPI Era

To make Zero-Based Budgeting thrive in a high-velocity digital payment environment, you need a modern system that pairs intentional planning with automated tracking:

### Step 1: Pre-Allocate Your Income on the 1st (The Blueprint)
Before a single UPI QR code is scanned, write down your realistic spending buckets for the month. Divide them into three main buckets:
* **Fixed Obligations:** Rent, EMIs, electricity, broadband, postpaid plans.
* **Automated Wealth Building:** Direct SIP mutual funds, recurring deposits, PPF transfers scheduled within 48 hours of salary credit.
* **Variable Living Budgets:** Groceries, dining out, commute, impulse allowances.

### Step 2: Establish an "Impulse Buffer" Category
Human life is unpredictable. If you allocate exactly ₹0 for spontaneity, your budget will break the first time a colleague suggests grabbing dinner. Always allocate a realistic 5% to 8% "Impulse & Miscellaneous" envelope. When unexpected expenses arise, absorb them through this dedicated buffer rather than draining your savings bucket.

### Step 3: Close the Review Loop Weekly, Not Monthly
Waiting until the 30th to audit your finances is an autopsy. Checking in every Sunday evening for 5 minutes is a course correction. If your dining-out envelope is 80% spent by the 12th, you have two full weeks to adjust your cooking habits before a deficit occurs.

### Step 4: Automate the Ledger Locally
The secret to sustainable budgeting is removing human effort from data entry. You should never manually type an expense that your bank has already recorded and transmitted via SMS alert.

---

## Why SpendSathi Is the Missing Engine for Local Zero-Based Budgeting

Most digital budgeting apps force an unacceptable trade-off: in exchange for automatic expense categorization, they require you to upload your complete financial life, SMS inbox, and bank transaction history to third-party cloud servers. 

Your salary, account numbers, merchant names, and daily spending habits are uploaded, indexed, and frequently mined for credit score ads and personal loan spam.

**SpendSathi was built on a radically different philosophy: 100% Local-First Privacy.**

1. **Instant On-Device SMS Parsing:** SpendSathi reads your bank and UPI debit alerts directly on your Android device using offline regex algorithms. Not a single byte of your financial data ever leaves your phone.
2. **Zero Account Required:** No cloud login, no Google sync, no external database. Your finances remain strictly between you and your device.
3. **Automated Envelope Categorization:** Every UPI payment is automatically parsed and mapped against your spending categories, giving you real-time visibility into whether your grocery or entertainment envelope is running low.
4. **Zero Latency:** Because everything runs locally in native Jetpack Compose, the app opens instantly with zero loading spinners or network lag.

---

## The 7-Day Zero-Based Challenge

Ready to take control of your financial cash flow? Start with this simple 7-day blueprint:

1. **Calculate your take-home pay** for the upcoming month.
2. **Deduct your fixed investments and mandatory bills** on day one.
3. **Assign every remaining rupee** to variable spending buckets until unassigned cash reaches exactly zero.
4. **Install [SpendSathi](https://play.google.com/store/apps/details?id=com.finmate.app)** to let on-device automation silently track and categorize every UPI debit in the background.

When every rupee knows where it is supposed to go, you stop wondering where your money went—and start choosing where it takes you.
"""
}


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

  <!-- Background -->
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect width="1200" height="630" fill="url(#grid)"/>

  <!-- Ambient Glows -->
  <ellipse cx="280" cy="310" rx="300" ry="250" fill="url(#glow-green)" filter="url(#blur24)"/>
  <ellipse cx="960" cy="280" rx="280" ry="260" fill="url(#glow-gold)" filter="url(#blur24)"/>
  <ellipse cx="850" cy="460" rx="200" ry="180" fill="url(#glow-cyan)" filter="url(#blur24)"/>

  <!-- Right Visual: Zero-Based Flow & Wallet Allocation Graphic -->
  <g transform="translate(720, 85)">
    <!-- Outer decorative guide circle -->
    <circle cx="210" cy="225" r="190" fill="none" stroke="#334155" stroke-width="1.5" stroke-dasharray="5,6" opacity="0.5"/>

    <!-- Central Zero-Balance Core Hub -->
    <circle cx="210" cy="225" r="110" fill="#0F172A" stroke="#16A34A" stroke-width="2.5"/>
    <circle cx="210" cy="225" r="90" fill="#1E293B"/>

    <!-- Large Rupee Equals Zero Mathematical Symbol -->
    <text x="210" y="215" font-family="'Inter', system-ui, sans-serif" font-size="28" font-weight="800" fill="#22C55E" text-anchor="middle">₹ IN - OUT</text>
    <text x="210" y="258" font-family="'Inter', system-ui, sans-serif" font-size="38" font-weight="900" fill="#FFFFFF" text-anchor="middle">= ₹0</text>

    <!-- Satellite Allocation Nodes -->
    <!-- Node 1: SIP & Wealth (Top Right) -->
    <g transform="translate(320, 60)">
      <rect x="0" y="0" width="130" height="42" rx="21" fill="#0F172A" stroke="#22C55E" stroke-width="1.5"/>
      <circle cx="20" cy="21" r="6" fill="#22C55E"/>
      <text x="36" y="26" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#F8FAFC">SIP / Invest</text>
    </g>
    <path d="M 285,150 L 320,102" fill="none" stroke="#22C55E" stroke-width="2" stroke-dasharray="3,3" opacity="0.7"/>

    <!-- Node 2: Fixed Bills (Top Left) -->
    <g transform="translate(0, 75)">
      <rect x="0" y="0" width="125" height="42" rx="21" fill="#0F172A" stroke="#06B6D4" stroke-width="1.5"/>
      <circle cx="20" cy="21" r="6" fill="#06B6D4"/>
      <text x="36" y="26" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#F8FAFC">Fixed Bills</text>
    </g>
    <path d="M 135,160 L 115,117" fill="none" stroke="#06B6D4" stroke-width="2" stroke-dasharray="3,3" opacity="0.7"/>

    <!-- Node 3: Daily UPI Spends (Bottom Left) -->
    <g transform="translate(15, 340)">
      <rect x="0" y="0" width="135" height="42" rx="21" fill="#0F172A" stroke="#EAB308" stroke-width="1.5"/>
      <circle cx="20" cy="21" r="6" fill="#EAB308"/>
      <text x="36" y="26" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#F8FAFC">UPI Expenses</text>
    </g>
    <path d="M 140,290 L 125,340" fill="none" stroke="#EAB308" stroke-width="2" stroke-dasharray="3,3" opacity="0.7"/>

    <!-- Node 4: Emergency Buffer (Bottom Right) -->
    <g transform="translate(305, 330)">
      <rect x="0" y="0" width="140" height="42" rx="21" fill="#0F172A" stroke="#A855F7" stroke-width="1.5"/>
      <circle cx="20" cy="21" r="6" fill="#A855F7"/>
      <text x="36" y="26" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#F8FAFC">Buffer Fund</text>
    </g>
    <path d="M 285,290 L 315,330" fill="none" stroke="#A855F7" stroke-width="2" stroke-dasharray="3,3" opacity="0.7"/>
  </g>

  <!-- Left Content: Editorial Typography -->
  <!-- Category Pill Badge -->
  <rect x="80" y="115" width="220" height="36" rx="18" fill="#14532D" stroke="#22C55E" stroke-width="1.2" stroke-opacity="0.6"/>
  <circle cx="102" cy="133" r="5" fill="#4ADE80"/>
  <text x="118" y="138" font-family="'Inter', system-ui, sans-serif" font-size="12" font-weight="700" fill="#BBF7D0" letter-spacing="1.5">{data['category']}</text>

  <!-- Main Headline -->
  <text x="80" y="210" font-family="'Inter', system-ui, sans-serif" font-size="50" font-weight="800" fill="#FFFFFF" letter-spacing="-1">{data['svg_headline_1']}</text>
  <text x="80" y="275" font-family="'Inter', system-ui, sans-serif" font-size="50" font-weight="800" fill="#FFFFFF" letter-spacing="-1">for <tspan fill="#22C55E">{data['svg_headline_2']}</tspan></text>

  <!-- Subtitle -->
  <text x="80" y="340" font-family="'Inter', system-ui, sans-serif" font-size="20" fill="#94A3B8" font-weight="400">{data['svg_subtitle_1']}</text>
  <text x="80" y="370" font-family="'Inter', system-ui, sans-serif" font-size="20" fill="#94A3B8" font-weight="400">{data['svg_subtitle_2']}</text>

  <!-- Divider line -->
  <line x1="80" y1="415" x2="600" y2="415" stroke="#334155" stroke-width="1.5"/>

  <!-- Author Meta -->
  <g transform="translate(80, 445)">
    <circle cx="16" cy="16" r="16" fill="#1E293B" stroke="#334155"/>
    <text x="16" y="21" font-family="'Inter', system-ui, sans-serif" font-size="13" font-weight="700" fill="#22C55E" text-anchor="middle">MV</text>
    <text x="44" y="21" font-family="'Inter', system-ui, sans-serif" font-size="15" fill="#CBD5E1" font-weight="500">By {data['author']} • {data['read_time']}</text>
  </g>

  <!-- Bottom Brand Signature -->
  <g transform="translate(80, 560)">
    <text x="0" y="0" font-family="'Inter', system-ui, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Spend<tspan fill="#22C55E">Sathi</tspan></text>
    <text x="125" y="-1" font-family="'Inter', system-ui, sans-serif" font-size="14" fill="#64748B">• Private Local-First Expense Tracking</text>
  </g>
</svg>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated SVG Banner: {output_path}")


def generate_markdown_post(data, output_path, timestamp_str):
    """Generate Markdown post with fully qualified IST timestamp and published: true."""
    tags_formatted = ", ".join(data["tags"])
    front_matter = f"""---
layout: post
title: "{data['title']}"
date: {timestamp_str}
author: {data['author']}
image: /assets/blog-images/{data['slug']}.svg
excerpt: "{data['excerpt']}"
tags: [{tags_formatted}]
published: true
---

{data['body'].strip()}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
    print(f"Generated Markdown Post: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="SpendSathi Blog Article Generator")
    parser.add_argument("--date", help="Custom timestamp in 'YYYY-MM-DD HH:MM:SS +0530' format")
    args = parser.parse_args()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(repo_root, "_posts")
    images_dir = os.path.join(repo_root, "assets", "blog-images")

    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(images_dir, exist_ok=True)

    if args.date:
        timestamp_str = args.date
        date_part = timestamp_str.split(" ")[0]
    else:
        now = datetime.now(IST)
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S +0530")
        date_part = now.strftime("%Y-%m-%d")

    data = DEFAULT_ARTICLE
    svg_filename = f"{data['slug']}.svg"
    md_filename = f"{date_part}-{data['slug']}.md"

    svg_path = os.path.join(images_dir, svg_filename)
    md_path = os.path.join(posts_dir, md_filename)

    generate_svg_banner(data, svg_path)
    generate_markdown_post(data, md_path, timestamp_str)

    print("\nGeneration summary:")
    print(f"  Post file:   {md_filename}")
    print(f"  Timestamp:   {timestamp_str}")
    print(f"  Published:   true")
    print(f"  Hero Banner: {svg_filename}")


if __name__ == "__main__":
    main()
