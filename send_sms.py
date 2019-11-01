from twilio.rest import Client
import os
import pandas

quote_list = pandas.read_csv("quotes.csv")
pandas.set_option('display.max_colwidth', -1)
concat_quote = quote_list["Author"] + ": " + quote_list["Quote"].map(str)
random_quote = concat_quote.sample()

message = random_quote.to_string(index=False, header=False)
tw_user = os.environ['TWILIO_ACCOUNT_SID']
tw_pass = os.environ['TWILIO_AUTH_TOKEN']
client = Client(tw_user, tw_pass)

client.messages.create(to="+14074735686", from_="+14073377803", body=message)
