from pandas_datareader.data import Options

fb_options = Options('TSLA', 'yahoo')
options_df = fb_options.get_options_data(expiry=fb_options.expiry_dates[0])

print(options_df.tail())