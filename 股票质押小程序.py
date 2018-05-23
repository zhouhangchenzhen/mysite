import tushare as ts
import numpy as np
import math
import matplotlib.pyplot as plt

# 查看当前版本
print(ts.__version__)

# get data about maotai
codename="600519"
# singe stock anylst

# 交易行情数据
##date：日期
##open：开盘价
##high：最高价
##close：收盘价
##low：最低价
##volume：成交量
##price_change：价格变动
##p_change：涨跌幅
##ma5：5日均价
##ma10：10日均价
##ma20:20日均价
##v_ma5:5日均量
##v_ma10:10日均量
##v_ma20:20日均量
##turnover:换手率

df=ts.get_hist_data(codename).reset_index().sort_values("date")

# 风险警示板股票数据
ststock=ts.get_st_classified().reset_index().sort_values("code")

# 股票基本信息
##code,代码##name,名称##industry,所属行业##area,地区
##pe,市盈率##outstanding,流通股本(亿)##totals,总股本(亿)
##totalAssets,总资产(万)##liquidAssets,流动资产##fixedAssets,固定资产
##reserved,公积金##reservedPerShare,每股公积金##esp,每股收益##bvps,每股净资##pb,市净率##timeToMarket,上市日期##undp,未分利润##perundp, 每股未分配
##rev,收入同比(%)##profit,利润同比(%)##gpr,毛利率(%)##npr,净利润率(%)##holders,股东人数
stockbasics=ts.get_stock_basics().reset_index().sort_values("code")
stockbasics1=stockbasics.set_index('code').ix[codename]
##按年度、季度获取盈利能力数据code,代码

##按年度、季度获取盈利能力数据code,代码
##code,代码
##name,名称
##roe,净资产收益率(%)
##net_profit_ratio,净利率(%)
##gross_profit_rate,毛利率(%)
##net_profits,净利润(万元)
##esp,每股收益
##business_income,营业收入(百万元)
##bips,每股主营业务收入(元)

year=2016
quarter=4
profit=ts.get_profit_data(year, quarter).reset_index().sort_values("code")
profit1=profit.set_index("code").ix[codename]

##按年度、季度获取成长能力数据
##code,代码
##name,名称
##mbrg,主营业务收入增长率(%)
##nprg,净利润增长率(%)
##nav,净资产增长率
##targ,总资产增长率
##epsg,每股收益增长率
##seg,股东权益增长率
growth=ts.get_growth_data(year, quarter).reset_index().sort_values("code")
growth1=growth.set_index("code").ix[codename]

##按年度、季度获取偿债能力数据
##code,代码
##name,名称
##currentratio,流动比率
##quickratio,速动比率
##cashratio,现金比率
##icratio,利息支付倍数
##sheqratio,股东权益比率
##adratio,股东权益增长率
debtpaying=ts.get_debtpaying_data(year, quarter).reset_index().sort_values("code")
debtpaying1=debtpaying.set_index("code").ix[codename]

##按年度、季度获取现金流量数据
##code,代码
##name,名称
##cf_sales,经营现金净流量对销售收入比率
##rateofreturn,资产的经营现金流量回报率
##cf_nm,经营现金净流量与净利润的比率
##cf_liabilities,经营现金净流量对负债比率
##cashflowratio,现金流量比率
cashflow=ts.get_cashflow_data(year, quarter).reset_index().sort_values("code")
cashflow1=cashflow.set_index("code").ix[codename]
####设置 股票质押条件
##禁止介入度股票
##风险警示板股票数据 code不属于ststock1
##上一年度不能亏损   ##net_profits,净利润(万元)大于0；
##估值不能太高       pe<100
##杠杆比例不能太高   sheqratio,股东权益比率>10%
## 最近一年涨幅不能超过100%  不同日期的##close：收盘价 比较计算涨幅
##是否为限售股
##是否为沪深300或者上证50 沪深三百则为hs300s1里面度代码  上证50指数里面度代码sz50s

##def stockrepo(codename):
##    if codename in ststock1:
##        print("a")
##    if codename not in ststock1:
##        print("b")
##
##stockrepo()

