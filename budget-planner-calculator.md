---
layout: default
title: 50-30-20 Budget Planner — Smart Income & Expense Calculator
description: Free 50-30-20 budget calculator. Allocate your monthly take-home salary into Needs (50%), Wants (30%), and Savings (20%) with real-time deficit alerts and visual breakdown.
permalink: /budget-planner-calculator.html
---

<!-- Breadcrumb Navigation -->
<nav class="mb-4 flex items-center space-x-2 text-xs font-medium text-slate-500" aria-label="Breadcrumb">
    <a href="/" class="hover:text-slate-900 transition">Home</a>
    <span>/</span>
    <a href="/calculators.html" class="hover:text-slate-900 transition">Calculators</a>
    <span>/</span>
    <span class="text-slate-900 font-semibold" aria-current="page">50-30-20 Budget Planner</span>
</nav>

<div class="mb-8">
    <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-semibold uppercase tracking-wider mb-3">
        <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
        <span>Budget Allocation Utility</span>
    </div>
    <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">50-30-20 Budget Planner</h1>
    <p class="text-base text-slate-500 leading-relaxed">
        Structure your monthly take-home salary using the classic 50/30/20 rule. Adjust actual spending in real-time to avoid deficits and maximize investments.
    </p>
</div>

<!-- Income Input Section -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-8">
    <div class="max-w-xl">
        <label for="budget-income-input" class="text-sm font-semibold text-slate-700 block mb-1">Monthly In-Hand (Take-Home) Salary</label>
        <p class="text-xs text-slate-400 mb-3">Enter the net salary credited to your bank account after EPF, TDS, and professional tax.</p>
        <div class="flex items-center gap-4 mb-3">
            <div class="relative flex-1">
                <span class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 font-bold text-base">&#8377;</span>
                <input type="number" id="budget-income-input" name="budget-income-input" value="50000" min="5000" max="2000000" step="1000"
                       class="w-full pl-8 pr-4 py-2.5 font-extrabold text-slate-900 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 text-lg">
            </div>
            <button type="button" id="budget-reset-btn"
                    class="px-4 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-xl transition whitespace-nowrap">
                Reset to 50/30/20
            </button>
        </div>
        <input type="range" id="budget-income-slider" name="budget-income-slider" aria-label="Monthly Take-Home Salary Slider" min="10000" max="300000" step="2000" value="50000"
               class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-blue-600">
        <div class="flex justify-between text-[11px] text-slate-400 mt-1">
            <span>&#8377;10,000</span>
            <span>&#8377;1,50,000</span>
            <span>&#8377;3,00,000</span>
        </div>
    </div>
</div>

<!-- Recommended 50-30-20 Target Cards -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-5 mb-8">
    <!-- Needs Card (50%) -->
    <div class="bg-blue-50/50 border border-blue-200 rounded-2xl p-5 flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-blue-700">Needs (50%)</span>
                <span class="text-[11px] font-semibold bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Essential</span>
            </div>
            <div id="target-needs-amount" class="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-1">&#8377;25,000</div>
            <p class="text-xs text-slate-500">Rent, groceries, utilities, loan EMIs, school fees &amp; health insurance.</p>
        </div>
        <div class="mt-4 pt-3 border-t border-blue-200/60 text-[11px] text-blue-900/80 font-medium">
            Maximum suggested cap: 50%
        </div>
    </div>

    <!-- Wants Card (30%) -->
    <div class="bg-purple-50/50 border border-purple-200 rounded-2xl p-5 flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-purple-700">Wants (30%)</span>
                <span class="text-[11px] font-semibold bg-purple-100 text-purple-800 px-2 py-0.5 rounded-full">Lifestyle</span>
            </div>
            <div id="target-wants-amount" class="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-1">&#8377;15,000</div>
            <p class="text-xs text-slate-500">Dining out, Swiggy, Netflix, shopping, hobbies, trips &amp; entertainment.</p>
        </div>
        <div class="mt-4 pt-3 border-t border-purple-200/60 text-[11px] text-purple-900/80 font-medium">
            Comfortable limit: 30%
        </div>
    </div>

    <!-- Savings Card (20%) -->
    <div class="bg-emerald-50/50 border border-emerald-200 rounded-2xl p-5 flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold uppercase tracking-wider text-emerald-700">Savings (20%)</span>
                <span class="text-[11px] font-semibold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">Wealth</span>
            </div>
            <div id="target-savings-amount" class="text-2xl sm:text-3xl font-extrabold text-slate-900 mb-1">&#8377;10,000</div>
            <p class="text-xs text-slate-500">Mutual Fund SIPs, emergency funds, PPF, NPS &amp; debt prepayments.</p>
        </div>
        <div class="mt-4 pt-3 border-t border-emerald-200/60 text-[11px] text-emerald-900/80 font-medium">
            Minimum recommended floor: 20%
        </div>
    </div>
