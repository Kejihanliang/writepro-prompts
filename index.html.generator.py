#!/usr/bin/env python3
"""
AI工具日报生成器 v2 - 增强版
- GitHub Trending
- Product Hunt  
- 套利机会
- 免费/开源项目推荐
"""

import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import os
import json
from datetime import datetime

# ── 数据源 ────────────────────────────────────────────────

GITHUB_TRENDING = []  # 动态获取
PRODUCT_HUNT = []     # 动态获取

# 固定的优质资源库（不依赖网络）
CURATED_TOOLS = {
    '🤖 AI对话': [
        {'name':'ChatGPT','desc':'OpenAI大模型，支持GPT-4o','url':'https://chat.openai.com','price':'免费基础版'},
        {'name':'Claude','desc':'Anthropic大模型，100K上下文','url':'https://claude.ai','price':'免费'},
        {'name':'Perplexity','desc':'AI搜索引擎，实时联网，回答带引用','url':'https://perplexity.ai','price':'免费'},
        {'name':'Gemini','desc':'Google大模型，2M上下文','url':'https://gemini.google.com','price':'免费'},
    ],
    '💻 编程工具': [
        {'name':'GitHub Copilot','desc':'AI编程助手，代码补全','url':'https://github.com/features/copilot','price':'$10/月'},
        {'name':'Cursor','desc':'AI代码编辑器，基于VS Code','url':'https://cursor.sh','price':'免费基础版'},
        {'name':'Replit Agent','desc':'AI全栈开发，Text-to-App','url':'https://replit.com','price':'免费'},
        {'name':'Codeium','desc':'免费AI代码补全，Copilot替代','url':'https://codeium.com','price':'免费'},
    ],
    '☁️ 部署平台': [
        {'name':'Vercel','desc':'免费部署前端/AI应用到全球CDN','url':'https://vercel.com','price':'免费起步'},
        {'name':'Railway','desc':'最简单的服务器部署，支持Python/Node','url':'https://railway.app','price':'500小时/月免费'},
        {'name':'Fly.io','desc':'容器化部署，全球边缘节点','url':'https://fly.io','price':'免费264小时'},
        {'name':'Render','desc':'Heroku替代，Web服务部署','url':'https://render.com','price':'免费'},
    ],
    '🗄️ 数据库&BaaS': [
        {'name':'Supabase','desc':'开源Firebase替代，后端即服务','url':'https://supabase.com','price':'免费开源版'},
        {'name':'Firebase','desc':'Google后端平台','url':'https://firebase.google.com','price':'免费起步'},
        {'name':'PlanetScale','desc':'Serverless MySQL，分支数据库','url':'https://planetscale.com','price':'免费'},
        {'name':'MongoDB Atlas','desc':'免费MongoDB云数据库','url':'https://mongodb.com/atlas','price':'512MB免费'},
    ],
    '🔧 开发工具': [
        {'name':'Cloudflare Workers','desc':'Edge计算，全球CDN，Serverless','url':'https://workers.cloudflare.com','price':'10万请求/天免费'},
        {'name':'Ngrok','desc':'内网穿透，本地开发暴露公网','url':'https://ngrok.com','price':'免费'},
        {'name':'Pipedream','desc':'API集成自动化，无服务器工作流','url':'https://pipedream.com','price':'免费'},
        {'name':'Zapier','desc':'工作流自动化，连接3000+应用','url':'https://zapier.com','price':'免费100次/月'},
    ],
    '📝 写作&内容': [
        {'name':'Notion AI','desc':'AI笔记、写作、总结、翻译','url':'https://notion.so','price':'免费20次'},
        {'name':'Claude for Work','desc':'Anthropic企业版，长文档处理','url':'https://claude.ai/business','price':'$20/人/月'},
        {'name':'Jasper','desc':'AI营销文案生成','url':'https://jasper.ai','price':'免费7天'},
        {'name':'Copy.ai','desc':'AI文案生成，Sales文案专家','url':'https://copy.ai','price':'免费2000词'},
    ],
    '🎨 设计&图片': [
        {'name':'Canva AI','desc':'AI设计图片、PPT、海报','url':'https://canva.com','price':'免费基础版'},
        {'name':'Figma AI','desc':'AI设计，Prototyping','url':'https://figma.com','price':'免费起步'},
        {'name':'Remove.bg','desc':'AI一键抠图','url':'https://remove.bg','price':'免费50张'},
        {'name':'Leonardo.ai','desc':'AI游戏资产生成','url':'https://leonardo.ai','price':'免费150Tokens'},
    ],
    '📊 数据&API': [
        {'name':'OpenAI API','desc':'GPT-4o、o1预览版，$5/10M tokens','url':'https://openai.com/api','price':'$5/10M tokens'},
        {'name':'Anthropic API','desc':'Claude 3.5 Sonnet，$3/10M tokens','url':'https://anthropic.com/api','price':'$3/10M tokens'},
        {'name':'Groq API','desc':'最快LLM推理，Mistral/LLaMA','url':'https://groq.com','price':'免费14M tokens/天'},
        {'name':'Telegram Bot API','desc':'免费消息推送，聊天机器人','url':'https://core.telegram.org/api','price':'免费'},
    ],
}

