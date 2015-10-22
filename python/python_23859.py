# SQLAlchemy complex query
((Unit.serve_setting.has(ServeSetting.serve_once_per_period == True)) &amp; (ServedUnitMetric.unit_id == Unit.id) &amp; (func.abs(func.unix_timestamp(datetime.utcnow()) - func.unix_timestamp(ServedUnitMetric.endDate)) &gt;= (ServeSetting.period_hours * 60 * 60)))