</div>

<!-- Interactive Spending Adjustment & Real-Time Reallocation -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-6 pb-4 border-b border-slate-200">
        <div>
            <h2 class="text-xl font-bold text-slate-900 tracking-tight">Interactive Spending Reallocation</h2>
            <p class="text-sm text-slate-500 mt-0.5">Adjust the sliders to mirror your real-world monthly expenses and check budget balance.</p>
        </div>
        <div id="budget-status-pill" class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 self-start sm:self-auto">
            100% Balanced
        </div>
    </div>

    <!-- Dynamic Warning / Surplus Alert Banner -->
    <div id="budget-alert-banner" class="mb-6 p-4 rounded-xl border border-emerald-200 bg-emerald-50 text-emerald-900 text-sm flex items-start gap-3">
        <svg class="w-5 h-5 flex-shrink-0 text-emerald-600 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <div id="budget-alert-text">
            <strong>Budget is perfectly balanced!</strong> Every Rupee of your income has an intentional purpose.
        </div>
    </div>

    <!-- Sliders for Actual Category Spending -->
    <div class="space-y-6 mb-8">
        <!-- Actual Needs Slider -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-blue-500"></span>
                    <label for="actual-needs-input" class="text-sm font-bold text-slate-800">Actual Needs Spending</label>
                    <span id="actual-needs-badge" class="text-xs font-semibold px-2 py-0.5 rounded-md bg-blue-100 text-blue-700">50%</span>
                </div>
                <div class="relative">
                    <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">&#8377;</span>
                    <input type="number" id="actual-needs-input" name="actual-needs-input" value="25000" min="0" max="2000000" step="500"
                           class="w-36 pl-7 pr-3 py-1.5 text-right font-bold text-slate-900 bg-white border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm">
                </div>
            </div>
            <input type="range" id="actual-needs-slider" name="actual-needs-slider" aria-label="Actual Needs Spending Slider" min="0" max="100000" step="500" value="25000"
                   class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-blue-600">
            <div class="flex justify-between items-center text-[11px] text-slate-400 mt-1.5">
                <span>Target: <span id="actual-needs-target-txt">&#8377;25,000</span> (50%)</span>
                <span id="actual-needs-diff" class="font-medium text-emerald-600">On Target</span>
            </div>
        </div>

        <!-- Actual Wants Slider -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-purple-500"></span>
                    <label for="actual-wants-input" class="text-sm font-bold text-slate-800">Actual Wants Spending</label>
                    <span id="actual-wants-badge" class="text-xs font-semibold px-2 py-0.5 rounded-md bg-purple-100 text-purple-700">30%</span>
                </div>
                <div class="relative">
                    <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">&#8377;</span>
                    <input type="number" id="actual-wants-input" name="actual-wants-input" value="15000" min="0" max="2000000" step="500"
                           class="w-36 pl-7 pr-3 py-1.5 text-right font-bold text-slate-900 bg-white border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-sm">
                </div>
            </div>
            <input type="range" id="actual-wants-slider" name="actual-wants-slider" aria-label="Actual Wants Spending Slider" min="0" max="100000" step="500" value="15000"
                   class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-purple-600">
            <div class="flex justify-between items-center text-[11px] text-slate-400 mt-1.5">
                <span>Target: <span id="actual-wants-target-txt">&#8377;15,000</span> (30%)</span>
                <span id="actual-wants-diff" class="font-medium text-emerald-600">On Target</span>
            </div>
        </div>

        <!-- Actual Savings Slider -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
                    <label for="actual-savings-input" class="text-sm font-bold text-slate-800">Actual Savings &amp; Investments</label>
                    <span id="actual-savings-badge" class="text-xs font-semibold px-2 py-0.5 rounded-md bg-emerald-100 text-emerald-700">20%</span>
                </div>
                <div class="relative">
                    <span class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 font-medium text-sm">&#8377;</span>
                    <input type="number" id="actual-savings-input" name="actual-savings-input" value="10000" min="0" max="2000000" step="500"
                           class="w-36 pl-7 pr-3 py-1.5 text-right font-bold text-slate-900 bg-white border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm">
                </div>
            </div>
            <input type="range" id="actual-savings-slider" name="actual-savings-slider" aria-label="Actual Savings Spending Slider" min="0" max="100000" step="500" value="10000"
                   class="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-emerald-600">
            <div class="flex justify-between items-center text-[11px] text-slate-400 mt-1.5">
                <span>Target: <span id="actual-savings-target-txt">&#8377;10,000</span> (20%)</span>
                <span id="actual-savings-diff" class="font-medium text-emerald-600">On Target</span>
            </div>
        </div>
    </div>

    <!-- Visual Category Allocation Bar -->
    <div>
        <div class="flex justify-between text-xs font-semibold text-slate-500 mb-2">
            <span>Spending Allocation Breakdown</span>
            <span id="budget-total-pct">Total Allocated: 100%</span>
        </div>
        <div class="w-full h-4 bg-slate-100 rounded-full overflow-hidden flex shadow-inner">
            <div id="bar-needs" class="bg-blue-500 h-full transition-all duration-300" style="width: 50%" title="Needs"></div>
            <div id="bar-wants" class="bg-purple-500 h-full transition-all duration-300" style="width: 30%" title="Wants"></div>
            <div id="bar-savings" class="bg-emerald-500 h-full transition-all duration-300" style="width: 20%" title="Savings"></div>
            <div id="bar-surplus" class="bg-slate-300 h-full transition-all duration-300" style="width: 0%" title="Unallocated Surplus"></div>
        </div>
        <div class="flex flex-wrap gap-4 items-center justify-between text-[11px] text-slate-500 mt-2 font-medium">
            <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
                <span>Needs: <span id="legend-needs-pct">50%</span></span>
            </div>
            <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
                <span>Wants: <span id="legend-wants-pct">30%</span></span>
            </div>
            <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <span>Savings: <span id="legend-savings-pct">20%</span></span>
            </div>
            <div class="flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-slate-400"></span>
                <span>Surplus: <span id="legend-surplus-pct">0%</span></span>
            </div>
        </div>
    </div>
