#!/usr/bin/env python3
import re
with open('src/pages/index.astro','r') as f:
 src = f.read()


#1. proofPoints array: re-indent lines starting with exactly1 space inside the array
src = re.sub(
 r'(const proofPoints = \[\n) (.*?\n)+ (\];)',
 lambda m: m.group(1) + '\n'.join(' ' *2 + line for line in m.group(0).split('\n')[1:-2] if line.strip()) + '\n' + m.group(3) + '\n',
 src,
 flags=re.DOTALL,
)


# Easier: do explicit string fixes for known broken sections.


# Replace the proofPoints block
src = src.replace(
 'const proofPoints = [\n "OPC",\n "AI ERA",\n "SHANGHAI",\n "COMPOSING STILL",\n "DISMANTLE / JUDGE / COMPLETE",\n];',
 'const proofPoints = [\n "OPC",\n "AI ERA",\n "SHANGHAI",\n "COMPOSING STILL",\n "DISMANTLE / JUDGE / COMPLETE",\n];',
)


# head meta block re-indent: lines after `<meta name="theme-color" />` that start with single space (the new injected meta)
# Pattern: fix the new meta block to4-space indent matching the rest of <head>
old_meta_block = ''' <meta name="theme-color" content="#090807" />
 <meta
 name="description"
 content="D.J.C，AI时代的一人公司方法论：拆解（Dismantle）、判断（Judge）、成事（Complete）。面向独立创造者与 AI转型经营者，提供从战略到落地的一体化陪跑。"
 />
 <meta name="author" content="D.J.C" />
 <link rel="canonical" href="https://opc.example.com/" />

 <meta property="og:type" content="website" />
 <meta property="og:site_name" content="D.J.C" />
 <meta property="og:title" content="D.J.C | AI时代的一人公司方法论" />
 <meta
 property="og:description"
 content="拆解问题，判断方向，把事做成。Dismantle · Judge · Complete。面向独立创造者与 AI转型经营者。"
 />
 <meta property="og:url" content="https://opc.example.com/" />
 <meta
 property="og:image"
 content="https://opc.example.com/images/djc-noir-door.png"
 />
 <meta property="og:image:alt" content="黑色空间里一道门缝透出金色光线" />
 <meta property="og:locale" content="zh_CN" />

 <meta name="twitter:card" content="summary_large_image" />
 <meta name="twitter:title" content="D.J.C | AI时代的一人公司方法论" />
 <meta
 name="twitter:description"
 content="拆解问题，判断方向，把事做成。Dismantle · Judge · Complete。"
 />
 <meta
 name="twitter:image"
 content="https://opc.example.com/images/djc-noir-door.png"
 />
 <meta name="twitter:image:alt" content="黑色空间里一道门缝透出金色光线" />

 <script type="application/ld+json" set:html={JSON.stringify({
 "@context": "https://schema.org",
 "@type": "Person",
 "@id": "https://opc.example.com/#person",
 "name": "D.J.C",
 "alternateName": "Dismantle Judge Complete",
 "description": "AI时代的一人公司方法论。拆解（Dismantle）、判断（Judge）、成事（Complete）三步法，面向独立创造者与 AI转型经营者，提供从战略到落地的一体化陪跑。",
 "url": "https://opc.example.com/",
 "jobTitle": "One Person Company",
 "knowsAbout": [
 "AI 工作流落地",
 "独立创造者战略",
 "业务诊断",
 "决策陪跑",
 "内容结构化",
 "长期主义"
 ],
 "workLocation": {
 "@type": "Place",
 "address": {
 "@type": "PostalAddress",
 "addressLocality": "Shanghai",
 "addressCountry": "CN"
 }
 },
 "sameAs": ["https://x.com/XianlaiSolo"]
 })} />'''


new_meta_block = ''' <meta name="theme-color" content="#090807" />
 <meta
 name="description"
 content="D.J.C，AI时代的一人公司方法论：拆解（Dismantle）、判断（Judge）、成事（Complete）。面向独立创造者与 AI转型经营者，提供从战略到落地的一体化陪跑。"
 />
 <meta name="author" content="D.J.C" />
 <link rel="canonical" href="https://opc.example.com/" />

 <meta property="og:type" content="website" />
 <meta property="og:site_name" content="D.J.C" />
 <meta property="og:title" content="D.J.C | AI时代的一人公司方法论" />
 <meta
 property="og:description"
 content="拆解问题，判断方向，把事做成。Dismantle · Judge · Complete。面向独立创造者与 AI转型经营者。"
 />
 <meta property="og:url" content="https://opc.example.com/" />
 <meta
 property="og:image"
 content="https://opc.example.com/images/djc-noir-door.png"
 />
 <meta property="og:image:alt" content="黑色空间里一道门缝透出金色光线" />
 <meta property="og:locale" content="zh_CN" />

 <meta name="twitter:card" content="summary_large_image" />
 <meta name="twitter:title" content="D.J.C | AI时代的一人公司方法论" />
 <meta
 name="twitter:description"
 content="拆解问题，判断方向，把事做成。Dismantle · Judge · Complete。"
 />
 <meta
 name="twitter:image"
 content="https://opc.example.com/images/djc-noir-door.png"
 />
 <meta name="twitter:image:alt" content="黑色空间里一道门缝透出金色光线" />

 <script type="application/ld+json" set:html={JSON.stringify({
 "@context": "https://schema.org",
 "@type": "Person",
 "@id": "https://opc.example.com/#person",
 "name": "D.J.C",
 "alternateName": "Dismantle Judge Complete",
 "description": "AI时代的一人公司方法论。拆解（Dismantle）、判断（Judge）、成事（Complete）三步法，面向独立创造者与 AI转型经营者，提供从战略到落地的一体化陪跑。",
 "url": "https://opc.example.com/",
 "jobTitle": "One Person Company",
 "knowsAbout": [
 "AI 工作流落地",
 "独立创造者战略",
 "业务诊断",
 "决策陪跑",
 "内容结构化",
 "长期主义"
 ],
 "workLocation": {
 "@type": "Place",
 "address": {
 "@type": "PostalAddress",
 "addressLocality": "Shanghai",
 "addressCountry": "CN"
 }
 },
 "sameAs": ["https://x.com/XianlaiSolo"]
 })} />'''


