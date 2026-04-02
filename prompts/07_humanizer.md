# 模块七：Humanizer规则 - 消除AI痕迹
## 让AI生成的文案读起来像真人写的

---

## 7.1 AI文案检测原理

AI生成的文案有几个明显特征：

1. **过于流畅** - 句子太长、措辞过于完美
2. **缺乏个性** - 没有具体的观点和情感
3. **模式化开头** - "In today's fast-paced world..."
4. **过度使用某些词** - "leverage", "robust", "seamless", "cutting-edge"
5. **缺乏具体细节** - 通用的"解决方案"而不是具体的案例

---

## 7.2 Humanizer核心技巧

### 技巧1：打破完美句式

**Before (AI痕迹明显):**
"Our revolutionary solution leverages state-of-the-art technology to seamlessly optimize your workflow, enabling you to achieve unprecedented efficiency gains."

**After (Humanized):**
"We built this thing because we were tired of wasting hours on [SPECIFIC_TASK]. What we ended up with is [TOOL_NAME] - it does [ONE SPECIFIC THING] without the usual headaches."

---

### 技巧2：添加具体细节

**Before:**
"Our product helps businesses increase productivity."

**After:**
"After using our product for 3 months, [REAL CUSTOMER TYPE] companies reported saving an average of [X] hours per week on [SPECIFIC TASK]. One client told us it 'finally made Monday meetings bearable.'"

---

### 技巧3：使用不完美的表达

真人写作的特点：
- 偶尔用短句
- 可以用问句开头
- 可以用"说实话"之类的口头禅
- 可以承认缺点

**Before:**
"While there may be a learning curve associated with implementation, the long-term benefits significantly outweigh initial challenges."

**After:**
"Look, there's definitely a learning curve. The first week kind of sucks. But after that? [CLIENTS] tell us they can't imagine going back to how things were."

---

### 技巧4：添加行业黑话/术语

每个行业都有自己的行话。加入1-2个会让文案更专业。

例如外贸行业：
- "tooling costs" / "production lead time" / " defect rate"
- "FOB" / "CIF" / "MOQ" / "L/C"
- "30% deposit, 70% against BL"

---

### 技巧5：使用真实场景描述

**Before:**
"Our platform is designed to streamline communication between teams."

**After:**
"Picture this: it's 9pm, you just got a message from your supplier about a quality issue. Instead of 15 emails back and forth, you hop onto our platform, flag the problem, and your whole team sees the update in real-time. That's what we built."

---

## 7.3 快速Humanizer检查清单

用这个清单检查任何AI生成的文案：

- [ ] **开头够不够抓人？** 读前50字是否能让人想继续读？
- [ ] **有没有具体数字？** 模糊的"很多"改成具体的"87%"
- [ ] **有没有个人视角？** 用"我觉得"而不是"人们认为"
- [ ] **有没有情绪？** 适当的幽默/惊讶/愤怒让文案更真实
- [ ] **有没有反常识？** "实际上..." "大部分人以为..." 
- [ ] **有没有具体例子？** "比如..." 比理论说服力强10倍
- [ ] **读起来顺不顺？** 大声读出来，拗口的地方改掉
- [ ] **有没有口语化表达？** "kind of" "pretty much" "honestly"
- [ ] **有没有主动承认缺点？** 真诚比完美更可信
- [ ] **结尾有没有CTA而不是空话？** "联系我" > "期待您的回复"

---

## 7.4 一键Humanizer Prompt

把这个Prompt贴在任何AI生成文案后面，可以一键去AI痕迹：

```
请把下面的文案改写成更人性化、更自然的版本。

要求：
1. 保留核心信息
2. 打破过于完美的句式
3. 加入1-2个具体的数字或例子
4. 添加行业相关的专业术语（如果适用）
5. 让它读起来像有10年经验的专业人士写的，而不是AI
6. 长度控制在原文±20%范围内

原文：
[PASTE_AI_GENERATED_TEXT_HERE]
```

---

## 7.5 常见AI表达 vs Humanized版本

| AI表达 | Humanized |
|--------|-----------|
| "Our innovative solution..." | "We built this because..." |
| "Leverage your data" | "Use your data to actually do [specific thing]" |
| "Seamless integration" | "Works with [TOOL X] without you needing to do anything" |
| "Robust and scalable" | "Doesn't fall apart when you throw more work at it" |
| "State-of-the-art" | "Actually pretty new/we just built this" |
| "Comprehensive suite" | "Everything you need to [specific outcome]" |
| "Enhance efficiency" | "Spend less time on [task], more time on [what matters]" |
| "Our team is dedicated to..." | "We personally reply to every message within 24h" |
| "Best-in-class" | "We looked at everything else and built the one we'd actually use" |
| "Transform your business" | "[Real result] in [specific timeframe] - that's what clients tell us" |

---

## 7.6 场景化Humanizer（外贸版）

针对外贸场景的专门优化：

**开发信Humanizer：**
```
把这封开发信改写得更像真人写的：
- 不要用"In today's business landscape"开头
- 加上具体的行业洞察或数据
- 语气像是在LinkedIn上认识这个人，而不是群发
- 让它听起来像是你特意为这个人写的研究信

原文：[PASTE_EMAIL_HERE]
```

**产品描述Humanizer：**
```
把这个产品描述改得更接地气：
- B2B客户想知道的是结果，不是形容词
- 加入"买家的声音"（如果你是买家会问什么问题）
- 让它听起来像是朋友推荐而不是销售在吹牛
- 具体数字比"卓越品质"更有说服力

原文：[PASTE_DESCRIPTION_HERE]
```

**报价邮件Humanizer：**
```
把这个报价邮件改得更专业但不失温度：
- 不要只说"我们有竞争力"，证明它
- 用"我建议"而不是"我们要求"
- 结尾留一个对话钩子而不是"期待您的回复"
- 让它听起来像是你想跟这个人长期合作

原文：[PASTE_EMAIL_HERE]
```

---

## 练习：找出AI痕迹

阅读以下文案，指出AI痕迹在哪里：

> "In the contemporary global marketplace, establishing robust and enduring business relationships is paramount to achieving sustained commercial success. Our organization has consistently demonstrated an unwavering commitment to delivering exceptional value to our esteemed clientele through the provision of premium-grade products and unparalleled service excellence. We cordially invite you to explore the transformative potential of a strategic partnership with our esteemed enterprise."

答案：
1. "contemporary global marketplace" - 太泛
2. "robust and enduring business relationships" - 空洞
3. "paramount to achieving sustained commercial success" - 废话
4. "unwavering commitment" - 陈词滥调
5. "premium-grade products" - 不知道什么品质
6. "unparalleled service excellence" - 典型的AI堆砌
7. "transformative potential" - 听起来很空洞
8. "strategic partnership" / "esteemed enterprise" - 过度正式

Humanized版本：
"We're not the biggest supplier in [CITY], and we don't want to be. What we do want is to be the one supplier your team actually enjoys working with. Here's why [COMPANY] chose us over cheaper options: [SPECIFIC_REASON]. If that sounds interesting, let's talk."