</div>

<!-- Detailed Indian Categorization Guide -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <h2 class="text-xl font-bold text-slate-900 tracking-tight mb-2">How to Categorize Your Expenses in India</h2>
    <p class="text-sm text-slate-500 mb-6">Practical breakdown of common Indian monthly transactions into the 50/30/20 buckets:</p>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="p-5 rounded-xl border border-blue-100 bg-blue-50/30">
            <div class="flex items-center space-x-2 mb-3">
                <span class="w-3 h-3 rounded-full bg-blue-500"></span>
                <h3 class="text-base font-bold text-blue-900">Needs (50%)</h3>
            </div>
            <p class="text-xs text-slate-600 mb-3 leading-relaxed">Mandatory expenses you cannot avoid without significant life disruption:</p>
            <ul class="text-xs text-slate-700 space-y-2 list-disc list-inside">
                <li>House Rent or Home Loan EMI</li>
                <li>Society Maintenance &amp; Municipal Taxes</li>
                <li>Groceries, Milk &amp; Daily Rations</li>
                <li>Electricity, Water, Gas &amp; Broadband Bills</li>
                <li>Office Commute (Metro, Fuel, Bus)</li>
                <li>School/College Tuition Fees</li>
                <li>Term &amp; Health Insurance Premiums</li>
                <li>Essential Medicines &amp; Healthcare</li>
            </ul>
        </div>

        <div class="p-5 rounded-xl border border-purple-100 bg-purple-50/30">
            <div class="flex items-center space-x-2 mb-3">
                <span class="w-3 h-3 rounded-full bg-purple-500"></span>
                <h3 class="text-base font-bold text-purple-900">Wants (30%)</h3>
            </div>
            <p class="text-xs text-slate-600 mb-3 leading-relaxed">Discretionary expenses that enrich lifestyle but are optional for survival:</p>
            <ul class="text-xs text-slate-700 space-y-2 list-disc list-inside">
                <li>Swiggy, Zomato &amp; Food Delivery</li>
                <li>Weekend Restaurants &amp; Cafes</li>
                <li>OTT Subscriptions (Netflix, Hotstar, Prime)</li>
                <li>Fashion Shopping &amp; Brand Clothing</li>
                <li>Weekend Outings, Movies &amp; Concerts</li>
                <li>Vacations, Road Trips &amp; Hotel Bookings</li>
                <li>Gadget Upgrades &amp; Electronics</li>
                <li>Gym Memberships &amp; Hobbies</li>
            </ul>
        </div>

        <div class="p-5 rounded-xl border border-emerald-100 bg-emerald-50/30">
            <div class="flex items-center space-x-2 mb-3">
                <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
                <h3 class="text-base font-bold text-emerald-900">Savings &amp; Wealth (20%)</h3>
            </div>
            <p class="text-xs text-slate-600 mb-3 leading-relaxed">Allocations toward future financial freedom and emergency protection:</p>
            <ul class="text-xs text-slate-700 space-y-2 list-disc list-inside">
                <li>Equity Mutual Fund SIPs</li>
                <li>Emergency Buffer (3–6 months in Liquid Funds)</li>
                <li>Public Provident Fund (PPF) &amp; EPF VPF</li>
                <li>National Pension System (NPS)</li>
                <li>Direct Equity / Stock Market Portfolio</li>
                <li>Sovereign Gold Bonds (SGB) or Digital Gold</li>
                <li>Prepaying High-Interest Debt or Credit Cards</li>
                <li>Recurring Deposits (RD) for Annual Goals</li>
            </ul>
        </div>
    </div>
