---
layout: default
title: Step-Up SIP Calculator — Calculate Top-Up Mutual Fund Returns Online
description: Free Step-Up SIP calculator with annual increment. Compare top-up SIP returns vs regular flat SIP, view yearly wealth progression, and calculate maturity value.
permalink: /step-up-sip-calculator.html
---

<!-- Breadcrumb Navigation -->
<nav class="mb-4 flex items-center space-x-2 text-xs font-medium text-slate-500" aria-label="Breadcrumb">
    <a href="/" class="hover:text-slate-900 transition">Home</a>
    <span>/</span>
    <a href="/calculators.html" class="hover:text-slate-900 transition">Calculators</a>
    <span>/</span>
    <span class="text-slate-900 font-semibold" aria-current="page">Step-Up SIP Calculator</span>
</nav>

<div class="mb-8">
    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs font-semibold uppercase tracking-wider mb-3">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
        <span>Wealth Multiplier Utility</span>
    </div>
    <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">Step-Up SIP Calculator</h1>
    <p class="text-base text-slate-500 leading-relaxed">
        Calculate your compounded mutual fund returns when you increase your monthly SIP contribution annually in tandem with your salary hikes.
    </p>
</div>

<!-- Interactive Calculator Widget -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        <!-- Controls Column (7 cols) -->
        <div class="lg:col-span-7 space-y-6">
            
            <!-- Monthly Investment Amount -->
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label for="stepup-amount-input" class="text-sm font-semibold text-slate-700">Initial Monthly Investment</label>
                    <div class="relative">
                        <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">&#8377;</span>
                        <input type="number" id="stepup-amount-input" name="stepup-amount-input" value="10000" min="500" max="500000" step="500"
                               class="w-36 pl-7 pr-3 py-1.5 text-right font-bold text-slate-900 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                    </div>
                </div>
                <input type="range" id="stepup-amount-slider" name="stepup-amount-slider" aria-label="Initial Monthly Investment Slider" min="500" max="100000" step="500" value="10000"
                       class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600">
                <div class="flex justify-between text-[11px] text-slate-400 mt-1">
                    <span>&#8377;500</span>
                    <span>&#8377;50,000</span>
                    <span>&#8377;1,00,000</span>
                </div>
            </div>

            <!-- Annual Step-Up Percentage -->
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label for="stepup-pct-input" class="text-sm font-semibold text-slate-700">Annual Step-Up (Top-Up)</label>
                    <div class="relative">
                        <input type="number" id="stepup-pct-input" name="stepup-pct-input" value="10" min="0" max="50" step="1"
                               class="w-24 pr-7 pl-3 py-1.5 text-right font-bold text-slate-900 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                        <span class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">%</span>
                    </div>
                </div>
                <input type="range" id="stepup-pct-slider" name="stepup-pct-slider" aria-label="Annual Step-Up Percentage Slider" min="0" max="30" step="1" value="10"
                       class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600">
                <div class="flex justify-between text-[11px] text-slate-400 mt-1">
                    <span>0% (Flat)</span>
                    <span>10% (Standard)</span>
                    <span>30%</span>
                </div>
            </div>

            <!-- Expected Return Rate -->
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label for="stepup-rate-input" class="text-sm font-semibold text-slate-700">Expected Annual Return Rate (p.a)</label>
                    <div class="relative">
                        <input type="number" id="stepup-rate-input" name="stepup-rate-input" value="12" min="1" max="30" step="0.5"
                               class="w-24 pr-7 pl-3 py-1.5 text-right font-bold text-slate-900 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                        <span class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">%</span>
                    </div>
                </div>
                <input type="range" id="stepup-rate-slider" name="stepup-rate-slider" aria-label="Expected Annual Return Rate Slider" min="1" max="30" step="0.5" value="12"
                       class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600">
                <div class="flex justify-between text-[11px] text-slate-400 mt-1">
                    <span>1%</span>
                    <span>12%</span>
                    <span>30%</span>
                </div>
            </div>

            <!-- Time Horizon -->
            <div>
                <div class="flex justify-between items-center mb-2">
                    <label for="stepup-years-input" class="text-sm font-semibold text-slate-700">Time Horizon</label>
                    <div class="relative">
                        <input type="number" id="stepup-years-input" name="stepup-years-input" value="10" min="1" max="35" step="1"
                               class="w-28 pr-11 pl-3 py-1.5 text-right font-bold text-slate-900 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                        <span class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-xs">Yrs</span>
                    </div>
                </div>
                <input type="range" id="stepup-years-slider" name="stepup-years-slider" aria-label="Time Horizon Slider" min="1" max="35" step="1" value="10"
                       class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600">
                <div class="flex justify-between text-[11px] text-slate-400 mt-1">
                    <span>1 Yr</span>
                    <span>15 Yrs</span>
                    <span>35 Yrs</span>
                </div>
            </div>

        </div>

        <!-- Results Display Column (5 cols) -->
        <div class="lg:col-span-5 bg-slate-50 border border-slate-200 rounded-xl p-6 flex flex-col justify-between">
            <div>
                <p class="text-xs uppercase tracking-wider font-semibold text-slate-400 mb-1">Step-Up Maturity Value</p>
                <div id="stepup-total-value" class="text-3xl sm:text-4xl font-extrabold text-slate-900 mb-5">&#8377;0</div>

                <div class="space-y-3 pb-5 border-b border-slate-200 text-sm">
                    <div class="flex justify-between items-center">
                        <span class="text-slate-500 flex items-center">
                            <span class="w-2.5 h-2.5 rounded-full bg-slate-400 inline-block mr-2"></span>
                            Total Invested
                        </span>
                        <span id="stepup-invested-amount" class="font-bold text-slate-800">&#8377;0</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span class="text-slate-500 flex items-center">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block mr-2"></span>
                            Est. Wealth Gain
                        </span>
                        <span id="stepup-returns-amount" class="font-bold text-emerald-700">&#8377;0</span>
                    </div>
                </div>

                <!-- Visual Ratio Bar (Invested vs Gain) -->
                <div class="mt-4 mb-6">
                    <div class="flex justify-between text-[11px] text-slate-400 font-medium mb-1.5">
                        <span id="stepup-invested-pct">Invested: 0%</span>
                        <span id="stepup-returns-pct">Gain: 0%</span>
                    </div>
                    <div class="w-full h-3 bg-slate-200 rounded-full overflow-hidden flex">
                        <div id="stepup-invested-bar" class="bg-slate-400 h-full transition-all duration-300" style="width: 50%"></div>
                        <div id="stepup-returns-bar" class="bg-emerald-500 h-full transition-all duration-300" style="width: 50%"></div>
                    </div>
                </div>

                <!-- Comparative Summary (Step-Up vs Flat SIP Baseline) -->
                <div class="p-4 bg-emerald-50/70 border border-emerald-200 rounded-xl space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-800">Step-Up Wealth Delta</span>
                        <span id="stepup-delta-badge" class="text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-200 text-emerald-900">+0% Extra</span>
                    </div>
                    <div class="grid grid-cols-2 gap-3 text-xs pt-1 border-t border-emerald-200/60">
                        <div>
                            <span class="text-slate-500 block">Flat SIP Maturity</span>
                            <span id="stepup-flat-total" class="font-bold text-slate-800 text-sm">&#8377;0</span>
                        </div>
                        <div>
                            <span class="text-slate-500 block">Additional Gain</span>
                            <span id="stepup-delta-amount" class="font-bold text-emerald-700 text-sm">+&#8377;0</span>
                        </div>
                    </div>
                    <p class="text-[11px] text-emerald-800/80 leading-relaxed pt-1">
                        By stepping up your investment by <span id="stepup-summary-pct" class="font-semibold">10%</span> annually, you create an additional <span id="stepup-summary-extra" class="font-semibold">&#8377;0</span> compared to a static flat SIP.
                    </p>
                </div>
            </div>

            <p class="text-[11px] text-slate-400 mt-5 leading-relaxed">
                *Projections are calculated with monthly compounding and beginning-of-period instalments. Mutual fund investments are subject to market risks.
            </p>
        </div>

    </div>
