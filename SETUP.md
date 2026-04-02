# WritePro - 上线配置指南

## 你需要做的（3步，10分钟）

### 第一步：获取你的TRC20地址

1. 打开 **OKX App**
2. 点击「钱包」→ 「USDT」
3. 点击「收币」→ 选择 **TRC20** 网络
4. 复制你的收款地址（以T开头，34位字符）

### 第二步：注册 Formspree（免费，接收订单通知）

1. 访问 [formspree.io](https://formspree.io)
2. 用邮箱注册（Google账号也行）
3. 点击 「New Form」
4. Form name 填：`WritePro Orders`
5. 复制你的 Form ID（格式：`xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`）

### 第三步：更新 payment.html

用文本编辑器打开 `payment.html`，找到以下两处并替换：

**替换1** — 你的TRC20地址：
```javascript
// 找到这行：
YOUR_TRC20_ADDRESS_HERE

// 替换为你的OKX TRC20地址（以T开头）
TKXRwB5a5...（你的地址）
```

**替换2** — 你的Formspree ID：
```html
<!-- 找到这行： -->
action="https://formspree.io/f/YOUR_FORMSPREE_ID"

<!-- 替换为： -->
action="https://formspree.io/f/你的实际ID"
```

---

## 订单流程

1. 客户访问 payment.html
2. 客户转USDT到你的TRC20地址
3. 客户填表（邮箱+TXID）
4. Formspree 邮件通知你订单详情
5. 你在 [tronscan.org](https://tronscan.org) 查TXID确认收款
6. 发货（把prompts文件夹打包发邮件）

---

## 发货设置

收到订单后：
1. 把 `prompts/` 文件夹打包成 `writepro-prompts.zip`
2. 用邮件发送下载链接（可以是百度网盘/Google Drive）

或者用自动化：
- 把文件上传到 Google Drive
- 生成分享链接
- 收到Formspree邮件后，自动回复链接

---

## 下一步（今晚完成）

1. [ ] 获取OKX TRC20地址
2. [ ] 注册 formspree.io
3. [ ] 更新 payment.html 里的地址和ID
4. [ ] 测试一下表单提交
5. [ ] 把 payment.html 部署到网上

---

## 部署选项（免费）

### 选项1：GitHub Pages（最简单）
1. 创建GitHub账号
2. 创建新仓库 `writepro`
3. 上传 `payment.html` 和 `prompts/` 文件夹
4. 开启 Pages 服务
5. 获得免费域名：`username.github.io/writepro`

### 选项2：Vercel（更快）
1. vercel.com 注册
2. 上传文件
3. 获得域名，立即可用

### 选项3：Netlify（拖拽上线）
1. netlify.com 注册
2. 拖拽文件夹到网页
3. 上线完成

---

你有GitHub账号吗？我可以帮你一步步部署上去。