</div>

<!-- Prominent Call to Action Banner -->
<div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-7 sm:p-8 text-white flex flex-col md:flex-row items-center justify-between gap-6 shadow-md mb-12">
    <div class="space-y-2 text-center md:text-left">
        <h3 class="text-xl font-bold">Track Your 50-30-20 Spends Offline</h3>
        <p class="text-sm text-slate-300 max-w-xl">
            Tired of manually writing down every UPI and card expense? SpendSathi parses your bank SMS notifications 100% locally on your phone to automatically classify spends into Needs, Wants, and Savings.
        </p>
    </div>
    <a href="https://play.google.com/store/apps/details?id=com.finmate.app"
       target="_blank"
       rel="noopener noreferrer"
       class="inline-flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm px-6 py-3 rounded-full transition shadow-sm whitespace-nowrap">
        <span>Download SpendSathi</span>
        <span>&rarr;</span>
    </a>
</div>

<!-- SEO Educational Content -->
<div class="space-y-8 text-slate-700 leading-relaxed">
    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">What is the 50/30/20 Budgeting Rule?</h2>
        <p>The <strong>50/30/20 rule</strong> is an intuitive personal finance budgeting framework popularized by Harvard bankruptcy expert and U.S. Senator Elizabeth Warren in her book <em>All Your Worth: The Ultimate Lifetime Money Plan</em>.</p>
        <p class="mt-3">Rather than forcing you into rigid micro-accounting categories (such as tracking 30 different sub-budgets for milk, detergent, and cab rides), the 50/30/20 rule aggregates all personal expenditures into three transparent buckets: <strong>Needs</strong> (50%), <strong>Wants</strong> (30%), and <strong>Savings</strong> (20%). It offers a sustainable balance between enjoying your present lifestyle and guaranteeing future financial autonomy.</p>
    </section>

    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">How to Adapt 50-30-20 for Tier-1 Indian Metros (Mumbai, Bengaluru, Delhi)</h2>
        <p>In high-cost Indian metro cities where apartment rents consume 35% to 45% of disposable income, sticking strictly to the 50% cap for Needs can be challenging for young professionals. Financial advisors suggest adjusting to a <strong>60/20/20</strong> or <strong>50/20/30</strong> distribution:</p>
        <ul class="list-disc list-inside space-y-2 mt-3 text-sm">
            <li><strong>The 60-20-20 Variant (High-Rent Phase)</strong>: Allocate 60% to Needs, 20% to Wants, and maintain a non-negotiable 20% for Savings. Never compromise your 20% wealth creation floor; compress discretionary Wants instead.</li>
            <li><strong>Aggressive FIRE Variant (50-20-30)</strong>: For high-earning individuals seeking Financial Independence, Retiring Early (FIRE), keep Needs at 50%, compress Wants to 20%, and elevate Savings and Investments to 30% or more.</li>
        </ul>
    </section>

    <section class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm">
        <h2 class="text-2xl font-bold text-slate-900 mb-3 tracking-tight">How SpendSathi Automates 50/30/20 Budgeting with Zero Manual Entry</h2>
        <p>Manual budgeting apps fail because users stop recording small UPI transactions after two weeks. <strong>SpendSathi</strong> eliminates friction by reading SMS transaction alerts generated by HDFC, SBI, ICICI, Axis, Paytm, and Google Pay directly on your Android device.</p>
        <p class="mt-3">It automatically organizes merchants (e.g., Blinkit, Swiggy, Cred, Zerodha, BESCOM) into Needs, Wants, and Investments. Your confidential financial data never uploads to third-party cloud servers or advertisers—everything stays 100% offline on your device.</p>
    </section>