</div>

<!-- Yearly Breakdown Schedule Table -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6 pb-4 border-b border-slate-200">
        <div>
            <h2 class="text-xl font-bold text-slate-900 tracking-tight">Year-by-Year Growth Schedule</h2>
            <p class="text-sm text-slate-500 mt-0.5">Track how your monthly deposit, invested capital, and portfolio value compound each year.</p>
        </div>
        <div class="text-xs text-slate-400 font-medium">
            Values in Indian Rupees (&#8377;)
        </div>
    </div>

    <div class="overflow-x-auto">
        <table class="w-full text-left text-sm text-slate-600 border-collapse">
            <thead class="bg-slate-50 text-slate-700 font-semibold text-xs uppercase tracking-wider border-b border-slate-200">
                <tr>
                    <th class="py-3 px-4">Year</th>
                    <th class="py-3 px-4 text-right">Monthly Deposit</th>
                    <th class="py-3 px-4 text-right">Annual Deposit</th>
                    <th class="py-3 px-4 text-right">Cumulative Invested</th>
                    <th class="py-3 px-4 text-right">Cumulative Gain</th>
                    <th class="py-3 px-4 text-right font-bold text-slate-900">End Balance</th>
                </tr>
            </thead>
            <tbody id="stepup-breakdown-body" class="divide-y divide-slate-100 font-medium text-xs sm:text-sm">
                <!-- Dynamically generated rows -->
            </tbody>
        </table>
    </div>
</div>

<!-- Prominent Call to Action Banner -->
<div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-7 sm:p-8 text-white flex flex-col md:flex-row items-center justify-between gap-6 shadow-md mb-12">
    <div class="space-y-2 text-center md:text-left">
        <h3 class="text-xl font-bold">Track Your Step-Up SIP Mandates Automatically</h3>
        <p class="text-sm text-slate-300 max-w-xl">
            Want to track your increasing monthly mutual fund debits and NACH mandates locally? SpendSathi parses bank SMS alerts directly on your Android phone with zero cloud tracking.
        </p>
    </div>
    <a href="https://play.google.com/store/apps/details?id=com.finmate.app"
       target="_blank"
       rel="noopener noreferrer"
       class="inline-flex items-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-sm px-6 py-3 rounded-full transition shadow-sm whitespace-nowrap">
        <span>Download SpendSathi</span>
        <span>&rarr;</span>
    </a>
</div>

<!-- SEO Educational Content -->
<div class="space-y-8 text-slate-700 leading-relaxed">
    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">What is a Step-Up SIP (Top-Up SIP)?</h2>
        <p>A <strong>Step-Up SIP</strong> (also known as a <em>Top-Up SIP</em>) is an automated mutual fund investment feature that increases your monthly investment instalment by a predetermined percentage or fixed Rupee amount at regular intervals—most commonly once every 12 months.</p>
        <p class="mt-3">In a conventional SIP, an investor commits a flat monthly amount (e.g., &#8377;10,000) for a 10 or 20-year horizon. While this promotes discipline, it ignores a fundamental reality of your financial journey: <strong>your earning capacity and disposable income expand over time</strong>. A Step-Up SIP automatically aligns your savings rate with your annual salary appraisals without requiring manual intervention or opening new folios.</p>
    </section>

    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">Why Does a 10% Step-Up Outperform a Flat SIP So Dramatically?</h2>
        <p>The mathematics of compound interest become exponentially more powerful when fresh capital is progressively scaled upwards. Consider an initial investment of <strong>&#8377;10,000 per month</strong> over a <strong>15-year period</strong> at an expected return of <strong>12% p.a.</strong>:</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
            <div class="p-5 rounded-xl border border-slate-200 bg-slate-50">
                <span class="text-xs font-bold uppercase tracking-wider text-slate-400">Regular Flat SIP</span>
                <p class="text-xl font-bold text-slate-800 mt-1 mb-2">&#8377;50.46 Lakhs</p>
                <p class="text-xs text-slate-500">Total Invested: &#8377;18.00 Lakhs | Wealth Gain: &#8377;32.46 Lakhs</p>
            </div>
            <div class="p-5 rounded-xl border border-emerald-200 bg-emerald-50/50">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">10% Step-Up SIP</span>
                <p class="text-xl font-bold text-emerald-800 mt-1 mb-2">&#8377;97.94 Lakhs</p>
                <p class="text-xs text-emerald-700">Total Invested: &#8377;38.13 Lakhs | Wealth Gain: &#8377;59.81 Lakhs</p>
            </div>
        </div>
        <p>By increasing your monthly deposit by just 10% each year, your final maturity corpus nearly <strong>doubles from &#8377;50 Lakhs to nearly &#8377;1 Crore</strong>! Because the increment is gradual, your day-to-day lifestyle never feels restricted.</p>
    </section>

    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">How is Compound Interest Calculated for a Step-Up SIP?</h2>
        <p>In a standard SIP, every monthly deposit is uniform ($P_0$). In a Step-Up SIP, the monthly deposit in year $y$ (where $y = 0, 1, 2, \dots, Y-1$) increases according to:</p>
        <div class="my-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-center font-mono text-sm text-slate-800">
            P<sub>y</sub> = P<sub>0</sub> &times; (1 + s)<sup>y</sup>
        </div>
        <p>Where:</p>
        <ul class="list-disc list-inside space-y-1 mt-2 text-sm">
            <li><strong>P<sub>0</sub></strong>: Initial monthly investment amount.</li>
            <li><strong>s</strong>: Annual step-up percentage (e.g., 0.10 for 10%).</li>
            <li><strong>y</strong>: Completed years of investment (0 for Year 1, 1 for Year 2, etc.).</li>
        </ul>
        <p class="mt-3">Each instalment deposited at month $k$ (where $k = 1, 2, \dots, 12Y$) compounds at the monthly rate $i = \frac{R}{12 \times 100}$ for the remaining $(12Y - k + 1)$ months. The calculator performs exact month-by-month compounding simulation to reflect real-world mutual fund NAV accrual.</p>
    </section>

    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">How to Track Monthly Step-Up SIP Mandates with SpendSathi?</h2>
        <p>As your mutual fund auto-debits step up year after year, keeping track of bank balances and NACH deduction dates becomes crucial to avoid costly bounce charges. <strong>SpendSathi</strong> reads transaction SMS notifications directly on your Android smartphone without requiring bank account logins or cloud syncing.</p>
        <p class="mt-3">It categorizes recurring investment debits, notifies you of monthly cash flow trends, and helps you maintain sufficient liquidity for your SIP dates with 100% on-device privacy.</p>
    </section>
</div>

<!-- FAQ Accordion Section -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10 mt-8">
    <h2 class="text-2xl font-bold text-slate-900 mb-6 tracking-tight">Frequently Asked Questions (FAQs)</h2>
    <div class="space-y-4">
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">What is the difference between a normal SIP and a Step-Up SIP?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                A normal SIP keeps the monthly investment amount constant for the entire duration (e.g., &#8377;5,000 every month for 10 years). A Step-Up SIP automatically raises your instalment annually by a chosen percentage (e.g., 10%) or a fixed amount (e.g., &#8377;1,000), compounding your wealth faster as your income rises.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">What is an ideal annual step-up percentage to choose?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                Most financial planners in India recommend an annual step-up rate between <strong>5% and 10%</strong>. This closely aligns with the standard annual salary increment in corporate sectors and allows your savings to outpace inflation without causing cash flow strain.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">Can I stop or pause a Step-Up SIP if my expenses increase?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                Yes. Mutual funds in India offer full flexibility. You can modify your SIP mandate, cap the step-up at a specific maximum monthly amount, or pause the step-up feature and continue with your current instalment amount at any time through your mutual fund platform or AMC portal.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">How does Step-Up SIP protect against inflation?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                In a flat SIP, inflation gradually reduces the real purchasing power of the fixed &#8377;5,000 or &#8377;10,000 you invest each month. A Step-Up SIP ensures your real investment value increases over time, helping you build a retirement corpus that remains robust against rising living costs.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">How can SpendSathi help track my increasing SIP commitments?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                SpendSathi automatically detects and categorizes bank SMS alerts whenever an auto-debit or UPI mandate goes through. It tracks your recurring investments on your phone without collecting passwords or sending sensitive data to the cloud.
            </p>
        </div>
    </div>
</div>

<!-- Cross-Navigation: Other Calculators -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-200">
        <h2 class="text-lg font-bold text-slate-900 tracking-tight">Explore More Financial Calculators</h2>
        <a href="/calculators.html" class="text-xs font-semibold text-emerald-700 hover:text-emerald-800 transition">View All &rarr;</a>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <a href="/sip-calculator.html" class="p-4 rounded-xl border border-slate-200 hover:border-emerald-500 hover:bg-slate-50 transition group flex flex-col justify-between">
            <div>
                <span class="text-[11px] font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full inline-block mb-2">Flat SIP</span>
                <h3 class="text-sm font-bold text-slate-800 group-hover:text-emerald-700">SIP Calculator</h3>
                <p class="text-xs text-slate-500 mt-1">Estimate wealth creation with fixed monthly mutual fund instalments.</p>
            </div>
            <span class="text-xs font-semibold text-emerald-600 mt-3 block">Calculate SIP &rarr;</span>
        </a>
        <a href="/budget-planner-calculator.html" class="p-4 rounded-xl border border-slate-200 hover:border-blue-500 hover:bg-slate-50 transition group flex flex-col justify-between">
            <div>
                <span class="text-[11px] font-semibold text-blue-700 bg-blue-50 px-2 py-0.5 rounded-full inline-block mb-2">Budgeting</span>
                <h3 class="text-sm font-bold text-slate-800 group-hover:text-blue-700">50-30-20 Planner</h3>
                <p class="text-xs text-slate-500 mt-1">Divide monthly salary into Needs, Wants, and Savings with real-time balance.</p>
            </div>
            <span class="text-xs font-semibold text-blue-600 mt-3 block">Plan Budget &rarr;</span>
        </a>
        <a href="/emi-calculator.html" class="p-4 rounded-xl border border-slate-200 hover:border-slate-500 hover:bg-slate-50 transition group flex flex-col justify-between">
            <div>
                <span class="text-[11px] font-semibold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-full inline-block mb-2">Loans</span>
                <h3 class="text-sm font-bold text-slate-800 group-hover:text-slate-700">EMI Calculator</h3>
                <p class="text-xs text-slate-500 mt-1">Calculate monthly EMIs and total interest payable on loans.</p>
            </div>
            <span class="text-xs font-semibold text-slate-600 mt-3 block">Calculate EMI &rarr;</span>
        </a>
    </div>
</div>

<!-- JSON-LD Structured Data: SoftwareApplication & FAQPage -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "SoftwareApplication",
      "@id": "https://spendsathi.com/step-up-sip-calculator.html#software",
      "name": "Step-Up SIP Calculator — SpendSathi",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All modern web browsers",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      },
      "description": "Free client-side Step-Up SIP calculator with annual increment percentage, yearly wealth schedule, and flat SIP comparison baseline.",
      "url": "https://spendsathi.com/step-up-sip-calculator.html",
      "author": {
        "@type": "Organization",
        "name": "SpendSathi",
        "url": "https://spendsathi.com/"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://spendsathi.com/step-up-sip-calculator.html#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is the difference between a normal SIP and a Step-Up SIP?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A normal SIP keeps the monthly investment amount constant for the entire duration. A Step-Up SIP automatically raises your instalment annually by a chosen percentage or fixed amount, compounding your wealth faster as your income rises."
          }
        },
        {
          "@type": "Question",
          "name": "What is an ideal annual step-up percentage to choose?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Most financial planners in India recommend an annual step-up rate between 5% and 10%, aligning with typical corporate salary increments."
          }
        },
        {
          "@type": "Question",
          "name": "Can I stop or pause a Step-Up SIP if my expenses increase?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, mutual funds in India offer full flexibility to pause, modify, or cap the annual step-up at any time through your distributor or AMC portal."
          }
        },
        {
          "@type": "Question",
          "name": "How does Step-Up SIP protect against inflation?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "A Step-Up SIP increases your investment amounts annually, ensuring your contributions and overall compounding outpace inflation over long tenures."
          }
        },
        {
          "@type": "Question",
          "name": "How can SpendSathi help track my increasing SIP commitments?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "SpendSathi automatically logs and categorizes bank SMS alerts for mutual fund SIP debits directly on your Android device with zero cloud tracking."
          }
        }
      ]
    }
  ]
}
</script>

