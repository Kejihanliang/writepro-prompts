#!/usr/bin/env python3
"""
AI工具日报 - Daily AI Tools Digest Generator
Automatically generates a daily newsletter about free AI tools
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from typing import List, Dict
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy settings - use system proxy if available
PROXY = None
for env_var in ['HTTPS_PROXY', 'HTTP_PROXY', 'https_proxy', 'http_proxy']:
    val = os.environ.get(env_var)
    if val:
        PROXY = val
        break
# Default to Clash proxy if available
if not PROXY:
    PROXY = os.environ.get('http://127.0.0.1:7890')

def get_session():
    s = requests.Session()
    if PROXY:
        s.proxies = {'http': PROXY, 'https': PROXY}
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
    return s

session = get_session()

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'site')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Affiliate links (这些链接放上去会持续产生佣金)
AFFILIATE_LINKS = {
    'chatgpt': 'https://chat.openai.com',  # OpenAI
    'claude': 'https://claude.ai',  # Anthropic
    'notion': 'https://notion.so',  # Notion
    'github': 'https://github.com',  # GitHub
    'vercel': 'https://vercel.com',  # Vercel (affiliate)
    'railway': 'https://railway.app',  # Railway (affiliate)
    'supabase': 'https://supabase.com',  # Supabase (affiliate)
    'cloudflare': 'https://cloudflare.com',  # Cloudflare
    'netlify': 'https://netlify.com',  # Netlify (affiliate)
    'digitalocean': 'https://m.do.co/c/xxxx',  # DigitalOcean affiliate
}

def fetch_github_trending() -> List[Dict]:
    """抓取GitHub热门项目"""
    try:
        resp = session.get('https://github.com/trending', timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = []
        for repo in soup.select('article.Box-row')[:8]:
            name = repo.select_one('h2 a').text.strip().replace('\n', '').replace(' ', '')
            desc = repo.select_one('p').text.strip() if repo.select_one('p') else ''
            lang = repo.select_one('[itemprop="programmingLanguage"]').text.strip() if repo.select_one('[itemprop="programmingLanguage"]') else ''
            stars = repo.select_one('a[href$="/stargazers"]').text.strip() if repo.select_one('a[href$="/stargazers"]') else ''
            url = 'https://github.com' + repo.select_one('h2 a')['href']
            
            # 分类
            category = '🔧 工具'
            if any(k in (name+desc).lower() for k in ['ai', 'gpt', 'llm', 'chat']): category = '🤖 AI'
            elif any(k in (name+desc).lower() for k in ['api', 'sdk', 'lib']): category = '📦 库'
            elif any(k in (name+desc).lower() for k in ['web', 'app', 'ui']): category = '🌐 Web'
            
            items.append({
                'name': name,
                'description': desc,
                'language': lang,
                'stars': stars,
                'url': url,
                'category': category
            })
        return items
    except Exception as e:
        print(f'[GitHub] Error: {e}')
        return []

def fetch_product_hunt() -> List[Dict]:
    """抓取Product Hunt热门产品"""
    try:
        resp = session.get('https://www.producthunt.com', timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = []
        for post in soup.select('[data-test="product-item"]')[:5]:
            name_el = post.select_one('a')
            name = name_el.text.strip() if name_el else ''
            url = 'https://producthunt.com' + name_el['href'] if name_el and 'href' in name_el.attrs else ''
            items.append({'name': name, 'url': url})
        return items
    except Exception as e:
        print(f'[PH] Error: {e}')
        return []

def fetch_free_tools() -> List[Dict]:
    """整理免费工具合集 - 完全自主生成"""
    return [
        {
            'name': 'ChatGPT (Free)',
            'description': 'OpenAI官方大模型，支持GPT-4，通用对话',
            'url': 'https://chat.openai.com',
            'category': '🤖 AI对话',
            'price': '免费',
            'affiliate': False
        },
        {
            'name': 'Claude (Free)',
            'description': 'Anthropic大模型，长上下文，擅长分析',
            'url': 'https://claude.ai',
            'category': '🤖 AI对话',
            'price': '免费',
            'affiliate': False
        },
        {
            'name': 'GitHub Copilot',
            'description': 'AI编程助手，代码补全，bug修复',
            'url': 'https://github.com/features/copilot',
            'category': '💻 编程',
            'price': '$10/月',
            'affiliate': True
        },
        {
            'name': 'Vercel AI SDK',
            'description': '在Vercel上快速部署AI应用',
            'url': 'https://vercel.com/blog/ai-sdk',
            'category': '🤖 AI部署',
            'price': '免费起步',
            'affiliate': True
        },
        {
            'name': 'Railway',
            'description': '最简单的服务器部署平台，支持Python/Node',
            'url': 'https://railway.app',
            'category': '☁️ 部署',
            'price': '免费500小时/月',
            'affiliate': True
        },
        {
            'name': 'Supabase',
            'description': '开源Firebase替代，后端即服务',
            'url': 'https://supabase.com',
            'category': '☁️ BaaS',
            'price': '免费开源版',
            'affiliate': True
        },
        {
            'name': 'Cloudflare Workers',
            'description': 'Edge计算，全球CDN，Serverless',
            'url': 'https://workers.cloudflare.com',
            'category': '☁️ Edge',
            'price': '免费10万请求/天',
            'affiliate': False
        },
        {
            'name': 'Notion AI',
            'description': 'AI笔记、写作、总结、翻译',
            'url': 'https://notion.so',
            'category': '📝 写作',
            'price': '免费20次',
            'affiliate': False
        },
        {
            'name': 'Canva AI',
            'description': 'AI设计图片、PPT、海报',
            'url': 'https://canva.com',
            'category': '🎨 设计',
            'price': '免费基础版',
            'affiliate': False
        },
        {
            'name': 'Perplexity AI',
            'description': 'AI搜索引擎，实时联网，回答带引用',
            'url': 'https://perplexity.ai',
            'category': '🔍 搜索',
            'price': '免费',
            'affiliate': False
        },
    ]

def generate_html(github_items: List, ph_items: List, free_tools: List) -> str:
    """生成HTML页面"""
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # 按分类分组免费工具
    categories = {}
    for tool in free_tools:
        cat = tool['category']
        if cat not in categories: categories[cat] = []
        categories[cat].append(tool)
    
    github_html = ''
    for item in github_items[:5]:
        github_html += f'''
        <div class="item">
          <div class="item-header">
            <a href="{item['url']}" target="_blank" class="item-name">{item['name']}</a>
            <span class="item-lang">{item['language']}</span>
            <span class="item-stars">⭐ {item['stars']}</span>
          </div>
          <p class="item-desc">{item['description']}</p>
          <span class="item-cat">{item['category']}</span>
        </div>'''
    
    tools_html = ''
    for cat, tools in categories.items():
        tools_html += f'<div class="cat-section"><h3>{cat}</h3><div class="tools-grid">'
        for tool in tools:
            aff_tag = ' 🔗' if tool['affiliate'] else ''
            tools_html += f'''
            <div class="tool-card">
              <div class="tool-header">
                <a href="{tool['url']}" target="_blank" class="tool-name">{tool['name']}{aff_tag}</a>
                <span class="tool-price">{tool['price']}</span>
              </div>
              <p class="tool-desc">{tool['description']}</p>
            </div>'''
        tools_html += '</div></div>'
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI工具日报 {today} - 每日精选免费AI工具</title>
  <meta name="description" content="每日精选免费AI工具、编程资源、套利机会。{today}期">
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0f; color: #e0e0e0; line-height: 1.6; }}
    .container {{ max-width: 900px; margin: 0 auto; padding: 40px 20px; }}
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
      <p class="date">📅 {today} · 第{datetime.now().strftime('%j')}天</p>
    </header>

    <div class="subscribe">
      <h2>📬 订阅每日推送</h2>
      <p>每天09:00收到精选工具列表，节省你自己搜索的时间</p>
      <a href="https://t.me/YourIntelBot" class="sub-btn">🔔 订阅 Telegram</a>
    </div>

    <div class="section">
      <div class="section-title">🔥 GitHub 热门项目</div>
      {github_html if github_html else '<p style="color:#8b949e">加载中...</p>'}
    </div>

    <div class="section">
      <div class="section-title">🛠️ 精选免费工具</div>
      {tools_html}
    </div>

    <footer>
      <p>🤖 AI工具日报 · AI自动生成 · 虾尾出品 🦐</p>
      <p style="margin-top:8px;">Affiliate links: 🔗 = 含联盟链接</p>
    </footer>
  </div>
</body>
</html>'''
    return html

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    print(f'[*] Generating daily digest {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    
    # Fetch data
    github = fetch_github_trending()
    ph = fetch_product_hunt()
    free = fetch_free_tools()
    
    # Generate HTML
    html = generate_html(github, ph, free)
    
    # Save
    index_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Save archive
    archive_path = os.path.join(OUTPUT_DIR, 'archive', f'{datetime.now().strftime("%Y-%m-%d")}.html')
    os.makedirs(os.path.dirname(archive_path), exist_ok=True)
    with open(archive_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f'[Daily] ✅ 生成完成: {index_path}')
    print(f'[+] GitHub: {len(github)} items | PH: {len(ph)} | Tools: {len(free)}')
    
    return html

if __name__ == '__main__':
    main()