# 套利机会库
ARBITRAGE = [
    {'title':'GitHub Copilot免费申请','desc':'学生认证免费使用，或白嫖Education pack','source':'信息差'},
    {'title':'Vercel Hobby→Pro升级','desc':'$20/月Vercel Pro可给多个项目用，转售服务','source':'套利'},
    {'title':'域名转售','desc':'监控过期优质域名，抢注后转卖','source':'高杠杆'},
    {'title':'API转售','desc':'OpenAI API $0.002/1K → 转售$0.01/1K (5x)','source':'高利润'},
    {'title':'Notion模板变现','desc':'制作Notion模板，Gumroad卖$19-89','source':'边际成本为零'},
    {'title':'Cursor Pro referral','desc':'推荐朋友获得Pro时长，可叠加','source':'Affiliate'},
]

def get_arbitrage_html():
    html = ''
    for item in ARBITRAGE:
        html += f'''<div class="arb-item">
  <div class="arb-title">📌 {item['title']}</div>
  <div class="arb-desc">{item['desc']}</div>
  <div class="arb-source">来源: {item['source']}</div>
</div>'''
    return html

def get_curated_html():
    html = ''
    cats = {
        '🤖 AI对话': '🤖 AI对话',
        '💻 编程工具': '💻 编程工具',
        '☁️ 部署平台': '☁️ 部署平台',
        '🗄️ 数据库&BaaS': '🗄️ 数据库',
        '🔧 开发工具': '🔧 开发工具',
        '📝 写作&内容': '📝 写作&内容',
        '🎨 设计&图片': '🎨 设计&图片',
        '📊 数据&API': '📊 数据&API',
    }
    for cat, cat_name in cats.items():
        tools = CURATED_TOOLS.get(cat, [])
        if not tools: continue
        html += f'<div class="cat-section"><h3>{cat_name}</h3><div class="tools-grid">'
        for t in tools:
            html += f'''<div class="tool-card">
  <div class="tool-header">
    <a href="{t['url']}" target="_blank" class="tool-name">{t['name']}</a>
    <span class="tool-price">{t['price']}</span>
  </div>
  <p class="tool-desc">{t['desc']}</p>
</div>'''
        html += '</div></div>'
    return html

def get_github_html():
    if not GITHUB_TRENDING: 
        return '<p style="color:#8b949e">🔥 GitHub Trending 数据加载中...</p>'
    html = ''
    for i, item in enumerate(GITHUB_TRENDING[:5], 1):
        html += f'''<div class="item">
  <div class="item-header">
    <a href="{item['url']}" target="_blank" class="item-name">{i}. {item['name']}</a>
    <span class="item-lang">{item.get('language','')}</span>
    <span class="item-stars">⭐ {item.get('stars','')}</span>
  </div>
  <p class="item-desc">{item.get('description','')}</p>
  <span class="item-cat">{item.get('category','🔧 工具')}</span>
</div>'''
    return html

