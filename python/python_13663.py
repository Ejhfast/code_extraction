# Good design pattern(s) for extensible program
fetcher_dict = {'X':XDataFetcher,'Y':YDataFetcher}
data_source = ...
fetcher = fetcher_dict[data_source]()
