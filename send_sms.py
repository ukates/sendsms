from twilio.rest import Client
import pandas

quote_list = pandas.read_csv("quotes.csv")
pandas.set_option('display.max_colwidth', -1)
concat_quote = quote_list["Author"] + ": " + quote_list["Quote"].map(str)
random_quote = concat_quote.sample()
message = random_quote.to_string(index=False, header=False)

client = Client("AC1cab582bf25d277d6fd11d94a07b072d","13ecbce49edb63482021bd51eb790a40")

client.messages.create(to="+14074735686", from_="+14073377803", body=message)