</div>

<!-- FAQ Accordion Section -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10 mt-8">
    <h2 class="text-2xl font-bold text-slate-900 mb-6 tracking-tight">Frequently Asked Questions (FAQs)</h2>
    <div class="space-y-4">
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">Should loan EMIs be classified under Needs or Savings?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                Home loan and education loan EMIs count as <strong>Needs</strong> because default impairs your credit score and legal shelter. However, extra voluntary principal prepayments to eliminate debt count toward your <strong>Savings</strong> bucket. Car loans or personal loans for luxury goods fall under <strong>Wants</strong>.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">Is the 50/30/20 rule calculated on gross or net take-home salary?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                The 50/30/20 rule should always be calculated on your <strong>Net Take-Home Salary</strong> (in-hand pay credited after EPF deductions and income tax TDS). If your employer deducts voluntary provident fund (VPF) or NPS at source, you can count those employer deductions as part of your 20% savings.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">What if my living expenses exceed 50% of my income?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                If rent and essential groceries exceed 50%, reduce your Wants bucket (e.g. from 30% to 15%) rather than eliminating your Savings. Maintaining even 10% to 15% monthly savings protects you from emergency debt cycles.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">How can freelancers or people with variable income apply this rule?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                Calculate your average monthly earnings over the last 6 to 12 months, or use your lowest-earning baseline month as your baseline salary. Any surplus income earned during bumper months should be deposited into a liquid buffer fund or invested directly.
            </p>
        </div>
        <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50">
            <h3 class="text-base font-semibold text-slate-900 mb-2">How does SpendSathi keep my budgeting private?</h3>
            <p class="text-sm text-slate-600 leading-relaxed">
                SpendSathi processes financial SMS alerts entirely on your smartphone using local pattern matching. It does not connect to banking APIs, require SMS logins, or transmit your expenditure data to any cloud database.
            </p>
        </div>
    </div>
</div>

