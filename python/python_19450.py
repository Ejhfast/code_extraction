# Pandas dataframe get next (trading) day in dataframe
next_trading_date = returns.index[(returns.index &gt; dt_query) &amp; (returns.index &lt;= dt_query + timedelta(days = 10))][0]
