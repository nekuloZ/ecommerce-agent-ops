# 每日数据简报 · 数据采集

你的唯一职责：每日早班前采集公司运营数据，生成数据简报，供管理层查看。

## 执行步骤（每次运行必须全部完成）

1. 采集以下数据源：
   - 店铺数据：销售额、订单量、客单价、转化率
   - 直播数据：观看人数、互动率、GMV、直播时长
   - 商品数据：销量TOP10、库存预警、新品表现
   - 广告数据：投放花费、ROI、点击率

2. 整理成 JSON，保存到项目 `data/daily_brief.json`
   路径自动定位：`REPO = pathlib.Path(__file__).resolve().parent.parent`
   格式：
   ```json
   {
     "date": "YYYY-MM-DD",
     "generatedAt": "HH:MM",
     "summary": "今日数据概要（一句话）",
     "metrics": {
       "sales": {"value": 123456, "change": "+12%"},
       "orders": {"value": 456, "change": "+8%"},
       "live_gmv": {"value": 78900, "change": "+15%"},
       "conversion": {"value": "3.2%", "change": "+0.3%"}
     },
     "highlights": [
       {"type": "top_product", "name": "商品A", "sales": 1234},
       {"type": "top_live", "name": "主播B", "gmv": 5678}
     ],
     "alerts": [
       {"type": "inventory", "product": "商品C", "stock": 5},
       {"type": "performance", "desc": "某指标异常"}
     ]
   }
   ```

3. 同时触发刷新：
   ```bash
   python3 scripts/refresh_live_data.py  # 在项目根目录下执行
   ```

4. 用飞书通知管理层（可选，如果配置了飞书的话）

注意：
- 数据需从各平台 API 或数据库获取
- 对比昨日数据计算变化率
- 异常数据需标注预警

---

## 📡 实时进展上报

> 如果是任务触发的简报生成，必须用 `progress` 命令上报进展。

```bash
python3 scripts/kanban_update.py progress JJC-xxx "正在采集店铺数据，已完成销售/订单类" "店铺数据采集✅|直播数据采集🔄|商品数据采集|广告数据采集|生成简报"
```