def generate():
    today = datetime.now()
    date_str = today.strftime('%Y年%m月%d日')
    day_of_year = today.strftime('%j')
    
    arb_html = get_arbitrage_html()
    tools_html = get_curated_html()
    github_html = get_github_html()
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI工具日报 {date_str} - 每日精选免费AI工具</title>
  <meta name="description" content="每日精选免费AI工具、编程资源、套利机会。程序员和外贸人必备。{date_str}第{day_of_year}天">
  <meta property="og:title" content="AI工具日报 {date_str}">
  <meta property="og:description" content="每日精选免费AI工具，节省搜索时间">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0f; color: #e0e0e0; line-height: 1.6; }}
    .container {{ max-width: 960px; margin: 0 auto; padding: 40px 20px; }}
    header {{ text-align: center; padding: 40px 0; border-bottom: 1px solid #1a1a2e; margin-bottom: 40px; }}
    h1 {{ font-size: 2.2rem; color: #7ee787; margin-bottom: 8px; }}
    .subtitle {{ color: #8b949e; font-size: 1rem; }}
    .date {{ color: #58a6ff; font-size: 0.9rem; margin-top: 12px; }}
    .section {{ margin: 40px 0; }}
    .section-title {{ display: flex; align-items: center; gap: 10px; font-size: 1.3rem; color: #c9d1d9; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #21262d; }}
    .item {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; margin-bottom: 12px; }}
    .item-header {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px; }}
    .item-name {{ color: #58a6ff; text-decoration: none; font-weight: bold; font-size: 1rem; }}
    .item-name:hover {{ text-decoration: underline; }}
    .item-lang {{ background: #1f6feb33; color: #58a6ff; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; }}
    .item-stars {{ color: #e3b341; font-size: 0.85rem; }}
    .item-desc {{ color: #8b949e; font-size: 0.9rem; margin-bottom: 8px; }}
    .item-cat {{ display: inline-block; background: #23863633; color: #7ee787; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; }}
    .cat-section {{ margin: 30px 0; }}
    .cat-section h3 {{ color: #c9d1d9; font-size: 1.1rem; margin-bottom: 16px; }}
    .tools-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }}
    .tool-card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; }}
    .tool-header {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; margin-bottom: 8px; }}
    .tool-name {{ color: #58a6ff; text-decoration: none; font-weight: bold; font-size: 0.95rem; }}
    .tool-name:hover {{ text-decoration: underline; }}
    .tool-price {{ background: #23863633; color: #7ee787; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; white-space: nowrap; }}
    .tool-desc {{ color: #8b949e; font-size: 0.85rem; }}
    .arb-item {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; margin-bottom: 10px; }}
    .arb-title {{ color: #f0883e; font-weight: bold; margin-bottom: 6px; }}
    .arb-desc {{ color: #c9d1d9; font-size: 0.9rem; margin-bottom: 6px; }}
    .arb-source {{ color: #8b949e; font-size: 0.75rem; }}
    .subscribe {{ background: linear-gradient(135deg, #1a4731, #0e3320); border: 1px solid #238636; border-radius: 12px; padding: 30px; text-align: center; margin: 50px 0; }}
    .subscribe h2 {{ color: #7ee787; margin-bottom: 12px; }}
    .subscribe p {{ color: #8b949e; margin-bottom: 20px; }}
    .sub-btn {{ display: inline-block; background: #238636; color: white; padding: 12px 30px; border-radius: 8px; text-decoration: none; font-weight: bold; }}
    footer {{ text-align: center; padding: 30px; color: #484f58; font-size: 0.8rem; border-top: 1px solid #21262d; margin-top: 50px; }}
    @media (max-width: 600px) {{ .tools-grid {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🤖 AI工具日报</h1>
      <p class="subtitle">每日精选 · 免费/开源优先 · 程序员&外贸人必备</p>
      <p class="date">📅 {date_str} · 第{day_of_year}天</p>
    </header>

    <div class="subscribe">
      <h2>📬 订阅每日推送</h2>
      <p>每天09:00收到精选工具列表 + 套利机会</p>
      <a href="https://t.me/YourIntelBot" class="sub-btn">🔔 订阅 Telegram</a>
    </div>

    <div class="section">
      <div class="section-title">🔥 GitHub 热门项目</div>
      {github_html}
    </div>

    <div class="section">
      <div class="section-title">💰 套利机会</div>
      {arb_html}
    </div>

    <div class="section">
      <div class="section-title">🛠️ 精选免费工具</div>
      {tools_html}
    </div>

    <footer>
      <p>🤖 AI工具日报 · 虾尾出品 🦐</p>
      <p style="margin-top:8px;">自动生成 · GitHub Actions驱动</p>
    </footer>
  </div>
</body>
</html>'''
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'[+] Generated: {len(github_html)} GH items, {len(ARBITRAGE)} arb opps, {sum(len(v) for v in CURATED_TOOLS.values())} tools')
    return html

if __name__ == '__main__':
    generate()
