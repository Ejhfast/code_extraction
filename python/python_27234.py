# Error using bootstrap_plot in pandas if values have NaN
bootstrap_plot( df[ df['x'].notnull() ]['x'] )