assert old_meta_block in src, 'old_meta_block not found'
src = src.replace(old_meta_block, new_meta_block,1)


# hero img block
old_hero_img = ''' <section class="hero">
 <img
 class="hero-image"
 src="/images/djc-noir-door.png"
 alt="黑色空间里一道门缝透出金色光线"
 width="1672"
 height="941"
 loading="eager"
 decoding="async"
 fetchpriority="high"
 />'''
new_hero_img = ''' <section class="hero">
 <img
 class="hero-image"
 src="/images/djc-noir-door.png"
 alt="黑色空间里一道门缝透出金色光线"
 width="1672"
 height="941"
 loading="eager"
 decoding="async"
 fetchpriority="high"
 />'''
assert old_hero_img in src, 'old_hero_img not found'
src = src.replace(old_hero_img, new_hero_img,1)


# belief img block
old_belief_img = ''' <figure class="belief-image reveal">
 <img
 src="/images/djc-noir-stairs.png"
 alt="暗色台阶通向一道发光的门"
 width="1536"
 height="1024"
 loading="lazy"
 decoding="async"
 />
 </figure>'''
new_belief_img = ''' <figure class="belief-image reveal">
 <img
 src="/images/djc-noir-stairs.png"
 alt="暗色台阶通向一道发光的门"
 width="1536"
 height="1024"
 loading="lazy"
 decoding="async"
 />
 </figure>'''
assert old_belief_img in src, 'old_belief_img not found'
src = src.replace(old_belief_img, new_belief_img,1)


# sr-only block
old_sr = '''    
 <section class="sr-only" aria-label="关于 D.J.C 的常见问题">
 <h2>关于 D.J.C</h2>
 <dl>
 <dt>什么是 D.J.C？</dt>
 <dd>D.J.C是一人公司方法论的实践品牌，核心方法是 Dismantle（拆解）、Judge（判断）、Complete（成事）三步法，把复杂问题拆到颗粒度，在信息噪音中做判断，把事稳定做成。</dd>
 <dt>D.J.C 提供哪些服务？</dt>
 <dd>六类服务：战略拆解（Strategy Dismantle）、业务诊断（Business Diagnosis）、决策陪跑（Decision Partner）、AI 工作流落地（AI Workflow）、内容结构化（Content System）、持续迭代（Continuous Iteration）。</dd>
 <dt>一次咨询的流程是怎样的？</dt>
 <dd>从一次不超过30 分钟的对话开始，先不急着选答案，一起看清什么是噪音、什么是正在发生的事，再决定是否进入2-4 周的深度陪跑。</dd>
 <dt>适合谁？</dt>
 <dd>一人公司创始人、独立创造者，以及正在把 AI 接进研究、设计、交付与复盘环节的经营者。</dd>
 <dt>在哪里？</dt>
 <dd>上海，中国。</dd>
 </dl>
 </section>'''
new_sr = '''

 <section class="sr-only" aria-label="关于 D.J.C 的常见问题">
 <h2>关于 D.J.C</h2>
 <dl>
 <dt>什么是 D.J.C？</dt>
 <dd>
 D.J.C是一人公司方法论的实践品牌，核心方法是 Dismantle（拆解）、Judge（判断）、Complete（成事）三步法，把复杂问题拆到颗粒度，在信息噪音中做判断，把事稳定做成。
 </dd>
 <dt>D.J.C 提供哪些服务？</dt>
 <dd>
 六类服务：战略拆解（Strategy Dismantle）、业务诊断（Business Diagnosis）、决策陪跑（Decision Partner）、AI 工作流落地（AI Workflow）、内容结构化（Content System）、持续迭代（Continuous Iteration）。
 </dd>
 <dt>一次咨询的流程是怎样的？</dt>
 <dd>
 从一次不超过30 分钟的对话开始，先不急着选答案，一起看清什么是噪音、什么是正在发生的事，再决定是否进入2-4 周的深度陪跑。
 </dd>
 <dt>适合谁？</dt>
 <dd>
 一人公司创始人、独立创造者，以及正在把 AI 接进研究、设计、交付与复盘环节的经营者。
 </dd>
 <dt>在哪里？</dt>
 <dd>上海，中国。</dd>
 </dl>
 </section>'''
assert old_sr in src, 'old_sr not found'
src = src.replace(old_sr, new_sr,1)


with open('src/pages/index.astro','w') as f:
 f.write(src)
print('ok, size:', len(src))