<!-- Calculator JavaScript -->
<script>
(function() {
    const amountSlider = document.getElementById('stepup-amount-slider');
    const amountInput = document.getElementById('stepup-amount-input');
    const pctSlider = document.getElementById('stepup-pct-slider');
    const pctInput = document.getElementById('stepup-pct-input');
    const rateSlider = document.getElementById('stepup-rate-slider');
    const rateInput = document.getElementById('stepup-rate-input');
    const yearsSlider = document.getElementById('stepup-years-slider');
    const yearsInput = document.getElementById('stepup-years-input');

    const totalValEl = document.getElementById('stepup-total-value');
    const investedEl = document.getElementById('stepup-invested-amount');
    const returnsEl = document.getElementById('stepup-returns-amount');
    const investedPctEl = document.getElementById('stepup-invested-pct');
    const returnsPctEl = document.getElementById('stepup-returns-pct');
    const investedBarEl = document.getElementById('stepup-invested-bar');
    const returnsBarEl = document.getElementById('stepup-returns-bar');

    const flatTotalEl = document.getElementById('stepup-flat-total');
    const deltaAmountEl = document.getElementById('stepup-delta-amount');
    const deltaBadgeEl = document.getElementById('stepup-delta-badge');
    const summaryPctEl = document.getElementById('stepup-summary-pct');
    const summaryExtraEl = document.getElementById('stepup-summary-extra');
    const tableBodyEl = document.getElementById('stepup-breakdown-body');

    const rupeeFormatter = new Intl.NumberFormat('en-IN', {
        maximumFractionDigits: 0
    });

    function calculateStepUpSIP() {
        const initialMonthly = Math.max(0, parseFloat(amountInput.value) || 0);
        const stepUpPct = Math.max(0, parseFloat(pctInput.value) || 0);
        const annualRate = Math.max(0, parseFloat(rateInput.value) || 0);
        const years = Math.max(1, parseInt(yearsInput.value) || 1);

        const monthlyRate = (annualRate / 12) / 100;
        const totalMonths = years * 12;

        let stepUpBalance = 0;
        let stepUpInvested = 0;
        const yearlyRows = [];

        for (let y = 0; y < years; y++) {
            const currentMonthly = initialMonthly * Math.pow(1 + stepUpPct / 100, y);
            let yearDeposit = 0;

            for (let m = 0; m < 12; m++) {
                stepUpInvested += currentMonthly;
                yearDeposit += currentMonthly;
                if (monthlyRate > 0) {
                    stepUpBalance = (stepUpBalance + currentMonthly) * (1 + monthlyRate);
                } else {
                    stepUpBalance += currentMonthly;
                }
            }

            const yearEndGain = Math.max(0, stepUpBalance - stepUpInvested);
            yearlyRows.push({
                year: y + 1,
                monthly: currentMonthly,
                annualDeposit: yearDeposit,
                cumulativeInvested: stepUpInvested,
                cumulativeGain: yearEndGain,
                balance: stepUpBalance
            });
        }

        const stepUpReturns = Math.max(0, stepUpBalance - stepUpInvested);

        // Baseline Flat SIP calculation
        let flatBalance = 0;
        const flatInvested = initialMonthly * totalMonths;
        if (monthlyRate > 0 && totalMonths > 0 && initialMonthly > 0) {
            flatBalance = initialMonthly * ((Math.pow(1 + monthlyRate, totalMonths) - 1) / monthlyRate) * (1 + monthlyRate);
        } else {
            flatBalance = flatInvested;
        }

        const wealthDelta = Math.max(0, stepUpBalance - flatBalance);
        const deltaPct = flatBalance > 0 ? Math.round((wealthDelta / flatBalance) * 100) : 0;

        // Render Summary Cards
        totalValEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(stepUpBalance));
        investedEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(stepUpInvested));
        returnsEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(stepUpReturns));

        // Render Ratio Bar
        if (stepUpBalance > 0) {
            const investedRatio = Math.round((stepUpInvested / stepUpBalance) * 100);
            const returnsRatio = 100 - investedRatio;
            investedPctEl.textContent = 'Invested: ' + investedRatio + '%';
            returnsPctEl.textContent = 'Gain: ' + returnsRatio + '%';
            investedBarEl.style.width = investedRatio + '%';
            returnsBarEl.style.width = returnsRatio + '%';
        } else {
            investedPctEl.textContent = 'Invested: 0%';
            returnsPctEl.textContent = 'Gain: 0%';
            investedBarEl.style.width = '50%';
            returnsBarEl.style.width = '50%';
        }

        // Render Comparative Delta
        flatTotalEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(flatBalance));
        deltaAmountEl.innerHTML = '+&#8377;' + rupeeFormatter.format(Math.round(wealthDelta));
        deltaBadgeEl.textContent = '+' + deltaPct + '% Extra';
        summaryPctEl.textContent = stepUpPct + '%';
        summaryExtraEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(wealthDelta));

        // Render Schedule Table
        let tableHtml = '';
        yearlyRows.forEach(row => {
            tableHtml += `
                <tr class="hover:bg-slate-50/80 transition-colors">
                    <td class="py-3 px-4 font-semibold text-slate-800">Yr ${row.year}</td>
                    <td class="py-3 px-4 text-right text-slate-600">&#8377;${rupeeFormatter.format(Math.round(row.monthly))}</td>
                    <td class="py-3 px-4 text-right text-slate-600">&#8377;${rupeeFormatter.format(Math.round(row.annualDeposit))}</td>
                    <td class="py-3 px-4 text-right text-slate-700">&#8377;${rupeeFormatter.format(Math.round(row.cumulativeInvested))}</td>
                    <td class="py-3 px-4 text-right text-emerald-700 font-semibold">&#8377;${rupeeFormatter.format(Math.round(row.cumulativeGain))}</td>
                    <td class="py-3 px-4 text-right font-bold text-slate-900">&#8377;${rupeeFormatter.format(Math.round(row.balance))}</td>
                </tr>
            `;
        });
        tableBodyEl.innerHTML = tableHtml;
    }

    function sync(slider, input) {
        slider.addEventListener('input', function() {
            input.value = slider.value;
            calculateStepUpSIP();
        });
        input.addEventListener('input', function() {
            slider.value = input.value;
            calculateStepUpSIP();
        });
    }

    sync(amountSlider, amountInput);
    sync(pctSlider, pctInput);
    sync(rateSlider, rateInput);
    sync(yearsSlider, yearsInput);

    calculateStepUpSIP();
})();
</script>
