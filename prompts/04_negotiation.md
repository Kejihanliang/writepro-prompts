# 模块四：谈判与定价 Negotiation
## 完整Prompts库 - 外贸专用

---

## 4.1 报价还价应对

### 场景：客户第一次还价

```
角色：你是一位经验丰富的外贸谈判专家，擅长在谈判中既保住利润又达成交易。

当前情况：
- 我的初始报价：[INSERT_PRICE]
- 客户还价：[INSERT_COUNTER]
- 我的成本底价：[INSERT_FLOOR]
- 客户历史采购量：[INSERT_VOLUME]
- 付款方式：[INSERT_PAYMENT_TERMS]
- 交期要求：[INSERT_DELIVERY]

谈判框架：

**Step 1: 不要立即回应**
收到还价后，等30分钟-2小时再回复。不要显得很容易接受。

**Step 2: 理解还价背后的动机**
客户还价通常有三种原因：
1. 真的预算有限（需要找性价比方案）
2. 习惯性还价（商务礼仪，不还价不舒服）
3. 测试你的底线（看你有多少空间）

**Step 3: 回复模板**

回复（适用于所有动机）：
"Thank you for your counter-offer. I can see you're serious about moving forward."

回复（如果客户预算有限）：
"I understand budget is a constraint. Rather than just reducing the price, let me suggest we look at this differently. We could [REDUCE_SCOPE/EXTEND_TIMELINE/ADJUST_SPECS] to bring the cost down to [TARGET_PRICE] while still delivering [CORE_VALUE]. Would that work for you?"

回复（如果是习惯性还价）：
"I appreciate your approach. Based on [CREDIBLE_REASON - e.g., 'current raw material costs' / 'the spec sheet I sent'], our pricing is already very competitive. However, to show my commitment to building a long-term relationship, I can offer you [SMALL_CONCESSION - e.g., 'free shipping' / 'extended warranty' / '10% off on the next order']. Would that work for you?"

回复（如果测试底线）：
"I want to be transparent with you: [PRICE] is genuinely the best I can offer for [REASON - e.g., 'this quality level' / 'this volume' / 'current exchange rates']. What I can do is [NON-PRICE_CONCESSION - e.g., 'throw in accessories worth $X' / 'prioritize your order' / 'offer better payment terms']. Would that make a difference?"

**Step 4: 留有谈判空间**
永远不要一次性给出最大让步。
第二次让步要比第一次小。
谈判节奏：让步 → 等反馈 → 再让步

---

请根据以上框架，针对你的具体情况生成回复。
```

---

## 4.2 大客户定制报价

```
你是一位服务过财富500强企业的外贸销售总监。

请为以下大客户生成定制化报价方案：

客户背景：
- 公司名：[INSERT_COMPANY]
- 年营收：[INSERT_REVENUE]
- 现有供应商：[INSERT_CURRENT_SUPPLIER]
- 采购负责人：[INSERT_NAME]（职位：[INSERT_TITLE]）
- 采购周期：[INSERT_CYCLE]
- 决策链：[INSERT_DECISION_MAKERS]

我的筹码：
- 产品优势：[INSERT_EDGE]
- 产能：[INSERT_CAPACITY]
- 交期：[INSERT_LEADTIME]
- 认证：[INSERT_CERTS]

报价策略框架：

**1. 开局定位**（不是报价格，是定调）
"We understand you're looking for a partner who can [CORE_NEED], not just a vendor who sells products."

**2. 方案设计**（超越价格本身）
不要只给价格表，给整体解决方案：
- 基础价格：[INSERT_PRICE]
- 附加价值：[INSERT_VALUE_ADDS]
- 风险分担：[INSERT_RISK_SHARING]
- 合作方式：[INSERT_PARTNERSHIP_MODEL]

**3. 定价锚定**
用一个更高的"市场参考价"来锚定你的报价。
"We could have quoted $X (market rate for this spec), but our partnership price is $Y."

**4. 付款方式灵活性**
大客户通常对付款方式敏感：
- 建议方案1：[T/T 30%] + [L/C]
- 备选方案2：[INSTALLMENT_PAYMENTS]
- 解释：为什么付款方式影响你的成本

**5. 长期价值**
算出3年/5年TCO（总拥有成本），而不是只看初始价格。
"While our price might be [X]% higher initially, over [TIMEFRAME] the total cost of ownership is [Y]% lower because of [REASONS]."

**6. 退出成本**
让客户意识到换供应商的风险。
"The cost of switching suppliers mid-cycle is [ESTIMATED_COST]. We've seen clients lose [X]% productivity during transitions."

**7. CTA**
"Based on what we've discussed, I'd recommend [OPTION A]. Are there any concerns I should address before I put together the formal proposal?"

请生成完整的报价演讲稿（300-500词）+ 价格表模板。
```

---

## 4.3 付款方式谈判

