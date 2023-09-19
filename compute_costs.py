import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
with open("input.txt", "r") as f:
    text = f.read()
ninput = len(encoding.encode(text))
input = 0.012 * ninput / 1000

with open("output.txt", "r") as f:
    text = f.read()
noutput = len(encoding.encode(text))
output = 0.016 * noutput / 1000
print("GPT-3.5-turbo")
quarterly = (input + output) * 130
yearly = quarterly * 3
print("Total per quarter:", quarterly, "Total per year:", yearly, "USD")
print("Monthly price per school: ", 12 * 5 * yearly / 9, "USD")
print("Monthly price per high/middle/elementary school: ", 4 * 5 * yearly / 9, "USD")
print("Monthly price per two of high/middle/elementary schools", 8 * 5 * yearly / 9, "USD")
print("Yearly price per high/middle/elementary school: ", 4 * 5 * yearly, "USD")
print("Yearly price per two of high/middle/elementary schools", 8 * 5 * yearly, "USD")
print("Yearly price per school:", 12 * 5 * yearly, "USD")
print()
print()
quarterly_4 = ((input * 1.33 + output * 1.125) * 130)
yearly_4 = quarterly_4 * 3
print("GPT-4")
print("Total per quarter:", quarterly_4, "Total per year:", yearly_4, "USD")
print("Monthly price per high/middle/elementary school: ", 4 * 5 * yearly_4 / 9, "USD")
print("Monthly price per two of high/middle/elementary schools", 8 * 5 * yearly_4 / 9, "USD")
print("Monthly price per school: ", 12 * 5 * yearly_4 / 9, "USD")
print("Yearly price per high/middle/elementary school: ", 4 * 5 * yearly_4, "USD")
print("Yearly price per two of high/middle/elementary schools", 8 * 5 * yearly_4, "USD")
print("Yearly price per school:", 12 * 5 * yearly_4, "USD")
