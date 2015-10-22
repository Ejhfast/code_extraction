# SQLAlchemy: filter_by with like() on foreign attribute
crsRuns = Session.query(CRRun, CR, Run).join(CR).join(Run)
crsRuns = crsRuns.filter(CR.state.like('%' + state + '%'))