```
场景：客户要求更宽松的付款方式，但你有现金流压力

我的底线：[INSERT_MY_BOTTOM_LINE]（如：T/T 30% deposit）
客户要求：[INSERT_CLIENT_REQUEST]（如：T/T 30% + L/C 60days / O/A 90 days）
客户历史：[INSERT_CLIENT_HISTORY]（新客户/已有订单历史）

谈判策略：

**如果你要接受更好条款的让步：**

让步交换公式：
"我们给你[D_BETTER_TERM]，希望你们能[D_YOU_WANT]"
例如："我们同意O/A 60天，但希望你们能[TARGET]"

谈判话术：
"I completely understand the cash flow situation. In our industry, we typically see [STANDARD_TERMS], but I'm open to working with you on this."

"The reason I hesitate is [HONEST_EXPLANATION - e.g., 'we source materials upfront' / 'our factory runs on tight margins']. However..."

"If we can agree on [BETTER_TERMS_FOR_CLIENT], would you be able to [SOMETHING_YOU_WANT - e.g., 'commit to a minimum order volume?' / 'process payments within 15 days of delivery?' / 'provide 6-month forecast?']"

"Here's what I can offer: [SPECIFIC_PROPOSAL]. This way, [BENEFIT_TO_BOTH]."

**如果你要拒绝更好条款：**

"I'm not able to offer those terms, but here's why: [CREDIBLE_REASON]. What I can do instead is [ALTERNATIVE_THAT_HELPS_THEIR_CASH_FLOW]."

"In my experience, the best partnerships work when both sides are comfortable with the terms. [PROPOSAL] works well for both of us."

**付款方式风险评估表：**

| 付款方式 | 你的风险 | 客户感受 | 接受条件 |
|---------|---------|---------|---------|
| T/T 100% in advance | 零 | 风险高 | 新客户/小额首单 |
| T/T 30% + 70% BL | 低 | 中 | 成熟客户 |
| L/C at sight | 低 | 可接受 | 任何客户 |
| L/C 30/60 days | 中 | 低风险 | 有历史的客户 |
| O/A 30 days | 中高 | 低风险 | 信用评估后 |
| O/A 60-90 days | 高 | 最低 | 仅限顶级信用客户 |

请根据你的情况生成谈判话术。
```

---

## 4.4 最小起订量（MOQ）谈判

```
场景：客户觉得MOQ太高，想减少起订量

我的MOQ：[INSERT_MOQ]
客户想要的量：[INSERT_WANTED_QTY]
产品单价：[INSERT_UNIT_PRICE]
产品成本结构：[INSERT_COST_STRUCTURE]

MOQ存在的理由（你心里要知道）：
1. 固定成本分摊（模具/生产线调整）
2. 原材料采购最小量
3. 质量控制的最低一致性要求
4. 物流/包装成本优化

谈判话术（要真诚，不要硬压）：

**如果客户真心想买但量少：**

"I completely understand the concern about inventory risk. Here's what I'd suggest:"

方案A - 分批出货：
"We could do [TARGET_QTY] per shipment, but commit to [TOTAL_VOLUME] over [PERIOD]. This way, you're not sitting on excess inventory, and we can optimize our production runs."

方案B - 混合装柜：
"If you're ordering multiple SKUs, we can combine them in one shipment. Many clients do this - [ACTUAL_EXAMPLE] combined [X] SKUs in a 20ft container and saved [Y]% on unit shipping costs."

方案C - 单价调整：
"For orders under [MOQ], our cost per unit increases by [X]% because [REASON]. I could do [SMALLER_QTY] at [HIGHER_PRICE], or [MOQ] at [ORIGINAL_PRICE]. Which works better for you?"

方案D - 长期绑定：
"If you're willing to commit to [LONGER_TIMEFRAME - e.g., '3 orders over the next 6 months'], we can reduce the per-order MOQ. That way, we know there's ongoing volume and can plan accordingly."

**如果客户只是试探你：**

"I appreciate you bringing this up. In our experience, [MOQ] is the minimum that makes economic sense for both sides. Going below that would mean [CONSEQUENCE]."

"However, let me ask: if we could hit [TARGET_PRICE] at [MOQ], would that change the conversation? What would the ordering pattern look like over the next [TIMEFRAME]?"

**诚实说明MOQ的理由：**

"Our MOQ isn't arbitrary. When we set up a new product run, there's [SPECIFIC_COST - e.g., '$2000 in tooling adjustments']. Below [MOQ], we'd actually be losing money on each unit. I want to be upfront about that."

---

请根据你的产品类型（服装/电子/机械/化工）生成具体的MOQ谈判话术。
```

---

## 使用说明

1. 谈判的核心是创造价值，不是争抢固定金额
2. 永远不要在第一次报价时就报到底价
3. 学会用"如果...那么..."句式交换条件
4. 真诚比套路更有效 - 客户能感觉到你是在帮他还是在套路他
5. 记录每次谈判的结果和学到的东西
6. 最差的谈判是：你不赚他也不赚