<!-- Cross-Navigation: Other Calculators -->
<div class="bg-white border border-slate-200 rounded-2xl p-6 sm:p-8 shadow-sm mb-10">
    <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-200">
        <h2 class="text-lg font-bold text-slate-900 tracking-tight">Explore More Financial Calculators</h2>
        <a href="/calculators.html" class="text-xs font-semibold text-blue-700 hover:text-blue-800 transition">View All &rarr;</a>
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
        <a href="/step-up-sip-calculator.html" class="p-4 rounded-xl border border-slate-200 hover:border-emerald-500 hover:bg-slate-50 transition group flex flex-col justify-between">
            <div>
                <span class="text-[11px] font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full inline-block mb-2">Top-Up SIP</span>
                <h3 class="text-sm font-bold text-slate-800 group-hover:text-emerald-700">Step-Up SIP Calculator</h3>
                <p class="text-xs text-slate-500 mt-1">Compound returns with annual investment increases aligned with salary.</p>
            </div>
            <span class="text-xs font-semibold text-emerald-600 mt-3 block">Calculate Step-Up &rarr;</span>
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
      "@id": "https://spendsathi.com/budget-planner-calculator.html#software",
      "name": "50-30-20 Budget Planner — SpendSathi",
      "applicationCategory": "FinanceApplication",
      "operatingSystem": "All modern web browsers",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "INR"
      },
      "description": "Free interactive 50-30-20 budget calculator and expense planner for Indian salaries. Allocate Needs, Wants, and Savings with real-time deficit alerts.",
      "url": "https://spendsathi.com/budget-planner-calculator.html",
      "author": {
        "@type": "Organization",
        "name": "SpendSathi",
        "url": "https://spendsathi.com/"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://spendsathi.com/budget-planner-calculator.html#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Should loan EMIs be classified under Needs or Savings?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Home loan and education loan EMIs count as Needs. Extra voluntary principal prepayments count as Savings. Personal or car loans for luxury goods fall under Wants."
          }
        },
        {
          "@type": "Question",
          "name": "Is the 50/30/20 rule calculated on gross or net take-home salary?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The 50/30/20 rule is calculated on net take-home salary credited after income tax TDS and standard EPF deductions."
          }
        },
        {
          "@type": "Question",
          "name": "What if my living expenses exceed 50% of my income?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "If fixed needs exceed 50%, reduce your Wants bucket rather than cutting savings completely, or adapt to a temporary 60-20-20 budget."
          }
        },
        {
          "@type": "Question",
          "name": "How can freelancers or people with variable income apply this rule?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Use your lowest-earning month as your baseline budget and channel surplus income from high-earning months directly into a liquid emergency fund."
          }
        },
        {
          "@type": "Question",
          "name": "How does SpendSathi keep my budgeting private?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "SpendSathi processes financial SMS alerts entirely on-device with zero cloud synchronization, ensuring your bank account details remain completely confidential."
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
    const incomeInput = document.getElementById('budget-income-input');
    const incomeSlider = document.getElementById('budget-income-slider');
    const resetBtn = document.getElementById('budget-reset-btn');

    const targetNeedsEl = document.getElementById('target-needs-amount');
    const targetWantsEl = document.getElementById('target-wants-amount');
    const targetSavingsEl = document.getElementById('target-savings-amount');

    const actualNeedsInput = document.getElementById('actual-needs-input');
    const actualNeedsSlider = document.getElementById('actual-needs-slider');
    const actualNeedsBadge = document.getElementById('actual-needs-badge');
    const actualNeedsTargetTxt = document.getElementById('actual-needs-target-txt');
    const actualNeedsDiff = document.getElementById('actual-needs-diff');

    const actualWantsInput = document.getElementById('actual-wants-input');
    const actualWantsSlider = document.getElementById('actual-wants-slider');
    const actualWantsBadge = document.getElementById('actual-wants-badge');
    const actualWantsTargetTxt = document.getElementById('actual-wants-target-txt');
    const actualWantsDiff = document.getElementById('actual-wants-diff');

    const actualSavingsInput = document.getElementById('actual-savings-input');
    const actualSavingsSlider = document.getElementById('actual-savings-slider');
    const actualSavingsBadge = document.getElementById('actual-savings-badge');
    const actualSavingsTargetTxt = document.getElementById('actual-savings-target-txt');
    const actualSavingsDiff = document.getElementById('actual-savings-diff');

    const alertBanner = document.getElementById('budget-alert-banner');
    const alertText = document.getElementById('budget-alert-text');
    const statusPill = document.getElementById('budget-status-pill');
    const totalPctEl = document.getElementById('budget-total-pct');

    const barNeeds = document.getElementById('bar-needs');
    const barWants = document.getElementById('bar-wants');
    const barSavings = document.getElementById('bar-savings');
    const barSurplus = document.getElementById('bar-surplus');

    const legendNeedsPct = document.getElementById('legend-needs-pct');
    const legendWantsPct = document.getElementById('legend-wants-pct');
    const legendSavingsPct = document.getElementById('legend-savings-pct');
    const legendSurplusPct = document.getElementById('legend-surplus-pct');

    const rupeeFormatter = new Intl.NumberFormat('en-IN', {
        maximumFractionDigits: 0
    });

    function updateTargetsAndLimits() {
        const income = Math.max(1000, parseFloat(incomeInput.value) || 0);

        const targetNeeds = income * 0.50;
        const targetWants = income * 0.30;
        const targetSavings = income * 0.20;

        targetNeedsEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetNeeds));
        targetWantsEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetWants));
        targetSavingsEl.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetSavings));

        actualNeedsTargetTxt.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetNeeds));
        actualWantsTargetTxt.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetWants));
        actualSavingsTargetTxt.innerHTML = '&#8377;' + rupeeFormatter.format(Math.round(targetSavings));

        // Adjust slider maximums based on income
        const sliderMax = Math.max(income * 1.5, 100000);
        actualNeedsSlider.max = sliderMax;
        actualWantsSlider.max = sliderMax;
        actualSavingsSlider.max = sliderMax;
    }

    function calculateBudget() {
        const income = Math.max(1000, parseFloat(incomeInput.value) || 0);

        const actualNeeds = Math.max(0, parseFloat(actualNeedsInput.value) || 0);
        const actualWants = Math.max(0, parseFloat(actualWantsInput.value) || 0);
        const actualSavings = Math.max(0, parseFloat(actualSavingsInput.value) || 0);

        const targetNeeds = income * 0.50;
        const targetWants = income * 0.30;
        const targetSavings = income * 0.20;

        const needsPct = Math.round((actualNeeds / income) * 100);
        const wantsPct = Math.round((actualWants / income) * 100);
        const savingsPct = Math.round((actualSavings / income) * 100);

        actualNeedsBadge.textContent = needsPct + '%';
        actualWantsBadge.textContent = wantsPct + '%';
        actualSavingsBadge.textContent = savingsPct + '%';

        // Check Needs status
        if (actualNeeds > targetNeeds) {
            const over = actualNeeds - targetNeeds;
            actualNeedsDiff.textContent = '+' + rupeeFormatter.format(Math.round(over)) + ' over 50%';
            actualNeedsDiff.className = 'font-semibold text-rose-600';
        } else if (actualNeeds < targetNeeds) {
            const under = targetNeeds - actualNeeds;
            actualNeedsDiff.textContent = rupeeFormatter.format(Math.round(under)) + ' under cap';
            actualNeedsDiff.className = 'font-medium text-blue-600';
        } else {
            actualNeedsDiff.textContent = 'On Target (50%)';
            actualNeedsDiff.className = 'font-medium text-emerald-600';
        }

        // Check Wants status
        if (actualWants > targetWants) {
            const over = actualWants - targetWants;
            actualWantsDiff.textContent = '+' + rupeeFormatter.format(Math.round(over)) + ' over 30%';
            actualWantsDiff.className = 'font-semibold text-rose-600';
        } else if (actualWants < targetWants) {
            const under = targetWants - actualWants;
            actualWantsDiff.textContent = rupeeFormatter.format(Math.round(under)) + ' under limit';
            actualWantsDiff.className = 'font-medium text-purple-600';
        } else {
            actualWantsDiff.textContent = 'On Target (30%)';
            actualWantsDiff.className = 'font-medium text-emerald-600';
        }

        // Check Savings status
        if (actualSavings >= targetSavings) {
            const extra = actualSavings - targetSavings;
            if (extra > 0) {
                actualSavingsDiff.textContent = '+' + rupeeFormatter.format(Math.round(extra)) + ' above 20% floor';
                actualSavingsDiff.className = 'font-semibold text-emerald-600';
            } else {
                actualSavingsDiff.textContent = 'On Target (20%)';
                actualSavingsDiff.className = 'font-medium text-emerald-600';
            }
        } else {
            const deficit = targetSavings - actualSavings;
            actualSavingsDiff.textContent = '-' + rupeeFormatter.format(Math.round(deficit)) + ' below 20%';
            actualSavingsDiff.className = 'font-semibold text-amber-600';
        }

        const totalAllocated = actualNeeds + actualWants + actualSavings;
        const totalPct = Math.round((totalAllocated / income) * 100);
        totalPctEl.textContent = 'Total Allocated: ' + totalPct + '%';

        const diff = income - totalAllocated;

        if (diff < 0) {
            // Deficit / Over budget
            const overAmount = Math.abs(diff);
            statusPill.textContent = 'Over Budget (' + totalPct + '%)';
            statusPill.className = 'inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-rose-100 text-rose-800 self-start sm:self-auto';

            alertBanner.className = 'mb-6 p-4 rounded-xl border border-rose-200 bg-rose-50 text-rose-900 text-sm flex items-start gap-3';
            alertText.innerHTML = `<strong>Over Budget by &#8377;${rupeeFormatter.format(Math.round(overAmount))} (${totalPct - 100}% deficit)!</strong> Your planned spending (&#8377;${rupeeFormatter.format(Math.round(totalAllocated))}) exceeds your monthly salary. Consider reducing discretionary 'Wants' or optimizing utility bills to avoid debt.`;

            // Bar allocation
            const nW = Math.min(100, Math.round((actualNeeds / totalAllocated) * 100));
            const wW = Math.min(100 - nW, Math.round((actualWants / totalAllocated) * 100));
            const sW = Math.max(0, 100 - nW - wW);

            barNeeds.style.width = nW + '%';
            barWants.style.width = wW + '%';
            barSavings.style.width = sW + '%';
            barSurplus.style.width = '0%';
            barSurplus.style.backgroundColor = '#f43f5e'; // red

            legendNeedsPct.textContent = needsPct + '%';
            legendWantsPct.textContent = wantsPct + '%';
            legendSavingsPct.textContent = savingsPct + '%';
            legendSurplusPct.textContent = '-' + Math.round((overAmount / income) * 100) + '% (Deficit)';
        } else if (diff > 0) {
            // Surplus
            const surplusPct = Math.round((diff / income) * 100);
            statusPill.textContent = 'Surplus Available (+' + surplusPct + '%)';
            statusPill.className = 'inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-sky-100 text-sky-800 self-start sm:self-auto';

            alertBanner.className = 'mb-6 p-4 rounded-xl border border-sky-200 bg-sky-50 text-sky-900 text-sm flex items-start gap-3';
            alertText.innerHTML = `<strong>Surplus of &#8377;${rupeeFormatter.format(Math.round(diff))} (${surplusPct}% unallocated)!</strong> You have uncommitted funds remaining. Channel this surplus into mutual fund SIPs, emergency funds, or prepaying loans.`;

            const nW = Math.round((actualNeeds / income) * 100);
            const wW = Math.round((actualWants / income) * 100);
            const sW = Math.round((actualSavings / income) * 100);
            const remW = Math.max(0, 100 - nW - wW - sW);

            barNeeds.style.width = nW + '%';
            barWants.style.width = wW + '%';
            barSavings.style.width = sW + '%';
            barSurplus.style.width = remW + '%';
            barSurplus.style.backgroundColor = '#cbd5e1'; // slate

            legendNeedsPct.textContent = needsPct + '%';
            legendWantsPct.textContent = wantsPct + '%';
            legendSavingsPct.textContent = savingsPct + '%';
            legendSurplusPct.textContent = surplusPct + '%';
        } else {
            // Exactly Balanced
            statusPill.textContent = '100% Balanced';
            statusPill.className = 'inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 self-start sm:self-auto';

            alertBanner.className = 'mb-6 p-4 rounded-xl border border-emerald-200 bg-emerald-50 text-emerald-900 text-sm flex items-start gap-3';
            alertText.innerHTML = `<strong>Budget is perfectly balanced!</strong> Every single Rupee of your take-home salary is intentionally allocated.`;

            barNeeds.style.width = needsPct + '%';
            barWants.style.width = wantsPct + '%';
            barSavings.style.width = savingsPct + '%';
            barSurplus.style.width = '0%';

            legendNeedsPct.textContent = needsPct + '%';
            legendWantsPct.textContent = wantsPct + '%';
            legendSavingsPct.textContent = savingsPct + '%';
            legendSurplusPct.textContent = '0%';
        }
    }

    function resetToDefault() {
        const income = Math.max(1000, parseFloat(incomeInput.value) || 0);
        const n = Math.round(income * 0.50);
        const w = Math.round(income * 0.30);
        const s = Math.round(income * 0.20);

        actualNeedsInput.value = n;
        actualNeedsSlider.value = n;

        actualWantsInput.value = w;
        actualWantsSlider.value = w;

        actualSavingsInput.value = s;
        actualSavingsSlider.value = s;

        calculateBudget();
    }

    function sync(slider, input) {
        slider.addEventListener('input', function() {
            input.value = slider.value;
            calculateBudget();
        });
        input.addEventListener('input', function() {
            slider.value = input.value;
            calculateBudget();
        });
    }

    // Income sync
    incomeSlider.addEventListener('input', function() {
        incomeInput.value = incomeSlider.value;
        updateTargetsAndLimits();
        resetToDefault();
    });
    incomeInput.addEventListener('input', function() {
        incomeSlider.value = incomeInput.value;
        updateTargetsAndLimits();
        resetToDefault();
    });

    sync(actualNeedsSlider, actualNeedsInput);
    sync(actualWantsSlider, actualWantsInput);
    sync(actualSavingsSlider, actualSavingsInput);

    resetBtn.addEventListener('click', resetToDefault);

    updateTargetsAndLimits();
    resetToDefault();
})();
</script>
